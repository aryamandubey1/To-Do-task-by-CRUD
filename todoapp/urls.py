from django.urls import path
from .import views

urlpatterns = [
    path('',views.home,name='home'),
    path('accounts/login/',views.login_view,name='login'),
    path('register/',views.register,name='register'),
    path('delete-task/<str:name>/',views.deleteTask,name='delete'),
    path('update/<str:name>/',views.Update,name='update'),
    path('undo/<str:name>/',views.UNDO,name='undooo'),
    path('logout/',views.Logoutview,name='logout')
  
]