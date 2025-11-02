import streamlit as st
import pandas as pd
import joblib
import os
from datetime import datetime

# ===== Load model and encoder =====
model = joblib.load("medexplain_random_forest.pkl")
encoder = joblib.load("label_encoder.pkl")

# ===== Page setup =====
st.set_page_config(page_title="MedExplain AI", page_icon="🧠", layout="wide")

st.title("🧠 MedExplain — AI-Powered Health Report Interpreter")
st.markdown("""
This demo shows how MedExplain uses AI + NLP to interpret medical reports,
allowing doctor feedback and simulated patient report sharing.
""")

# ===== Sidebar: Explain Parameters =====
st.sidebar.header("📘 Learn About Your Parameters")
st.sidebar.markdown("""
**Blood Glucose** — Sugar level in the blood. Normal: *70–110 mg/dL*  
**HbA1c** — Average blood sugar (3 months). Normal: *<5.7 %*  
**Systolic BP / Diastolic BP** — Blood pressure values. Normal: *120/80 mmHg*  
**LDL / HDL** — Cholesterol levels. LDL (bad) <100, HDL (good) >40  
**Triglycerides** — Type of fat in blood. Normal: *<150 mg/dL*  
**Haemoglobin** — Oxygen-carrying protein. Normal: *13–17 (M), 12–15 (F)*  
**MCV** — Average size of red blood cells. Normal: *80–100 fL*  
""")

# ===== NLP suggestion dictionary =====
nlp_suggestions = {
    "Fit": {
        "explanation": "Your health parameters appear within normal ranges.",
        "suggestion": "Maintain a balanced diet, regular exercise, and get routine checkups."
    },
    "Anemia": {
        "explanation": "Your haemoglobin or MCV levels may be low, reducing oxygen-carrying capacity.",
        "suggestion": "Include iron-rich foods (like spinach, beans, jaggery) and Vitamin C in your diet."
    },
    "Diabetes": {
        "explanation": "Your glucose and HbA1c values suggest elevated blood sugar levels.",
        "suggestion": "Reduce sugar intake, exercise daily, and consult an endocrinologist for guidance."
    },
    "Hypertension": {
        "explanation": "Your blood pressure readings indicate possible high blood pressure.",
        "suggestion": "Reduce salt intake, manage stress, and monitor blood pressure regularly."
    },
    "High Cholesterol": {
        "explanation": "Your LDL and triglyceride levels appear higher than normal.",
        "suggestion": "Avoid fried foods, eat fiber-rich meals, and exercise regularly."
    }
}

# ===== Input form =====
with st.form("input_form"):
    st.subheader("🧾 Enter Patient Details and Test Results")

    patient_name = st.text_input("👤 Patient Name", placeholder="John Doe")
    patient_email = st.text_input("📧 Patient Email", placeholder="johndoe@example.com")

    col1, col2 = st.columns(2)
    with col1:
        blood_glucose = st.number_input("Blood Glucose (mg/dL)", 50.0, 400.0, 100.0)
        hba1c = st.number_input("HbA1c (%)", 3.0, 15.0, 5.5)
        systolic_bp = st.number_input("Systolic BP (mmHg)", 80.0, 200.0, 120.0)
        diastolic_bp = st.number_input("Diastolic BP (mmHg)", 50.0, 120.0, 80.0)
    with col2:
        ldl = st.number_input("LDL (mg/dL)", 30.0, 300.0, 110.0)
        hdl = st.number_input("HDL (mg/dL)", 20.0, 100.0, 50.0)
        triglycerides = st.number_input("Triglycerides (mg/dL)", 50.0, 500.0, 120.0)
        haemoglobin = st.number_input("Haemoglobin (g/dL)", 6.0, 20.0, 14.0)
        mcv = st.number_input("MCV (fL)", 60.0, 120.0, 90.0)

    submitted = st.form_submit_button("🔍 Generate Report")

# ===== Prediction + NLP Explanation =====
if submitted:
    new_data = pd.DataFrame([{
        "blood_glucose": blood_glucose,
        "hba1c": hba1c,
        "systolic_bp": systolic_bp,
        "diastolic_bp": diastolic_bp,
        "ldl": ldl,
        "hdl": hdl,
        "triglycerides": triglycerides,
        "haemoglobin": haemoglobin,
        "mcv": mcv
    }])

    prediction = model.predict(new_data)
    disease = encoder.inverse_transform(prediction)[0]
    confidence = model.predict_proba(new_data).max()

    st.markdown("---")
    st.subheader("🩺 AI-Generated Health Report")

    st.write(f"**Patient:** {patient_name or 'N/A'}")
    st.write(f"**Email:** {patient_email or 'N/A'}")
    st.write(f"**Predicted Condition:** {disease}")
    st.write(f"**Confidence:** {confidence*100:.2f}%")

    # ===== NLP-based Explanation =====
    condition_info = nlp_suggestions.get(
        disease,
        {"explanation": "Further medical review is advised.",
         "suggestion": "Consult a healthcare provider for confirmation."}
    )

    st.markdown("### 💬 AI Explanation")
    st.write(condition_info["explanation"])

    st.markdown("### 💡 Suggested Next Steps")
    st.write(condition_info["suggestion"])

    if disease.lower() == "fit":
        st.info("✅ You appear healthy! Keep maintaining your lifestyle.")
    else:
        st.warning("⚠️ The AI suggests possible signs of a medical condition. Please consult a doctor.")

    # ===== Doctor Feedback Section =====
    st.markdown("---")
    st.subheader("👨‍⚕️ Doctor Feedback")

    st.markdown("If you’re a reviewing physician, please confirm or correct the prediction below:")

    doctor_name = st.text_input("Doctor's Name (optional)")
    feedback_choice = st.radio(
        "Is the AI prediction correct?",
        ["Yes", "No"],
        horizontal=True
    )

    corrected_label = None
    if feedback_choice == "No":
        corrected_label = st.selectbox(
            "Select the correct condition:",
            encoder.classes_.tolist()
        )

    send_email = st.checkbox("📤 Send this report to patient's email (demo only)")

    if st.button("💾 Submit Feedback"):
        feedback_data = {
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "doctor": doctor_name if doctor_name else "Anonymous",
            "patient_name": patient_name,
            "patient_email": patient_email,
            "ai_prediction": disease,
            "ai_confidence": round(confidence * 100, 2),
            "feedback": feedback_choice,
            "corrected_label": corrected_label if corrected_label else disease,
            **new_data.iloc[0].to_dict()
        }

        feedback_df = pd.DataFrame([feedback_data])

        if not os.path.exists("doctor_feedback.csv"):
            feedback_df.to_csv("doctor_feedback.csv", index=False)
        else:
            feedback_df.to_csv("doctor_feedback.csv", mode='a', header=False, index=False)

        st.success("✅ Doctor feedback recorded successfully!")
        if send_email and patient_email:
            st.info(f"📧 Report sent to **{patient_email}** successfully (Demo Only).")
        st.balloons()

st.markdown("---")
st.caption("Made with ❤️ for the Loop × IIT Bombay Hackathon 2025 — Bridging Doctors, AI, and Patients")
