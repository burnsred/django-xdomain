from django.conf.urls import url

try:
    from django.conf.urls import patterns
except:
    def patterns(_, *urls):
        return urls

from .views import proxy, javascript, javascript_min

urlpatterns = patterns(
    "",
    url(
        regex=r"v1/proxy$",
        view=proxy,
        name="xdomain-proxy"
    ),
    url(
        regex=r"v1/xdomain.js$",
        view=javascript,
        name="xdomain-javascript"
    ),
    url(
        regex=r"v1/xdomain.min.js$",
        view=javascript_min,
        name="xdomain-javascript-min"
    )
)
