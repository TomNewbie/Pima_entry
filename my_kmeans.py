import numpy as np
from itertools import permutations
from sklearn import datasets
from matplotlib import pyplot


def centroids_random_select(X, n_clusters):
    return X[np.random.choice(X.shape[0], size=n_clusters, replace=False), :]


def centroids_smart_select(X, n_clusters):
  k = np.random.randint(X.shape[0])
  centroids_pos = np.array([X[k]])
  dist = np.zeros(X.shape[0])
  for i in range(1, n_clusters):
    for j in range (X.shape[0]):
      _ , dist[j] = find_nearest_centroid(X[j], centroids_pos)
    t = np.argmax(dist)
    centroids_pos = np.append(centroids_pos, X[t].reshape(1,2), axis = 0)
  """
  Input:
  X: numpy array, dimension (n, d) - dataset
  n_clusters: int - so cum (clusters)
  Output:
  centroids: numpy array, dimension (n_cluster, d)
            - cac centroid duoc chon de bat dau thuat toan
  """
  return centroids_pos # Day la output sai, hay sua lai cho dung


def find_nearest_centroid(x, centroids):
  row = centroids.shape[0]
  dist = np.zeros((row))
  for j in range (row):
    dist[j]= np.linalg.norm(x-centroids[j])
  label_x= np.argmin(dist)
  distance_x = dist[label_x]
  """
  Input:
  x: numpy array, dimension (d, ) - diem data
  centroids: numpy array, dimension (n_clusters, d) - cac centroid hien tai
  Output:
  label_x: int - so thu tu centroid gan x nhat (trong khoang 0...n_clusters)
  distance_x: float64 - khoang cach tu x den centroid gan x nhat
  """
  return label_x, distance_x  # Day la output sai, hay sua lai cho dung


def find_new_centroid(X, labels, j):
  # new_centroid_j = np.zeros((labels.shape[0], X.shape[1]))
  cluster_k = np.where(labels == j)
  sum = np.sum(X[cluster_k], axis =0)
  new_centroid_j = sum / (X[cluster_k].shape[0])
  """
  Input:
  X: numpy.ndarray, dimension (n, d) - dataset
  labels: numpy.ndarray, dimension (n, ) - array chua cluster hien tai cua tung diem data
          (Voi diem data X[i], labels[i] = so thu tu cua cluster dang chua X[i])
  j: int (trong khoang 0...n_clusters) - so thu tu cua cluster dang can update centroid
  Output:
  new_centroid_j: numpy.ndarray, dimension (d, ) - centroid moi cua cluster thu j
  """
  return new_centroid_j  # Day la output sai, hay sua lai cho dung


def my_kmeans(X, n_clusters, max_iter=100, smart=False):
    # Khoi tao cac centroid ban dau bang cach chon ngau nhien
    centroids = (
        centroids_smart_select(X, n_clusters) if smart
        else centroids_random_select(X, n_clusters)
    )
    labels = - np.ones(X.shape[0])  # khoi tao bang vector [-1, -1, ..., -1]
    for iteration in range(max_iter):
        # voi moi diem data X[i], tim centroid gan nhat cho X[i]
        for i in range(X.shape[0]):
            labels[i], _ = find_nearest_centroid(X[i], centroids)
        # voi moi cluster j, cap nhat lai centroid cho cluster j
        new_centroids = np.empty((n_clusters, X.shape[1]))
        for j in range(n_clusters):
            new_centroids[j] = find_new_centroid(X, labels, j)
        # neu cac centroid da cap nhat van bang cac centroid cu thi dung lai
        if np.sum((centroids - new_centroids) ** 2) < 1e-200:
            break
        else:
            centroids = new_centroids
    return centroids, labels
