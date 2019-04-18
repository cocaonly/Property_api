#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import tornado.web
import methods.readdb as mrd

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        pass

    def post(self):
        result = {}
        username = self.get_argument("username")
        password = self.get_argument("password")
        user_infos = mrd.select_table(table="admin",column="*",condition="username",value=username)
        if user_infos:
            db_pwd = user_infos[0][1]
            userId = user_infos[0][2]
            if db_pwd == password:
                result.setdefault('code', 200)
                result.setdefault('data', 'successful')
                result.setdefault('userId', userId)
            else:
                result.setdefault('code', 404)
                result.setdefault('data', 'failure')
        else:
            result.setdefault('data', 'Without this user')
        self.write(result)


class RegisterHandler(tornado.web.RequestHandler):
    def get(self):
        pass

    def post(self):
        try:
            result = {}
            username = self.get_argument("username")
            user_infos = mrd.select_table(table="admin", column="*", condition="username", value=username)
            if user_infos:
                result.setdefault('code', 200)
                result.setdefault('data', "该用户已存在")
                return self.write(result)
            password = self.get_argument("password")
            key = "(username,password)"
            value = f"('{username}',{password})"
            user_infos = mrd.add_table(table="admin", key=key ,value=value)
            if user_infos:
                result.setdefault('code', 404)
                result.setdefault('data', "failure")
            else:
                result.setdefault('code', 200)
                result.setdefault('data', "successful")
            self.write(result)
        except:
            result.setdefault('code', 200)
            result.setdefault('data', "该用户已存在")
            self.write(result)


class GetStaffHandler(tornado.web.RequestHandler):
    def get(self):
        pass

    def post(self):
        result = {}
        user_list = []
        # enterpriseId = self.get_argument("id")
        user_infos = mrd.select_table(table="staff",column="*",condition="1",value="1")
        for user_info in user_infos:
            oneInofo = {}
            oneInofo['id'] = user_info[0]
            oneInofo['userId'] = user_info[1]
            oneInofo['name'] = user_info[2]
            oneInofo['job'] = user_info[3]
            oneInofo['sex'] = user_info[4]
            oneInofo['hiredate'] = user_info[5]
            oneInofo['department'] = user_info[7]
            oneInofo['remark'] = user_info[6]
            user_list.append(oneInofo)
        result.setdefault('code', 200)
        result.setdefault('data', user_list)
        self.write(result)


class AdminAddStaffHandler(tornado.web.RequestHandler):
    def get(self):
        pass

    def post(self):
        result = {}
        userId = self.get_argument("userId")
        name = self.get_argument("name")
        job = self.get_argument("job")
        sex = self.get_argument("sex")
        rzsj = self.get_argument("rzsj")
        department = self.get_argument("department")
        remark = self.get_argument("remark")

        key = "(userId,name,job,sex,rzsj,department,remark)"
        value = f"({userId},'{name}','{job}','{sex}','{rzsj}','{department}','{remark}')"
        infos = mrd.add_table(table="staff", key=key, value=value)
        if infos:
            result.setdefault('code', 404)
            result.setdefault('data', "failure")
        else:
            result.setdefault('code', 200)
            result.setdefault('data', "successful")
        self.write(result)


class DelStaffHandler(tornado.web.RequestHandler):
    def get(self):
        pass

    def post(self):
        result = {}
        id = self.get_argument("id")
        value = f"(id = {id})"
        infos = mrd.del_table(table="staff", value=value)
        if infos:
            result.setdefault('code', 404)
            result.setdefault('data', "failure")
        else:
            result.setdefault('code', 200)
            result.setdefault('data', "successful")
        self.write(result)


class AdminModPasswordHandler(tornado.web.RequestHandler):
    def get(self):
        pass

    def post(self):
        result = {}
        id = self.get_argument("id")
        password = self.get_argument("password")
        where = f"(id = {id})"
        value = f"password = {password}"
        infos = mrd.update_table(table="admin", value=value, where=where)
        if infos:
            result.setdefault('code', 404)
            result.setdefault('data', "failure")
        else:
            result.setdefault('code', 200)
            result.setdefault('data', "successful")
        self.write(result)


