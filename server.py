from flask import Flask

app = Flask(__name__)


@app.route
def show_homepage:

    return render_template homepage.html


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)