# -*- coding: utf-8 -*-
from user_state import set_user_state, get_user_state, \
    set_user_last_interact_time, get_user_last_interact_time, delete_user_state
from check import is_rollnum, is_location, is_phonenum, is_mail
import time
import re
from models import add_picked_card_num, add_picked_card_location, add_lost_card_num


def wechat_response(FromUserName, msg):
    global user_openid, content  # 此处通过参数来设置全局变量，感觉有隐患
    user_openid = FromUserName
    content = msg
    command_match = False
    # 各大功能命令
    commands = {'pack': pack_command,
                'lost': enter_log_lostcard,
                'pick': enter_log_picked_card,
                'reg': enter_register,
                u'取消': cancel_command
                }
    # key-用户当前所处的状态，value - 对应将执行的函数操作
    state_commands = {'ready_input_lost_card_rollnum': log_lost_card_rollnum,
                      'ready_input_pickedCard_rollNum': log_picked_card_rollnum,
                      'ready_input_picked_card_location': log_picked_card_location,
                      'ready_register_rollnum': register_rollnum,
                      'ready_register_mail': register_mail,
                      'ready_register_phone': register_phone}

    for key_word in commands:
        if re.match(key_word, content):
            response = commands[key_word]()
            command_match = True
            break
    if not command_match:
        state = get_user_state(user_openid)
        if not state:
            response = command_not_found()
        else:
            response = state_commands[state]()

    set_user_last_interact_time(user_openid, int(time.time()))
    return response


def pack_command():
    return 'success'


def cancel_command():
    delete_user_state(user_openid)
    reply = u'你成功挣脱了小鞭，交易中断'
    return reply


"""处理注册"""


def enter_register():
    set_user_state(user_openid, 'ready_register_rollnum')
    reply = u'叼毛，我们来注(p)册(y)了，请输入你的学号！'
    return reply


def register_rollnum():
    if is_rollnum(content):
        set_user_state(user_openid, 'ready_register_mail')
        reply = u'已记录你的学号！下面来输邮箱，不给就通知不了你啦（祝你丢卡）'
    else:
        reply = u'学号有误，请重新输入'
    return reply


def register_mail():
    if is_mail(content):
        set_user_state(user_openid, 'ready_register_phone')
        reply = u'已记录你的邮箱！下面来输手机号，不想给就发”bye“'
    else:
        reply = u'邮箱有误，请重新输入'
    return reply


def register_phone():
    if is_phonenum(content):
        reply = u'已记录你的手机号！注册完成'
    else:
        reply = u'手机有误，请重新输入'
    return reply


"""处理挂失"""


def enter_log_lostcard():
    set_user_state(user_openid, 'ready_input_lost_card_rollnum')
    return u'你这个几把又不见卡了？马上给我输入学号！'


def log_lost_card_rollnum():
    timeout = int(time.time()) - int(get_user_last_interact_time(user_openid))
    # 距离最后一次交互的时间太久，则退出模式
    if timeout > 20:  # 单位：秒
        delete_user_state(user_openid)
    if is_rollnum(content):
        add_lost_card_num(content)
        reply = u'已记录几把的学号！如果真有人这么倒霉，捡到几把的卡，我们也不得不第一时间通知你了'
    else:
        reply = '学号有误，请重新输入'
    return reply


"""处理拾卡"""


def enter_log_picked_card():
    set_user_state(user_openid, 'ready_input_pickedCard_rollNum')
    return u'请输入卡上的学号！'


def log_picked_card_rollnum():
    timeout = int(time.time()) - int(get_user_last_interact_time(user_openid))
    # 距离最后一次交互的时间太久，则退出模式
    if timeout > 20:  # 单位：秒
        delete_user_state(user_openid)
    if is_rollnum(content):
        add_picked_card_num(content)
        set_user_state(user_openid, 'ready_input_picked_card_location')
        reply = u'已记录该学号！请告诉我，你将卡放到哪里了？是不是在你下面'
    else:
        reply = '学号有误，请重新输入'
    return reply


def log_picked_card_location():
    timeout = int(time.time()) - int(get_user_last_interact_time(user_openid))
    # 距离最后一次交互的时间太久，则退出模式
    if timeout > 20:  # 单位：秒
        delete_user_state(user_openid)
    if is_location(content):
        add_picked_card_location(content)
        reply = u'感谢叼毛的拾卡，我们已经第一时间通知施主了'
    else:
        reply = ' 地点有误，请重新输入'
    return reply


def command_not_found():
    """非关键词回复"""
    return 'plz check your input'
