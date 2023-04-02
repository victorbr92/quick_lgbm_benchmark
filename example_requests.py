import requests
from sklearn.datasets import make_classification
import numpy as np
import timeit

data, target = make_classification(n_features=100, n_samples=1000, random_state=42)

payload = {"data": data.tolist()}
num_runs =100

def preds(port: int = 8000, model: int = 0):
    url = f"http://localhost:{port}/predict/{model}"
    response = requests.post(url, json=payload)
    assert len(response.json()['prediction']) == len(target)

def report(execution_times):   
    # Calculate the statistics
    avg_time = np.mean(execution_times)
    p95_time = np.percentile(execution_times, 95)
    stdev_time = np.std(execution_times)

    # Print the results
    print(f"Avg execution time: {1000*avg_time:.4f} ms")
    print(f"95th percentile: {1000*p95_time:.4f} ms")
    print(f"Standard deviation: {1000*stdev_time:.4f} ms")


print(f"{'Benchmark':*^25}")
for model in range(4):
    print(f"{model:*^25}")
    print(f"{'OMP_NUM_THREADS=1':-^25}")
    execution_times = np.array([timeit.timeit(lambda: preds(port=8000, model=model), number=1) for _ in range(num_runs)])
    report(execution_times)

    print(f"{'OMP_NUM_THREADS=-1':-^25}")
    execution_times = np.array([timeit.timeit(lambda: preds(port=8001, model=model), number=1) for _ in range(num_runs)])
    report(execution_times)
