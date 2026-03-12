import numpy as np
def k_means_centroid_update(points, assignments, k):
    """
    Compute new centroids as the mean of assigned points.
    Number of clusters: k
    
    """
    # Write code here
    points, assignments = np.asarray(points), np.asarray(assignments)
    return np.array([points[assignments == j].mean(axis=0) for j in range(k)]).tolist()