from sklearn.mixture import GaussianMixture
import numpy as np

# 生成数据
X = np.random.rand(100, 2)

# 定义 GMM 模型
gmm = GaussianMixture(n_components=3, covariance_type='full', random_state=42)

# 拟合模型
gmm.fit(X)

# 获取预测的簇标签
labels = gmm.predict(X)

# 获取每个点的后验概率
probabilities = gmm.predict_proba(X)

print("Labels:", labels)
print("Probabilities:", probabilities)