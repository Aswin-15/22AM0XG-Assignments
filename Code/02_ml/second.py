from flask import Flask
app=Flask(__name__)

@app.route('/')
def hello():
    return 'Hai...!, i am ' + 'BALA ASWIN B' + '7376222AD119' + 'Department of AI&DS'

if __name__=="__main__":
    app.run(host='0.0.0.0', port=5000)
