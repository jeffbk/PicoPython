# -*- coding: utf-8 -*-
"""
    urls
    ~~~~

    URL definitions.

    :copyright: 2009 by tipfy.org.
    :license: BSD, see LICENSE.txt for more details.
"""
from tipfy import Rule, import_string


def get_rules(app):
    """Returns a list of URL rules for the application. The list can be
    defined entirely here or in separate ``urls.py`` files.

    :param app:
        The WSGI application instance.
    :return:
        A list of class:`tipfy.Rule` instances.
    """

    rules = [
    	Rule('/hello-world', endpoint='hello-world', handler='apps.hello_world.handlers.HelloWorldHandler'),
    	Rule('/hello-world-pretty', endpoint='hello-world-pretty', handler='apps.hello_world.handlers.PrettyHelloWorldHandler')
	]

    return rules
