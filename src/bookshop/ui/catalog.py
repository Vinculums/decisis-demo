import importlib

from bookshop.api import client
from bookshop.db import models
from ..db.session import open_session


def plugin(name):
    return importlib.import_module(name)


def show_catalog():
    return client.fetch("catalog"), models.Book, open_session
