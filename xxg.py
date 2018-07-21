import time,random


kw_num = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0')


global msg23
global code
global myVerson


myVerson = '3.2.0'

'''
鱼肝油机器人重置版 V3.2
2018.6.29
By Cubic @qq290577145
当前版本 myVerson
========
更新日志
========
2018.7.4:  v3.1.2&3.1.3:Bug Fixed
2018.7.5:  v3.1.4&3.1.5:新增霸群功能,改善霸群功能
2018.7.6:  v3.1.6      :新旧三连加入；暂停tql功能
2018.7.21: v3.2.0      :更新事件23算法；增加女孩子功能（ID=28）
'''


def xTime():
    i = str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    return i


'''
警告等级
S：Start   事件开始触发
I：Info    事件的提示信息
W：Warning 事件发出警告
E：Error   事件出错
Y：Yes     事件成功完成
N：No      事件未成功完成
'''


def writeLog_S(code):
    print('['+xTime()+']'+' [INFO_P]'+' [ID = '+str(code)+']'+'事件启动')
def writeLog_I(code, msg):
    print('['+xTime()+']'+' [INFO_P]'+' [ID = '+str(code)+']'+'事件提示： '+msg)
def writeLog_W(code, msg):
    print('['+xTime()+']'+' [WARNING_P]'+' [ID = '+str(code)+']'+'事件警告： '+msg)
def writeLog_E(code, msg):
    print('['+xTime()+']'+' [ERROR_P]'+' [ID = '+str(code)+']'+'事件出错，错误信息为： '+msg)
def writeLog_Y(code):
    print('['+xTime()+']'+' [INFO_P]'+' [ID = '+str(code)+']'+'事件正常结束')
def writeLog_N(code):
    print('['+xTime()+']'+' [WARNING_P]'+' [ID = '+str(code)+']'+'事件未正常结束')


def getEventID(input):    # 获取事件ID
    if '/测试' in input:
        return 1
    elif '/介绍' in input:
        return 2
    elif '倒计时' in input:
        return 3
    elif '女装' in input:
        return 4
    elif '海豹' in input:
        return 5
    elif '祝欧' in input:
        return 6
    elif '出货' in input:
        return 7
    elif '立方三连' in input:
        return 8
    elif '蹦迪' in input:
        return 9
    elif '机器人在吗' in input:
        return 10
    elif '迎新' in input:
        return 11
    elif '嗝屁' in input:
        return 12
    elif '新旧三连' in input:
        return 13
    elif '犯杏病' in input:
        return 14
    elif '吃B酱' in input:
        return 15
    elif '打恐龙' in input:
        return 16
    elif '炖月兔' in input:
        return 17
    elif '喝鱼粥' in input:
        return 18
    elif '喝奶茶' in input:
        return 19
    elif '炖梓念' in input:
        return 20
    elif '吃年糕' in input:
        return 21
    elif 'yosoro' in input:
        return 22
    elif '喵' in input:
        return 23
    elif '咕' in input:
        return 24
    elif 'tql' == input:
        return 25
    elif '..verson' == input:
        return 26
    elif '霸' in input:
        return 27
    elif '可爱的女孩子都是' in input:
        if '的哦' in input:
            return 28
        elif '的哦' in input:
            return 28
        else:
            return 0
    else:
        return 0


