from scripts.preprocess import preprocess_log
import joblib

def detect_anomalies():
    model = joblib.load('model/anomaly_model.pkl')
    data = preprocess_log('data/logs.csv')
    data['anomaly'] = model.predict(data)
    return data