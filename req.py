import requests

# コピーしたリクエストのURL
url = "https://example.com/api/endpoint"

# コピーしたリクエストのヘッダ
headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer YOUR_ACCESS_TOKEN",
    # 他の必要なヘッダをここに追加
}

# 変更したいクエリの中身
data = {
    "key1": "new_value1",
    "key2": "new_value2",
    # 他の必要なデータをここに追加
}

# POSTリクエストの送信
response = requests.post(url, headers=headers, json=data)

# レスポンスの表示
print(response.status_code)
print(response.json())
