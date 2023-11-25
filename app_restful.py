import json
from flask import Flask
from flask import request
from flask_restful import Resource
from flask_restful import Api
from abilities import Abilities


app = Flask(__name__)
api = Api(app)

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


class Developer(Resource):
    def get(self, id):
        try:
            response = dev_list[id]
        except IndexError:
            message = "Desenvolvedor de id {} não existe".format(id)
            response = {"status": "error", "message": message}
        except Exception:
            message = "Erro desconhecido"
            response = {"status": "error", "message": message}
        return response

    def put(self, id):
        datas = json.loads(request.data)
        dev_list[id] = datas
        return datas

    def delete(self, id):
        dev_list.pop(id)
        return {"status": "success", "message": "Registro excluído"}


class DevList(Resource):
    def get(self):
        return Developer

    def post(self):
        datas = json.loads(request.data)
        position = len(dev_list)
        datas["id"] = position
        dev_list.append(datas)
        return dev_list[position]


api.add_resource(Developer, "/dev/<int:id>/")
api.add_resource(DevList, '/dev/')
api.add_resource(Abilities, '/abilities/')

if __name__ == "__main__":
    app.run(debug=True)
