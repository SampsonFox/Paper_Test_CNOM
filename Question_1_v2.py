#本程序是功能是判断两个给定字符串a_str和b_str是否完全相等

def BooleanExample(a_str,b_str):
    '''递归操作判断两个给定字符串a和b的第一个字符是否相等'''
    a = []
    b = []
    for i in a_str:
        a.append(i)
    for n in b_str:
        b.append(n)

    if len(a) != len(b):
        return False

    for x in range(len(b)):
        #判断字符串a的第一个字符和字符串b的第一个字符是否相等
        if a[0] == b[0]:
            a.pop(0)
            b.pop(0)
            return BooleanExample(a,b)

    #判断字符串b有没有剩余的元素，如果有，说明b和a不完全相等返回False，反之亦然
    return len(b) == 0

print(BooleanExample('asdawf','asdawf'))