from django.conf.urls import patterns, url

from .views import proxy

urlpatterns = patterns("",
    url(
        regex=r"v1/proxy$",
        view=proxy,
        name="xdomain-proxy"
    )
)