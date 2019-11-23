import base64
import json

a = b'{"data":null,"info":"\\u7528\\u6237\\u5df2\\u767b\\u5f55","status":0}'

# a = bytes(map(ord, a))
a = a.decode("unicode-escape")


print(a)


