#!/usr/bin/env Python
# coding=utf-8
"""
the url structure of website
"""

from handlers.index import *

url = [
    (r'/login', IndexHandler),
    (r'/register', RegisterHandler),
    (r'/admin/ModPassword', AdminModPasswordHandler),
    (r'/admin/addStaff', AdminAddStaffHandler),
    (r'/admin/delStaff', DelStaffHandler),
    (r'/admin/getStaff', GetStaffHandler),
    (r'/getSex', GetSexHandler),
    (r'/addloudong', AddLoudongHandler),
    (r'/addlouceng', AddLoucengHandler),
    (r'/addfangjian', AddFanjianHandler),
    (r'/user/login', UserLoginHandler),
    (r'/user/ModPassword', UserModPasswordHandler),
    (r'/admin/getroom', AdminGetroomHandler),
    (r'/admin/getloudong', AdminGetloudongHandler),
    (r'/user/baoxiu', UserBaoxiuHandler),
    (r'/user/yijian', UserYijianHandler),
    (r'/admin/getbaoxiu', AdminGetbaoxiuHandler),
    (r'/admin/getyijian', AdminGetyijianHandler),
    (r'/admin/getloudong', AdminGetloudongHandler),
    (r'/admin/getloudonglist', AdminGetloudongListHandler),
    (r'/admin/getloudonglist', AdminGetloudongListHandler),
    (r'/admin/getloudonglist', AdminGetloudongListHandler),
]
