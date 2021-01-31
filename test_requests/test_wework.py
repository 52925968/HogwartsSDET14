import random
import re

import pytest
import requests


def test_creat_data():
    "userid,name,mobile"
    data = [("kenanXX" + str(x),
             "柯南",
             "135%08d" % x)
            for x in range(10)
            ]
    return data


class Testwework:
    @pytest.fixture(scope="session")
    def token(self):
        request_params = {
            "corpid": "ww840acd806fdd8531",
            "corpsecret": "f7JQ26fQ4391_a0NZn_xuzKR5uYuVlTVAza1dlj5mjQ"
        }
        r = requests.get(
            "https://qyapi.weixin.qq.com/cgi-bin/gettoken",
            params=request_params
        )

        return r.json()['access_token']

    # def get_token(self):
    #     """
    #     获取token
    #     请求方式： GET（HTTPS）
    #     请求地址： https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=ID&corpsecret=SECRET
    #     :return:
    #     """
    #     request_params={
    #         "corpid":"ww840acd806fdd8531",
    #         "corpsecret":"f7JQ26fQ4391_a0NZn_xuzKR5uYuVlTVAza1dlj5mjQ"
    #     }
    #     r = requests.get(
    #         "https://qyapi.weixin.qq.com/cgi-bin/gettoken",
    #         params=request_params
    #     )
    #
    #     return r.json()['access_token']

    def test_create(self, token, userid, mobile, name="柯南", department=None):
        """
        创建成员
        请求方式：POST（HTTPS）
        请求地址：https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token=ACCESS_TOKEN
        :return:
        """

        # access_token = self.get_token()
        if department is None:
            department = [1]
        request_body = {
            "userid": userid,
            "name": name,
            "mobile": mobile,
            "department": department
        }
        r = requests.post(f"https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={token}",
                          json=request_body
                          )
        return r.json()

    def test_get(self, token, userid):
        """
        请求方式：GET（HTTPS）
        请求地址：https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token=ACCESS_TOKEN&userid=USERID
        :return:
        """
        # access_token = self.get_token()
        r = requests.get(f"https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token={token}&userid={userid}")
        return r.json()

    def test_update(self, token, userid, name="柯南"):
        """
        更新
        请求方式：POST（HTTPS）
        请求地址：https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token=ACCESS_TOKEN
        :return:
        """
        request_body = {
            "userid": userid,
            "name": name,
        }
        # access_token = self.get_token()
        r = requests.post(f"https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token={token}",
                          json=request_body)
        return r.json()

    def test_delete(self, token, userid):
        """
        删除成员
        请求方式：GET（HTTPS）
        请求地址：https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token=ACCESS_TOKEN&userid=USERID
        :return:
        """
        # access_token = self.get_token()
        r = requests.get(f"https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token={token}&userid={userid}")
        return r.json()

    @pytest.mark.parametrize("userid, name, mobile", test_creat_data())
    def test_wework(self, token, userid, name, mobile):
        """
        整体断言
        :return:
        """
        userid = userid
        name = name
        mobile = mobile
        try:
            assert "created" == self.test_create(token, userid, mobile)["errmsg"]
        except AssertionError as e:
            if "mobile existed" in e.__str__():
                re_userid = re.findall(":(.*)'$", e.__str__())[0]
                self.test_delete(token, re_userid)
                assert "created" == self.test_creat(token, userid, "13500000000")["errmsg"]

        assert name == self.test_get(token, userid)["name"]
        assert "updated" == self.test_update(token, userid, name="柯南")["errmsg"]
        assert name == self.test_get(token, userid)['name']
        assert "deleted" == self.test_delete(token, userid)["errmsg"]
        assert 60111 == self.test_get(token, userid)["errcode"]
