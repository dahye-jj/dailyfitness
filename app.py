from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
   return '성현님 , 광우님 수고하셨습니당~~'
if __name__=='__main__':
    import os
    app.run('0.0.0.0', port=os.environ.get('PORT',5000))