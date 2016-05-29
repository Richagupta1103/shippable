from django.conf.urls import include, url
from github.view import ResultView
from rest_framework import routers


router = routers.SimpleRouter()
urlpatterns = [
    url(r'^viewresult$', ResultView.as_view()),
    url(r'^', include(router.urls)),
]
