import pytest
import json
import validators

"""
Tests to read the appsettings.json for application settings
"""

def test_get_setting():
    f = open('settings.json')
    settings = json.load(f)
    f.close()
    s = settings['settings']
    p = s[0]
    pattern = p['pattern1']
    assert pattern

def test_url_validate():
    valid = validators.url('https://en.wikipedia.org/wiki/Marlin_Schmidt')
    print (valid)