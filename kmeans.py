#!/usr/bin/env python

# I suppose I cannot use numpy or any ready made library here...

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

	for _ in range(max_iteration) :
		labels = []
		for i in P :
			dist_squared = [(i[0]-a)*(i[0]-a) + (i[1]-b)*(i[1]-b) for a,b in clusters]

			labels.append( argmin( dist_squared ))

		error = 0
		for k in range(n_clusters) :
			if labels.count(k) == 0 : break

			center_x = sum(P[i][0] for i in labels if i == k) / labels.count(k)
			center_y = sum(P[i][1] for i in labels if i == k) / labels.count(k)

			error += abs(center_x - clusters[0])
			error += abs(center_y - clusters[1])

			clusters[k] = (center_x, center_y)

		if error < tolerance : break

	return labels, clusters

if __name__ == '__main__' :
	test_set = [(random.randint(1,100), random.randint(1,100)) for _ in range(100)]

	labels = fit( test_set )


