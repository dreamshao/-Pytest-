"""
Author: WangXing
Time: 2024/7/10 11:24
Description: 基本请求配置
"""

import requests
from . import logger


class BaseRequests():
    def get_request(self, url, params=None, headers=None):
        """
        get 请求
        :param url: 请求url
        :param params: 请求入参
        :param headers: 请求头
        :return: Boolean
        """
        try:
            logger.info(f"开始进入get请求, 当前请求url是{url}, params是{params}, headers是{headers}")
            result = requests.get(url=url, params=params, headers=headers)
            if result.status_code == 200:
                logger.info(f'当前请求成功，返回的http_code是 200, 返回结果是 {result.text}')
                return result.text
            else:
                logger.info(f'当前返回出现了问题，返回的http_code是{result.status_code},返回的信息是{result.text}')
                return False
        except Exception as e:
            logger.info(f"当前请求出现了问题，请求方式是 GET, 地址是 {url}, params是{params}, headers是{headers}, 出现的问题是 {e}")
            return False

    def post_request(self, url, data=None, headers=None, json=None):
        """
         post 请求
        :param url: 请求url
        :param data: 请求data
        :param json: 请求json
        :param headers: 请求头
        :return: Boolean
        """
        try:
            logger.info(f"开始进入post请求, 当前请求url是{url}, data是{data}, json是{json}, headers是{headers}")
            result = requests.post(url=url, data=data, json=json, headers=headers)
            if result.status_code == 200:
                logger.info(f'当前请求成功，返回的http_code是 200, 返回结果是 {result.text}')
                return result.text
            else:
                logger.info(f'当前返回出现了问题，返回的http_code是{result.status_code},返回的信息是{result.text}')
                return False
        except Exception as e:
            logger.info(f"当前请求出现了问题，请求方式是 POST, 地址是 {url}, data是{data},  json是{json}, headers是{headers}, 出现的问题是 {e}")
            return False

    def put_request(self, url, data=None, params=None, headers=None):
        """
        put 请求
        :param url: 请求url
        :param data: 请求data
        :param params: 请求参数
        :param headers: 请求头
        :return: Boolean
        """
        try:
            logger.info(f"开始进入put请求, 当前请求url是{url}, data是{data}, params是{params}, headers是{headers}")
            result = requests.put(url=url, data=data, params=params, headers=headers)
            if result.status_code == 200:
                logger.info(f'当前请求成功，返回的http_code是 200, 返回结果是 {result.text}')
                return result.text
            else:
                logger.info(f'当前返回出现了问题，返回的http_code是{result.status_code},返回的信息是{result.text}')
                return False
        except Exception as e:
            logger.info(f"当前请求出现了问题，请求方式是 PUT, 地址是 {url}, data是{data},  params是{params}, headers是{headers}, 出现的问题是 {e}")
            return False

    def delete_request(self, url, data=None, params=None, headers=None):
        """
        delete 请求
        :param url: 请求url
        :param data: 请求data
        :param params: 请求参数
        :param headers: 请求头
        :return:  Boolean
        """
        try:
            logger.info(f"开始进入delete请求, 当前请求url是{url}, data是{data}, params是{params}, headers是{headers}")
            result = requests.delete(url=url, data=data, params=params, headers=headers)
            if result.status_code == 200:
                logger.info(f'当前请求成功，返回的http_code是 200, 返回结果是 {result.text}')
                return result.text
            else:
                logger.info(f'当前返回出现了问题，返回的http_code是{result.status_code},返回的信息是{result.text}')
                return False
        except Exception as e:
            logger.info(f"当前请求出现了问题，请求方式是 PUT, 地址是 {url}, data是{data},  params是{params}, headers是{headers}, 出现的问题是 {e}")
            return False
