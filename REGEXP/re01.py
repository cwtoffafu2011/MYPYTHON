import re

print(re.match('www','www.qishon.con').start())#返回匹配开始的位置
print(re.match('www','www.qishon.con').end())#返回匹配结束的位置
print(re.match('www','www.qishon.con').span())# 返回一个元组包含匹配 (开始,结束) 的位置