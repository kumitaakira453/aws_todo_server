# aws-todo-back

##　 DB 構成

```python
class Todo(models.Model):
    title = models.CharField(max_length=200)
    detail = models.TextField(null=True, blank=True)  # detailが空でもOK
    deadLine = models.DateField(
        default=timezone.now
    )  # deadLineが指定されなければ今日の日付
    is_done = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.title
```

## 基本 URL

`default/todo/update_todo/`

## API エンドポイント

### 1. Todo リストの取得

- **メソッド**: `GET`
- **エンドポイント**: `/todo/`
- **説明**: 削除されていない Todo のリストを取得します。

#### レスポンス例

```json
{
  "Items": [
    {
      "id": 1,
      "title": "タスク1",
      "detail": "詳細情報1",
      "deadLine": "2024-09-30",
      "is_done": false,
      "is_deleted": false
    },
    {
      "id": 2,
      "title": "タスク2",
      "detail": "詳細情報2",
      "deadLine": "2024-10-01",
      "is_done": true,
      "is_deleted": false
    }
  ]
}
```

### 2.Todo の新規作成

- **メソッド**: `POST`
- **エンドポイント**: `/todo/update_todo`
- **説明**: 新しい todo を作成する

#### リクエスト例

```json
{
  "post_type": "create_new",
  "title": "新しいタスク",
  "detail": "タスクの詳細",
  "deadLine": "2024-10-10"
}
```

#### レスポンス例

```json
{
  "message": "Todo created successfully!"
}
```

### 3.todo の更新

- **メソッド**: `POST`
- **エンドポイント**: `/todo/update_todo`
- **説明**: 既存の todo の`title`,`detail`,`deadLine`を更新

####　リクエスト例

```json
{
  "post_type": "update_content",
  "id": 1,
  "title": "更新されたタスク",
  "detail": "更新された詳細",
  "deadLine": "2024-10-15"
}
```

####レスポンス例

```json
{
  "message": "Todo updated successfully!"
}
```

### 4.todo の完了状態の更新

- **メソッド**: `POST`
- **エンドポイント**: `/todo/update_todo`
- **説明**: todo の完了状態を更新する

####　リクエスト例

```json
{
  "post_type": "update_is_done",
  "id": 1,
  "is_done": true
}
```

#### レスポンス例

```json
{
  "message": "Todo is_done updated successfully!"
}
```

### 5.todo の削除

- **メソッド**: `POST`
- **エンドポイント**: `/todo/update_todo`
- **説明**: todo を削除済みにする(論理削除)

#### リクエスト例

```json
{
  "post_type": "update_is_deleted",
  "id": 1
}
```

#### レスポンス例

```json
{
  "message": "Todo is_deleted updated successfully!"
}
```
