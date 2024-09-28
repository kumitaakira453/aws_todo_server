import requests

# APIのベースURL
BASE_URL = "http://127.0.0.1:8000/default/todo/"


def test_get_todos():
    response = requests.get(BASE_URL)
    if response.status_code == 200:
        print("GETリクエスト成功:", response.json())
    else:
        print("GETリクエスト失敗:", response.status_code, response.text)


def test_create_todo():
    # TODOアイテムのデータ
    todo_data = {
        "change_type": "create_new",
        "title": "テストタスク",
        "detail": "テストタスクの詳細",
        "deadLine": "2024-09-30",
        "is_done": False,
        "is_deleted": False,
    }
    response = requests.post(BASE_URL + "update_account_book/", json=todo_data)
    if response.status_code in (200, 201):
        print("POSTリクエスト成功:", response.json())
    else:
        print("POSTリクエスト失敗:", response.status_code, response.text)


if __name__ == "__main__":
    test_get_todos()  # GETリクエストのテスト
    test_create_todo()  # POSTリクエストのテスト
