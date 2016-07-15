
 # K-Means model
 
 from sklearn.cluster import KMeans
 
 hpc = power_consumption.values
 kmeans = KMeans()
 kmeans.fit(hpc)
 

''' parameters:

n_clusters
max_iter
n_init
init
precompute_distances
tol
n_jobs
random_state

'''
