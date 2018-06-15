__Author__ = 'jfsu'

info = {
    'name':'jfsu',
    'age':20
}

f=open('data.txt','w')
f.write(str(info))
f.close()


with open("data.txt",'r') as f:
    a = eval(f.read())
    print(a['age'])



# eval不是通用，标准的反序列化工具
# json 是标准的
import json
f = open('test.txt', 'w')
a = json.dumps(info)  #标准序列化
f.write(a)
f.close()

import json
with open("test.txt",'r') as f:
    b = json.loads(f.read())  # 标准反序列化
    print(b["name"])
