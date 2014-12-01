import pygal
import os

def get_x_bounds(data):
	min_x = None
	max_x = None
	for d in data:
		if min_x == None or d[0] < min_x:
			min_x = d[0]
		if max_x == None or d[0] > max_x:
			max_x = d[0]
	return (min_x, max_x)


def create_cluster_chart(data, labels): 

	config = pygal.Config()
	config.js.append(os.path.join(os.getcwd(), "static", "line.js"))
	config.css.append(os.path.join(os.getcwd(), "static", "line.css"))
	line_chart = pygal.Line(config)
	line_chart.title = 'Line Clusters'

	bounds = get_x_bounds(data)
	num_x = bounds[1] - bounds[0] + 1
	num_x = int(num_x)
	print "bounds are %s" % (bounds,)

	line_chart.x_labels = map(str, range(int(bounds[0]), int(bounds[1]) + 1))
	for (d, l) in zip(data, labels):
		# set all values to be None at first
		values = [None] * num_x
		# set the y coordinate of the x coordinate
		values[int(d[0])] = d[1]
		# if the data point is not at 0, set the 0th point to 0
		if d[0] != 0:
			values[0] = 0

		line_chart.add(str(d) + "#" + str(l), values)
	return line_chart.render_to_file('output1.svg')
