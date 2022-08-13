import numpy as np
import random 

s1 = np.array([random.choice([-1, 1]) for i in range(4)])
t1 = np.array([random.choice([-1, 1]) for i in range(3)])
s1 = np.expand_dims(s1, axis=-1)
s1.reshape(1, 4); t1.reshape(3, 1)

s2 = np.array([random.choice([-1, 1]) for i in range(4)])
t2 = np.array([random.choice([-1, 1]) for i in range(3)])
s2 = np.expand_dims(s2, axis=-1)
s2.reshape(1, 4); t2.reshape(3, 1)

s3 = np.array([random.choice([-1, 1]) for i in range(4)])
t3 = np.array([random.choice([-1, 1]) for i in range(3)])
s3 = np.expand_dims(s3, axis=-1)
s3.reshape(1, 4); t3.reshape(3, 1)

# training
w1 = np.multiply(s1, t1)
w2 = np.multiply(s2, t2)
w3 = np.multiply(s3, t3)

# Construction of the weight matrix
w = w1 + w2 + w3

s = np.array([0, -1, -1, 0])
print(s)
