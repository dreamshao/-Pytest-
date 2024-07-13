# 接口自动化测试框架

这是一款基于pytest框架的开源测试框架,功能涵盖请求体保存, allure生成, log生成, 全局变量存储, 全局变量使用, 断言返回体 等多种功能组合

## 详细介绍

    框架图：
      —接口自动化测试
         --allure_report
         --allure-results
         --BaseRequests
           ---__init__.py
           ---BaseRequests.py
         --Data
           ---data.db
           ---data.xlsx
           ---sqlite 可视化安装包
           ---read_data.py
         --logs
         --RequestObject
           ---request_runner.py
         --TestCases
           -- 测试用例
         --Utils
           --json_assert.py
           --logger.py
           --replace_requests.py
           --variable_handler.py
          --man.py
          --requirements.txt
         
           

## 具体框架解析传递关系
  
  可以点击我的博客: https://8888666.top/2024/07/12/pytest%E6%8E%A5%E5%8F%A3%E6%B5%8B%E8%AF%95%E6%A1%86%E6%9E%B6/  对此有详细的介绍，欢迎探讨以及提出批评和建议!          
