#!/usr/bin/env python
import os
import re
from distutils.core import setup


def get_version(package):
    """
    Returns version of a package (`__version__` in `init.py`).
    """
    init_py = open(os.path.join(package, '__init__.py')).read()
    return re.match("__version__ = ['\"]([^'\"]+)['\"]", init_py).group(1)


version = get_version('telegram_simple')


setup(
    name='python-telegram_simple',
    version=version,
    description='Python library to help you build your own Telegram clients with modified namespace so that it is'
                'so that it is compatible with other telegram libraries',
    author='Alexander Akhmetov',
    author_email='me@aleks.sh',
    url='https://github.com/minusmagis/python-telegram-simple',
    packages=[
        'telegram_simple',
    ],
    package_data={
        'telegram_simple': [
            'lib/darwin/*',
            'lib/linux/*',
        ],
    },
)
