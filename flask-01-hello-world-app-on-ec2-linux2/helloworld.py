from flask import Flask

app = Flask(__name__)

@app.route('/')             # Decorator connect app to the path
def hello():
    return "Hello World from Rafe Stefano"

if __name__=='__main__':
    #  app.run('localhost', port=5000, debug=True)
    # app.run(debug=True)
    app.run('0.0.0.0', port=80)   # Can be accessable from anywhere, port 80(HTTP)