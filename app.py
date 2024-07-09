from flask_app.init import create_app

app = create_app()

#テスト用
if __name__ == "__main__":
    app.run(debug=True)