def onQQMessage(bot, contact, member, content):


    def sendQQ(msg):
        msg = str(msg)
        bot.SendTo(contact, msg)


    if bot.isMe(contact, member):
        print('[' + xTime() + ']' + ' [INFO_P]'+ ' 收到自身消息')


    else:
        code = int(getEventID(content))
        if code == 0:
            writeLog_I(0, '未检出关键词')
        elif code == 1:
            sendQQ('咕咕咕')
            writeLog_Y(code)
        elif code == 2:
            sendQQ('唔系小箱咕，倒计时就来找我吧')
            writeLog_Y(code)
        elif code == 3:
            if content[0:1].startswith(kw_num):
                i = '倒计时'
                if content[1:4] == i:
                    m = int(content[0])
                    if m > 7:
                        sendQQ(str(m)+'秒太长啦，试着换个短点的吧')
                        writeLog_I(code,'时长大于7')
                    elif m == 0:
                        sendQQ('看来你要当时间旅行者呢')
                        writeLog_I(code,'时长为零')
                    else:
                        sendQQ('要开始倒计时啦~三秒后开始，设定的时间是:'+str(m)+'秒')
                        writeLog_I(code,'正在进行'+str(m)+'秒计时')
                        time.sleep(3)
                        while m >= 0:
                            sendQQ(m)
                            time.sleep(1)
                            m = m - 1
                        writeLog_Y(code)
        elif code == 22:
            sendQQ("yosoro！")
            writeLog_Y(code)
        elif code == 23:
            if content.count('喵') == len(content):
                a = len(content)
                b = content.count('喵')
                msg23 = '咕'
                # while a > 0:
                #     msg23 = msg23 + msg23
                #     a = a - 1
                # # # 由于不明原因经过递归的msg23变量比原先长了一倍，用下面的代码截取一半
                # # # m = int(len(msg23) * 0.5 - 1)
                # # 递归出的变量输出成谜，直接截取输出原始文字长度
                # 7.21 更新字符串输出方式，优化算法
                sendQQ(msg23*b)
        elif code == 24:
            sendQQ('请停止你的鸽子行为')
            writeLog_Y(code)
        elif code == 25:
            writeLog_W(code, '功能暂停')
            # prop = random.randint(1 ,3)
            # if prop == 1:
                # sendQQ('tql')
            writeLog_Y(code)
        elif code == 26:
            sendQQ('group.yuganyou.projectXiaoxiang_Gu@v'+str(myVerson)+'(openSource)@Cubic')
            writeLog_Y(code)
        elif code == 27:
            if '群' in content:
                a = random.randint(1, 3)
                if a == 2:
                    sendQQ('抱歉，机器人就是可以一直在线的')
                    writeLog_Y(code)
                elif a == 3:
                    b = random.randint(1,10)
                    writeLog_I(code, '随机结果为' + str(b) + '后发出')
                    time.sleep(b)
                    sendQQ('抱歉，机器人就是可以一直在线的')
                    writeLog_Y(code)
                else:
                    writeLog_I(code,'随机结果为不响应')
                    writeLog_Y(code)
        else:
            if '肝' in contact.name:
                if code > 3:
                    if code == 4:
                        sendQQ('说起女装，群主似乎还没有女装呢')
                    # elif code == 5:
                    # elif code == 6:
                    # elif code == 7:
                    # elif code == 8:
                    # elif code == 9:
                    # elif code == 10:
                    # elif code == 11:
                    # elif code == 12:
                    elif code == 13:
                        sendQQ('忧心爷爷？')
                        time.sleep(0.5)
                        sendQQ('有心爷爷？')
                        time.sleep(0.5)
                        sendQQ('有新爷爷？')
                        writeLog_Y(code)
                    elif code == 28:
                        writeLog_S(code)
                        if content.rfind('哦') > 0:
                            sendQQ('可爱的'+str(content[8:content.find('的',4,len(content))])+'都是女孩子的哦！')
                            writeLog_I(code,'哦')
                            writeLog_Y(code)
                        elif content.rfind('噢') > 0:
                            sendQQ('可爱的' + str(content[8:content.find('的', 4, len(content))]) + '都是女孩子的噢！')
                            writeLog_I(code,'噢')
                            writeLog_Y(code)
                        else:
                            writeLog_E(code,'匹配出错')
                    # elif code == 14:
                    # elif code == 15:
                    # elif code == 16:
                    # elif code == 17:
                    # elif code == 18:
                    # elif code == 19:
                    # elif code == 20:
                    # elif code == 21:
                    # elif code == 25:
                else:
                    sendQQ('功能尚未开通')




