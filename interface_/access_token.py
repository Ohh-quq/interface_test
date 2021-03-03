import requests
import pytest


def test_demo():
	# 获取token
	url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=wwa96c9d5c142dc810&corpsecret=BTykvBxsTgQvTnvBuHwfoXwp5wHccwvxVOG2fRIVUDs"
	r = requests.get(url)
	token = r.json()['access_token']
	# 读取成员
	url = f"https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token={token}&userid=YangQingQing"
	r = requests.get(url)
	print(r.json())

