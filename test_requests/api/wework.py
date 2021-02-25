import requests
import yaml

from test_requests.api.baseapi import BaseApi
from test_requests.api.util import Util


class WeWork(BaseApi):
    def __init__(self):
        self.token = Util().get_token()
        self.params["token"] = self.token

    def test_create(self, userid, mobile, name="柯南", department=None):
        """
        创建成员
        请求方式：POST（HTTPS）
        请求地址：https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token=ACCESS_TOKEN
        :return:
        """

        # access_token = self.get_token()
        if department is None:
            department = "1"
        # request_body = {
        #     "userid": userid,
        #     "name": name,
        #     "mobile": mobile,
        #     "department": department
        # }
        # r = requests.post(f"https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={self.token}",
        #                   json=request_body
        #                   )
        # return r.json()
        # data={
        #     "method": "post",
        #     "url": f"https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={self.token}",
        #     "json": {
        #         "userid": userid,
        #         "name": name,
        #         "mobile": mobile,
        #         "department": department
        #     }
        # }
        self.params["userid"] = userid
        self.params["name"] = name
        self.params["mobile"] = mobile
        self.params["department"] = department
        with open("../api/wework.yaml", encoding="utf-8") as f:
            data = yaml.load(f)
        return self.send(data["create"])

    def test_get(self, userid):
        """
        请求方式：GET（HTTPS）
        请求地址：https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token=ACCESS_TOKEN&userid=USERID
        :return:
        """
        # access_token = self.get_token()
        # r = requests.get(f"https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token={self.token}&userid={userid}")
        # data = {
        #    "method" : "get",
        #     "url": f"https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token={self.token}&userid={userid}"
        # }
        self.params["userid"] = userid
        with open("../api/wework.yaml", encoding="utf-8") as f:
            data = yaml.load(f)
        return self.send(data["get"])

    def test_update(self, userid, name="柯南"):
        """
        更新
        请求方式：POST（HTTPS）
        请求地址：https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token=ACCESS_TOKEN
        :return:
        """
        # request_body = {
        #     "userid": userid,
        #     "name": name
        # }
        # access_token = self.get_token()
        # r = requests.post(f"https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token={self.token}",
        #                 json=request_body)

        # data={
        #     "method":"post",
        #     "url":f"https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token={self.token}",
        #     "json":{
        #         "userid": userid,
        #         "name": name
        #     }
        # }

        self.params["userid"] = userid
        self.params["name"] = name
        with open("../api/wework.yaml") as f:
            data = yaml.load(f)
        return self.send(data["update"])

    def test_delete(self, userid):
        """
        删除成员
        请求方式：GET（HTTPS）
        请求地址：https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token=ACCESS_TOKEN&userid=USERID
        :return:
        """
        # access_token = self.get_token()
        r = requests.get(f"https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token={self.token}&userid={userid}")

        # data={
        #     "method": "get",
        #     "url": f"https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token={self.token}&userid={userid}"
        # }

        self.params["userid"] = userid
        with open("../api/wework.yaml") as f:
            data = yaml.load(f)
        return self.send(data["delete"])
