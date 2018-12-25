# -*- coding: UTF-8 -*-
# @Time: 2018/12/25 6:37
# @Author: Sai_12
# @Email: 932934045@qq.com
# @File: request.py

import requests

class Request:
    '''接口请求类'''
    def __init__(self, method, url, data=None, cookies=None, headers=None):
        try:
            if method == 'get':
                self.resp = requests.get(url=url, params=data, cookies=cookies, headers=headers)
            elif method == 'post':
                self.resp = requests.post(url=url, data=data, cookies=cookies, headers=headers)
            elif method == 'delete':
                self.resp = requests.delete(url=url, data=data, cookies=cookies, headers=headers)
        except Exception as e:
            raise e

    def get_status_code(self):
         return self.resp.status_code

    def get_text(self):
        return self.resp.text

    def get_json(self):
        return self.resp.json()
