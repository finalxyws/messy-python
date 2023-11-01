#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re

a = '11-01 12:44:31.832  3011  3011 I KaiWeather: Content JS LOG: ERROR CONNECTION API'

re_result = re.findall('[A-Z]|[0-9]', a)

print(re_result)