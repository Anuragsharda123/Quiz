from django.contrib import admin
from django.urls import path
from .views import createuser, home, login, verify, signup, test_series, instruction
urlpatterns = [
    path('', home.Home.as_view(), name='home'),
    path('login/', login.Login.as_view(), name='login'),
    path('logout/', login.Logout, name='logout'),
    path('createuser/', createuser.CreateUser.as_view(), name='createuser'),
    path('verify/', verify.Verify.as_view(), name='verify'),
    path('signup/', signup.Signup.as_view(), name='signup'), 
    path('test_series/', test_series.Test_Series.as_view(), name='test_series'),
    path('instruction', instruction.Instruction.as_view(), name="instruction")
    
]
