from flask import Flask,request,jsonify
from flask_cors import CORS
import json,random


app=Flask(__name__)
CORS(app,origin=["http://localhost:3000"])

  
with open('questions.json') as f:
    questions=json.load(f)

@app.route('/question',methods=["GET"])
def get_question():
    question=random.choice(questions)
    return jsonify(question)


@app.route('/check-answer', methods=['POST'])
def check_answer():
    data=request.get_json()
    answer=data.get('answer','').stripe()
    correct=data.get('correct_answer','').stripe()

    if answer == correct:
           return jsonify({"result": "correct"})  
    else:
           return jsonify({"result": "wrong"}) 





if __name__=='__main__':
    app.run(debug=True)