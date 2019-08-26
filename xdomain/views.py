import json

from django.conf import settings
from django.urls import reverse
from django.http import HttpResponse
from django.template.response import TemplateResponse
from django.views.decorators.cache import cache_control
from django.views.decorators.clickjacking import xframe_options_exempt

@xframe_options_exempt
@cache_control(public=True, max_age=3600)
def proxy(request):
    js_url = request.build_absolute_uri(reverse('xdomain-javascript-min'))
    if isinstance(settings.XDOMAIN_ORIGIN_REGEX, dict):
        return HttpResponse("""
<!DOCTYPE HTML>
<script src="{0}"></script>
<script>
xdomain.masters({1})
</script>
        """.format(js_url, json.dumps(settings.XDOMAIN_ORIGIN_REGEX)))
    else:
        return HttpResponse("""
<!DOCTYPE HTML>
<script src="{0}" data-master="{1}"></script>
        """.format(js_url, settings.XDOMAIN_ORIGIN_REGEX))

@cache_control(public=True, max_age=3600)
def javascript(request):
    return TemplateResponse(
        request,
        'xdomain/xdomain.js',
        {
            'csrf_cookie_name': settings.CSRF_COOKIE_NAME
        },
        content_type='text/javascript'
    )

@cache_control(public=True, max_age=3600)
def javascript_min(request):
    return TemplateResponse(
        request,
        'xdomain/xdomain.min.js',
        {
            'csrf_cookie_name': settings.CSRF_COOKIE_NAME
        },
        content_type='text/javascript'
    )
