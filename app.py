from utils import load_all_data, load_data, save_data, hash_user_data, generate_user_id, hash_set

# グローバルデータ
all_data = load_all_data()

# ページング機能（辞書順で並べ替え、複数選択対応）
def paginate_options(options, per_page=10):
    options = sorted(options)  # 辞書順に並べ替え
    page = 1
    total_pages = (len(options) + per_page - 1) // per_page  # 総ページ数

    while True:
        start = (page - 1) * per_page
        end = start + per_page
        current_page_options = options[start:end]
        
        print(f"\n--- Page {page}/{total_pages} ---")
        for idx, option in enumerate(current_page_options, start=start + 1):
            print(f"{idx}. {option}")

        # ナビゲーションオプション
        nav = input("次へ[N]、前へ[P]、スキップ[Q]、または選択肢の番号をカンマで区切って入力: ").strip().lower()

        if not nav:  # エンターキーだけで終了
            return []
        
        elif nav.isdigit() or ("," in nav and all(part.strip().isdigit() for part in nav.split(","))):
            # 複数の番号が入力された場合も対応し、選択肢をそのまま返す
            indices = [int(idx.strip()) - 1 for idx in nav.split(",") if idx.strip().isdigit()]
            selected_options = [options[index] for index in indices if 0 <= index < len(options)]
            return selected_options  # 入力が完了したら選択肢を即時返す
        
        elif nav == "n" and page < total_pages:
            page += 1
        elif nav == "p" and page > 1:
            page -= 1
        elif nav == "q":
            return []  # スキップして全オプションを表示
        else:
            print("無効な入力です。もう一度試してください。")

# ユーザーを追加
def add_user(display_name, user_data):
    data = load_data()
    user_id = generate_user_id()
    data[user_id] = {
        "display_name": display_name,
        "data": hash_user_data(user_data)
    }
    save_data(data)
    print(f"ユーザー '{display_name}' (ID: {user_id}) のデータを追加しました。")

# 特定カテゴリを更新
def update_user_category(user_id):
    data = load_data()
    if user_id not in data:
        print(f"ユーザーID '{user_id}' が存在しません。")
        return
    
    display_name = data[user_id].get("display_name", "不明なユーザー")
    print(f"\n{display_name} の現在のデータ:")
    user_data = data[user_id]["data"]
    for category, items in user_data.items():
        original_items = [item for item in all_data[category] if hash_set([item]).pop() in items]
        print(f"  {category}: {original_items}")
    
    category_to_update = input("\n更新したいカテゴリ名を入力してください (例: hobbies): ")
    if category_to_update in all_data:
        print(f"\n{category_to_update} の選択肢:")
        options = all_data[category_to_update]
        selected_options = paginate_options(options)
        
        # 選択した項目をハッシュ化して保存
        selected_items = [options[options.index(opt)] for opt in selected_options if opt in options]
        data[user_id]["data"][category_to_update] = list(hash_set(selected_items))
        save_data(data)
        print(f"{display_name} の '{category_to_update}' カテゴリを更新しました。")
    else:
        print("無効なカテゴリ名です。")

# データベースからユーザーを削除
def delete_user(user_id):
    data = load_data()
    if user_id in data:
        del data[user_id]
        save_data(data)
        print(f"ユーザーID '{user_id}' のデータを削除しました。")
    else:
        print(f"ユーザーID '{user_id}' が存在しません。")

# ユーザーの一覧を表示
def list_users():
    data = load_data()
    if data:
        print("\n登録されたユーザー一覧:")
        for idx, (user_id, user_info) in enumerate(data.items(), start=1):
            display_name = user_info.get("display_name", "不明なユーザー")
            print(f"  {idx}. {display_name} (ID: {user_id})")
        return list(data.keys())
    else:
        print("\nユーザーが登録されていません。")
        return []

