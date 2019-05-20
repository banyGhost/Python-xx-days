def get_suffix(str):
    pos = str.rfind('.')
    if 0 < pos < len(str) - 1:
        index = pos
        return str[index:]
    else:
        return ''


print(get_suffix('xxx.avi'))
print(get_suffix('xxx.mp3'))
print(get_suffix('xxx.'))
