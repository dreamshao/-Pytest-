"""
Author: WangXing
Time: 2024/7/10 11:36
Description: 测试用例
"""
import pytest
from Data.read_data import DataManger
from RequestObject.request_runner import Request_Runner
from Utils.logger import MyLog
import allure
from Utils.variable_handler import Variable_Handler

logger = MyLog().get_logger()


class Test_Match_list():
    @allure.step("比赛列表广告位")
    @pytest.mark.parametrize('id, url, method, headers, request_data, params, json, assert_jsonpath, response_body, remarks',
                             DataManger().get_data_from_sqlite(name="data", sql_command='''select * from requests where id= 1''', query_sql_type=True))
    def test_match_ads_list(self, id, url, method, headers, request_data, params, json, assert_jsonpath, response_body, remarks):
        """
        测试用例，采用pytest 参数化模式，读取数据库用例信息
        :param id: 数据库id
        :param url: 数据库的url
        :param method: 数据库的 method
        :param headers: 数据库的 headers
        :param request_data: 数据库的 request_data
        :param params: 数据库的 params
        :param json: 数据库的 json
        :param assert_jsonpath: 数据库的 assert_json_path
        :param response_body: 数据库的 response_body
        :param remarks: 数据库的 remarks
        :return:
        """
        logger.info(f"开始测试比赛列表")
        result = Request_Runner(url=url, headers=headers, data=request_data, assert_info=assert_jsonpath).post_request_runner(id=id)
        logger.info(f"测试结果是 {result}")
        assert result is not False

    @allure.step("Today比赛列表")
    @pytest.mark.parametrize('id, url, method, headers, request_data, params, json, assert_jsonpath, response_body, remarks',
                             DataManger().get_data_from_sqlite(name="data",sql_command='''select * from requests where id= 2''',
                                                               query_sql_type=True))
    def test_match_list(self, id, url, method, headers, request_data, params, json, assert_jsonpath, response_body, remarks):
        logger.info(f"开始测试比赛列表")
        result = Request_Runner(url=url, headers=headers, assert_info=assert_jsonpath).get_request_runner(id=id)
        logger.info(f"测试结果是 {result}")
        if result:
            Variable_Handler(variable_name=["eventid","competitorid"], response_body=result).variable_handler()
        assert result is not False

    @allure.step("比赛详情页面，采用全局变量")
    @pytest.mark.parametrize(
        'id, url, method, headers, request_data, params, json, assert_jsonpath, response_body, remarks',
        DataManger().get_data_from_sqlite(name="data", sql_command='''select * from requests where id= 3''',
                                          query_sql_type=True))
    def test_match_detail_list(self, id, url, method, headers, request_data, params, json, assert_jsonpath, response_body,
                        remarks):
        logger.info(f"比赛详情页面")
        result = Request_Runner(url=url, headers=headers, assert_info=assert_jsonpath).get_request_runner(id=id, replace_type=1)
        logger.info(f"测试结果是 {result}")
        # if result[0] is True:
        #     Variable_Handler(id=2, variable_name="eventid").variable_handler()
        assert result is not False

    @allure.step("订阅比赛，采用全局变量")
    @pytest.mark.parametrize(
        'id, url, method, headers, request_data, params, json, assert_jsonpath, response_body, remarks',
        DataManger().get_data_from_sqlite(name="data", sql_command='''select * from requests where id= 4''',
                                          query_sql_type=True))
    def test_match_subscribe_list(self, id, url, method, headers, request_data, params, json, assert_jsonpath,
                               response_body,
                               remarks):
        logger.info(f"订阅比赛信息")
        result = Request_Runner(url=url, headers=headers, data=request_data, assert_info=assert_jsonpath).post_request_runner(id=id, replace_type=1)
        logger.info(f"测试结果是 {result}")
        # if result[0] is True:
        #     Variable_Handler(id=2, variable_name="eventid").variable_handler()
        assert result is not False

    @allure.step("深度数据，采用全局变量")
    @pytest.mark.parametrize(
        'id, url, method, headers, request_data, params, json, assert_jsonpath, response_body, remarks',
        DataManger().get_data_from_sqlite(name="data", sql_command='''select * from requests where id= 5''',
                                          query_sql_type=True))
    def test_match_subscribe_list(self, id, url, method, headers, request_data, params, json, assert_jsonpath,
                                  response_body,
                                  remarks):
        logger.info(f"订阅比赛信息")
        result = Request_Runner(url=url, headers=headers, data=request_data,
                                assert_info=assert_jsonpath).post_request_runner(id=id, replace_type=2)
        logger.info(f"测试结果是 {result}")
        assert result is not False

