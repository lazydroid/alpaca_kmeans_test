#!/usr/bin/env python

# I suppose I cannot use numpy or any ready-made library here...

import matplotlib.pyplot as plt

import random

def argmin( A ) :
	return A.index( min(A) )

def fit( P, n_clusters = 8, max_iteration = 300, tolerance = 0.0001 ) :
	'''
	P -- the source data [(1,2),(3,4)...]
	n_clusters -- the number of clusters / centroids
	max_iteration -- run for this many times
	tolerance -- unless the error becomes less than this
	'''

	# init cluster centers
	clusters = [(i,i) for i in range(n_clusters)]

	# rearrange points in the clusters
	for _ in range(max_iteration) :
		labels = []
		for i in P :
			dist_squared = [(i[0]-a)*(i[0]-a) + (i[1]-b)*(i[1]-b) for a,b in clusters]

			labels.append( argmin( dist_squared ))	# assign to the closest cluster

		# now move the clusters to the new positions
		error = 0
		for k in range(n_clusters) :
			if labels.count(k) == 0 : continue

			center_x = sum(a[0] for a,b in zip(P, labels) if b == k) / labels.count(k)
			center_y = sum(a[1] for a,b in zip(P, labels) if b == k) / labels.count(k)

			error += abs(center_x - clusters[k][0])
			error += abs(center_y - clusters[k][1])

			clusters[k] = (center_x, center_y)

		# cumulative cluster movement within tolerance, exit early
		if error < tolerance : break

	return labels, clusters

if __name__ == '__main__' :
	# make a test set
	test_set = [(random.randint(1,100), random.randint(1,100)) for _ in range(100)]

	labels, clusters = fit( test_set )

	print labels
	print clusters

	# cluster colors
	clrs = ['#1f77b4', '#aec7e8', '#ff7f0e', '#ffbb78', '#2ca02c',
		'#98df8a', '#d62728', '#ff9896', '#9467bd', '#c5b0d5',
		'#8c564b', '#c49c94', '#e377c2', '#f7b6d2', '#7f7f7f',
		'#c7c7c7', '#bcbd22', '#dbdb8d', '#17becf', '#9edae5']

	# make a single large picture
	fig, ax = plt.subplots(1, 1, figsize=(14, 12), facecolor='white')

	# draw the colored points
	plt.scatter( [i[0] for i in test_set], [i[1] for i in test_set], c=[clrs[i%len(clrs)] for i in labels], s=40)	#, alpha=0.8 )

	# draw the centroids
	plt.scatter( [i[0] for i in clusters], [i[1] for i in clusters], marker='D', c=[clrs[i%len(clrs)] for i in range(len(clusters))], s=150)

	# remove white frame around the picture
	fig.tight_layout()

	plt.show()
