import re

if __name__ == "__main__":
    data = '''peter.p@agvf.com
            radadarade@gmail.com'''
    pattern = re.compile(r"(\w+)(\.\w+)*(@\w+(\.\w+)+)")
    result = re.finditer(pattern, data)
    print(result)
    for p in result:
        print(p.group())
