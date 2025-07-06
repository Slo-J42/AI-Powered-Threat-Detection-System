import os, sys, time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '.')))
from scripts.detect_anomalies import detect_anomalies
from alert_email import send_alert_email

class Handler(FileSystemEventHandler):
    def on_modified(self, event):
        if event.src_path.endswith('logs.csv'):
            df = detect_anomalies()
            flagged = df[df['anomaly'] == -1]
            if not flagged.empty:
                print('⚠️ Anomalies detected! Sending email...')
                send_alert_email(flagged)

if __name__ == '__main__':
    observer = Observer()
    observer.schedule(Handler(), path='data', recursive=False)
    observer.start()
    print('🔁 Live log monitoring started.')
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()