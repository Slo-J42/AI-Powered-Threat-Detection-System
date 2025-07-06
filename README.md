
# 🛡️ AI-Powered Threat Detection System

An end‑to‑end cybersecurity project that:

* Monitors logs in real time  
* Detects anomalies with ML (Isolation Forest, One‑Class SVM, Elliptic Envelope, LOF)  
* Sends email alerts for suspicious activity  
* Presents a Streamlit dashboard  

## 🚀 Quick Start
```bash
git clone <repo>
cd ai_threat_detection_final
pip install -r requirements.txt
cp .env.example .env   # add your Gmail + App Password
python scripts/train_model.py            # default Isolation Forest
streamlit run dashboard/app.py           # browse results
python live_monitor.py                   # enable live alerts
```

## 📄 .env
```
EMAIL_SENDER=youremail@gmail.com
EMAIL_PASSWORD=your16charAppPassword
EMAIL_RECEIVER=youremail@gmail.com
```

## 🖥️ Dashboard
Run `streamlit run dashboard/app.py` and open `localhost:8501` to visualize logs & anomalies.

## 📬 Email Alerts
Uses Gmail SMTP with App Passwords for 2FA accounts. Alerts trigger when anomalies are found during live monitoring.

---

Made with ❤️ by Shlok Jadhav
