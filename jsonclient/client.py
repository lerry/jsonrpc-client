#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
As its name, jsonrpc-client, is a json-rpc client.
Homepage and documentation: https://github.com/lerry/jsonrpc-client
Copyright (c) 2015, Lerry.
License: MIT (see LICENSE for details)
"""
import requests
import sys, traceback
from uuid import uuid4
try:
    from ujson import dumps, loads
except ImportError:
    from json import dumps, loads

class Client(object):
    def __init__(self, url, **kwargs):
        self.url = url
        headers = {'Content-type': 'application/json', 'Accept': 'application/json'}
        if kwargs.get("headers"):
            kwargs["headers"].update(headers)
        else:
            kwargs["headers"] = headers
        self.kwargs = kwargs
        self.request = requests.Session()

    def _make_data(self, method, *args, **kwargs):
        if kwargs:
            params = kwargs
            if args:
                params["__args"] = args
        else:
            params = args
        return {
            "method": unicode(method),
            "id": unicode(uuid4()),
            "jsonrpc": "2.0",
            "params": params
        }

    def _fetch(self, method, *args, **kwargs):
        data = self._make_data(method, *args, **kwargs)
        req = self.request.post(self.url, data=dumps(data), **self.kwargs)
        if req.status_code == 200:
            return self._parse_result(data, req.text)
        else:
            msg = "\nHTTP Error: %s\n %s" % (req.status_code, req.content)
            raise Exception(msg)

    def _parse_result(self, request, text):
        data = loads(text)
        if request["id"] != data["id"]:
            msg = "\nError: \n  id not match"
        elif data["error"]:
            msg = "\nREMOTE Server Error: \n  " + data["error"]
        else:
            return data["result"]
        raise Exception(msg)

    def __getattr__(self, method):
        def _(*args, **kwargs):
            return self._fetch(method, *args, **kwargs)
        return _