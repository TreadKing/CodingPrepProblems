import re

def urlify(s1):
    s1 = s1.strip()
    s1 = re.sub(r'\s+', '%20', s1)
    return s1

print(urlify('    hello world   '))