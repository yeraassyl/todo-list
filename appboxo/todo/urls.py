from django.urls import path

from .views import CategoryListView, CategoryDetail, TodoDetail, TodoList

urlpatterns = [
    path('categories', CategoryListView.as_view()),
    path('category/<int:pk>', CategoryDetail.as_view()),
    path('todos', TodoList.as_view()),
    path('todo/<int:pk>', TodoDetail.as_view())
]
