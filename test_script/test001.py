import allure, pytest

class Test_Abc:
    # 添加测试步骤
    @allure.step("第一个测试")
    # 添加严重级别
    @allure.severity(allure.severity_level.CRITICAL)
    # 测试用例链接，用例的地址
    @allure.testcase('http://www.baidu.com/test001')
    def test_abc_001(self):
        # 添加测试描述('描述内容','描述标题',)
        allure.attach('我是测试001的描述～～～','描述')

        assert 1

    @allure.severity(allure.severity_level.BLOCKER)
    def test_002(self):
        allure.attach('我是测试002的描述～～～','描述')
        assert False
# if __name__ == '__main__':
#     pytest.main(["-s","--alluredir report","test_001.py"])