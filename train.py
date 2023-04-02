import lightgbm as lgb
from sklearn.datasets import make_classification

data, target = make_classification(n_features=100, n_samples=50_000, random_state=42)

params = {
    'boosting_type': 'gbdt',
    'objective': 'cross_entropy',
    'metric': 'log-loss',
    'num_leaves': 31,
    'max_depth': 20,
    'learning_rate': 0.05,
    'feature_fraction': 0.9,
    'bagging_fraction': 0.8,
    'bagging_freq': 5,
    'verbose': 0,
    'num_threads': -1  # enable multithreading
}

train_data = lgb.Dataset(data, label=target)

for i, num_boost_round in enumerate([100, 500, 1000, 2000]):
    gbm = lgb.train(params, train_data, num_boost_round=num_boost_round)
    gbm.save_model(f'model_{i}.txt')
