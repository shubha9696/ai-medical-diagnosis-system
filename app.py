import os
from flask import Flask, render_template, request, jsonify
from ai_helper import get_diagnosis
import symptoms

app = Flask(__name__)
app.secret_key = os.environ.get("FLASK_SECRET_KEY") or "medical-diagnosis-secret-key"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/diagnosis/<category>')
def diagnosis(category):
    category_symptoms = getattr(symptoms, f"{category}_symptoms", [])
    return render_template('diagnosis.html', 
                         category=category,
                         symptoms=category_symptoms)

@app.route('/get_diagnosis', methods=['POST'])
def process_diagnosis():
    try:
        data = request.json
        category = data.get('category')
        selected_symptoms = data.get('symptoms', [])

        if not selected_symptoms:
            return jsonify({"error": "No symptoms selected"}), 400

        diagnosis_result = get_diagnosis(category, selected_symptoms)
        return jsonify(diagnosis_result)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/bmi')
def bmi_calculator():
    return render_template('bmi.html')

@app.route('/calculate_bmi', methods=['POST'])
def calculate_bmi():
    try:
        data = request.json
        weight = float(data.get('weight', 0))  # in kg
        height = float(data.get('height', 0))  # in meters

        if weight <= 0 or height <= 0:
            return jsonify({"error": "Invalid weight or height"}), 400

        bmi = weight / (height * height)
        category = ""
        if bmi < 18.5:
            category = "Underweight"
        elif bmi < 25:
            category = "Normal weight"
        elif bmi < 30:
            category = "Overweight"
        else:
            category = "Obese"

        return jsonify({
            "bmi": round(bmi, 2),
            "category": category
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/chatbot')
def chatbot():
    return render_template('chatbot.html')

@app.route('/chat', methods=['POST'])
def chat():
    try:
        message = request.json.get('message')
        response = get_chatbot_response(message)
        return jsonify({"response": response})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == "__main__":
    app.run(debug=True)