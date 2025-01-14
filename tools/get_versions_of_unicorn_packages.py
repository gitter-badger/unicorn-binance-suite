#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# File: tools/get_versions_of_unicorn_packages.py
#
# Part of ‘UNICORN Binance Suite’
# Project website: https://www.lucit.tech/unicorn-binance-suite.html
# Github: https://github.com/LUCIT-Systems-and-Development/unicorn-binance-suite
# Documentation: https://unicorn-binance-suite.docs.lucit.tech
# PyPI: https://pypi.org/project/unicorn-binance-suite
#
# Author: LUCIT Systems and Development
#
# Copyright (c) 2022-2022, LUCIT Systems and Development (https://www.lucit.tech) and Oliver Zehentleitner
# # All rights reserved.
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

import logging

logging.basicConfig(level=logging.ERROR,
                    format="{asctime} [{levelname:8}] {process} {thread} {module}: {message}",
                    style="{")

try:
    import unicorn_fy
    unify_version = unicorn_fy.UnicornFy().get_version()
except ModuleNotFoundError:
    unify_version = "not found"

try:
    import unicorn_binance_local_depth_cache
    ubldc = unicorn_binance_local_depth_cache.BinanceLocalDepthCacheManager(warn_on_update=False)
    ubldc_version = ubldc.get_version()
    ubldc.stop_manager_with_all_depth_caches()
except ModuleNotFoundError:
    ubldc_version = "not found"
except AttributeError:
    pass

try:
    import unicorn_binance_rest_api
    ubra_version = unicorn_binance_rest_api.BinanceRestApiManager(warn_on_update=False).get_version()
except ModuleNotFoundError:
    ubra_version = "not found"

try:
    import unicorn_binance_websocket_api
    ubwa = unicorn_binance_websocket_api.BinanceWebSocketApiManager(warn_on_update=False)
    ubwa_version = ubwa.get_version()
    ubwa.stop_manager_with_all_streams()
except ModuleNotFoundError:
    ubwa_version = "not found"


print(f"Please post this to your github issue:")
print(f"unicorn_fy: {unify_version}")
print(f"unicorn_binance_local_depth_cache: {ubldc_version}")
print(f"unicorn_binance_rest_api: {ubra_version}")
print(f"unicorn_binance_websocket_api: {ubwa_version}")
