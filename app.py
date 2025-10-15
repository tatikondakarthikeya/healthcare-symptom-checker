import streamlit as st
import requests

st.set_page_config(page_title="Healthcare Symptom Checker", page_icon="🩺")

st.markdown(
    """
    <style>
    body {
        background: linear-gradient(110deg, #d4fc79 0%, #96e6a1 70%, #f8ffae 100%) !important;
    }
    .stApp {
        background: linear-gradient(110deg, #ffe8fa 0%, #bbffe7 100%) !important;
        color: #222;
    }
    header {background: none !important;}
    .stTextArea textarea {
        background: #fffbe7 !important; 
        font-size: 16px !important;
        color: #111 !important; /* Black text inside textarea */
    }
    .stForm {
        background: #ffffffcc !important;
        border-radius: 20px !important;
        padding: 20px !important;
        border: 1px solid #dbece6 !important;
    }
    .stButton > button {
        background: linear-gradient(90deg,#46c2ff 0,#67ffcf 100%) !important;
        color: #222 !important;
        font-weight: bold !important;
        border-radius: 10px !important;
        box-shadow: 0 4px 16px rgba(58,171,242,0.10);
    }
    label, .css-1c7y2kd, .st-bx, .stTextInput label, .stTextArea label {
        color: #111 !important;
        font-weight: 700 !important;
        font-size: 1.07rem !important;
    }
    /* Make ALL markdown subheaders and result text black and bold */
    h2, .black-subheader, .result-box, .substeps {
        color: #111 !important;
        font-weight: 700 !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

API_URL = "http://127.0.0.1:8000/check-symptoms"

# Black, bold title
st.markdown(
    "<h1 style='color:#222; font-size:2.8rem; margin-bottom:12px'><span style='font-size:2.2rem'>🩺</span> Healthcare Symptom Checker</h1>",
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div style='font-size:18px; padding-bottom:10px; color:#222; background:rgba(255, 255, 255, 0.85); border-radius:10px; padding:14px 18px; font-weight:600'>
    Enter your symptoms below to get probable conditions and recommendations.<br>
    <i style='color:#ebc634; font-weight:bold;'>For educational purposes only.</i>
    </div>
    """,
    unsafe_allow_html=True,
)

with st.form(key="symptom_form"):
    symptoms = st.text_area("📝 Symptoms", placeholder="e.g. fever, headache, sore throat")
    submit_btn = st.form_submit_button("🔎 Analyze Symptoms")

if submit_btn:
    if not symptoms.strip():
        st.error("Please enter your symptoms!")
    else:
        with st.spinner("Analyzing symptoms..."):
            try:
                resp = requests.post(API_URL, json={"symptoms": symptoms})
                if resp.status_code == 200:
                    data = resp.json()
                    st.markdown("<h2 class='black-subheader'>💡 Probable Conditions:</h2>", unsafe_allow_html=True)
                    st.write(
                        "".join(
                            [
                                f"<div class='result-box' style='background:linear-gradient(90deg,#fffbe7,#e1ffc7);padding:12px;border-radius:8px;margin:4px 0;font-weight:700;color:#111;'>• <b>{cond}</b></div>"
                                for cond in data.get("probable_conditions", [])
                            ]
                        ),
                        unsafe_allow_html=True,
                    )

                    st.markdown("<h2 class='black-subheader'>🗒️ Recommended Next Steps:</h2>", unsafe_allow_html=True)
                    st.write(
                        "".join(
                            [
                                f"<div class='result-box substeps' style='background:linear-gradient(90deg,#d7faff,#ffe2f7);padding:10px;border-radius:8px;margin:4px 0;font-weight:700;color:#111;'>• {step}</div>"
                                for step in data.get("next_steps", [])
                            ]
                        ),
                        unsafe_allow_html=True,
                    )

                    st.info(f"{data.get('disclaimer', '')}", icon="ℹ️")
                else:
                    st.error(f"API error: {resp.text}")
            except Exception as e:
                st.error(f"Connection error: {e}")

if st.button("🔄 Clear"):
    st.experimental_rerun()
