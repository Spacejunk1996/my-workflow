# encoding: utf-8
import json

import pyperclip

API_KEY = 'jf'


def getJsonDict(jsonData):
    if type(jsonData) != dict:
        return
    for i in jsonData.keys():
        try:
            jsonData[i] = json.loads(jsonData[i])
            getJsonDict(jsonData[i])
        except TypeError:

            if (type(jsonData[i])) == dict:
                getJsonDict(jsonData[i])

            if (type(jsonData[i])) == list:
                for index in range(len(jsonData[i])):
                    try:
                        jsonData[i][index] = json.loads(jsonData[i][index])
                        getJsonDict(jsonData[i][index])
                    except TypeError:
                        if (type(jsonData[i][index])) == dict:
                            getJsonDict(jsonData[i][index])
                    except json.decoder.JSONDecodeError:
                        if (type(jsonData[i][index])) == dict:
                            getJsonDict(jsonData[i][index])

        except json.decoder.JSONDecodeError:

            if (type(jsonData[i])) == dict:
                getJsonDict(jsonData[i])

            if (type(jsonData[i])) == list:
                for index in range(len(jsonData[i])):
                    try:
                        jsonData[i][index] = json.loads(jsonData[i][index])
                        getJsonDict(jsonData[i][index])
                    except TypeError:
                        if (type(jsonData[i][index])) == dict:
                            getJsonDict(jsonData[i][index])
                    except json.decoder.JSONDecodeError:
                        if (type(jsonData[i][index])) == dict:
                            getJsonDict(jsonData[i][index])

if __name__ == "__main__":
    jsonData = json.loads(pyperclip.paste())
    # jsonData = '{"baseResult":{"resultCode":200,"resultMsg":"查询活动成功"},"couponRule":{"activeId":4,"activeType":"0","avtiveDeadTime":"23:59:59","avtiveLifeTime":"00:00:00","beginTime":1656382248000,"couponKey":"vender_FP#d534dc0030f04ffd85cea20bbb02b82c","couponType":1,"createtime":1656382263000,"dayNum":-1,"encryptedKey":"h1ies0h9o0p5c6o4u9p9o6nfs1o5a3eb","endTime":1659283198000,"id":"79924382","linkKey":"AAROH_xIpeffAs_-naABEFoewvPDA8VYTBOgZWrK9pw4n9SS7Yqfk87DxGuCDXD1-InrEC7kNJsAMbgQk5QXmQ8JP3lzrw","modifytime":1656382263000,"num":50000,"openRealName":0,"openType":"1","parallelBlack":false,"refId":0,"refType":0,"ruleExts":[{"channelParam":"1","channelType":"1000","createtime":1656382263000,"id":"441293398","modifytime":1656382263000,"roleId":"79924382"},{"channelParam":"2","channelType":"1000","createtime":1656382263000,"id":"441293399","modifytime":1656382263000,"roleId":"79924382"},{"channelParam":"3","channelType":"1000","createtime":1656382263000,"id":"441293400","modifytime":1656382263000,"roleId":"79924382"},{"channelParam":"4","channelType":"1000","createtime":1656382263000,"id":"441293401","modifytime":1656382263000,"roleId":"79924382"},{"channelParam":"-1","channelType":"appId","createtime":1656382263000,"id":"441293402","modifytime":1656382263000,"roleId":"79924382"},{"channelParam":"CN","channelType":"country","createtime":1656382263000,"id":"441293403","modifytime":1656382263000,"roleId":"79924382"},{"channelParam":"343","channelType":"orgtype","createtime":1656382263000,"id":"441293404","modifytime":1656382263000,"roleId":"79924382"},{"channelParam":"-1","channelType":"platform","createtime":1656382263000,"id":"441293405","modifytime":1656382263000,"roleId":"79924382"},{"channelParam":"1","channelType":"8011","createtime":1656382263000,"id":"441293406","modifytime":1656382263000,"roleId":"79924382"},{"channelParam":"AAROH_xIpeffAs_-naABEFoeWZmaT6qlgOBhEDI2GWUrikXn-zc","channelType":"putKey","createtime":1656382263000,"id":"441293407","modifytime":1656382263000,"roleId":"79924382"},{"channelParam":"AAROH_xIpeffAs_-naABEFoe6jfxaHO_QAFqySLMKHRG4GJka6oETI7RFyYIinMgT1Np6lxxQzpB2AbIgeUh13dX79StBg","channelType":"linkKey","createtime":1656382263000,"id":"441293408","modifytime":1656382263000,"roleId":"79924382"}],"ruleName":"商羚小程序99-10","toUrl":"babybus.jd.com","userClass":10000,"userRiskLevel":5,"yn":1}}'
    getJsonDict(jsonData)
    # print(json.dumps(jsonData))
    pyperclip.copy(json.dumps(jsonData))
    items = {"items": []}
    template = {
        "title": "",
        "subtitle": "",
        "arg": ""
    }
    template["title"] = jsonData
    template["subtitle"] = jsonData
    template["arg"] = jsonData
    items["items"].append(template)
    print(json.dumps(items))