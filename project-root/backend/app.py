# backend/app.py

from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_socketio import SocketIO

app = Flask(__name__)
CORS(app)
socketio = SocketIO(app, cors_allowed_origins="*")

# 仮のデータベース（メモリ上のリスト）
users = []

@app.route('/')
def index():
    return 'バックエンドサーバーが動作しています'

# ユーザー登録API
@app.route('/api/users', methods=['POST'])
def create_user():
    data = request.get_json()
    user = {
        'name': data['name'],
        'hometown': data['hometown'],
        'mbti': data.get('mbti', ''),
        'hobby': data.get('hobby',''),
        'favoriteFood':data.get('favoriteFood',''),
        'club':data.get('club',''),
        'image': data.get('image',None)
    }
    users.append(user)
    return jsonify(user), 201

# 共通点を取得するAPI (例)
@app.route('/api/common-interests', methods=['POST'])
def common_interests():
    data = request.get_json()
    # 共通点のロジックを追加 (必要に応じて)
    return jsonify({"commonInterests": []}), 200

# Socket.ioイベント
@socketio.on('connect')
def handle_connect():
    print('A user connected')

@socketio.on('disconnect')
def handle_disconnect():
    print('A user disconnected')

if __name__ == '__main__':
    socketio.run(app, port=5000)
