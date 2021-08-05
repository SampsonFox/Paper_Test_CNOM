# coding:utf-8

import json
import urllib
from wsgiref.simple_server import make_server

def max_num(nums):
    '''此处收到的是带有【】和，的看起来像是数组的字符串'''
    #把字符串变成数组
    num_list = []

    #储存数字的头指针和尾指针，头指针一定是‘【’后的第一个数字，所以预设为1
    num_range = [1,1]

    for i in range(len(nums)):

        if nums[i] == ',':
            #队列滑动数组
            num_range[0] = num_range[1]
            num_range[1] = i
            print(i,num_range)
            num = nums[num_range[0]:num_range[1]]
            num_list.append(num)

        if nums[i] == ']':
            num_list.append(int(nums[num_range[1]:]))

    print(num_list)

    max_1 = num_list[0]

    for i in num_list:
        if i > max_1:
            max_1 = i
    return max_1


def application(environ, start_response):
    '''api'''
    # 定义文件请求的类型和当前请求成功的code
    start_response('200 OK', [('Content-Type', 'list')])
    # environ是当前请求的所有数据，包括Header和URL，body，这里只涉及到get
    # 获取当前get请求的所有数据，返回是string类型
    params = urllib.parse.parse_qs(environ['QUERY_STRING'])
    list = params.get('list', [''])[0]
    print(list)
    # # 获取get中key为list的值
    # list = params['list']
    # print(list)

    return [json.dumps(max_num(list))]


if __name__ == "__main__":
    port = 5088
    httpd = make_server("0.0.0.0", port, application)
    print
    ("serving http on port {0}...".format(str(port)))
    httpd.serve_forever()





