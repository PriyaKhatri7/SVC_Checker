from main import check
import requests
import pytest

def test_check_times_out_gracefully(monkeypatch):
    def fake_get(*_, **__):
        raise requests.exceptions.Timeout()
    monkeypatch.setattr(requests, "get", fake_get)
    with pytest.raises(Exception):
        check("httpe://example.com", timeout=1, attempts=2)