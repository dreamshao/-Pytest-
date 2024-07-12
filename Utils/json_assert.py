"""
Author: WangXing
Time: 2024/7/10 15:29
Description:
"""
import jsonpath
import json
from Utils.logger import MyLog

logger = MyLog().get_logger()


class Assert_Json():
    def assert_info(self, data, assert_info):
        """
        json 对比，就是断言
        :param data: 请求返回的response
        :param assert_info: 需要断言的jsonpath
        :return: Boolean
        """
        try:
            logger.info(f"当前进入数据对比, 需要对比的json是{data}, 对比的jsonpath 是 {assert_info}")
            assert_info = json.loads(assert_info)
            pass_info = True
            for key, value in assert_info.items():
                value_info = jsonpath.jsonpath(data, key)
                if value_info:
                    value_info = ', '.join([str(item) for item in value_info])
                    if str(value) == value_info:
                        logger.info(f"当前对比成功, 对比的语法是{key}, 对比的值是{value_info}, 用户需要对比的值是{value}, 当前对比一致通过测试！")
                    else:
                        logger.info(f"当前对比失败, 对比的语法是{key}, 对比的值是{value_info}, 用户需要对比的值是{value}, 当前对比失败！")
                        pass_info = False
                else:
                    logger.info(f"当前jsonpath语法错误, 对比的语法是{key}, 对比的值是{value}")
                    pass_info = False
            if pass_info:
                logger.info(f"当前对比成功, 返回True")
                return True
            else:
                logger.info(f"当前对比失败, 返回False")
                return False
        except Exception as e:
            logger.info(f"当前对比发生了异常, 需要对比的json是{data}, 对比的jsonpath 是 {assert_info}, 异常是{e}")
            return False
