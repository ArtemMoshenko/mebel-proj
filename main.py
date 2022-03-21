from flask import Flask
from flask import render_template
from flask import url_for

app = Flask(__name__)


@app.route('/')
def index():
    return "Колонизация Марса"

@app.route('/index')
def index2():
    return "И на Марсе будут яблони цвести!"

@app.route('/promotion')
def index3():
    return render_template("promotion.html")

@app.route('/image_sample')
def image4():
    return render_template("image_sample.html")

@app.route('/promotion_image')
def image5():
    return render_template("promotion_image.html")

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')