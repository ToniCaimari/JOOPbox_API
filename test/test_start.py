from flask import request, jsonify
import pytest
from repository.data import Data
import json


@pytest.mark.wellcome
def test_start(client):
    rv = client.get('/')
    # assert b'Data.datos' in rv.data
    assert Data.datos == rv.get_json()
