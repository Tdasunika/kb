from flask import Flask, request, jsonify
import json

app = Flask(__name__)

# load knowledge base
with open('C:\\Users\\HIYATH\\OneDrive\\Desktop\\knowledgebase\\fa.json', 'r') as file:
    knowledge_base = json.load(file)

def find_condition_by_keyword(keyword):
    for item in knowledge_base["intents"]:
        if keyword.lower() in (kw.lower() for kw in item["patterns"]):
            return item
    return None

@app.route('/condition',methods=['GET'])
def get_condition():
    keyword = request.args.get('keyword')
    condition = find_condition_by_keyword(keyword)
    if condition:
        response = {
            "condition": condition["condition"],
            "emergency_help": condition["emergency_help"],
            "first_aid": condition["first_aid"],
            "warning": condition["warning"]
        }
        return jsonify(response)
    else:
        return jsonify({"error": "Condition not found"}), 404
    
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')