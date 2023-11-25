from flask_restful import Resource


abilities = ['Python', 'Java', 'Flask', 'PHP', 'JavaScript']


class Abilities(Resource):
    def get(self):
        return abilities
