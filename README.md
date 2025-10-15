🩺 Healthcare Symptom Checker
A simple, modern web app for checking symptoms, getting probable medical conditions, and recommended next steps. Built with Streamlit (frontend) and FastAPI (backend).

🚀 Features
Enter symptoms in plain language (e.g., "fever, headache, sore throat")

Instantly see possible medical conditions based on your symptoms

Get friendly recommendations about what to do next

Modern, responsive UI with pastel backgrounds

Easy to deploy and extend!

📦 Installation

1. Clone the repository
bash
git clone https://github.com/tatikondakarthikeya/healthcare-symptom-checker.git
cd healthcare-symptom-checker
2. Setup Python environment (optional, but recommended)
bash
python3 -m venv venv
source venv/bin/activate           # Mac/Linux
venv\Scripts\activate              # Windows
3. Install dependencies
bash
pip install -r requirements.txt
⚡ Usage
1. Start the FastAPI backend
Make sure your backend server (API with symptom logic) is running.
Example (if main.py is your FastAPI script):

bash
uvicorn main:app --reload
By default, it will serve at http://127.0.0.1:8000.

2. Start the Streamlit frontend
bash
streamlit run app.py
Open the link shown in your terminal (typically http://localhost:8501) in your browser.

🖥️ Project Structure
text
├── app.py                  # Streamlit UI
├── main.py                 # FastAPI backend
├── requirements.txt        # Python dependencies
├── README.md               # Project documentation
👤 Author
Karthikeya Tatikonda

📄 License
This project is for educational and demonstration purposes only.

📝 Disclaimer
Outputs do not replace professional medical advice.

For any serious health concerns, consult a registered medical practitioner.
