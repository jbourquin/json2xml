#!/usr/bin/env python

"""Tests for `dicttoxml` package."""

import unittest
import xmltodict

from json2xml import json2xml


class TestDictToXML(unittest.TestCase):
  """Tests for `dicttoxml` package."""

  def test_boolean_conversion(self):
    sample_dict = {
      "boolean": True,
      "boolean_dict_list": [
        {"boolean_dict": {"boolean": True }},
        {"boolean_dict": {"boolean": False} }
      ],
      "boolean_list": [True, False]
    }
    xml = json2xml.Json2xml(sample_dict, pretty=True).to_xml()
    result = xmltodict.parse(xml)

    try:
      assert result['all']['boolean']['#text'] == 'true'
      assert result['all']['boolean_dict_list']['item'][0]['boolean_dict']['boolean']['#text'] == 'true'
      assert result['all']['boolean_dict_list']['item'][1]['boolean_dict']['boolean']['#text'] == 'false'
      assert result['all']['boolean_list']['item'][0]['#text'] == 'true'
      assert result['all']['boolean_list']['item'][1]['#text'] == 'false'
    except Exception as e:
      print(xml)
      raise(e)


  def test_nested_conversion(self):
    sample_dict = {
      "boolean_list": [True, False],
      "number_list": [1, 2, 3],
      "string_list": ["a", "b", "c"],
      "dict_list": [
        {
          "boolean": True,
          "string": "Hello",
          "number": 42,
          "dict": {
            "boolean": True,
            "string": "Hello",
            "number": 42,
          },
          "list": ["a", 1, True]
        },
        {
          "boolean": True,
          "string": "Hello",
          "number": 42,
          "dict": {
            "boolean": True,
            "string": "Hello",
            "number": 42,
          },
          "list": ["a", 1, True]
        }
      ],
      "list_list": [
        ["a", "b", "c"],
        [1, 2, 3],
        [True, False]
      ]
    }
    xml = json2xml.Json2xml(sample_dict, pretty=True).to_xml()
    print(xml)
    result = xmltodict.parse(xml)
    try:
      assert result['all']['boolean_list']['item'][0]['#text'] == 'true'
      assert result['all']['boolean_list']['item'][1]['#text'] == 'false'
      
      assert result['all']['number_list']['item'][0]['#text'] == '1'
      assert result['all']['number_list']['item'][1]['#text'] == '2'
      assert result['all']['number_list']['item'][2]['#text'] == '3'
      
      assert result['all']['string_list']['item'][0]['#text'] == 'a'
      assert result['all']['string_list']['item'][1]['#text'] == 'b'
      assert result['all']['string_list']['item'][2]['#text'] == 'c'
      
      assert result['all']['dict_list']['item'][0]['boolean']['#text'] == 'true'
      assert result['all']['dict_list']['item'][0]['string']['#text'] == 'Hello'
      assert result['all']['dict_list']['item'][0]['number']['#text'] == '42'
      assert result['all']['dict_list']['item'][0]['dict']['boolean']['#text'] == 'true'
      assert result['all']['dict_list']['item'][0]['dict']['string']['#text'] == 'Hello'
      assert result['all']['dict_list']['item'][0]['dict']['number']['#text'] == '42'
      assert result['all']['dict_list']['item'][0]['list']['item'][0]['#text'] == 'a'
      assert result['all']['dict_list']['item'][0]['list']['item'][1]['#text'] == '1'
      assert result['all']['dict_list']['item'][0]['list']['item'][2]['#text'] == 'true'
      
      assert result['all']['list_list']['item'][0]['item'][0]['#text'] == 'a'
      assert result['all']['list_list']['item'][0]['item'][1]['#text'] == 'b'
      assert result['all']['list_list']['item'][0]['item'][2]['#text'] == 'c'
      assert result['all']['list_list']['item'][1]['item'][0]['#text'] == '1'
      assert result['all']['list_list']['item'][1]['item'][1]['#text'] == '2'
      assert result['all']['list_list']['item'][1]['item'][2]['#text'] == '3'
      assert result['all']['list_list']['item'][2]['item'][0]['#text'] == 'true'
      assert result['all']['list_list']['item'][2]['item'][1]['#text'] == 'false'
    except Exception as e:
      print(xml)
      raise(e)
