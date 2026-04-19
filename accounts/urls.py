from django.urls import path
from .views import (
    SignUpView,
    MyLoginView,
    MyLogOutView,
    MyPasswordChangeView,
    MyPasswordChangeDoneView,
    MyPasswordResetView,
    MyPasswordResetDoneView,
    MyPasswordResetConfirmView,
    MyPasswordResetCompleteView,
)

urlpatterns = [
    path("login/", MyLoginView.as_view(), name="login"),
    path("logout/", MyLogOutView.as_view(), name="logout"),
    path("signup/", SignUpView.as_view(), name="signup"),
    path("password_change/", MyPasswordChangeView.as_view(), name="password_change"),
    path(
        "password_change/done/",
        MyPasswordChangeDoneView.as_view(),
        name="password_change_done",
    ),
    path("password_reset/", MyPasswordResetView.as_view(), name="password_reset"),
    path(
        "password_reset/done/",
        MyPasswordResetDoneView.as_view(),
        name="password_reset_done",
    ),
    path(
        "reset/<uidb64>/<token>/",
        MyPasswordResetConfirmView.as_view(),
        name="password_reset_confirm",
    ),
    path(
        "password_reset/complete/",
        MyPasswordResetCompleteView.as_view(),
        name="password_reset_complete",
    ),
]
