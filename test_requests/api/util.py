import requests


class Util:
    def get_token(self):
        request_params = {
            "corpid": "ww840acd806fdd8531",
            "corpsecret": "f7JQ26fQ4391_a0NZn_xuzKR5uYuVlTVAza1dlj5mjQ"
        }
        r = requests.get(
            "https://qyapi.weixin.qq.com/cgi-bin/gettoken",
            params=request_params
        )

        return r.json()['access_token']
