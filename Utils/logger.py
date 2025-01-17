"""
Author: WangXing
Time: 2024/7/10 11:39
Description: 日志
"""
import logging
import os
import time


class MyLog(object):
    _instance = None  # 类变量来保存单例实例

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(MyLog, cls).__new__(cls)
        return cls._instance

    def __init__(self, logger_name='my_logger'):
        """
        指定保存日志的文件路径，日志级别，以及调用文件
        将日志存入到指定的文件中
        """
        if hasattr(self, '_initialized'):
            # 确保只初始化一次
            return

            # 日志文件夹，如果不存在则自动创建
        cur_path = os.path.dirname(os.path.realpath(__file__))
        log_path = os.path.join(os.path.dirname(cur_path), 'Logs')
        if not os.path.exists(log_path):
            os.makedirs(log_path)

            # log 日期文件夹
        now_date = time.strftime('%Y-%m-%d', time.localtime(time.time()))
        phone_log_path = os.path.join(log_path, now_date)
        if not os.path.exists(phone_log_path):
            os.makedirs(phone_log_path)

            # 创建一个logger
        self.logger = logging.getLogger(logger_name)
        if not self.logger.handlers:  # 确保不重复添加handler
            self.logger.setLevel(logging.INFO)

            # 创建一个handler，用于写入日志文件
            now_time = time.strftime('%Y%m%d-%H%M%S', time.localtime(time.time()))
            log_name = os.path.join(phone_log_path, f'{now_time}.log')
            fh = logging.FileHandler(log_name)
            fh.setLevel(logging.INFO)

            # 再创建一个handler，用于输出到控制台
            ch = logging.StreamHandler()
            ch.setLevel(logging.INFO)

            # 定义handler的输出格式
            formatter = logging.Formatter('%(asctime)s - %(levelname)s %(filename)s [line:%(lineno)d]: %(message)s')
            fh.setFormatter(formatter)
            ch.setFormatter(formatter)

            # 给logger添加handler
            self.logger.addHandler(fh)
            self.logger.addHandler(ch)

        self._initialized = True  # 标记已初始化

    def get_logger(self):
        """获取logger实例"""
        return self.logger