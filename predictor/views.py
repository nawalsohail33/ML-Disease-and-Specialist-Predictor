from django.shortcuts import render
from .voice import get_symptoms_from_voice, speak_output
import joblib

# Load model assets (same as before)
reg = joblib.load("reg_model.pkl")
reg_specialist = joblib.load("reg_specialist.pkl")
condition_encoder = joblib.load("condition_encoder.pkl")
specialist_encoder = joblib.load("specialist_encoder.pkl")
v = joblib.load("vectorizer.pkl")

def voice_diagnosis_view(request):
    result = ""
    if request.method == "POST":
        symptoms = get_symptoms_from_voice()  # ✅ This is only triggered on form submit
        if symptoms:
            symptom_vector = v.transform([symptoms])
            predicted_condition = condition_encoder.inverse_transform(reg.predict(symptom_vector))
            predicted_specialist = specialist_encoder.inverse_transform(reg_specialist.predict(symptom_vector))

            result = f"You may have {predicted_condition[0]}. You should consult a {predicted_specialist[0]}"
            speak_output(result)
        else:
            result = "Sorry, I could not understand the symptoms."
            speak_output(result)

    return render(request, "form.html", {"result": result})
