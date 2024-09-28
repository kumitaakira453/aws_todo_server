# from rest_framework import viewsets
# from rest_framework.decorators import action
# from rest_framework.response import Response

# from .models import Todo
# from .serializers import TodoSerializer


# class TodoViewSet(viewsets.ViewSet):
#     def list(self, request):
#         todos = Todo.objects.filter(is_deleted=False)
#         serializer = TodoSerializer(todos, many=True)
#         return Response({"Items": serializer.data})

#     @action(detail=False, methods=["post"])
#     def update_account_book(self, request):
#         post_type = request.data.get("post_type")
#         if post_type == "create_new":
#             serializer = TodoSerializer(data=request.data)
#             if serializer.is_valid():
#                 serializer.save()
#                 return Response({"message": "Todo created successfully!"}, status=201)
#             return Response(serializer.errors, status=400)

#         elif post_type == "update_content":
#             todo_id = request.data.get("id")
#             try:
#                 todo = Todo.objects.get(id=todo_id)
#                 serializer = TodoSerializer(todo, data=request.data, partial=True)
#                 if serializer.is_valid():
#                     serializer.save()
#                     return Response(
#                         {"message": "Todo updated successfully!"}, status=200
#                     )
#                 return Response(serializer.errors, status=400)
#             except Todo.DoesNotExist:
#                 return Response({"error": "Todo not found."}, status=404)
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Todo
from .serializers import TodoSerializer


class TodoViewSet(viewsets.ViewSet):
    # GETメソッドでis_deleted=FalseのTodoを返す
    def list(self, request):
        todos = Todo.objects.filter(is_deleted=False)
        serializer = TodoSerializer(todos, many=True)
        return Response({"Items": serializer.data})

    # POSTメソッドで様々なアクションを処理
    @action(detail=False, methods=["post"])
    def update_todo(self, request):
        post_type = request.data.get("post_type")

        # create_new: 新しいTodoを作成する
        if post_type == "create_new":
            serializer = TodoSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(
                    {"message": "Todo created successfully!"},
                    status=status.HTTP_201_CREATED,
                )
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # update_content: idを必須としてtitle, detail, deadLineを更新する
        elif post_type == "update_content":
            todo_id = request.data.get("id")
            try:
                todo = Todo.objects.get(id=todo_id)
                # partial=Falseなので必須フィールドの全てを渡す必要がある
                serializer = TodoSerializer(todo, data=request.data, partial=False)
                if serializer.is_valid():
                    serializer.save()
                    return Response(
                        {"message": "Todo updated successfully!"},
                        status=status.HTTP_200_OK,
                    )
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            except Todo.DoesNotExist:
                return Response(
                    {"error": "Todo not found."}, status=status.HTTP_404_NOT_FOUND
                )

        # update_is_done: idを必須としてis_doneを更新する
        elif post_type == "update_is_done":
            todo_id = request.data.get("id")
            is_done = request.data.get("is_done")
            try:
                todo = Todo.objects.get(id=todo_id)
                todo.is_done = is_done
                todo.save()
                return Response(
                    {"message": "Todo is_done updated successfully!"},
                    status=status.HTTP_200_OK,
                )
            except Todo.DoesNotExist:
                return Response(
                    {"error": "Todo not found."}, status=status.HTTP_404_NOT_FOUND
                )

        # update_is_deleted: idを必須としてis_deletedをFalseにする
        elif post_type == "update_is_deleted":
            todo_id = request.data.get("id")
            try:
                todo = Todo.objects.get(id=todo_id)
                todo.is_deleted = True
                todo.save()
                return Response(
                    {"message": "Todo is_deleted updated successfully!"},
                    status=status.HTTP_200_OK,
                )
            except Todo.DoesNotExist:
                return Response(
                    {"error": "Todo not found."}, status=status.HTTP_404_NOT_FOUND
                )

        # 不明なpost_typeが渡された場合
        else:
            return Response(
                {"error": "Invalid post_type."}, status=status.HTTP_400_BAD_REQUEST
            )
