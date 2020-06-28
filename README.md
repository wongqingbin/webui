# 说明书

## allure

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

## pytest-html

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

## pytest运行显示print、logger日志 -s

```bash
pytest -s -q
```
