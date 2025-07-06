# 🛡️ AI‑Powered Threat Detection System

A full‑stack cybersecurity project that

- ingests & preprocesses logs  
- detects anomalies with four ML models (Isolation Forest, One‑Class SVM, Elliptic Envelope, LOF)  
- monitors logs live with watchdog  
- sends email alerts (secrets stored in .env)  
- visualises everything in a Streamlit dashboard  

## 🚀 Quick start
```bash
pip install -r requirements.txt          # pandas, sklearn, streamlit…
cp .env.example .env                     # add Gmail + 16‑char App Password
python scripts/train_model.py            # default Isolation Forest
# or: python scripts/train_model.py svm | elliptic | lof
streamlit run dashboard/app.py           # UI on http://localhost:8501
python live_monitor.py                   # live monitoring + email alerts
