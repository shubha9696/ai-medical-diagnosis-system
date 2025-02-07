# Structured medical diagnosis data
brain_diagnosis = {
    "Migraine": {
        "symptoms": ["Severe headache", "Sensitivity to light", "Nausea", "Vision changes"],
        "precautions": [
            "Rest in a quiet, dark room",
            "Stay hydrated",
            "Avoid bright lights and loud sounds",
            "Keep a regular sleep schedule"
        ],
        "remedies": [
            "Apply cold or warm compress",
            "Practice relaxation techniques",
            "Stay in a quiet, dark room",
            "Take prescribed medications as directed"
        ]
    },
    "Tension Headache": {
        "symptoms": ["Dull headache", "Pressure around forehead", "Neck pain", "Fatigue"],
        "precautions": [
            "Maintain good posture",
            "Take regular breaks from screens",
            "Practice stress management",
            "Get adequate sleep"
        ],
        "remedies": [
            "Gentle neck stretches",
            "Over-the-counter pain relievers",
            "Massage therapy",
            "Apply warm compress"
        ]
    }
}

skin_diagnosis = {
    "Eczema": {
        "symptoms": ["Itching", "Dry skin", "Redness", "Skin rash"],
        "precautions": [
            "Avoid harsh soaps",
            "Use gentle moisturizers",
            "Wear soft, breathable fabrics",
            "Avoid scratching"
        ],
        "remedies": [
            "Apply moisturizer regularly",
            "Use cold compress for itching",
            "Take lukewarm baths",
            "Use prescribed topical treatments"
        ]
    },
    "Contact Dermatitis": {
        "symptoms": ["Redness", "Itching", "Burning sensation", "Skin rash"],
        "precautions": [
            "Identify and avoid triggers",
            "Wear protective gloves",
            "Keep skin clean and dry",
            "Use hypoallergenic products"
        ],
        "remedies": [
            "Cool compress application",
            "Calamine lotion",
            "Oatmeal baths",
            "Antihistamine medications"
        ]
    }
}

eye_diagnosis = {
    "Conjunctivitis": {
        "symptoms": ["Redness", "Itching", "Discharge", "Watery eyes"],
        "precautions": [
            "Avoid touching or rubbing eyes",
            "Wash hands frequently",
            "Use separate towels",
            "Avoid sharing eye products"
        ],
        "remedies": [
            "Warm compress",
            "Artificial tears",
            "Keep eyes clean",
            "Use prescribed eye drops"
        ]
    },
    "Eye Strain": {
        "symptoms": ["Blurred vision", "Eye fatigue", "Headache", "Dry eyes"],
        "precautions": [
            "Take regular screen breaks",
            "Maintain proper lighting",
            "Use proper screen distance",
            "Blink regularly"
        ],
        "remedies": [
            "20-20-20 rule (every 20 minutes, look 20 feet away for 20 seconds)",
            "Use artificial tears",
            "Adjust screen brightness",
            "Eye exercises"
        ]
    }
}

heart_diagnosis = {
    "Hypertension": {
        "symptoms": ["Headache", "Shortness of breath", "Chest pain", "Dizziness"],
        "precautions": [
            "Regular blood pressure monitoring",
            "Limit salt intake",
            "Maintain healthy weight",
            "Regular exercise"
        ],
        "remedies": [
            "Follow DASH diet",
            "Regular physical activity",
            "Stress management",
            "Take prescribed medications"
        ]
    },
    "Angina": {
        "symptoms": ["Chest pain", "Shortness of breath", "Nausea", "Fatigue"],
        "precautions": [
            "Avoid overexertion",
            "Manage stress levels",
            "Regular check-ups",
            "Take medications as prescribed"
        ],
        "remedies": [
            "Rest during episodes",
            "Use prescribed nitroglycerin",
            "Practice relaxation techniques",
            "Follow heart-healthy diet"
        ]
    }
}

digestive_diagnosis = {
    "Acid Reflux": {
        "symptoms": ["Heartburn", "Chest pain", "Difficulty swallowing", "Regurgitation"],
        "precautions": [
            "Avoid lying down after meals",
            "Eat smaller meals",
            "Avoid trigger foods",
            "Maintain healthy weight"
        ],
        "remedies": [
            "Elevate head while sleeping",
            "Avoid eating before bedtime",
            "Chew gum after meals",
            "Take antacids as needed"
        ]
    },
    "Gastritis": {
        "symptoms": ["Abdominal pain", "Nausea", "Bloating", "Loss of appetite"],
        "precautions": [
            "Avoid spicy foods",
            "Limit alcohol consumption",
            "Eat smaller meals",
            "Avoid NSAIDs"
        ],
        "remedies": [
            "Eat bland foods",
            "Stay hydrated",
            "Probiotics",
            "Prescribed medications"
        ]
    }
}

hmpv_diagnosis = {
    "HMPV Infection": {
        "symptoms": ["Cough", "Fever", "Shortness of breath", "Nasal congestion"],
        "precautions": [
            "Rest and isolation",
            "Wear mask when around others",
            "Practice good hand hygiene",
            "Monitor symptoms"
        ],
        "remedies": [
            "Rest and sleep",
            "Stay hydrated",
            "Use humidifier",
            "Over-the-counter fever reducers"
        ]
    },
    "Upper Respiratory Infection": {
        "symptoms": ["Sore throat", "Cough", "Runny nose", "Fatigue"],
        "precautions": [
            "Rest adequately",
            "Practice good hygiene",
            "Stay hydrated",
            "Avoid close contact with others"
        ],
        "remedies": [
            "Salt water gargle",
            "Honey and warm tea",
            "Steam inhalation",
            "Over-the-counter medications"
        ]
    }
}

# Dictionary mapping categories to their diagnosis data
diagnosis_data = {
    "brain": brain_diagnosis,
    "skin": skin_diagnosis,
    "eye": eye_diagnosis,
    "heart": heart_diagnosis,
    "digestive": digestive_diagnosis,
    "hmpv": hmpv_diagnosis
}
