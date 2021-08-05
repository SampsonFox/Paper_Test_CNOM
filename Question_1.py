#本程序是功能是判断两个给定字符串a和b是否完全相等

def Function(s,j):
    '''敲掉字符串s中下标为j的元素'''
    #
    ret = []

    for i in range(len(s)-1):
        ret.append('')

    print(len(s))

    d = 0

    for k in range(len(s)):

        if k == j:
            d=1

        else:
            ret[k - d] = s[k]

    return ''.join(ret)

def BooleanExample(a,b):
    '''递归操作判断两个给定字符串a和b的第一个字符是否相等'''

    if len(a) != len(b):
        return False

    for x in range(len(b)):
        print('len(b)',len(b))
        #判断字符串a的第一个字符和字符串b的第一个字符是否相等
        if a[0] == b[0]:
            #如果相等则调用自己进行递归操作
            #返回的值发送给Function函数去掉最前面的数
            #第二个Function是障眼法，因为如果x不等于0的话说明a[0]!=b[0] 但是这样的话本条语句就会被直接跳过
            #所以Function函数其实只需要一个参数就可以了
            return BooleanExample(Function(a,0),Function(b,x))

    #判断字符串b有没有剩余的元素，如果有，说明b和a不完全相等返回False，反之亦然
    return len(b) == 0

print(BooleanExample('asdawf','asdawf'))