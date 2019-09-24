from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def Say_Hello():
    return 'Hello World !!'

if __name__ == '__main__':
    app.run(debug=True)
