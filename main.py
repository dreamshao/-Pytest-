"""
Author: WangXing
Time: 2024/7/10 14:25
Description: 主运行文件
"""
import pytest
import subprocess

if __name__ == "__main__":
    pytest.main(['-v', '-s', '--alluredir=allure-results', '--clean-alluredir'])
    cmd = "allure generate ./allure-results report --clean"
    subprocess.run(cmd, shell=True)
    cmd = "allure open -h 127.0.0.1 -p 8883 allure-report"
    subprocess.run(cmd, shell=True)
