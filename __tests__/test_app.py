import pytest

import pymysql as mysql
import bottle
import requests
import pytest

def test_mysql_version():
    assert (mysql.__version__) == "0.9.3"

def test_bottle_version():
    assert (bottle.__version__) == "0.12.18"

def test_requests_vetrsion():
    assert (requests.__version__) == "2.23.0"

def pytest():
    assert (pytest.__version__) == "5.3.5"
