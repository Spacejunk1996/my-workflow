# encoding: utf-8
import json
import sys

import browser_cookie3
import browsercookie as browsercookie
import requests as requests

from workflow import Workflow

API_KEY = 'your-pinboard-api-key'

class user():
    def __int__(self, id, user_id, username, name, avatar_url, org_name, position_name):
        self.id = id
        self.user_id = user_id
        self.username = username
        self.name = name
        self.avatar_url = avatar_url
        self.org_name = org_name
        self.position_name = position_name

def user(cls):
    return {
        'id': cls.id,
        'user_id': cls.user_id,
        'username': cls.username,
        'name': cls.name,
        'avatar_url': cls.avatar_url,
        'org_name': cls.org_name,
        'position_name': cls.position_name
    }

class Search_request():
    def __init__(self, search, page_id, mode, scene, folder_id):
        self.search = search
        self.page_id = page_id
        self.mode = mode
        self.scene = scene
        self.folder_id = folder_id

def search_to_direct(cls):
    return {
        'search': cls.search,
        'page_id': cls.page_id,
        'mode': cls.mode,
        'scene': cls.scene,
        'folder_id': cls.folder_id
    }

class Search_response():
    def __init__(self, user):
        self.__dict__ = user

    def add_user(self, user):
        self.users.append(user)

