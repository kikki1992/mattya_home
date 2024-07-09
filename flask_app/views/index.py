from flask import Flask,Blueprint 
from flask import render_template,send_file,request,redirect,url_for,session #templatesのファイルを読み込む関数

bp_index = Blueprint('index', __name__, url_prefix='/')

@bp_index.route('/')
def hello_world():
    return render_template("index.html") 