class AddAssetsHandler(tornado.web.RequestHandler):
    def get(self):
        pass

    def post(self):
        result = {}
        assets = str(self.get_argument("assets"))
        type = self.get_argument("type")
        entrytime = self.get_argument("entrytime")
        deliverytime = self.get_argument("deliverytime")
        remark = self.get_argument("remark")
        personid = self.get_argument("personid", 0)
        status = self.get_argument("status", 0)
        companyid = self.get_argument("companyid")
        assetsid = self.get_argument("assetsid")
        key = "(assets,type,entrytime,deliverytime,remark,personid,status,companyid,assetsid)"
        value = f"('{assets}','{type}','{entrytime}','{deliverytime}','{remark}','{personid}','{status}','{companyid}','{assetsid}')"
        infos = mrd.add_table(table="assets", value=value, key=key)
        if infos:
            result.setdefault('code', 404)
            result.setdefault('data', "failure")
        else:
            result.setdefault('code', 200)
            result.setdefault('data', "successful")
        self.write(result)


class GetAssetsHandler(tornado.web.RequestHandler):
    def get(self):
        pass

    def post(self):
        result = {}
        user_list = []
        companyid = self.get_argument("companyid")
        user_infos = mrd.select_table(table="assets",column="*",condition="companyid",value=companyid)
        for user_info in user_infos:
            oneInofo = {}
            oneInofo['assetId'] = user_info[0]
            oneInofo['personid'] = user_info[1]
            oneInofo['assets'] = user_info[2]
            oneInofo['type'] = user_info[3]
            oneInofo['entrytime'] = user_info[4]
            oneInofo['deliverytime'] = user_info[5]
            oneInofo['remark'] = user_info[6]
            oneInofo['status'] = user_info[7]
            oneInofo['companyid'] = user_info[8]
            oneInofo['assetsid'] = user_info[9]
            user_list.append(oneInofo)
        result.setdefault('code', 200)
        result.setdefault('data', user_list)
        self.write(result)


class DelAssetsHandler(tornado.web.RequestHandler):
    def get(self):
        pass

    def post(self):
        result = {}
        id = self.get_argument("id")
        value = f"(id = {id})"
        infos = mrd.del_table(table="assets", value=value)
        if infos:
            result.setdefault('code', 404)
            result.setdefault('data', "failure")
        else:
            result.setdefault('code', 200)
            result.setdefault('data', "successful")
        self.write(result)


class AllotAssetsHandler(tornado.web.RequestHandler):
    def get(self):
        pass

    def post(self):
        result = {}
        id = self.get_argument("assetsid")
        personid = self.get_argument("personid")
        where = f"(id = {id})"
        value = f"personid = {personid}, status = 1"
        infos = mrd.update_table(table="assets", value=value, where=where)
        if infos:
            result.setdefault('code', 404)
            result.setdefault('data', "failure")
        else:
            result.setdefault('code', 200)
            result.setdefault('data', "successful")
        self.write(result)


class PersonLoginHandler(tornado.web.RequestHandler):
    def get(self):
        pass

    def post(self):
        result = {}
        account = self.get_argument("account")
        password = self.get_argument("password")
        user_infos = mrd.select_table(table="personnel",column="*",condition="account",value=account)
        if user_infos:
            db_pwd = user_infos[0][11]
            userId = user_infos[0][1]
            personId = user_infos[0][0]
            if db_pwd == password:
                result.setdefault('code', 200)
                result.setdefault('data', 'successful')
                result.setdefault('userId', userId)
                result.setdefault('personId', personId)
            else:
                result.setdefault('code', 404)
                result.setdefault('data', 'failure')
        else:
            result.setdefault('data', 'Without this user')
        self.write(result)


class PersonModPasswordHandler(tornado.web.RequestHandler):
    def get(self):
        pass

    def post(self):
        result = {}
        id = self.get_argument("id")
        password = self.get_argument("password")
        where = f"(id = {id})"
        value = f"password = {password}"
        infos = mrd.update_table(table="personnel", value=value, where=where)
        if infos:
            result.setdefault('code', 404)
            result.setdefault('data', "failure")
        else:
            result.setdefault('code', 200)
            result.setdefault('data', "successful")
        self.write(result)


class GetSexHandler(tornado.web.RequestHandler):
    def get(self):
        pass

    def post(self):
        result = {}
        result['data'] = [[3,2,3,4,5,4,5,3,5,4,1,2]]
        sex = {}
        sql = "select s.sex,count(s.sex) from staff s GROUP BY sex;"
        infos = mrd.exec_sql(sql=sql)
        print(infos)
        if infos:
            result.setdefault('code', 200)
            for info in infos:
                sex[info[0]] = info[1]
            result['data'].append(sex)
        else:
            result.setdefault('code', 404)
            result.setdefault('data', "failure")
        self.write(result)


