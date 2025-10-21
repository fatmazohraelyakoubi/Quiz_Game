from flask import Flask,request,jsonify
from flask_cors import CORS

app=Flask(__name__)
CORS(app)


@app.route('/check-answer', methods=['POST'])

def check_answer():
    data=request.get_json()
    answer=data.get('answer','')

    if answer == "cooperative":
          return jsonify({"result": "correct"})  
    else:
           return jsonify({"result": "wrong"}) 



if __name__=='__main__':
    app.run(debug=True)