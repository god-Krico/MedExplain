# 🧠 MedExplain — AI-Powered Health Report Interpreter  

### 🚀 Overview  
**MedExplain** is an AI + NLP-powered platform that helps patients easily understand complex medical reports.  
It translates medical jargon into **simple, multilingual explanations**, highlights key findings, and suggests potential next steps.  
Doctors can review, correct, and improve the AI’s interpretation through a **doctor-in-the-loop feedback system**, making the model smarter and more reliable over time.  

---

## 💡 Problem Statement  
In India and many developing regions:
- Patients often receive lab reports full of **medical terms they cannot understand**.  
- Reports are sometimes **sent to city hospitals** for interpretation, delaying treatment.  
- **Doctors are overburdened** with explaining repetitive test findings.  
- Health insurance firms struggle to help employees stay proactive about their health.  

---

## 💊 Our Solution — MedExplain  
MedExplain bridges this gap by combining **machine learning**, **natural language processing**, and **human feedback** to create an intelligent health interpretation assistant.

### ✨ Key Capabilities
1. 🧬 **AI Health Prediction**  
   - Uses a trained **Random Forest** model to predict if a patient is *Fit* or shows signs of conditions such as  
     **Anemia, Diabetes, Hypertension, or High Cholesterol** based on lab test data.  

2. 🗣️ **NLP Report Explanation**  
   - Automatically generates human-friendly explanations for medical parameters (e.g., “LDL Cholesterol is high — avoid fried foods”).  
   - Suggests personalized lifestyle improvements (e.g., increase iron intake for anemia).  

3. 🧑‍⚕️ **Doctor-in-the-Loop Feedback System**  
   - Doctors can confirm or correct AI predictions.  
   - Corrections are stored for **continuous model retraining** to improve accuracy.  

4. 🌍 **Multilingual Accessibility (Future Scope)**  
   - Medical explanations and suggestions can be translated into **regional languages** using multilingual NLP (e.g., Hindi, Marathi, Tamil).  

5. 📤 **Patient Communication (Demo)**  
   - Pathologists can enter results; patients automatically receive **interpreted reports via email** (demo feature).  

6. ⏰ **Health Checkup Reminders**  
   - For insurance firms, MedExplain can send **proactive reminders** for periodic health checkups, promoting preventive care.  

7. ⚙️ **Integration-Ready for Health Insurance Providers**  
   - Firms can embed MedExplain in their employee wellness portals for automated health tracking and report interpretation.  

---

## 🧩 Tech Stack
| Category | Technology |
|-----------|-------------|
| **Frontend/UI** | Streamlit |
| **Backend** | Python (FastAPI planned for API integration) |
| **Machine Learning** | Scikit-learn (Random Forest Classifier) |
| **Data Processing** | Pandas, NumPy |
| **NLP** | Rule-based suggestions + extendable to transformers |
| **Storage** | CSV feedback logs (can scale to database) |
| **Model Persistence** | Joblib |
| **Version Control** | Git, GitHub |
| **Deployment (Planned)** | Streamlit Cloud / Hugging Face Spaces |

---

## 📘 Input Parameters  
| Parameter | Description | Normal Range |
|------------|--------------|---------------|
| Blood Glucose | Blood sugar level | 70–110 mg/dL |
| HbA1c | 3-month sugar avg | < 5.7% |
| Systolic BP | Upper blood pressure | 120 mmHg |
| Diastolic BP | Lower blood pressure | 80 mmHg |
| LDL | “Bad” cholesterol | < 100 mg/dL |
| HDL | “Good” cholesterol | > 40 mg/dL |
| Triglycerides | Blood fat level | < 150 mg/dL |
| Haemoglobin | Oxygen-carrying protein | 13–17 (M), 12–15 (F) |
| MCV | Red blood cell size | 80–100 fL |

---

## 🧮 Model Training
- The dataset includes blood test metrics with a target label — **condition** (`Fit`, `Anemia`, `Diabetes`, `Hypertension`, `High Cholesterol`).
- Data preprocessing:
  - Missing value imputation  
  - Label encoding for categorical outputs  
  - Median/mode fill for missing numerical data  
- Model: **Random Forest Classifier**  
- Saved artifacts:  
  - `medexplain_random_forest.pkl` — Trained ML model  
  - `label_encoder.pkl` — Encoded label mapping  

---

## ⚙️ How It Works  
1. **Pathologist enters lab values** into the app.  
2. **AI model predicts** possible condition + confidence score.  
3. **NLP engine explains** findings in plain language with actionable advice.  
4. **Doctor reviews** and provides feedback if needed.  
5. **System logs feedback** for retraining.  
6. *(Optional)* Report is “sent” to the patient’s email for demonstration.  

---

## 🧠 Example Output
Patient: John Doe
Email: johndoe@example.com

Predicted Condition: Diabetes
Confidence: 92.3%

Explanation:
Your glucose and HbA1c values suggest elevated blood sugar levels.

Suggested Next Steps:
Reduce sugar intake, exercise daily, and consult an endocrinologist for guidance.



---

## 🔄 Future Enhancements
- 🧩 Integration with real hospital/LIS systems  
- 🧠 Use of LLMs for personalized report summarization  
- 🌍 Real-time multilingual translation (English ↔ regional languages)  
- 📈 Continuous model improvement using doctor feedback  
- 💬 Chatbot interface for patient Q&A  
- 🔔 Automated health reminders via email/SMS  

---

## ❤️ Built For
**Loop × IIT Bombay Hackathon 2025**  
Theme: *“Information that makes sense” & “People and technology working together”*  

**Team: ML PAGLUS**  
**Ashwin Mankar**
**Vishal Patel**


