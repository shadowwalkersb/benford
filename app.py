from flask import Flask, render_template, request


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


if __name__ == '__main__':
	app.run(host='0.0.0.0')
