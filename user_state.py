# -*- coding: utf-8 -*-
import models
import pylibmc  # 以使用 Memcached 功能

global mc
mc = pylibmc.Client()  # 初始化一个memcache实例用来保存用户的操作


def set_user_state(openid, state):
    """设置用户状态"""
    return mc.set(openid, state)


def delete_user_state(openid):
    mc.delete(openid)
    return None


def get_user_state(openid):
    """获取用户状态"""
    return mc.get(openid)


def set_user_last_interact_time(openid, timestamp):
    """保存最后一次交互时间"""
    mc.set(openid+':last_interact_time', timestamp)
    return None


def get_user_last_interact_time(openid):
    """获取最后一次交互时间"""
    last_time = mc.get(openid+':last_interact_time')
    if last_time:
        return last_time
    else:
        return 0
