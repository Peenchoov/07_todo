from django.urls import path
from .views import HomePageView, AboutPageView, ContactPageView, WhatsNewPageView


urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("about/", AboutPageView.as_view(), name="about"),
    path("contact/", ContactPageView.as_view(), name="contact"),
    path("whats_new/", WhatsNewPageView.as_view(), name="whatsnew"),
]
