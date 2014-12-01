from sklearn.cluster import KMeans

# loads data from file
# input: tab delimited file where each line is a sample. Each tab is a feature
# output: array of arrays 
def load_data(filename):
	data = []
	with open(filename) as fin:
		for l in fin:
			data_line = l.strip().split()
			data.append(map(lambda x : float(x), data_line))
	return data

# build k means model
# input:
#	n_clusters = number of clusters to generate
#	data = data input
#	n_init = number of times k means will run
def build_k_means_model(n_clusters, data, n_init=10):
	estimator = KMeans(init='k-means++', n_clusters=n_clusters, n_init=n_init)
	estimator.fit(data)
	return estimator

# score a trained model. Given a model and data, assign labels to the data
# input:
#	model = trained model
# 	data = data to label
# output:
#	labels = array of labels for each sample in data
def score_model(model, data):
	return model.predict(data)



