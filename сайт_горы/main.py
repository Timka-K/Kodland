from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
 return render_template('index.html')


@app.route('/mountain')
def mountain():
    return render_template('mountain.html')


@app.route('/mountain1')
def mountain1():
    return render_template('mountain1.html')


if __name__ == '__main__':
 app.run(debug=True)
