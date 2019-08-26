# django-xdomain

A Django app for integrating [jpillora's XDomain](https://github.com/jpillora/xdomain)
into Django.

## Usage

Install the package (not yet in PyPI) and add `xdomain` to your
`INSTALLED_APPS` setting:

    INSTALLED_APPS = (
        ...
        'xdomain',
    )

Then include the URLs somewhere in your URLconf:

    urlpatterns = patterns('',
        ...
        url(r'^xdomain/', include('xdomain.urls')),
    )


## Requirements

Django 2.0+
