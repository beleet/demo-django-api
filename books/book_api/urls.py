from . import views
from django.urls import path

urlpatterns = [
    path('', views.BookAPIList.as_view()),
    path('<int:pk>/', views.BookAPIRetrieve.as_view()),
    path('create/', views.BookAPICreate.as_view()),
    path('update/<int:pk>/', views.BookAPIUpdate.as_view()),
    path('destroy/<int:pk>/', views.BookAPIDestroy.as_view())
]