class AddLoudongHandler(tornado.web.RequestHandler):
    def get(self):
        pass

    def post(self):
        result = {}
        name = self.get_argument("name")
        key = "(name)"
        value = f"('{name}')"
        infos = mrd.add_table(table="loudong", value=value, key=key)
        user_infos = mrd.select_table(table="loudong",column="max(id)",condition="1",value="1")
        if infos:
            result.setdefault('code', 404)
            result.setdefault('data', "failure")
        else:
            result.setdefault('code', 200)
            result.setdefault('data', {'loudong_id':user_infos[0][0]})
        self.write(result)


class AddLoucengHandler(tornado.web.RequestHandler):
    def get(self):
        pass

    def post(self):
        result = {}
        loudong_id = self.get_argument("loudong_id")
        name = self.get_argument("name")
        cengshu = self.get_argument("cengshu")
        key = "(loudong_id,name,cengshu)"
        value = f"('{loudong_id}','{name}','{cengshu}')"
        infos = mrd.add_table(table="louceng", value=value, key=key)
        user_infos = mrd.select_table(table="louceng",column="max(id)",condition="1",value="1")
        if infos:
            result.setdefault('code', 404)
            result.setdefault('data', "failure")
        else:
            result.setdefault('code', 200)
            result.setdefault('data', {'louceng_id':user_infos[0][0]})
        self.write(result)



class AddFanjianHandler(tornado.web.RequestHandler):
    def get(self):
        pass

    def post(self):
        result = {}
        loudong_id = self.get_argument("loudong_id")
        louceng_id = self.get_argument("louceng_id")
        name = self.get_argument("name", 1)
        shui = self.get_argument("shui", 1)
        dian = self.get_argument("dian", 1)
        meiqi = self.get_argument("meiqi", 1)
        mensuo = self.get_argument("mensuo", 1)
        deng = self.get_argument("deng", 1)
        xiashui = self.get_argument("xiashui", 1)
        dire = self.get_argument("dire", 1)
        user_name = self.get_argument("user_name")
        phone_number = self.get_argument("phone_number")
        password = self.get_argument("password", 123456)
        status = self.get_argument("status", 1)
        key = "(loudong_id,louceng_id,name,shui,dian,meiqi,mensuo,deng,xiashui,dire,user_name,phone_number,password,status)"
        value = f"('{loudong_id}','{louceng_id}','{name}','{shui}','{dian}','{meiqi}','{mensuo}','{deng}','{xiashui}','{dire}','{user_name}','{phone_number}','{password}','{status}')"
        infos = mrd.add_table(table="fangjian", value=value, key=key)
        if infos:
            result.setdefault('code', 404)
            result.setdefault('data', "failure")
        else:
            result.setdefault('code', 200)
            result.setdefault('data', "successful")
        self.write(result)


class UserLoginHandler(tornado.web.RequestHandler):
    def get(self):
        pass

    def post(self):
        result = {}
        phone_number = self.get_argument("phone_number")
        password = self.get_argument("password")
        user_infos = mrd.select_table(table="fangjian",column="*",condition="phone_number",value=phone_number)
        if user_infos:
            user_infos = user_infos[0]
            db_pwd = user_infos[13]
            if db_pwd == password:
                result.setdefault('code', 200)
                result.setdefault('data', 'successful')
                oneInofo = {}
                oneInofo['id'] = user_infos[0]
                oneInofo['loudong_id'] = user_infos[1]
                oneInofo['louceng_id'] = user_infos[2]
                oneInofo['name'] = user_infos[3]
                oneInofo['shui'] = user_infos[4]
                oneInofo['dian'] = user_infos[5]
                oneInofo['meiqi'] = user_infos[6]
                oneInofo['mensuo'] = user_infos[7]
                oneInofo['deng'] = user_infos[8]
                oneInofo['xiashui'] = user_infos[9]
                oneInofo['dire'] = user_infos[10]
                oneInofo['user_name'] = user_infos[11]
                oneInofo['phone_number'] = user_infos[12]
                oneInofo['status'] = user_infos[14]
                result.setdefault('userId', oneInofo)
            else:
                result.setdefault('code', 404)
                result.setdefault('data', 'failure')
        else:
            result.setdefault('data', 'Without this user')
        self.write(result)


