import os
import json
from diagnosis_data import diagnosis_data

OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")

def get_diagnosis(category, symptoms):
    try:
        category_data = diagnosis_data.get(category, {})
        if not category_data:
            return json.dumps({"error": "Category not found"})

        # Find the best matching condition based on symptoms
        best_match = None
        max_matches = 0

        for condition, data in category_data.items():
            matches = len(set(symptoms) & set(data["symptoms"]))
            if matches > max_matches:
                max_matches = matches
                best_match = (condition, data)

        if not best_match:
            return json.dumps({
                "diagnosis": "No matching condition found",
                "precautions": ["Please consult a healthcare professional"],
                "remedies": ["Seek medical advice"]
            })

        condition, data = best_match
        return json.dumps({
            "diagnosis": f"Based on your symptoms, you may have {condition}",
            "precautions": data["precautions"],
            "remedies": data["remedies"]
        })

    except Exception as e:
        raise Exception(f"Diagnosis failed: {str(e)}")