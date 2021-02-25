from test_requests.api.wework import WeWork


class TestWework:
    def test_create(self):
        # print(WeWork().test_get("zhangsan"))
        print(WeWork().test_create("zhangsan", "10086000066"))

    def test_get(self):
        print(WeWork().test_get("zhangsan"))

    def test_update(self):
        print(WeWork().test_update("zhangsan"))

    def test_delete(self):
        print(WeWork().test_delete("zhangsan"))
