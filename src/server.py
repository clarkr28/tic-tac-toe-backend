from flask import Flask, Response
from flask_cors import CORS
from services.tic_tac_toe_board import TicTacToeBoard
import json


'''Flask setup'''
app = Flask(__name__)
CORS(app)


@app.route('/', methods=['GET'])
def hello_world():
    return Response(response=json.dumps({'message': 'hello world!'}),
                        status=200,
                        mimetype='application/json')


@app.route('/nextmove/<board_state>/<next_move>', methods=['GET'])
def get_next_move(board_state, next_move): 
    '''given the board and next mover, perform a move and return the new board state'''
    if len(board_state) != 9:
        return Response(response=json.dumps({'message': 'invalid board'}),
                        status=400,
                        mimetype='application/json')

    # parse the board and try to perform the next move
    board = TicTacToeBoard(board_state)
    valid_move_performed = board.performMove(next_move)

    if not valid_move_performed:
        return Response(response=json.dumps({'message': 'move could not be performed'}),
                        status=400,
                        mimetype='application/json')

    return Response(response=json.dumps({'board': str(board)}),
                        status=200,
                        mimetype='application/json')



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)