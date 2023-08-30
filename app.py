from flask import Flask, render_template, request
import benford


app = Flask(__name__)

fdata = None
# column = None

@app.route("/")
def index():
	return render_template('index.html')

@app.route("/upload", methods=["POST"])
def upload():
	if request.method == "POST":
		global fdata
		f = request.files['file']
		f.save('data.txt')

		fdata = f.filename

		return render_template('index.html')

@app.route("/run_benford", methods=["POST"])
def run_benford():
	col = request.form.get("column")
	benford.process_file_and_save_plot(from_file='data.txt', col=int(col), title=fdata, to_file="static/benford.png")

	return render_template('index.html')


if __name__ == '__main__':
	app.run(host='0.0.0.0')
