from flask import Flask
from basic_k_means import *
from chart_creator import *
import os

app = Flask(__name__,
	static_folder=os.path.join(os.getcwd(), 'static'))

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/chart")
def chart():
	data = load_data('basic_k_means_input.txt')
	model = build_k_means_model(3, data)
	result = score_model(model, data)
	print result
	return create_cluster_chart(data, result)


if __name__ == "__main__":
	data = load_data('basic_k_means_input.txt')
	model = build_k_means_model(4, data)
	result = score_model(model, data)
	print result
	create_cluster_chart(data, result)
	#app.run()
