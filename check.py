# _*_ coding:utf-8 _*_
import re


def is_rollnum(num):
    return (num.startswith('20')) and (len(num) == 10)


def is_mail(content):
    if len(content) > 7:
        pattern_mail = re.compile('[^\._-][\w\.-]+@(?:[A-Za-z0-9]+\.)+[A-Za-z]+$')
        match = pattern_mail.match(content)
        if match:
            return True
    else:
        return False


def is_phonenum(content):
    if len(content) == 11:
        pattern_phonenum = re.compile('^0\d{2,3}\d{7,8}$|^1[358]\d{9}$|^147\d{8}$')
        match = pattern_phonenum.match(content)
        if match:
            return True
    else:
        return False


def is_location(content):
    return True
