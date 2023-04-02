# Benchmark 

Hacky script to quickly benchmark the impact of OMP_NUM_THREADS and num_estimators in lightgbm speed of prediction.

## How to run
`docker-compose up -d`

`python3 -m python example_requests.py`

## Results so far for 100 runs

When we set OMP_NUM_THREADS=-1, the OpenMP library will create a large number of threads, which can lead to excessive context switching, memory thrashing, and cache contention. Doubling the size of estimators highly increase latency.

```
********Benchmark********
************0************
----OMP_NUM_THREADS=1----
Avg execution time: 197.3501 ms
95th percentile: 211.0349 ms
Standard deviation: 10.4599 ms
---OMP_NUM_THREADS=-1----
Avg execution time: 349.8191 ms
95th percentile: 583.9568 ms
Standard deviation: 92.9066 ms
************1************
----OMP_NUM_THREADS=1----
Avg execution time: 225.5192 ms
95th percentile: 238.2434 ms
Standard deviation: 7.1689 ms
---OMP_NUM_THREADS=-1----
Avg execution time: 547.5686 ms
95th percentile: 832.2592 ms
Standard deviation: 175.0446 ms
************2************
----OMP_NUM_THREADS=1----
Avg execution time: 251.8405 ms
95th percentile: 268.1442 ms
Standard deviation: 7.6871 ms
---OMP_NUM_THREADS=-1----
Avg execution time: 775.7895 ms
95th percentile: 1296.3087 ms
Standard deviation: 262.7199 ms
************3************
----OMP_NUM_THREADS=1----
Avg execution time: 321.6820 ms
95th percentile: 347.2821 ms
Standard deviation: 16.1465 ms
---OMP_NUM_THREADS=-1----
Avg execution time: 1095.9684 ms
95th percentile: 1696.8768 ms
Standard deviation: 286.8636 ms
```