class UserModPasswordHandler(tornado.web.RequestHandler):
    def get(self):
        pass

    def post(self):
        result = {}
        id = self.get_argument("id")
        password = self.get_argument("password")
        where = f"(id = {id})"
        value = f"password = {password}"
        infos = mrd.update_table(table="fangjian", value=value, where=where)
        if infos:
            result.setdefault('code', 404)
            result.setdefault('data', "failure")
        else:
            result.setdefault('code', 200)
            result.setdefault('data', "successful")
        self.write(result)


class AdminGetroomHandler(tornado.web.RequestHandler):
    def get(self):
        pass

    def post(self):
        result = {}
        id = self.get_argument("id")
        user_infos = mrd.select_table(table="fangjian",column="*",condition="id",value=id)
        if user_infos:
            user_infos = user_infos[0]
            result.setdefault('code', 200)
            oneInofo = {}
            oneInofo['id'] = user_infos[0]
            oneInofo['loudong_id'] = user_infos[1]
            oneInofo['louceng_id'] = user_infos[2]
            oneInofo['name'] = user_infos[3]
            oneInofo['shui'] = user_infos[4]
            oneInofo['dian'] = user_infos[5]
            oneInofo['meiqi'] = user_infos[6]
            oneInofo['mensuo'] = user_infos[7]
            oneInofo['deng'] = user_infos[8]
            oneInofo['xiashui'] = user_infos[9]
            oneInofo['dire'] = user_infos[10]
            oneInofo['user_name'] = user_infos[11]
            oneInofo['phone_number'] = user_infos[12]
            oneInofo['status'] = user_infos[14]
            result.setdefault('data', oneInofo)
        else:
            result.setdefault('code', 404)
            result.setdefault('data', "failure")
        self.write(result)


class AdminGetloudongHandler(tornado.web.RequestHandler):
    def get(self):
        pass

    def post(self):
        result = {}
        id = self.get_argument("id")
        user_infos = mrd.select_table(table="louceng",column="*",condition="id",value=id)
        if user_infos:
            user_infos = user_infos[0]
            result.setdefault('code', 200)
            oneInofo = {}
            oneInofo['id'] = user_infos[0]
            oneInofo['loudong_id'] = user_infos[1]
            oneInofo['louceng_id'] = user_infos[2]
            oneInofo['name'] = user_infos[3]
            oneInofo['shui'] = user_infos[4]
            oneInofo['dian'] = user_infos[5]
            oneInofo['meiqi'] = user_infos[6]
            oneInofo['mensuo'] = user_infos[7]
            oneInofo['deng'] = user_infos[8]
            oneInofo['xiashui'] = user_infos[9]
            oneInofo['dire'] = user_infos[10]
            oneInofo['user_name'] = user_infos[11]
            oneInofo['phone_number'] = user_infos[12]
            oneInofo['status'] = user_infos[14]
            result.setdefault('data', oneInofo)
        else:
            result.setdefault('code', 404)
            result.setdefault('data', "failure")
        self.write(result)


class UserBaoxiuHandler(tornado.web.RequestHandler):
    def get(self):
        pass

    def post(self):
        result = {}
        fangjian_id = self.get_argument("fangjian_id")
        shui = self.get_argument("shui", 1)
        dian = self.get_argument("dian", 1)
        meiqi = self.get_argument("meiqi", 1)
        mensuo = self.get_argument("mensuo", 1)
        deng = self.get_argument("deng", 1)
        xiashui = self.get_argument("xiashui", 1)
        dire = self.get_argument("dire", 1)
        key = "(fangjian_id,shui,dian,meiqi,mensuo,deng,xiashui,dire)"
        value = f"('{fangjian_id}','{shui}','{dian}','{meiqi}','{mensuo}','{deng}','{xiashui}','{dire}')"
        infos = mrd.add_table(table="baoxiu", value=value, key=key)
        if infos:
            result.setdefault('code', 404)
            result.setdefault('data', "failure")
        else:
            result.setdefault('code', 200)
            result.setdefault('data', "successful")
        where = f"(id = {fangjian_id})"
        value = f"status = 0,shui={shui},dian={dian},meiqi={meiqi},mensuo={mensuo},deng={deng},xiashui={xiashui},dire={dire}"
        infos = mrd.update_table(table="fangjian", value=value, where=where)
        self.write(result)


