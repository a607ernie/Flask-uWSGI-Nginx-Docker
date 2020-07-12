#!/usr/bin/env python

from app import create_app

app = create_app()

@app.route('/',methods=['GET'])
def index():
    return """
    <h1>Python Flask in Docker!</h1>
    <p>A sample web-app for running Flask inside Docker.</p>
    <p>API list :<p> 
    <li>[GET]  /hi
    <li>[POST] /post_name
    """

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000,debug=True)

