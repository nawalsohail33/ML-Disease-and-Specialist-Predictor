# 🩺 Medical Assistant using Voice Recognition & Machine Learning

This project is an intelligent medical assistant that takes user symptoms via **voice input**, predicts possible **medical conditions**, and recommends the relevant **specialist** using machine learning. It also speaks back the prediction using **text-to-speech**.

A Django-based web interface is also included for easier interaction.

---

## 🚀 Features

- 🎙 Voice Input — Speak your symptoms naturally
- 🧠 Condition Prediction — ML model predicts likely medical condition
- 👨‍⚕️ Specialist Suggestion — Recommends the appropriate doctor
- 🔊 Voice Output — Speaks back the result using `pyttsx3`
- 🌐 Django Interface — Web-based GUI for interaction
- 📊 Data Visualization — Includes scatter and bar plots for model evaluation

---
![image](https://github.com/user-attachments/assets/1f22a485-6028-477f-b00b-2470a9985fb4)


---

## 🧪 How It Works

1. The user speaks symptoms into the microphone.
2. `speech_recognition` captures and transcribes the voice.
3. A trained **TF-IDF vectorizer** transforms the text.
4. Logistic Regression models predict:
   - The **condition** (`condition_model.pkl`)
   - The **specialist** (`specialist_model.pkl`)
5. The assistant:
   - **Displays** the result
   - **Speaks** it using `pyttsx3`

---

## 💻 Web Interface

- Built using Django
- Input form to type or speak symptoms
- Displays diagnosis and specialist recommendation
- Optionally plays audio of diagnosis

---

## 🧠 Machine Learning Details

- Models: `LogisticRegression()`
- Dataset: Synthetic medical symptom-condition-specialist dataset
- Preprocessing:
  - TF-IDF for symptoms
  - `LabelEncoder` for labels
- Addressed class imbalance using `SMOTE` / `RandomOverSampler`
- Achieved 98% accuracy (on synthetic, noise-free data)

---

## 📦 Installation & Run Instructions

### 1. Clone the Repo

```bash
git clone https://github.com/yourusername/medical-voice-assistant.git
cd medical-voice-assistant
pip install -r requirements.txt
python manage.py runserver
Visit http://127.0.0.1:8000/ in your browser.




