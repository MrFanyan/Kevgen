# 验证正则子模式
import re

# pattern = re.compile(r'<(?P<he>\w+)><(?P<la>\w+)>.*</(?P=la)></(?P=he)>')
pattern = re.compile(r'<\w+><\w+>.*</\w+></\w+>')

ret = pattern.search('lala<maodan><span>七里香是周杰伦唱的歌</span></maodan>dudu')

print(ret.group())


