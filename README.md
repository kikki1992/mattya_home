# mattya_home
抹茶のホームページ作成
目的：(renderのお試しのため)

制作開始 2024/7/9 
requirements.txtの作成方法
pip freeze > requirements.txt

静的サイトじゃないとrender.comでは画像表示できない 2024/07/09
python freeze.py を実行してbuildする
(flaskのstaticを使用していたらpathエラーになったので"static"を"data"フォルダに名前変えて実行→buildできたのでそのまま)

@bp_index.route('/test.html/')
パスにhtmlをつけないと生成されるファイルに拡張子がつかず表示されない

2024/7/12
動的サイトで作る場合
各ページ遷移時に変数を渡して、ページを作るようにすれば、comics内のhtmlは統一できる
今回は静的サイトで作るため、各本ごとのhtmlを作成する

@bp_index.route('/test.html/')
def test():
  code = request.args.get('code')
  return render_template("/comics/再録本2020-2021.html",code=code)