class AdminGetbaoxiuHandler(tornado.web.RequestHandler):
    def get(self):
        pass

    def post(self):
        result = {}
        user_list = []
        user_infos = mrd.select_table(table="baoxiu",column="*",condition="1",value="1")
        for user_info in user_infos:
            oneInofo = {}
            oneInofo['id'] = user_info[0]
            oneInofo['fangjian_id'] = user_info[1]
            oneInofo['shui'] = user_info[2]
            oneInofo['dian'] = user_info[3]
            oneInofo['meiqi'] = user_info[4]
            oneInofo['mensuo'] = user_info[5]
            oneInofo['deng'] = user_info[6]
            oneInofo['xiashui'] = user_info[7]
            oneInofo['dire'] = user_info[8]
            fangjian_info = mrd.select_table(table="fangjian", column="name,loudong_id", condition="id",
                                             value=str(oneInofo['fangjian_id']))[0]
            oneInofo['fangjian_name'] = fangjian_info[0]
            oneInofo['loudong_name'] = mrd.select_table(table="loudong", column="name", condition="id",
                                             value=str(fangjian_info[1]))[0][0]
            user_list.append(oneInofo)
        result.setdefault('code', 200)
        result.setdefault('data', user_list)
        self.write(result)


class UserYijianHandler(tornado.web.RequestHandler):
    def get(self):
        pass

    def post(self):
        result = {}
        fangjian_id = self.get_argument("fangjian_id")
        yijian = self.get_argument("yijian", "")
        key = "(fangjian_id,yijian)"
        value = f"('{fangjian_id}','{yijian}')"
        infos = mrd.add_table(table="yijian", value=value, key=key)
        if infos:
            result.setdefault('code', 404)
            result.setdefault('data', "failure")
        else:
            result.setdefault('code', 200)
            result.setdefault('data', "successful")
        self.write(result)


class AdminGetyijianHandler(tornado.web.RequestHandler):
    def get(self):
        pass

    def post(self):
        result = {}
        user_list = []
        user_infos = mrd.select_table(table="yijian",column="*",condition="1",value="1")
        for user_info in user_infos:
            oneInofo = {}
            oneInofo['id'] = user_info[0]
            oneInofo['fangjian_id'] = user_info[1]
            oneInofo['yijian'] = user_info[2]
            fangjian_info = mrd.select_table(table="fangjian", column="name,loudong_id", condition="id",
                                             value=str(oneInofo['fangjian_id']))[0]
            oneInofo['fangjian_name'] = fangjian_info[0]
            oneInofo['loudong_name'] = mrd.select_table(table="loudong", column="name", condition="id",
                                             value=str(fangjian_info[1]))[0][0]
            user_list.append(oneInofo)
        result.setdefault('code', 200)
        result.setdefault('data', user_list)
        self.write(result)


class AdminGetloudongHandler(tornado.web.RequestHandler):
    def get(self):
        pass

    def post(self):
        result = {}
        id = self.get_argument("loudong_id")
        oneInofo = {}
        loudong_infos = mrd.select_table(table="loudong",column="*",condition="id",value=id)[0]
        if loudong_infos:
            oneInofo['loudong_name'] = loudong_infos[1]
            oneInofo['louceng_info'] = []
        else:
            result.setdefault('code', 404)
            result.setdefault('data', "failure")
        louceng_infos = mrd.select_table(table="louceng", column="*", condition="loudong_id",value=id)
        for louceng_info in louceng_infos:
            louceng = {}
            louceng['louceng_name'] = louceng_info[2]
            louceng['cengshu'] = louceng_info[3]
            louceng['fangjian_info'] = []
            fangjian_infos = mrd.select_table(table="fangjian", column="id,name,user_name", condition="louceng_id", value=str(louceng_info[0]))
            for fangjian_info in fangjian_infos:
                fanjian = {}
                fanjian['fangjian_id'] = fangjian_info[0]
                fanjian['fangjian_name'] = fangjian_info[1]
                fanjian['user_name'] = fangjian_info[2]
                louceng['fangjian_info'].append(fanjian)
            oneInofo['louceng_info'].append(louceng)
        result.setdefault('data', oneInofo)
        self.write(result)


class AdminGetloudongListHandler(tornado.web.RequestHandler):
    def get(self):
        pass

    def post(self):
        result = {}
        user_list = []
        loudong_infos = mrd.select_table(table="loudong",column="*",condition="1",value="1")
        for loudong_info in loudong_infos:
            if loudong_info:
                oneInfo = {}
                oneInfo['loudong_id'] = loudong_info[0]
                oneInfo['loudong_name'] = loudong_info[1]
                user_list.append(oneInfo)
                result.setdefault('code', 200)
                result.setdefault('data', user_list)
            else:
                result.setdefault('code', 404)
                result.setdefault('data', "failure")
        self.write(result)




