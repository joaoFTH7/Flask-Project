import json
from models.games import Games
from flask import render_template

#realizar uma consulta no banco, e mostrar um JSON com os JOGOS

class JsonController:

    def json_view():
        init_dic = {}
        consult_db = Games.query.order_by(Games.id).all()
        for key in range (len(consult_db)):
            init_dic[key] = consult_db[key].gamename, consult_db[key].category, consult_db[key].console 
        
        dic_to_json = json.dumps(init_dic)
        return render_template('json_preview/json_preview.html', page_title='Preview', header_title="Json", games=dic_to_json)
