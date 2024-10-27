import hashlib
import random

# 各カテゴリのサンプルデータ
all_data = {
    "hobbies": ["biking", "hot springs", "running", "hiking", "coding", "reading", "cooking", "swimming", "gaming", "traveling"],
    "mbti": ["INTJ", "ENFP", "ISTP", "ISFJ", "ENTJ", "INFP", "ESTJ", "INFJ", "ESFP", "ISTJ"],
    "movies": ["Inception", "The Matrix", "Parasite", "Interstellar", "Avengers", "Forrest Gump", "The Godfather", "Spirited Away", "Titanic", "Joker"],
    "foods": ["sushi", "pizza", "burger", "ramen", "pasta", "steak", "salad", "curry", "sandwich", "tacos"],
    "sports": ["soccer", "basketball", "tennis", "baseball", "swimming", "running", "golf", "boxing", "cycling", "yoga"],
    "manga": ["One Piece", "Naruto", "Attack on Titan", "My Hero Academia", "Demon Slayer", "Death Note", "Dragon Ball", "Bleach", "Fullmetal Alchemist", "Hunter x Hunter"]
}

# 複数のユーザーのデータを生成
num_users = 5  # 例として5ユーザーを設定
user_data = {}

for i in range(1, num_users + 1):
    # 各カテゴリごとにランダムな項目を選択
    interests = {category: random.sample(items, k=random.randint(1, 3)) for category, items in all_data.items()}
    user_data[f"user_{i}"] = interests

# ハッシュ化関数
def hash_set(data):
    """リスト内のデータをハッシュ化してセットで返す"""
    return {hashlib.sha256(item.encode()).hexdigest() for item in data}

# 各ユーザーのデータをカテゴリごとにハッシュ化
hashed_user_data = {user: {category: hash_set(items) for category, items in interests.items()} for user, interests in user_data.items()}

# 特定の2ユーザー間で共通集合を計算する関数
def calculate_psi(user1, user2):
    common_items = {}
    inverse_map = {hashlib.sha256(item.encode()).hexdigest(): item for category, items in all_data.items() for item in items}
    # 各カテゴリごとに共通集合を抽出
    for category in all_data.keys():
        intersection = hashed_user_data[user1][category].intersection(hashed_user_data[user2][category])
        common_items[category] = [inverse_map[hashed] for hashed in intersection if hashed in inverse_map]
    return common_items

# 各ユーザーのデータを表示
print("ユーザーデータ:")
for user, interests in user_data.items():
    print(f"{user}:")
    for category, items in interests.items():
        print(f"  {category}: {items}")

# 特定の2ユーザー間の共通項目を抽出
user1 = "user_1"
user2 = "user_2"
common_items = calculate_psi(user1, user2)

# 結果の表示
print(f"\n{user1} と {user2} のカテゴリごとの共通項目:")
for category, items in common_items.items():
    print(f"  {category}: {items}")