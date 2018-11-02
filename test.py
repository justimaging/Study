import  json

fo = open("json.txt")
info  = json.load(fo)
print(info['a'])
# # str = fo.read()
# # print(str)
# # params = json.loads(str)
# # print(params['name'])

#info = {'name' : 'jay', 'sex' : 'male', 'age': 22}
# info = fo.read()
# jsoninfo = json.dumps(info)
