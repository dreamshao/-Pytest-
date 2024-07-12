"""
Author: WangXing
Time: 2024/7/10 11:55
Description: 二次封装请求
"""
from BaseRequests.BaseRequests import BaseRequests
import json
from Utils.logger import MyLog
from Utils.json_assert import Assert_Json
from Utils.replece_request import Replace_Request
from Data.read_data import DataManger

logger = MyLog().get_logger()


class Request_Runner():
    def __init__(self, url, headers, params=None, data=None, json=None, assert_info=None):
        self.url = url
        self.headers = headers
        self.params = params
        self.data = data
        self.json = json
        self.assert_info = assert_info

    def get_request_runner(self, id, replace_type=None):
        """
        get 请求
        :param id: 数据库用例Id
        :param replace_type: 替换类型 1：url 替换 2：data 替换 默认None 不替换
        :return: 失败 False 成功 dict
        """
        logger.info("当前进入get测试用例中")
        if replace_type == 1:
            self.url = Replace_Request(url=self.url).repalce_request_url()
        else:
            self.data = Replace_Request(data=self.data).replace_request_data()
        result = BaseRequests().get_request(url=self.url, headers=json.loads(self.headers), params=self.params)
        if result:
            result_json = json.loads(result)
            DataManger().get_data_from_sqlite(name="data",
                                              sql_command="UPDATE requests SET response_body = '{response_body}' where id = {id}".format(
                                                  response_body=json.dumps(result), id=id),
                                              query_sql_type=False)
            if self.assert_info is not None:
                result = Assert_Json().assert_info(result_json, self.assert_info)
                if result:
                    logger.info("测试全部通过")
                    return result_json
                else:
                    logger.info("测试存在失败")
                    return False
            else:
                logger.info("测试全部通过")
                return result_json
        else:
            logger.info("当前请求失败")
            print("失败了！")
            return False

    def post_request_runner(self, id, replace_type=None):
        """
         post请求
        :param id: id: 数据库用例Id
        :param replace_type: replace_type: 替换类型 1：url 替换 2：data 替换 默认None 不替换
        :return: 失败 False 成功 dict
        """
        logger.info("当前进入post测试用例中")
        if replace_type == 1:
            self.url = Replace_Request(url=self.url).repalce_request_url()
        else:
            self.data = Replace_Request(data=self.data).replace_request_data()
        result = BaseRequests().post_request(url=self.url, headers=json.loads(self.headers), data=self.data)
        if result:
            result_json = json.loads(result)
            DataManger().get_data_from_sqlite(name="data",
                                              sql_command="UPDATE requests SET response_body = '{response_body}' where id = {id}".format(
                                                  response_body=json.dumps(result), id=id),
                                              query_sql_type=False)
            if self.assert_info is not None:
                result = Assert_Json().assert_info(result_json, self.assert_info)
                if result:
                    logger.info("测试全部通过")
                    return result_json
                else:
                    logger.info("测试存在失败")
                    return False
            else:
                logger.info("测试全部通过")
                return result_json

        else:
            logger.info("当前请求失败")
            print("失败了！")

    def put_request_runner(self, id, replace_type=None):
        """
        put 请求
        :param id: 数据库用例Id
        :param replace_type:  replace_type: 替换类型 1：url 替换 2：data 替换 默认None 不替换
        :return: 失败 False 成功 dict
        """
        logger.info("当前进入put测试用例中")
        if replace_type == 1:
            self.url = Replace_Request(url=self.url).repalce_request_url()
        else:
            self.data = Replace_Request(data=self.data).replace_request_data()
        result = BaseRequests().put_request(url=self.url, headers=json.loads(self.headers), data=self.data)
        if result:
            result_json = json.loads(result)
            DataManger().get_data_from_sqlite(name="data",
                                              sql_command="UPDATE requests SET response_body = '{response_body}' where id = {id}".format(
                                                  response_body=json.dumps(result), id=id),
                                              query_sql_type=False)
            if self.assert_info is not None:
                result = Assert_Json().assert_info(result_json, self.assert_info)
                if result:
                    logger.info("测试全部通过")
                    return result_json
                else:
                    logger.info("测试存在失败")
                    return False
            else:
                logger.info("测试全部通过")
                return result_json

        else:
            logger.info("当前请求失败")
            print("失败了！")

    def delete_request_runner(self, id, replace_type=None):
        """
        delete 请求
        :param id: 数据库用例Id
        :param replace_type: replace_type: 替换类型 1：url 替换 2：data 替换 默认None 不替换
        :return: 失败 False 成功 dict
        """
        logger.info("当前进入delete测试用例中")
        if replace_type == 1:
            self.url = Replace_Request(url=self.url).repalce_request_url()
        else:
            self.data = Replace_Request(data=self.data).replace_request_data()
        result = BaseRequests().delete_request(url=self.url, headers=json.loads(self.headers), data=self.data)
        if result:
            result_json = json.loads(result)
            DataManger().get_data_from_sqlite(name="data",
                                              sql_command="UPDATE requests SET response_body = '{response_body}' where id = {id}".format(
                                                  response_body=json.dumps(result), id=id),
                                              query_sql_type=False)
            if self.assert_info is not None:
                result = Assert_Json().assert_info(result_json, self.assert_info)
                if result:
                    logger.info("测试全部通过")
                    return result_json
                else:
                    logger.info("测试存在失败")
                    return False
            else:
                logger.info("测试全部通过")
                return result_json

        else:
            logger.info("当前请求失败")
            print("失败了！")
