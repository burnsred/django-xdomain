from django.conf import settings
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.template.response import TemplateResponse
from django.views.decorators.cache import cache_control
from django.views.decorators.clickjacking import xframe_options_exempt

@xframe_options_exempt
@cache_control(public=True, max_age=3600)
def proxy(request):
	return HttpResponse(
		"""
<!DOCTYPE HTML>
<script src="{0}" data-master="{1}"></script>
	""".format(
			request.build_absolute_uri(reverse('xdomain-javascript-min')),
			settings.XDOMAIN_ORIGIN_REGEX
		)
	)

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