# ユーザーデータの表示
def display_user_data(user_id):
    data = load_data()
    user_data = data.get(user_id, None)
    if user_data:
        display_name = user_data.get("display_name", "不明なユーザー")
        print(f"\n{display_name} のデータ:")
        for category, items in user_data["data"].items():
            original_items = [item for item in all_data[category] if hash_set([item]).pop() in items]
            print(f"  {category}: {original_items}")
    else:
        print(f"ユーザーID '{user_id}' のデータが見つかりません。")

# 秘匿共通集合演算を実行
def perform_private_set_intersection(user_id1, user_id2):
    data = load_data()
    user_data1 = data.get(user_id1, {}).get("data", {})
    user_data2 = data.get(user_id2, {}).get("data", {})

    common_data = {}
    for category in user_data1.keys() & user_data2.keys():
        set1 = set(user_data1[category])
        set2 = set(user_data2[category])
        common_data[category] = list(set1 & set2)

    common_data_count = 0
    if common_data:
        print("\n共通の項目:")
        for category, items in common_data.items():
            if len(items) != 0:
                original_items = [item for item in all_data[category] if hash_set([item]).pop() in items]
                print(f"  {category}: {original_items}")
                common_data_count += 1
    else:
        print("\n共通の項目はありません。")
    print("一致率：" + str(100*common_data_count/len(common_data)) + "%")

# ユーザー入力によるデータ作成（ページング機能を適用）
def create_user_data():
    user_data = {}
    print("ユーザーデータを作成してください。各カテゴリに対して番号をカンマで区切って選択してください。")
    for category, options in all_data.items():
        print(f"\n{category} の選択肢:")
        
        # ページング機能を使用してカテゴリを表示
        selected_options = paginate_options(options)
        
        # 選択した項目をリストに追加
        selected_items = [options[options.index(opt)] for opt in selected_options if opt in options]
        user_data[category] = selected_items
    
    return user_data

# メインの実行部分
if __name__ == "__main__":
    while True:
        print("\n--- メニュー ---")
        print("1. ユーザーの追加")
        print("2. 秘匿共通集合演算を実行")
        print("3. ユーザーの特定カテゴリを更新")
        print("4. ユーザーの削除")
        print("5. ユーザー一覧の表示")
        print("6. ユーザーデータの表示")
        print("7. 終了")
        
        choice = input("選択肢を入力してください: ")
        
        if choice == "1":
            display_name = input("表示名を入力してください: ")
            user_data = create_user_data()
            add_user(display_name, user_data)
        
        elif choice == "2":
            users = list_users()
            if len(users) >= 2:
                user_idx1 = int(input("\n最初のユーザーの番号を選択してください: ")) - 1
                user_idx2 = int(input("比較する2番目のユーザーの番号を選択してください: ")) - 1
                if 0 <= user_idx1 < len(users) and 0 <= user_idx2 < len(users):
                    perform_private_set_intersection(users[user_idx1], users[user_idx2])
                else:
                    print("無効な番号です。")
            else:
                print("ユーザーが2人以上必要です。")

        elif choice == "3":
            users = list_users()
            if users:
                user_idx = int(input("\n更新するユーザーの番号を選択してください: ")) - 1
                if 0 <= user_idx < len(users):
                    update_user_category(users[user_idx])
                else:
                    print("無効な番号です。")
        
        elif choice == "4":
            users = list_users()
            if users:
                user_idx = int(input("\n削除するユーザーの番号を選択してください: ")) - 1
                if 0 <= user_idx < len(users):
                    delete_user(users[user_idx])
                else:
                    print("無効な番号です。")

        elif choice == "5":
            list_users()
        
        elif choice == "6":
            users = list_users()
            if users:
                user_idx = int(input("\n表示するユーザーの番号を選択してください: ")) - 1
                if 0 <= user_idx < len(users):
                    display_user_data(users[user_idx])
                else:
                    print("無効な番号です。")

        elif choice == "7":
            print("終了します。")
            break
        else:
            print("無効な選択です。もう一度入力してください。")