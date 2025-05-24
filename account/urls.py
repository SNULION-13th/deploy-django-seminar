from django.urls import path
## 수정
from .views import SignOutView, SignUpView, SignInView, TokenRefreshView, UserInfoView


app_name = "account"
urlpatterns = [
    # CBV url path
    path("signup/", SignUpView.as_view()),
    path("signin/", SignInView.as_view()),
    path("refresh/", TokenRefreshView.as_view()),
    path("signout/", SignOutView.as_view()),
    ## 추가
    path("info/", UserInfoView.as_view()),
		## /account/info 를 통해 접근 가능!
]
