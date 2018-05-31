# \d可以匹配一个数字
# \w可以匹配一个字母或数字
# .可以匹配任意字符
# 用*表示任意个字符（包括0个）
# 用+表示至少一个字符
# 用?表示0个或1个字符
# 用{n}表示n个字符
# 用{n,m}表示n-m个字符
# \s可以匹配一个空格
# 元字符^$()*+?.[{|

import re
def is_valid_email(addr):
    ematch = re.compile(r'^[0-9a-zA-Z]+[\.]?[0-9a-zA-Z]+@[0-9a-zA-Z]+[\.][0-9a-zA-Z]+$')
    if ematch.match(addr):
        return True
    else:
        return False

# assert is_valid_email('someone@gmail.com')
# assert is_valid_email('bill.gates@microsoft.com')
# assert not is_valid_email('bob#example.com')
# assert not is_valid_email('mr-bob@example.com')
# print('ok')

def name_of_email(addr):
    nmatch = re.compile(r'^<?(\w+\s?\w+)>?\s?\w*@\w+\.\w+$')
    if nmatch.match(addr):
        return nmatch.match(addr).group(1)
    else:
        return False

assert name_of_email('<Tom Paris> tom@voyager.org') == 'Tom Paris'
assert name_of_email('tom@voyager.org') == 'tom'
print('ok')