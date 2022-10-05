
from urllib import request
from flask import Flask, request, json

app = Flask(__name__)

@app.route('/user', methods=['GET','POST'])
def index():
    if request.method == 'POST':

        data = request.json

        print(data)    

        with open('data.json', 'a') as outfile:
            json.dump(data, outfile)
        
        return "200"
    if request.method == 'GET':

        return data
 
if __name__ == '__main__':
    app.run(port=3005, debug=True)



