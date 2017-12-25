import json

filename = '../source/namejson.json'
try:
    with open(filename) as file_object:
        username = json.load(file_object)
except FileNotFoundError:
    username = input("please input your name: ")
    with open(filename,'w') as file_object:
        json.dump(username,file_object)
else:
    print("welcome back,"+ username)
