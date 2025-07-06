import pandas as pd

def preprocess_log(filepath):
    df = pd.read_csv(filepath)
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    df['hour'] = df['timestamp'].dt.hour
    df['is_failed'] = df['status'].eq('failed').astype(int)
    df['is_scan'] = df['event_type'].eq('scan').astype(int)
    return df[['hour', 'is_failed', 'is_scan']]