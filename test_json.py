import pytest
import json


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
