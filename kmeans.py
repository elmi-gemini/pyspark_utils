
 # K-Means model:
 
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


# Graphing the variance:

#determine the range of K-s
k_range = range(1,14)

# Fit the kmeans model for each n_clusters = k
k_means_var = [KMeans(n_clusters=k).fit(hps) for k in k_range]

#pull out the cluster centers for each model
centroids = [X.cluster_centers_ for X in k_means_var]

#Calculate the Euclidean distance from each point to each cluster center:

k_euclid = [cdist(hpc, cent, 'euclidean') for cent in centroids]
dist = [np.min(ke, axis = 1) for ke in k_euclid]


#Total within-cluster sum of squares:
wcss = [sum(d**2) for d in dist]

# Total sum of squares:
tss = sum(pdist(hpc)**2)/hpc.shape[0]

#The between-cluster sum of squares:
bss = tss - wcss







