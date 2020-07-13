# 说明书

```text
亮点：
 * 数据驱动
 * 行为驱动(关键字驱动)
 * 数据分离
 * PO封装
 * 自定义测试报告
技术栈：
 * python
 * selenium
 * pytest
 * allure
 * yaml
 * PageObject设计模式
```

## pytest调试（运行显示print、logger日志 -s）

```bash
pytest -s -q
```

## allure报告模式运行

```bash
####### https://docs.qameta.io/allure/ #########
# 1. pytest运行输出allure results
pytest --alluredir=allure/results

# 2. allure 查看预览报告
allure serve allure/results

# 3. allure 生成静态HTML报告
# 3.1 安装allure命令行版并配置环境变量https://github.com/allure-framework/allure2/releases
# allure generate <directory-with-results> -o <directory-with-report> --clean
allure generate allure/results -o allure/report --clean
```

## pytest-html简单静态报告模式运行

```bash
# 独立HTML单文件报告(pytest-html)
pytest --html=report.html --self-contained-html
```

## pytest自动查找收集用例的规则

```txt
1. file name：test_*.py 或者 *test.py
2. class name：Test* 且类内没有 __init__ 函数
3. function name: test_*
```

## tree
```text
.
|-- README.md
|-- allure                          # allure测试报告
|   |-- report
|   |-- results
|-- data                            # 关键字驱动的case数据
|   `-- README.md
|-- debug.log
|-- images                          # selenium截图目录
|-- libs                            # 第三方库或项目其他依赖
|   `-- chromedriver.exe            # selenium的Chromedriver(83版本号)
|-- logs
|   `-- logger.log                  # 运行日志
|-- pages                           # PO封装之page页面
|   |-- __init__.py
|   |-- app_page.py                 # driver初始化
|   |-- base_page.py                # 基类，公共方法
|   |-- elements.yml                # 数据分离之页面元素定位信息集合
|   |-- home_page.py                # 业务页面
|   |-- main_page.py                # 业务主页面
|   `-- search_page.py              # 业务页面
|-- report.html                     # pytest-html生成的简单静态页面报告
|-- requirements.txt                # 项目的pip依赖库
|-- testcase                        
|   |-- __init__.py
|   |-- conftest.py                 # fixture
|   `-- test_case.py                # 执行用例
`-- utils
    |-- __init__.py
    `-- logger.py                   # loguru日志库的再次封装
```