import requests, urllib.parse, pandas
def get_name(encoded_text):
    return urllib.parse.quote(encoded_text, encoding='utf-8')
def get_header(mpt):
    return {
        "Host": "www.zhipin.com",
        "charset": "utf-8",
        "ver": "5.0901",
        "miniappversion": "5.0901",
        "zpappid": "10002",
        "user-agent": "Mozilla/5.0 (Linux; Android 10; IN2010 Build/QKQ1.191222.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.99 XWEB/3263 MMWEBSDK/20220204 Mobile Safari/537.36 MMWEBID/7687 MicroMessenger/8.0.20.2100(0x28001439) Process/appbrand2 WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64 MiniProgramEnv/android",
        "ua": "{\"model\":\"IN2010\",\"platform\":\"android\"}",
        "platform": "zhipin/android",
        "scene": "1106",
        "mpt": mpt,
        "wt2": "",
        "x-requested-with": "XMLHttpRequest",
        "content-type": "application/x-www-form-urlencoded",
        "referer": "https://servicewechat.com/wxa8da525af05281f3/448/page-frame.html"
    }
list1 = pandas.DataFrame(columns=['职位名称', '职位描述'])
def xiyu(mpt):
    try:
        job_name_list = ['广告设计', '人力资源', '法务专员']
        for iii in job_name_list:
            job_list = []
            job_name = get_name(str(iii))
            for ii in range(1, 35):
                url_list = 'https://www.zhipin.com/wapi/zpgeek/miniapp/search/joblist.json?pageSize=15&query=' + job_name + '&city=100010000&source=1&stage=&scale=&degree=&industry=&salary=&experience=&sortType=0&subwayLineId=&subwayStationId=&districtCode=&businessCode=&longitude=&latitude=&position=&expectId=&expectPosition=&page=' + str(
                    ii) + '&appId=10002'
                res_list = requests.get(url_list, headers=get_header(mpt)).json()
                # print(res_list)
                if res_list['code'] == 0 and res_list['zpData']['list'] != None:
                    for i in res_list['zpData']['list']:
                        encryptJobId = i['encryptJobId']
                        securityId = i['securityId']
                        lid = i['lid']
                        url_text = 'https://www.zhipin.com/wapi/zpgeek/miniapp/job/detail.json?securityId=' + securityId + '&jobId=' + encryptJobId + '&lid=' + lid + '&source=11&scene=&appId=10002'
                        res_text = requests.get(url_text, headers=get_header(mpt)).json()
                        # print(res_text)
                        jobName = res_text['zpData']['jobBaseInfoVO']['positionName']
                        jobDesc = str(res_text['zpData']['jobBaseInfoVO']['jobDesc']).replace('\n', '')
                        jobDesc = jobDesc.replace('\r', '')
                        job_list.append({jobName, jobDesc})
                        # print(job_list)
                        list1.loc[len(list1.index)] = [jobName, jobDesc]
                    list1.to_excel("BOSS直聘.xlsx", index=False)
                else:
                    print('error2')
                    break
                iii += 1
    except:
        print('error1')


if __name__ == '__main__':
    xiyu('')  # 个人信息协议头
