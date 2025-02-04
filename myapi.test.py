import pytest
from fastapi.testclient import TestClient
from myapi import app, TextData, MESSAGE_FILE
import json
import os

client = TestClient(app)

def test_submit_text():
    pass
