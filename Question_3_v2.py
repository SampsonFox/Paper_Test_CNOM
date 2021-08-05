from flask import Flask, request
app = Flask(__name__)

'''本实例可以实现写入一个数组后得到数组中的最大值'''
# 假设发送的请求链接为 http://localhost:5000/max?list=[1,2,3,4,5]
# 则返回其中最大值 5

def max_num(nums):
    '''本函数用于转换接收到的字符串并取最大值返回主程序'''
    '''此处收到的是带有[]和，的看起来像是数组的字符串'''
    #把字符串变成数组
    num_list = []
    max_1 = 0

    #储存数字的头指针和尾指针，头指针一定是‘[’后的第一个数字，所以预设为1
    num_range = [0,0]

    for i in range(len(nums)):

        if nums[i] == ',':
            #队列滑动数组
            num_range[0] = num_range[1]
            num_range[1] = i
            num = int(nums[num_range[0]+1:num_range[1]])
            num_list.append(num)

        #滑动到最后一位的情况
        if nums[i] == ']':
            num_list.append(int(nums[num_range[1]+1:-1]))

    max_1 = num_list[0]

    for i in num_list:
        if i > max_1:
            max_1 = i
    return str(max_1)

@app.route("/max")
def application():
    '''api主程序'''
    # 假设发送的请求链接为 http://localhost:5000/max?list=[1,2,3,4,5]
    # 可通过 request 来得到参数
    list = request.args.get("list")

    #调用判断函数得到最大值
    max_1 = max_num(list)

    return max_1

if __name__ == "__main__":
    app.run()
