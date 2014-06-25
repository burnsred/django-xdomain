from django.conf import settings
from django.http import HttpResponse
from django.templatetags.static import static
from django.views.decorators.clickjacking import xframe_options_exempt

@xframe_options_exempt
def proxy(request):
	return HttpResponse(
		"""
<!DOCTYPE HTML>
<script src="{0}" data-master="{1}"></script>
	""".format(
			static('xdomain/0.6-csrf/xdomain.min.js'),
			settings.XDOMAIN_ORIGIN_REGEX
		)
	)
