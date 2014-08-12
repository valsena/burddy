from functools import wraps
from collections import Mapping
from random import randint
from flask import render_template


def get_random(cls):
	r = randint(0, cls.query.count())
	return cls.query.all()[r]


def template(path=None, **default_context):
    """Render a template if the decorated view returns a context dictionary.

    If the returned context includes the key '_template', that value is used as the template path.

    If the view does not return a dictionary, the return value will be passed through.

    :param path: template to render
    :param kwargs: default context to pass to template, can be overridden by view context
    :return: view decorator
    """
    def decorator(func):
        @wraps(func)
        def inner(*args, **kwargs):
            result = func(*args, **kwargs)

            if not isinstance(result, Mapping):
                return result

            context = default_context.copy()
            context.update(result)

            template_path = context.pop('_template', path)

            if template_path is None:
                raise KeyError('No default template provided, and no template passed in context.')

            return render_template(template_path, **context)

        return inner

    return decorator
