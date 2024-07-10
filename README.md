# mattya_home
抹茶のホームページ作成
目的：(renderのお試しのため)

制作開始 2024/7/9 
requirements.txtの作成方法
pip freeze > requirements.txt

静的サイトじゃないとrender.comでは画像表示できない 2024/07/09
python freeze.py を実行してbuildする
(flaskのstaticを使用していたらpathエラーになったので"static"を"data"フォルダに名前変えて実行→buildできたのでそのまま)