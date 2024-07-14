from flask_app.init import create_app

app = create_app()

#テスト用
if __name__ == "__main__":
    app.run(debug=True)
    #app.run(host='0.0.0.0',port=8005,debug=True)
