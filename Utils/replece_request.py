"""
Author: WangXing
Time: 2024/7/11 19:20
Description:
"""
import re, json
from Data.read_data import DataManger
from Utils.logger import MyLog

logger = MyLog().get_logger()


class Replace_Request():
    def __init__(self, url=None, data=None):
        self.url = url
        self.data = data

    def repalce_request_url(self):
        """
        替换 url
        :return: 没有成功：None  替换成功 url
        """
        try:
            logger.info(f"开始进入替换url,当前需要被替换的url是{self.url}")
            # 使用正则表达式查找花括号内的内容
            match = re.search(r'\{([^}]+)\}', self.url)
            if match:
                # 如果找到匹配项，返回花括号内的内容
                variable_name = match.group(1)
                logger.info(f"找到了变量名字, 是 {variable_name}")
                variable_value = DataManger().get_data_from_sqlite(name="data",
                                                                   sql_command="select variable_value from variable where variable_name='{variable_name}'".format(
                                                                       variable_name=variable_name),
                                                                   query_sql_type=True)
                variable_value = str(variable_value)[2:-2].replace("'", '"').strip('"')
                logger.info(f"找到了变量信息是 {variable_value}")
                new_url = re.sub(r'\{([^}]+)\}', variable_value, self.url, count=1)
                logger.info(f"替换url成功,是{new_url}")
                return new_url

            else:
                logger.info(f"当前没有找到需要被替换的信息,请检查输入内容")
                # 如果没有找到花括号或花括号内没有内容，返回None
                return None
        except Exception as e:
            logger.info(f"出现异常了，异常是{e}")
            return None

    def replace_request_data(self):
        """
        替换data
        :return: 没有成功None, 成功 data
        """
        try:
            logger.info(f"开始进入替换data,当前需要被替换的data是{self.data}")
            self.data = json.loads(self.data)
            global count_time
            count_time = 0
            replace_value = []
            for key, value in self.data.items():
                logger.info(f"当前value {value}")
                # 使用正则表达式查找花括号内的内容
                match = re.search(r'\{([^}]+)\}', str(value))
                if match:
                    variable_name = match.group(1)
                    logger.info(f"当前key 和value是 {key}, {value}")
                    replace_value.append(key + ":" + variable_name)
            if len(replace_value) > 0:
                logger.info(f"当前 replace_value是 {replace_value}")
                count_value = len(replace_value)
                for variable_name in replace_value:
                    key = variable_name.split(":")[0]
                    variable_name = variable_name.split(":")[1]
                    logger.info(f"找到了变量名字, 是 {variable_name}")
                    variable_value = DataManger().get_data_from_sqlite(name="data",
                                                                       sql_command="select variable_value from variable where variable_name='{variable_name}'".format(
                                                                           variable_name=variable_name),
                                                                       query_sql_type=True)
                    variable_value = str(variable_value)[2:-2].replace("'", '"').strip('"')
                    logger.info(f"找到了变量信息是 {variable_value}")
                    new_value = re.sub(r'\{([^}]+)\}', variable_value, "{" + variable_name + "}", count=1)
                    logger.info(f"此时的new_value是 {new_value}")
                    logger.info(f"此时的key 是{key}")
                    self.data[key] = new_value
                    logger.info(f"替换data成功,是{self.data}")
                    count_time += 1
                    if count_value == count_time:
                        return json.dumps(self.data)
            else:
                logger.info(f"当前没有找到需要被替换的信息,请检查输入内容")
                # 如果没有找到花括号或花括号内没有内容，返回None
                return None
        except Exception as e:
            logger.info(f"出现异常了，异常是{e}")
            return None
        finally:
            count_time = 0

    # def replace_request_data(self):
    #     try:
    #         logger.info(f"开始进入替换data,当前需要被替换的data是{self.data}")
    #         self.data = json.loads(self.data)
    #         sum_for_time = len(self.data)
    #         global count_time
    #         count_time = 0
    #         for key, value in self.data.items():
    #             # 使用正则表达式查找花括号内的内容
    #             match = re.search(r'\{([^}]+)\}', value)
    #             if match:
    #                 # 如果找到匹配项，返回花括号内的内容
    #                 variable_name = match.group(1)
    #                 logger.info(f"找到了变量名字, 是 {variable_name}")
    #                 variable_value = DataManger().get_data_from_sqlite(name="data",
    #                                                                    sql_command="select variable_value from variable where variable_name='{variable_name}'".format(
    #                                                                        variable_name=variable_name),
    #                                                                    query_sql_type=True)
    #                 variable_value = str(variable_value)[2:-2].replace("'", '"').strip('"')
    #                 logger.info(f"找到了变量信息是 {variable_value}")
    #                 logger.info(f"此时的value 是{value}")
    #                 new_value = re.sub(r'\{([^}]+)\}', variable_value, value, count=1)
    #                 logger.info(f"此时的new_value是 {new_value}")
    #                 logger.info(f"此时的key 是{key}")
    #                 self.data[key]=new_value
    #                 logger.info(f"替换data成功,是{self.data}")
    #                 count_time += 1
    #                 if sum_for_time == count_time:
    #                     return json.dumps(self.data)
    #
    #             else:
    #                 count_time += 1
    #                 if sum_for_time == count_time:
    #                     logger.info(f"当前没有找到需要被替换的信息,请检查输入内容")
    #                     # 如果没有找到花括号或花括号内没有内容，返回None
    #                     return None
    #     except Exception as e:
    #         logger.info(f"出现异常了，异常是{e}")
    #         return None
    #     finally:
    #         count_time = 0
