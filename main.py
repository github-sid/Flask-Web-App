from website import create_app

app = create_app()

if __name__ == '__main__':
    # Every time the file changes the web server will be restarted since debug = True
    app.run(debug=True)
