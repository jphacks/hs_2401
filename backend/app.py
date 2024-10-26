# backend/app.py

from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

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
        'mbti': data.get('mbti', '')
    }
    users.append(user)
    return jsonify(user), 201

# ユーザー一覧取得API
@app.route('/api/users', methods=['GET'])
def get_users():
    return jsonify(users), 200

if __name__ == '__main__':
    app.run(port=5000)