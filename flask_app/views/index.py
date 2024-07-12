from flask import Flask,Blueprint 
from flask import render_template,send_file,request,redirect,url_for,session #templatesのファイルを読み込む関数

bp_index = Blueprint('index', __name__, url_prefix='/')

@bp_index.route('/')
def hello_world():
    return render_template("index.html") 

@bp_index.route('/comic_1.html/')
def comic_1():
  return render_template("/comics/comic_1.html") 

@bp_index.route('/comic_2.html/')
def comic_2():
  return render_template("/comics/comic_2.html") 