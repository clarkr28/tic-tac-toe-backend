from flask import Flask, Response
import json

'''Flask setup'''
app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello_world():
    response = Response(response=json.dumps({'message': 'hello world!'}),
                        status=200,
                        mimetype='application/json')
    return response

@app.route('/nextmove/<board_state>/<next_move>', methods=['GET'])
def get_next_move(board_state, next_move): 
    if len(board_state) != 9:
        return Response(response=json.dumps({'message': 'invalid board'}),
                        status=400,
                        mimetype='application/json')

    board_state = f'{next_move}{board_state[1:]}'
    return Response(response=json.dumps({'board': board_state}),
                        status=200,
                        mimetype='application/json')



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)