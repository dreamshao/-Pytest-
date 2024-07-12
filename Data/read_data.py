"""
Author: WangXing
Time: 2024/7/10 14:08
Description:
"""

import pandas as pd
from Utils.logger import MyLog
import sqlite3

logger = MyLog().get_logger()


class DataManger():
    def get_data_from_excel(self, name, sheet_name, nums):
        try:
            logger.info(f"开始读取excel, excel名字是 {name}, sheet_name是 {sheet_name}")
            path = './Data/' + name + '.xlsx'
            logger.info(f"整体路径是{path}")
            df = pd.read_excel(path, sheet_name=sheet_name)
            data = df.values.tolist()
            logger.info(f"读取到的数据{data}")
            return [data[nums]]
        except Exception as e:
            logger.info(f"读取数据失败, 具体原因是 {e}")
            return False

    def write_data_to_execl(self, name, sheet_name, nums):
        pass

    def connect_sqlite(self, name, sql_db_path=None):
        try:
            logger.info("开始连接数据库")
            # 连接到SQLite数据库
            # 如果文件不存在，会自动在当前目录创建:
            path = './Data/' + name + '.db'
            conn = sqlite3.connect(path)
            # 创建一个Cursor对象
            cur = conn.cursor()
            logger.info("连接数据库成功")
            return cur, conn
        except Exception as e:
            logger.info(f"连接数据库失败,具体原因是 {e}")
            return False

    def get_data_from_sqlite(self, sql_command, name, sql_db_path=None, query_sql_type=False):
        try:
            cur = self.connect_sqlite(name)
            if query_sql_type:
                if cur:
                    logger.info(f"执行查询操作 执行语句是 {sql_command}")
                    cur[0].execute(sql_command)
                    re = cur[0].fetchall()
                    print(re)
                    # 关闭Cursor
                    cur[0].close()
                    # 关闭conn
                    cur[1].close()
                    list_of_re = [[item for item in tup] for tup in re]
                    logger.info(f"执行查询操作 成功返回的数据是 {list_of_re}")
                    return list_of_re
            else:
                if cur:
                    logger.info(f"执行非查询操作 执行语句是 {sql_command}")
                    cur[0].execute(sql_command)
                    cur[1].commit()
                    # 关闭Cursor
                    cur[0].close()
                    # 关闭conn
                    cur[1].close()
        except Exception as e:
            logger.info(f"创建数据库失败,具体原因是 {e}")
            return False