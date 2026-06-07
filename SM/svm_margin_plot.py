import numpy as np
import matplotlib.pyplot as plt
from sklearn.svm import SVC

def plot_svm_boundary(clf, X, y, ax=None):
    """
    Plots the decision boundary, margins, and support vectors for a trained SVM classifier.
    
    Parameters:
    -----------
    clf : sklearn.svm.SVC
        A trained Support Vector Machine classifier.
    X : ndarray of shape (n_samples, 2)
        The input features (must be 2D for visualization).
    y : ndarray of shape (n_samples,)
        The target labels.
    ax : matplotlib.axes.Axes, optional
        An existing axes object to plot onto. If None, a new plot is created.
    """
    if ax is None:
        ax = plt.gca()

    # 1. Scatter plot the data points
    ax.scatter(X[:, 0], X[:, 1], c=y, s=50, cmap='autumn', edgecolors='k', zorder=3)

    # 2. Extract plot limits to create a grid
    xlim = ax.get_xlim()
    ylim = ax.get_ylim()

    # 3. Create a grid of points to evaluate the model
    xx = np.linspace(xlim[0], xlim[1], 30)
    yy = np.linspace(ylim[0], ylim[1], 30)
    YY, XX = np.meshgrid(yy, xx)
    xy = np.vstack([XX.ravel(), YY.ravel()]).T
    
    # Get the decision function values for the grid
    Z = clf.decision_function(xy).reshape(XX.shape)

    # 4. Plot decision boundary and margins
    # levels=[-1, 0, 1] corresponds to the negative margin, decision boundary, and positive margin
    ax.contour(XX, YY, Z, colors='k', levels=[-1, 0, 1], alpha=0.5,
               linestyles=['--', '-', '--'], linewidths=[1, 2, 1])

    # 5. Highlight the Support Vectors
    ax.scatter(clf.support_vectors_[:, 0], clf.support_vectors_[:, 1], s=150,
               linewidth=1.5, facecolors='none', edgecolors='black', 
               label='Support Vectors', zorder=2)
    
    ax.set_title("SVM Decision Boundary & Margin")
    ax.legend(loc='best')


# ==========================================
# EXAMPLE USAGE (Optional test block)
# ==========================================
if __name__ == "__main__":
    from sklearn.datasets import make_blobs

    # Generate synthetic, linearly separable data
    X, y = make_blobs(n_samples=50, centers=2, random_state=42, cluster_std=1.2)

    # Train a linear SVM
    model = SVC(kernel='linear', C=1.0)
    model.fit(X, y)

    # Setup the plot
    plt.figure(figsize=(8, 6))
    
    # Call the function
    plot_svm_boundary(model, X, y)
    
    # Show the result
    plt.show()