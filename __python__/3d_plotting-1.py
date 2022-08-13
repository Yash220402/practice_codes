tjfrom mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np


def bivariate_normal(X, Y, sigmax=1.0, sigmay=1.0,
                     mux=0.0, muy=0.0, sigmaxy=0.0):
    """
    Bivariate Gaussian distribution for equal shape *X*, *Y*.
    See `bivariate normal
    <http://mathworld.wolfram.com/BivariateNormalDistribution.html>`_
    at mathworld.
    """
    Xmu = X-mux
    Ymu = Y-muy

    rho = sigmaxy/(sigmax*sigmay)
    z = Xmu**2/sigmax**2 + Ymu**2/sigmay**2 - 2*rho*Xmu*Ymu/(sigmax*sigmay)
    denom = 2*np.pi*sigmax*sigmay*np.sqrt(1-rho**2)
    return np.exp(-z/(2*(1-rho**2))) / denom


def get_test_data(delta=0.05):
    # from matplotlib.mlab import bivariate_normal #deprecated
    x = y = np.arange(-3.0, 3.0, delta)
    X, Y = np.meshgrid(x, y)

    Z1 = bivariate_normal(X, Y, 1.0, 0.0, 0.0)
    Z2 = bivariate_normal(X, Y, 1.5, 1, 1)
    Z = Z2 - Z1

    X = X*10
    Y = Y*10
    Z = Z*500
    return X, Y, Z


fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")

x, y, z = axes3d.get_test_data(0.02)
ax.plot_wireframe(x, y, z, rstride=10, cstride=10)

plt.show()
