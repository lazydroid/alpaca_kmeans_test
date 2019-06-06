## Alpaca k-means test

This came as a test task during a coding test, I was asked to write a script to calculate K-means from a 2d data set that looks like `[(1,2), (3,4) ... ]` about a few hundreds elements in size. The interface should have resemble `sklearn.kmeans` somehow, so I took the most interesting parameters from the original `sklearn` package and implemented probably not the most optimal, but working solution.

### Here's the test picture that clusters random points into 8 clusters

Cluster centers are marked with `diamond` markers and have the same color as the points that belong to the cluster.

![test picture](https://github.com/lazydroid/alpaca_kmeans_test/raw/master/kmeans.png "Random points split into 8 clusters")
