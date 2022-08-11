from app.gamebrary import server
from controllers.game import GameController
from controllers.auth import AuthController
from controllers.json_preview import JsonController
from controllers.update_game import UpdateGameController
from controllers.delete_game import DeleteGameController

server.add_url_rule("/", view_func=GameController.hello)
server.add_url_rule('/newgame', view_func=GameController.new)
server.add_url_rule('/create', view_func=GameController.create, methods=['POST'])
server.add_url_rule('/login', view_func=AuthController.login)
server.add_url_rule('/auth', view_func=AuthController.auth, methods=['POST'])
server.add_url_rule('/logout', view_func=AuthController.logout)
server.add_url_rule('/json', view_func=JsonController.json_view)
server.add_url_rule('/edit/<int:id>', view_func=UpdateGameController.edit_game)
server.add_url_rule('/updated', view_func=UpdateGameController.update_game, methods=['POST'])
server.add_url_rule('/delete/<int:id>', view_func=DeleteGameController.delete_game, methods=['DELETE', 'GET'])
server.add_url_rule('/uploads/<coverfile>', view_func=GameController.image_cover)