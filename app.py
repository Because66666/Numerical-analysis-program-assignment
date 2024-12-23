from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def main():
    return render_template('main.html')

@app.route('/lag')
def lag():
    return render_template('lag.html')

@app.route('/linear')
def linear():
    return render_template('linear.html')


if __name__ == '__main__':
    app.run(debug=True)