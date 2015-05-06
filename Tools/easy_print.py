#-*-coding:utf-8-*-

import json


'''
    用来输出字典和数组，显示里面的中文内容
'''
def json_print(s):
    print json.dumps(s, encoding="utf-8", ensure_ascii=False)
    
def json_easy_dump(s):
    return json.dumps(s, encoding="utf-8", ensure_ascii=False)
def object2dict(obj):
    #convert object to a dict
    d = {}
    d['__class__'] = obj.__class__.__name__
#     d['__module__'] = obj.__module__
#     d.update(obj.__dict__)
    return d