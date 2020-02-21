from flask import Flask
from flask_restful import Api, Resource, reqparse
from werkzeug.serving import run_simple
import cherrypy

app = Flask(__name__)
api = Api(app)

contato = [
	{
		"name": "John Wick",
		"idade": 39,
		"telefone": 3344-3333,
	},
	
	{
		"name": "Joao",
		"idade": 43,
		"telefone": 5544-5678,
	}
]

class Users(Resource):
	def get(self, name):
	    for i in contato:
	        if(name == i["name"]):
		    return i, 200
	    return "User not fount", 404

	def post(self, name):
	    parser = reqparse.RequestParser()
            parser.add_argument("idade")
	    parser.add_argument("telefone")
            args = parser.parse_args()
	
	    for i in contato:
		if(name == i["name"]):
		    return "User with name {} already exists".format(name), 400
	
            i = {
	      "name": name,
	      "idade": args["idade"],
	       "telefone": args["telefone"],
            }
	    contato.append(i)
	    return i, 201

	def put(self, name):
	    parser = reqparse.RequestParser()
            parser.add_argument("idade")
	    parser.add_argument("telefone")
	    args = parser.parse_args()
	
	    for i in contato:
		if(name == i["name"]):
		    i["idade"] = args["idade"]
	            i["telefone"] = args["telefone"]
		    return i, 200
	    i = {
	     "name": name,
	     "idade": args["idade"],
	     "telefone": args["telefone"],
	    }
	    contato.append(i)
	    return i, 201

	def delete(self, name):
	    global contato
	    contato = [i for i in contato if i["name"] != name]
	    return "{} is deleted,".format(name), 200


#Para rodar a api
api.add_resource(Users, "/i/<string:name>")

#app.run(debug=True,port=8080)
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
