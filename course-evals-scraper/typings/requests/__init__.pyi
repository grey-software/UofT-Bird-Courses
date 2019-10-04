"""
This type stub file was generated by pyright.
"""

import urllib3
import chardet
import warnings
import logging
from .exceptions import ConnectTimeout, ConnectionError, FileModeWarning, HTTPError, ReadTimeout, RequestException, RequestsDependencyWarning, Timeout, TooManyRedirects, URLRequired
from urllib3.exceptions import DependencyWarning
from .__version__ import __author__, __author_email__, __build__, __cake__, __copyright__, __description__, __license__, __title__, __url__, __version__
from . import packages, utils
from .models import PreparedRequest, Request, Response
from .api import delete, get, head, options, patch, post, put, request
from .sessions import Session, session
from .status_codes import codes
from logging import NullHandler

"""
This type stub file was generated by pyright.
"""
def check_compatibility(urllib3_version, chardet_version):
    ...

def _check_cryptography(cryptography_version):
    ...

