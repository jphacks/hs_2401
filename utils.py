import json
import os
import hashlib
import uuid

DATA_FILE = "user_data.json"
ALL_DATA_FILE = "data/all_data.json"

# JSONファイルからデータを読み込み
def load_all_data(file_path=ALL_DATA_FILE):
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"{file_path} が見つかりません。")
        return {}

# ユーザーのデータファイルをロード
def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}

# データをファイルに保存
def save_data(data, file_path=DATA_FILE):
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

# ユーザーID生成
def generate_user_id():
    return str(uuid.uuid4())

# ハッシュ化
def hash_set(data):
    return {hashlib.sha256(item.encode()).hexdigest() for item in data}

# ユーザーのデータをハッシュ化
def hash_user_data(user_data):
    return {category: list(hash_set(items)) for category, items in user_data.items()}