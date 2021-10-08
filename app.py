from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route('/')
def render_index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
