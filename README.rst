django-dict-response
====================

Overview
--------

Write ``views.py`` simply.

Usage
-----

Before::
    
    from django.shortcuts import render

    def view(request):
        ...
        response = render(request, template_name, dict(obj=obj, title=title), status=200)
        response['Age'] = 120
        return response

After::

    def view(request):
        ...
        return dict(Age=120, obj=obj, template_name=template_name, title=title, status=200)

Installation
------------

1. Install using pip:

    ``pip install -U django-dict-response``

2. Add to **last** of MIDDLEWARE_CLASSES in your ``settings.py``:

    ``'django_dict_response.middlewares.DictResponseMiddleware',``

Dependencies
------------

Django >= 1.7
