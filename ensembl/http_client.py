# Copyright (c) 2014 Katsuya Noguchi
#
# Permission is hereby granted, free of charge, to any person obtaining a
# copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish, dis-
# tribute, sublicense, and/or sell copies of the Software, and to permit
# persons to whom the Software is furnished to do so, subject to the fol-
# lowing conditions:
#
# The above copyright notice and this permission notice shall be included
# in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
# OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABIL-
# ITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT
# SHALL THE AUTHOR BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
# WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
# IN THE SOFTWARE.

import requests
import ensembl
from ensembl.exceptions import EnsembleError


DEFAULT_PARAMS = { 'content-type': 'application/json' }


def get(path):
    url = ensembl.api_base_url + path
    response = requests.get(url, params=DEFAULT_PARAMS, verify=False).json()
    _raise_error_if_not_ok(response)
    return response

def post(path, data):
    url = ensembl.api_base_url + path
    response = requests.post(
        url, params=DEFAULT_PARAMS, data=data, verify=False).json()
    _raise_error_if_not_ok(response)
    return response

def _raise_error_if_not_ok(response):
    if 'error' in response:
        raise EnsembleError(response['error'])
