# _*_ coding:utf-8 _*_
import MySQLdb
import sae.const  # 新浪云下连接MySQL的API
from LightMysql import LightMysql

username = 'test'
roll_number = '293'
card_number = '234'
mobile = '1342222'
mail = 'pyrl@ou.com'

# config info, necessary parameters host, port, user, passwd, db
dbconfig = {'host': sae.const.MYSQL_HOST,
            'port': int(sae.const.MYSQL_PORT),
            'user': sae.const.MYSQL_USER,
            'passwd': sae.const.MYSQL_PASS,
            'db': sae.const.MYSQL_DB,
            'charset': 'utf8'}

db = LightMysql(dbconfig)


def add_openid(user_openid):
    pass
    # # 使用cursor()方法获取操作游标
    # cursor = db.cursor()
    #
    # # SQL 插入语句
    # sql = "INSERT INTO test(user_openid) VALUES ('%s')" % (user_openid)
    # try:
    #     # 执行sql语句
    #     cursor.execute(sql)
    #     # 提交到数据库执行
    #     db.commit()
    # except:
    #     # 发生错误时回滚
    #     db.rollback()
    #
    # # 关闭数据库连接
    # db.close()
    # return


def insert_test(content):
    sql_insert = "INSERT INTO test(user_openid) VALUES ('%s')" % (content)
    result_insert = db.dml(sql_insert)
    return result_insert


def add_rollnum(rollnum):
    pass


def add_phonenum(phonenum):
    pass


def add_mail(mail):
    pass


def add_picked_card_num(num):
    pass


def add_picked_card_location(content):
    pass


def add_lost_card_num(num):
    pass
