from django.urls import re_path

from .views import proxy, javascript, javascript_min

urlpatterns = [
    re_path(r"v1/proxy$", proxy, name="xdomain-proxy"),
    re_path(r"v1/xdomain.js$", javascript, name="xdomain-javascript"),
    re_path(r"v1/xdomain.min.js$", javascript_min, name="xdomain-javascript-min")
]
