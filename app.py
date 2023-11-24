from flask import Flask
from flask import jsonify
from flask import request
import json


app = Flask(__name__)

dev_list = [
    {
     "id": "0",
     "name": "Italo",
     "abilities": ["Python", "Flask"]},

    {
     "id": "1",
     "name": "George",
     "abilities": ["Python", "Django"]}
]


# Return a developer by ID, alter and delete a developer too
@app.route("/dev/<int:id>/", methods=["GET", "PUT", "DELETE"])
def developer(id):
    if request.method == "GET":
        try:
            response = dev_list[id]
        except IndexError:
            message = "Desenvolvedor de id {} não existe".format(id)
            response = {"status": "error", "message": message}
        except Exception:
            message = "Erro desconhecido"
            response = {"status": "error", "message": message}
        return jsonify(response)
    elif request.method == "PUT":
        datas = json.loads(request.data)
        dev_list[id] = datas
        return jsonify(datas)
    elif request.method == "DELETE":
        dev_list.pop(id)
        return jsonify({"status": "success", "message": "Registro excluído"})


# List all developers and includes a new developer
@app.route("/dev/", methods=["POST", "GET"])
def list_devs():
    if request.method == "POST":
        datas = json.loads(request.data)
        position = len(dev_list)
        datas["id"] = position
        dev_list.append(datas)
        return jsonify(dev_list[position])
    elif request.method == "GET":
        return jsonify(dev_list)


if __name__ == '__main__':
    app.run(debug=True)
