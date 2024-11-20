from flask import Flask,jsonify,request

app = Flask(__name__)

todo_list = [
    {"task_id": 1, "task": "Buy groceries", "due_date": "2024-11-21", "priority": "High", "status": "Pending"},
    {"task_id": 2, "task": "Complete Python project", "due_date": "2024-11-25", "priority": "Medium", "status": "In Progress"},
    {"task_id": 3, "task": "Attend team meeting", "due_date": "2024-11-22", "priority": "High", "status": "Pending"},
    {"task_id": 4, "task": "Read Data Science book", "due_date": "2024-11-30", "priority": "Low", "status": "Not Started"},
    {"task_id": 5, "task": "Submit assignment", "due_date": "2024-11-20", "priority": "High", "status": "Completed"},
    {"task_id": 6, "task": "Clean the house", "due_date": "2024-11-23", "priority": "Medium", "status": "Pending"}
]

@app.route("/")
def home():
    return "Welcome to Our home page"

@app.route("/items",methods=["GET"])
def get_items():
    return jsonify(todo_list)

@app.route("/items/<int:item_id>",methods=["GET"])
def get_item(item_id):
    item = next((item for item in todo_list if item["task_id"]==item_id),None)
    if item is None:
        return jsonify({"error":"item not found"})
    return jsonify(item)

@app.route("/items",methods =["POST"])
def create_item():
    if not request.json or not 'task' in request.json:
        return jsonify({"error":"item is not found"})
    new_item = {
        "task_id": todo_list[-1]["task_id"] + 1 if todo_list else 1,
        "task":request.json['task'],
        "due_date": request.json['due_date'],
        "priority": request.json['priority'],
        "status" : request.json['status']
    }
    todo_list.append(new_item)
    return jsonify(new_item)

@app.route("/items/<int:item_id>", methods =["PUT"])
def update_item(item_id):
    item = next((item for item in todo_list if item["task_id"]==item_id),None)
    if item is None:
        return jsonify({"error":"item not found"})
    item['task'] = request.json.get('task',item['task'])
    item['due_date'] = request.json.get('due_date',item['due_date'])
    item['priority'] = request.json.get('priority',item['priority'])
    item['status'] = request.json.get('status',item['status'])
    return jsonify(item)

@app.route("/items/<int:item_id>", methods =["DELETE"])
def delete_item(item_id):
    global todo_list
    todo_list = [item for item in todo_list if item["task_id"] != item_id]
    return jsonify({"result":"item deleted"})

if __name__ == "__main__":
    app.run(debug=True)