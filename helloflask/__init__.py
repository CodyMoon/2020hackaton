from flask import Flask, make_response,g, Response
from flask import render_template, Markup

app = Flask(__name__)
app.debug = True
app.jinja_env.trim_blocks = True

@app.route('/res1')
def res1():
    custom_res = Response("Custom Response", 200, {'test': 'ttt'})
    return make_response(custom_res)

# @app.before_request
# def before_request():
#     print("before_request!!!")  #/gg 로 다음페이지를 넘길수있음.
#     g.str="Korean"

@app.route("/tmpl")
def t():
    tit = Markup("<strong>Title</strong>")
    mu = Markup("<h1>iii = <i>%s</i></h1>")
    h = mu % "Italic"
    print("h=", h)

    lst = [("Meet1", "kim"), ("meet2", "sa")]
    
    return render_template('index.html', title=tit, mu = h, lst = lst)

@app.route("/gg")
def helloworld2():
    return "Hello World!" + getattr(g,'str','111')

@app.route("/")
def helloworld():
    return "Hello Flask World!"

