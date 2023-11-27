from website import create_app #from __init__.py
#You must go here to run the website
app=create_app()
if __name__ == '__main__':
    app.run(debug=True)