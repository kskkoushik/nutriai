from flask import Flask, request, jsonify , session
from flask_cors import CORS
from google.genai import types
import json
from reg_agent import get_details , extract_details
from mdb import delete_data, insert_data , get_data , inser_user_structured_data




app = Flask(__name__)
CORS(app)
app.secret_key = "super secret key"



@app.route('/api/chat', methods=['POST'])
def chat():
    data = request.json
    user_message = data['message']

    user_name = "RadheKrishna"

    data_user = {"name" : user_name , "message" :{'role':'user', 'content': user_message}}

    insert_data(data_user , user_name)

    updated_data = get_data(data_user['name'])

    model_response = get_details(updated_data['history'])

    model_msg = {"name" : user_name , "message" :{'role':'model', 'content': model_response}}

    insert_data(model_msg , user_name)

    if "@@@@@END CHAT@@@@@" in model_response:

        data = get_data(user_name)

        chat_str = ''''''

        for msg in data['history']:

            chat_str += f'''{msg['role']} : + {msg['content']} + "\n"
             ================================================================================================================================ '''
        
        structured_data = extract_details(chat_str)



        inser_user_structured_data(structured_data)
        delete_data(user_name)

    return jsonify({'reply': model_response})

if __name__ == '__main__':
    app.run(debug=True)