from flask import flask

app = flask(__name__)

# 用修饰器修饰index()函数, 让index成为/这个 url所对应的函数.
@app.route('/')
def index():
    return '<h1>Hello World!</h1>'

if __name__ == '__main__':
    app.run(debug=True)