def search(query):
    cj = browsercookie.chrome()
    url = "https://apijoyspace.jd.com/v1/search"
    temp_request = Search_request(query, 'cgHL83y1H66MU9Frjlh2', 15, 'share', '')
    request_dic = search_to_direct(temp_request)
    request = json.dumps(request_dic)
    cookie = browser_cookie3.chrome(domain_name='.jd.com')
    # cookie = get_cookies("erp.jd.com")
    headers = {
        # 'Cookie': '__jdu=1648707705279400184581; shshshfpb=n9clUZ1-1tG8q0AlGur7wnQ; shshshfpa=4efe2be1-b972-eef4-557d-d76147e3a6fe-1648721635; TrackID=1WiG4XAHWh1pEyfOtLnJd4x7ReUX43gpx_x5Q2WhQVTDZRzQjjYAhL_D2AmOmm4RKJBikuOf00sEhrJ1dpIbrt3RyutEYPG0L_CZMk3oIYGJWaQxiFAXZEuwFeSUNXuA-; pinId=81xeT4lO_4rOXAsqqg30B7V9-x-f3wj7; shshshfp=af2938a2ac564ca534a17c627e6905ac; jd.erp.lang=zh_CN; jdd69fo72b8lfeoe=XXICZ6ST3OV65AIHVFWDHHVJXYISPWBUNP6HHDPMCANQOMPA7GTFFGHCFMOLMZO6YJJSOGM3GFZIAU4UHSTUXXFANA; qd_uid=L7G5IXUR-EMDKK8N36QGLFC5NL6FR; qd_fs=1661861662946; qd_ls=1661861662946; __jdv=137579179|direct|-|none|-|1661915503713; retina=1; cid=3; webp=1; mba_muid=1648707705279400184581; visitkey=11735532290693252; qd_ts=1662373509449; qd_sq=2; areaId=1; ipLoc-djd=1-2802-0-0; 3AB9D23F7A4B3C9B=BZOP3SI27JS3UQSPOWHN43T23I26N7WU7IF73ZFW767PRMF4HM3UC6X2XQIECZBTK5M2UCLX4DLAWQN7LHDVBD3J6Q; X-JACP-TOKEN=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJtb2JpbGUiOiIxNTAwMTIxMDcyOSIsInVzZXJJZCI6ImppYW5neml4dSIsImVtYWlsIjoiamlhbmd6aXh1QGpkLmNvbSIsInVzZXJuYW1lIjoiamlhbmd6aXh1IiwiaWF0IjoxNjYyNTM4NTg2LCJpc3MiOiJ4aW5neXVuLmpkLmNvbSIsInN1YiI6InNzbyIsImV4cCI6MTY2MjYyNDk4Nn0.bH7PZq0BIkfRabT83N2ZlqakikbrVfOCBdlHk4eb-m9W-AHIavOX-yBhMVtyAVuO8WpgnE_GQYkpSukJJ1OyHM9IHMvzuQcyF4f3gbVhKZCtl3upoRmQrlFGGpLxre_aGKEFriF6h1E6PaGg289iQHizfWdNiZ836fJjGFuaNLrwfXGT6U4wg6zg6TuDLP6crsE0JjY_08P_iNRE-3gjdm90ymH9M7jPB1Ns8sr8xkBPRfL6jZA0V84Nl-MmVOHpCxXV6VAS2HaIWN116DYGNn9U4Y9ZYKSIUB63snLFFF1rzUvo2u0LVvQNtjsl87ijLdijaj3xEgaBulb0R-9Ubg; token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6Ikhub3ZINFp1VzFRQVRqU2d3czFHIiwiaWF0IjoxNjYyNDQ3MzE3LCJleHAiOjE2NjMwNTIxMTd9.EuIkxKUXMpCR27aSJ5SJVuzKLfMsDklHyf0FucU1ikE; focus-team-id=00046419; focus-client=WEB; __jda=137579179.1648707705279400184581.1648707705.1662558012.1662561897.863; __jdb=137579179.1.1648707705279400184581|863.1662561897; __jdc=137579179; RT="z=1&dm=jd.com&si=1qvismg3p9g&ss=l7rqfcjb&sl=1&tt=xi"; focus-token=0e686e6ed06de14dfeafd9f3a352ee33',
        # 'Cookie': '__jdu=1648707705279400184581; shshshfpb=n9clUZ1-1tG8q0AlGur7wnQ; shshshfpa=4efe2be1-b972-eef4-557d-d76147e3a6fe-1648721635; shshshfp=af2938a2ac564ca534a17c627e6905ac; jd.erp.lang=zh_CN; jdd69fo72b8lfeoe=XXICZ6ST3OV65AIHVFWDHHVJXYISPWBUNP6HHDPMCANQOMPA7GTFFGHCFMOLMZO6YJJSOGM3GFZIAU4UHSTUXXFANA; qd_uid=L7G5IXUR-EMDKK8N36QGLFC5NL6FR; qd_fs=1661861662946; qd_ls=1661861662946; __jdv=137579179|direct|-|none|-|1661915503713; retina=1; cid=3; webp=1; mba_muid=1648707705279400184581; visitkey=11735532290693252; qd_ts=1662373509449; qd_sq=2; areaId=1; ipLoc-djd=1-2802-0-0; token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6Ikhub3ZINFp1VzFRQVRqU2d3czFHIiwiaWF0IjoxNjYyNDQ3MzE3LCJleHAiOjE2NjMwNTIxMTd9.EuIkxKUXMpCR27aSJ5SJVuzKLfMsDklHyf0FucU1ikE; __jd_ref_cls=elive_live_close_browser_pc; logbook_u=jiangzixu; TrackID=1AKN7Gkz46a1ujFmSN4OjsStu5E9buJR38B2igeDyAXRlxmNWoQeGOz688AG4wDAlaeO7tdS8u3sksdAmTY_AgR8TAY1hUBkba938WJwVZ95TJREdc2rlQmDeQE4AiXwB; pinId=vvqpEsAmxYpxxNbKfQGgEQ; pin=%E5%A7%BF%E7%94%9F%E7%A7%91%E6%8A%80; unick=%E5%A7%BF%E7%94%9F%E7%A7%91%E6%8A%80; ceshi3.com=000; _tp=FLwB%2Fh33LOB7HA0wB6kCyX9syEAuI2SrShECYJ1%2B8DI2%2BZ6dBrXtnwTSMCk65lD4; _pst=%E5%A7%BF%E7%94%9F%E7%A7%91%E6%8A%80; __USE_NEW_PAGEFRAME__=false; _base_=YKH2KDFHMOZBLCUV7NSRBWQUJPBI7JIMU5R3EFJ5UDHJ5LCU7R2NILKK5UJ6GLA2RGYT464UKXAI5TPYU4VBBBWDQX6FGO2MU2LUEV7IHRRGLNJQTRAV45D7XFAQPGQXTCNE6YVKRXISU2WLRJ47JBGDYZZELA6E4S4L2GMCISTNJJIUDMCG2YNJHAVPRUPVR23HV67S3YPT3KUNF2XFZ2E7RKLOUMQ6VUD7HOUCGWIP6DFCY2FTOVASYUCMC7CDSCF555UOYV4EB2RTH6M4DIDBJCUVH46IGQS4XX2SG4SOQWCP5WPWO6EFS7HEHMRWVKBRVHB33TFD42FNF7I3FHNLBFYW4JC55NT7KE6KT47K7XGVE7YLNCVYYQJXJA4AWVLKIN4C7LOHU2RV7JNQCYPEOXH3ZRU7WA5GKJMYGGXIN62B2M7UBSRP2BADLWCZF25FLID4YQWGVNQYUJ6OPOO2D7HILCXLWITI57M57T2UNCAXV73TM4ZERFD4FFFN; 3AB9D23F7A4B3C9B=BZOP3SI27JS3UQSPOWHN43T23I26N7WU7IF73ZFW767PRMF4HM3UC6X2XQIECZBTK5M2UCLX4DLAWQN7LHDVBD3J6Q; X-JACP-TOKEN=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJtb2JpbGUiOiIxNTAwMTIxMDcyOSIsInVzZXJJZCI6ImppYW5neml4dSIsImVtYWlsIjoiamlhbmd6aXh1QGpkLmNvbSIsInVzZXJuYW1lIjoiamlhbmd6aXh1IiwiaWF0IjoxNjYyODY3OTkwLCJpc3MiOiJ4aW5neXVuLmpkLmNvbSIsInN1YiI6InNzbyIsImV4cCI6MTY2Mjk1NDM5MH0.Bmx6YNw8_Z0Vek5GWj18RLeLyQqDHrs1ZAOn_SdS4MmebI2iUk1PQovE9f9xLU4oXmpXIOs5l2arwpVltGxo9HvSxvs46YguHunCSSTLJggad2o4mpxH4sWkpOR2de99ERo7mSy9zvnQJoQAAa1AtvqpHrK1iG_-q6mPsUFThkyVwc1B8VF4ANsBKpkeXZsTUWaHvqs7afQJXAa1aLZdnCXJ11BcLdtE9iJ6OII2rvg4R2sEGRMVnuXipaha5gyrzlqcpxMXRs9XvNKsaxZaI5NdGcL7-aivwE7hAJ-5u2RXiybBDIXxJglJN7c0k6cmoJEi06jY9ICP7rjzDZMHKQ; focus-team-id=00046419; focus-client=WEB; __jda=137579179.1648707705279400184581.1648707705.1662871647.1662875716.26; __jdc=137579179; focus-token=ed63db475522ef85d9c96452ac878d5a; __jdb=137579179.2.1648707705279400184581|26.1662875716; RT="z=1&dm=jd.com&si=v2zeovao53k&ss=l7wx9l8j&sl=4&tt=4cj&ld=a4f"; sso.jd.com=BJ.F881C3B05504D2040575B8E258E238A1.4020220911140127',
        'Content-Type': 'application/json'
    }

    response = requests.post(url, data=request, cookies=cookie, headers=headers)
    # response = requests.request("POST", url, headers=headers, data=request)

    # print(response)

    # str = "{\"status\":\"success\",\"data\":{\"users\":[{\"to_id\":\"HnovH4ZuW1QATjSgws1G\",\"permission_type\":0,\"share_id\":\"cgHL83y1H66MU9Frjlh2-2GzR0sBwHOSMWF0hATbV\",\"isUsed\":1,\"isShared\":true,\"id\":\"HnovH4ZuW1QATjSgws1G\",\"tenant_id\":\"00046419\",\"user_id\":\"uxEuZe7L5SLc7bzTHSPc-\",\"username\":\"jiangzixu\",\"name\":\"蒋子旭\",\"avatar_url\":\"https://img12.360buyimg.com/ee/jfs/t1/204221/24/21307/35766/6263ab9aE6442dbfd/cba6e55cba095484.jpg\",\"org_name\":\"商羚研发部\",\"full_org_name\":\"京东集团-京东零售-技术与数据中心-零售云业务部-零售云技术部-商羚研发部\",\"org_code\":\"00101961\",\"position_name\":\"软件开发工程师岗\",\"user_type\":1,\"status\":1,\"itemType\":\"user\"},{\"id\":\"TJQxrM5fAmbbzaFQxaqH\",\"tenant_id\":\"00046419\",\"user_id\":\"d5Pt8SHteLRBbfYi98PA9\",\"username\":\"jiangzixuan5\",\"name\":\"蒋子璇\",\"avatar_url\":\"https://m.360buyimg.com/jmeside/jfs/t1/26538/36/17937/87636/62bb1691Ea5b9fc24/be0bfb4cc4bcaaf3.png\",\"org_name\":\"技术项目交付组\",\"full_org_name\":\"京东集团-京东零售-技术与数据中心-项目交付与运营提升部-技术项目交付组\",\"org_code\":\"00008395\",\"position_name\":\"技术研发项目经理岗\",\"user_type\":1,\"status\":1,\"itemType\":\"user\",\"isUsed\":0,\"isShared\":false},{\"id\":\"mLpJf5O9Kvj9SAe5OFjv\",\"tenant_id\":\"00046419\",\"user_id\":\"6YJPDRdt2Mfab07fZcLrY\",\"username\":\"jiangzixuan6\",\"name\":\"江子璇\",\"avatar_url\":\"http://img12.360buyimg.com/ee/jfs/t1/94519/39/21897/26744/6213485aEca3247a6/0a635de3f7ae695c.jpg\",\"org_name\":\"芜湖冰洗部\",\"full_org_name\":\"京东集团-京东零售-3C家电事业群-五星电器-五星电器业务部-五星分部支持部-芜湖分部-芜湖分部家电支持组-芜湖冰洗部\",\"org_code\":\"00077758\",\"position_name\":\"冰洗品管岗\",\"user_type\":1,\"status\":1,\"itemType\":\"user\",\"isUsed\":0,\"isShared\":false}],\"orgs\":[],\"groups\":[{\"owner\":\"jiangzixu\",\"highlight\":[{\"uid\":\"<p style='color:yellow;'>jiangzixu</p>\"}],\"gid\":\"1027432346\",\"scode\":\"\",\"max\":1000,\"encrypt\":0,\"members\":[{\"app\":\"ee\",\"pin\":\"jiangzixu\",\"name\":\"蒋子旭\"}],\"name\":\"E端查询店铺企微授权信息需求\",\"avatar\":\"https://img30.360buyimg.com/ddgroup/jfs/t1/209492/28/20632/118023/6269269aEbcbfefaa/677c0b0c582153b3.png\",\"ownername\":\"蒋子旭\",\"itemType\":\"group\"},{\"owner\":\"jiangzixu\",\"highlight\":[{\"uid\":\"<p style='color:yellow;'>jiangzixu</p>\"}],\"gid\":\"1027999663\",\"scode\":\"\",\"max\":1000,\"encrypt\":0,\"members\":[{\"app\":\"ee\",\"pin\":\"jiangzixu\",\"name\":\"蒋子旭\"}],\"name\":\"优惠券领券分享页，入参不合法，无效告警问题修复\",\"avatar\":\"https://img30.360buyimg.com/ddgroup/jfs/t1/136107/28/27407/173220/6298838eE0f4183f3/a52aad5e0249bcb1.png\",\"ownername\":\"蒋子旭\",\"itemType\":\"group\"},{\"owner\":\"jiangzixu\",\"highlight\":[{\"uid\":\"<p style='color:yellow;'>jiangzixu</p>\"}],\"gid\":\"1027137162\",\"scode\":\"\",\"max\":1000,\"encrypt\":0,\"members\":[{\"app\":\"ee\",\"pin\":\"jiangzixu\",\"name\":\"蒋子旭\"}],\"name\":\"商羚券个人中心查询问题\",\"avatar\":\"https://img30.360buyimg.com/ddgroup/jfs/t1/129976/3/24091/214167/624e9626E70b99c31/b04aa7b335fcdb35.png\",\"ownername\":\"蒋子旭\",\"itemType\":\"group\"},{\"owner\":\"jiangzixu\",\"highlight\":[{\"uid\":\"<p style='color:yellow;'>jiangzixu</p>\"}],\"gid\":\"1025968758\",\"scode\":\"\",\"max\":1000,\"encrypt\":0,\"members\":[{\"app\":\"ee\",\"pin\":\"jiangzixu\",\"name\":\"蒋子旭\"}],\"name\":\"蒋子旭、王型明、周云\",\"avatar\":\"https://img30.360buyimg.com/ddgroup/jfs/t1/140778/15/26614/179560/61e01ae6Ed76f1233/decb32da55ebf76b.png\",\"ownername\":\"蒋子旭\",\"itemType\":\"group\"},{\"owner\":\"jiangzixu\",\"highlight\":[{\"uid\":\"<p style='color:yellow;'>jiangzixu</p>\"}],\"gid\":\"1029301633\",\"scode\":\"\",\"max\":1000,\"encrypt\":0,\"members\":[{\"app\":\"ee\",\"pin\":\"jiangzixu\",\"name\":\"蒋子旭\"}],\"name\":\"color网关 连接异常，商羚外贸优惠码弹窗可用率告警\",\"avatar\":\"https://img30.360buyimg.com/ddgroup/jfs/t1/102958/31/25645/24108/63034916E7a94a7ab/c2899cb9a597ad9a.png\",\"ownername\":\"蒋子旭\",\"itemType\":\"group\"},{\"owner\":\"jiangzixu\",\"highlight\":[{\"uid\":\"<p style='color:yellow;'>jiangzixu</p>\"}],\"gid\":\"1026843288\",\"scode\":\"\",\"max\":1000,\"encrypt\":0,\"members\":[{\"app\":\"ee\",\"pin\":\"jiangzixu\",\"name\":\"蒋子旭\"}],\"name\":\"雪花算法改造 潮汐系统接入\",\"avatar\":\"https://img30.360buyimg.com/ddgroup/jfs/t1/115619/35/23447/208505/6255c0acE0ecd86da/db92c9bcafb6249f.png\",\"ownername\":\"蒋子旭\",\"itemType\":\"group\"},{\"owner\":\"jiangzixu\",\"highlight\":[{\"uid\":\"<p style='color:yellow;'>jiangzixu</p>\"}],\"gid\":\"1027859537\",\"scode\":\"\",\"max\":1000,\"encrypt\":0,\"members\":[{\"app\":\"ee\",\"pin\":\"jiangzixu\",\"name\":\"蒋子旭\"}],\"name\":\"fastJSON改造\",\"avatar\":\"https://img30.360buyimg.com/ddgroup/jfs/t1/205612/36/22985/115711/628dcde5E8e88be44/d25fa84e75f76562.png\",\"ownername\":\"蒋子旭\",\"itemType\":\"group\"},{\"owner\":\"jiangzixu\",\"highlight\":[{\"uid\":\"<p style='color:yellow;'>jiangzixu</p>\"}],\"gid\":\"1025975480\",\"scode\":\"\",\"max\":1000,\"encrypt\":0,\"members\":[{\"app\":\"ee\",\"pin\":\"jiangzixu\",\"name\":\"蒋子旭\"}],\"name\":\"蒋子旭、王金鹏、于浩\",\"avatar\":\"https://img30.360buyimg.com/ddgroup/jfs/t1/97580/1/19569/208111/61df8f53E37af5832/08d6270a9bc9d1e1.png\",\"ownername\":\"蒋子旭\",\"itemType\":\"group\"},{\"owner\":\"jiangzixu\",\"highlight\":[{\"uid\":\"<p style='color:yellow;'>jiangzixu</p>\"}],\"gid\":\"1028878559\",\"scode\":\"\",\"max\":1000,\"encrypt\":0,\"members\":[{\"app\":\"ee\",\"pin\":\"jiangzixu\",\"name\":\"蒋子旭\"}],\"name\":\"MT批量加粉（公域加粉，手机号导入，订单加粉）技术方案沟通\",\"avatar\":\"https://img30.360buyimg.com/ddgroup/jfs/t1/160941/4/29046/19124/62da6d5dE28a058bb/89a10b07e073d38b.png\",\"ownername\":\"蒋子旭\",\"itemType\":\"group\"},{\"owner\":\"jiangzixu\",\"highlight\":[{\"uid\":\"<p style='color:yellow;'>jiangzixu</p>\"}],\"gid\":\"1027186480\",\"scode\":\"\",\"max\":1000,\"encrypt\":0,\"members\":[{\"app\":\"ee\",\"pin\":\"jiangzixu\",\"name\":\"蒋子旭\"}],\"name\":\"预发环境 - 验资接口风控问题\",\"avatar\":\"https://img30.360buyimg.com/ddgroup/jfs/t1/103219/22/27367/214970/6253fd2aEc6d79683/320bdf130c55e10d.png\",\"ownername\":\"蒋子旭\",\"itemType\":\"group\"}],\"mailGroups\":[]}}"

    result = json.loads(response.text, object_hook=Search_response)
    users = result.data.users

    for i in range(len(users)):
        wf.add_item(uid=users[i].username, arg=users[i].username, title="姓名: " + users[i].name, subtitle="erp: " + users[i].username, valid=True, icon=users[i].avatar_url)
    wf.send_feedback()


if __name__ == "__main__":
    wf = Workflow()
    query = sys.argv[1]
    search(query)
