from sklearn.ensemble import IsolationForest
from sklearn.svm import OneClassSVM
from sklearn.covariance import EllipticEnvelope
from sklearn.neighbors import LocalOutlierFactor
from scripts.preprocess import preprocess_log
import joblib, sys

def train_model(algo='isolation'):
    data = preprocess_log('data/logs.csv')
    if algo == 'svm':
        model = OneClassSVM(nu=0.05, kernel='rbf', gamma='auto')
    elif algo == 'elliptic':
        model = EllipticEnvelope(contamination=0.05)
    elif algo == 'lof':
        model = LocalOutlierFactor(n_neighbors=20, contamination=0.05, novelty=True)
    else:
        model = IsolationForest(contamination=0.05)
    model.fit(data)
    joblib.dump(model, 'model/anomaly_model.pkl')
    print(f'✅ {algo.upper()} model trained and saved.')

if __name__ == '__main__':
    algo = sys.argv[1] if len(sys.argv) > 1 else 'isolation'
    train_model(algo)