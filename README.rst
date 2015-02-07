django-dict-response
====================

Usage
-----

Example::

    def view(request):
        ...
        return dict(Age=120, obj=obj, template_name=template_name, title=title, status=200)

Installation
------------

1. Install using pip:

    ``pip install -U django-dict-response``

2. Add to **last** of MIDDLEWARE_CLASSES in your ``settings.py``:

    ``'django_dict_response.middlewares.DictResponseMiddleware',``

Requirements
------------

Django >= 1.7
