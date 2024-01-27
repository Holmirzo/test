from flask import Flask, request, jsonify

app = Flask(__name__)


class User:
    def __init__(self, _id, _username, _password):
        self.id = _id
        self.name = _username
        self.password = _password


Users = [
    User(1, "Mirzo", "q1w2e3"),
    User(2, "Misha", "2005"),
    User(3, "Amir", "Baki"),
]


@app.route('/', methods=["GET"])
def index():
    return jsonify({"status": "server is up and running..."}), 200


@app.route('/users', methods=["GET"])
def get_all_users():

    serialized_users = []

    for task in Users:
        serialized_users.append(task.__dict__)

    return serialized_users


@app.route('/users', methods=["POST"])
def create_user():
    data = request.get_json()

    new_task = User(len(Users) + 1, data["name"], data["description"])
    Users.append(new_task)

    return jsonify(
        {
            'message': 'User created successfully'
        }
    ), 201

@app.route('/users', methods=["DELETE"])
def delete_user():

    res_id = request.get_json()

    for i in Users:
        if getattr(i, "id") == res_id['id']:
            Users.remove(i)
           
    return f'Пользователь с {res_id} был удален'

if __name__ == "__main__":
    app.run(debug=True)

