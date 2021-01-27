import requests


class Testwework:
    def get_token(self):
        """
        获取token
        请求方式： GET（HTTPS）
        请求地址： https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=ID&corpsecret=SECRET
        :return:
        """
        r = requests.get(
            "https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=ww840acd806fdd8531&corpsecret=f7JQ26fQ4391_a0NZn_xuzKR5uYuVlTVAza1dlj5mjQ")

        return r.json()['access_token']

    def test_create(self):
        """
        创建成员
        请求方式：POST（HTTPS）
        请求地址：https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token=ACCESS_TOKEN
        :return:
        """

        access_token = self.get_token()
        request_body = {
            "userid": "zhangsan",
            "name": "张三",
            "mobile": "13800000000",
            "department": [1]
        }
        r = requests.post(f"https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={access_token}",
                          json=request_body
                          )
        print(r.json())

    def test_get(self):
        """
        请求方式：GET（HTTPS）
        请求地址：https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token=ACCESS_TOKEN&userid=USERID
        :return:
        """
        access_token = self.get_token()
        r = requests.get(f"https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token={access_token}&userid=zhangsan")
        print(r.json())

    def test_update(self):
        """
        更新
        请求方式：POST（HTTPS）
        请求地址：https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token=ACCESS_TOKEN
        :return:
        """
        request_body = {
            "userid": "zhangsan",
            "name": "李四",
        }
        access_token = self.get_token()
        r = requests.post(f"https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token={access_token}",
                          json=request_body)
        print(r.json())

    def test_delete(self):
        """
        删除成员
        请求方式：GET（HTTPS）
        请求地址：https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token=ACCESS_TOKEN&userid=USERID
        :return:
        """
        access_token = self.get_token()
        r = requests.get(f"https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token={access_token}&userid=zhangsan")
        print(r.json())
