import urllib.request
import urllib.error
import json
import os
from dotenv import load_dotenv
import logging

def azure_scoring_model(data, timeout=30):
    load_dotenv()

    api_key = os.getenv("api_key")
    url = os.getenv("url")

    if not api_key:
        raise Exception("A key should be provided to invoke the endpoint (api_key missing).")
    if not url:
        raise Exception("Endpoint URL is not configured (url missing).")

    body = json.dumps(data).encode("utf-8")
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer {api_key}"
    }

    req = urllib.request.Request(url, data=body, headers=headers, method="POST")

    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            raw = resp.read()
            text = raw.decode("utf-8", errors="ignore")
            logging.info("Azure ML raw response: %s", text)

            # Try to parse JSON
            try:
                payload = json.loads(text)
            except json.JSONDecodeError:
                # If not JSON, raise with the raw text for debugging
                raise ValueError(f"Non-JSON response from model endpoint: {text}")

            # Common response shapes:
            # 1) {"result": {"label": "positive", "probability": 0.87}}
            # 2) {"predictions": [{"label":"positive","probability":0.87}]}
            # 3) {"label": "positive", "probability": 0.87}
            # 4) Azure ML sometimes returns {"results": {...}} or {"output1": {...}}
            # Try to find label and probability robustly:
            def extract_label_prob(obj):
                if not obj:
                    return None
                if isinstance(obj, dict):
                    # direct keys
                    if "label" in obj and ("probability" in obj or "prob" in obj):
                        return obj.get("label"), float(obj.get("probability", obj.get("prob")))
                    # nested common keys
                    for key in ("result", "results", "output1", "output"):
                        if key in obj and isinstance(obj[key], dict):
                            res = extract_label_prob(obj[key])
                            if res:
                                return res
                    # predictions list
                    if "predictions" in obj and isinstance(obj["predictions"], list) and obj["predictions"]:
                        first = obj["predictions"][0]
                        return extract_label_prob(first)
                    # sometimes predictions are under 'value' or 'values'
                    if "value" in obj and isinstance(obj["value"], list) and obj["value"]:
                        first = obj["value"][0]
                        return extract_label_prob(first)
                return None

            found = extract_label_prob(payload)
            # after `found = extract_label_prob(payload)` and before `if found: ...`
            # handle Azure Designer output shape: {"Results": {"WebServiceOutput0": [ { ... } ]}}
            if not found and isinstance(payload, dict):
                results = payload.get("Results") or payload.get("results")
                if isinstance(results, dict):
                    # common Designer output key
                    out_list = results.get("WebServiceOutput0") or results.get("webServiceOutput0") or None
                    if isinstance(out_list, list) and out_list:
                        first = out_list[0]
                        # check for Scored Labels / Scored Probabilities
                        label = first.get("Scored Labels") or first.get("ScoredLabel") or first.get("Scored Labels".lower())
                        prob = first.get("Scored Probabilities") or first.get("ScoredProbabilities") or first.get("Scored Probabilities".lower())
                        if label is not None and prob is not None:
                            # normalize label to your expected values
                            return str(label).strip(), float(prob)

            if found:
                label, prob = found
                return str(label), float(prob)

            # As a last resort, try to inspect common nested structures
            # e.g., payload might be {"result": ["positive", 0.87]}
            if isinstance(payload, dict):
                for v in payload.values():
                    if isinstance(v, list) and len(v) >= 2:
                        try:
                            return str(v[0]), float(v[1])
                        except Exception:
                            pass

            raise ValueError(f"Could not extract label/probability from model response: {payload}")

    except urllib.error.HTTPError as e:
        # Read body for debugging
        try:
            body = e.read().decode("utf-8", errors="ignore")
        except Exception:
            body = "<could not read body>"
        logging.error("Model HTTPError %s: %s", e.code, body)
        raise
    except urllib.error.URLError as e:
        logging.error("Model URLError: %s", e)
        raise