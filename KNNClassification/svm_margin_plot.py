import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


def plot_svm_bounndary (model,X,y):
    
    X = X.values   
    y = y.values
    
    plt.scatter(X[:,0], X[:,1],c=y,s=30,cmap='seismic')
    
    ax.plt.gca()
    xlim = ax.get_xlim()
    ylim = ax.get_ylim()

xx = np.linspace(xlim[0],xlim[1],30)
yy = np.linspace(ylim[0], ylim[1],30)
YY,XX = np.meshgrid(yy,xx)