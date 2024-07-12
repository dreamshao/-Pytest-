"""
Author: WangXing
Time: 2024/7/11 14:58
Description: 全局变量处理
"""
from Data.read_data import DataManger
import json
import jsonpath
from Utils.logger import MyLog

logger = MyLog().get_logger()



class Variable_Handler():
    def __init__(self, response_body, variable_name=None):
        """
        :param response_body: 需要传递一个列表
        :param variable_name: 传递变量名字
        """
        self.response_body = response_body
        self.variable_name = variable_name

    def variable_handler(self):
        """
        全局变量处理
        :return: Boolean
        """
        try:
            logger.info("开始进行变量存储")
            pass_info = True
            sum_for_time = len(self.variable_name)
            global count_time
            count_time = 0
            for variable_name in self.variable_name:
                count_time += 1
                variable_jsonpath = DataManger().get_data_from_sqlite(name="data",
                                                                      sql_command="select variable_jsonpath from variable where variable_name='{variable_name}'".format(
                                                                          variable_name=variable_name),
                                                                      query_sql_type=True)
                variable_jsonpath = str(variable_jsonpath)[2:-2].replace("'", '"').strip('"')
                response_jsonpath = json.loads(variable_jsonpath)
                for key, value in response_jsonpath.items():
                    logger.info(f"当前的key,value {key}, {value}")
                    value_info = jsonpath.jsonpath(self.response_body, value)
                    logger.info(f"当前是否找到 {value_info}")
                    if value_info:
                        value_info = ', '.join([str(item) for item in value_info])
                        logger.info(f"需要存储的变量值{value_info}")
                        DataManger().get_data_from_sqlite(name="data",
                                                          sql_command="UPDATE variable SET variable_value = '{variable_value}' where variable_name = '{variable_name}'".format(
                                                              variable_value=value_info, variable_name=variable_name),
                                                          query_sql_type=False)
                    else:
                        logger.info(f"当前jsonpath语法错误, 对比的语法是{key}, 对比的值是{value}")
                        pass_info = False
            if sum_for_time == count_time:
                if pass_info:
                    logger.info(f"当前变量存储成功")
                    return True
                else:
                    logger.info(f"当前变量存储失败, 返回False")
                    return False
        except Exception as e:
            logger.info(f"当前变量存储发生了异常, 异常是{e}")
            return False
        finally:
            count_time = 0
