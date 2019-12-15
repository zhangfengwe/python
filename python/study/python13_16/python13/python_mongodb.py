# MongoDB数据库

from pymongo import MongoClient
from python.study.other.util import fileutil
import csv


def client():
    # dbclient = MongoClient('mongodb://localhost:27017')
    dbclient = MongoClient(host='localhost', port=27017)
    db = dbclient.weather
    # db.authenticate('fwzhang', 'fwzhang')
    cityurlcoll = db.conghua
    # collection.insert_one({'dbname': 'mongodb', 'user': 'admin', 'password': '123456'})
    # file = fileutil.get_all_file('C:/Users/zhangfengwei/Desktop/201703.csv')
    # for file in files:
    with open('C:/Users/zhangfengwei/Desktop/201703.csv', 'r', encoding='utf8') as f:
        reader = csv.reader(f)
        datas = []
        for row in reader:
            dic = {'date': row[0].replace('-', ''), 'low': row[2], 'hight': row[1],
                   'weather': row[3], 'windirction': row[4], 'windlevel': row[5]}
            datas.append(dic)
            # datas.append(dic)
    cityurlcoll.insert_many(datas)


def select():
    dbclient = MongoClient(host='localhost', port=27017)
    db = dbclient.mongodb_study
    cityurlcoll = db.cityurl
    result = cityurlcoll.find({'city_name': {'$regex': '^安'}}, {'_id': 0})
    # 获取结果条数
    print(result.count())
    for row in result:
        print(row)


def update():
    dbclient = MongoClient(host='localhost', port=27017)
    db = dbclient.mongodb_study
    user = db.user
    # 更新时对于array类型的字段，每次只能更新array中的一条
    # 将address数组中的所有数据更新为city:乌鲁木齐
    user.update_one({'name': '张三', 'address.state': 0}, {'$set': {'address': {'city': '乌鲁木齐'}}})
    # 将address中的state为0的一条数据的city的值更新为乌鲁木齐
    user.update_one({'name': '张三', 'address.state': 0}, {'$set': {'address.$.city': '乌鲁木齐'}})
    # 向address中追加一条数据
    user.update_one({'name': '张三'}, {'$push': {'address': {'city': '单县', 'state': 1}}})
    # 删除address中符合条件的数据
    user.update_one({'name': '张三'}, {'$pull': {'address': {'city': '上海'}}})


def insert_city_data():
    dbclient = MongoClient(host='localhost', port=27017)
    db = dbclient.weather
    city_name_coll = db.cityname
    files = fileutil.get_all_file('D:/python/data/weather/matplot_data/备份/city_month_data')
    for file in files:
        city_name = fileutil.get_file_dir(file)
        city_name_ch = fileutil.get_file_name(file).split('_')[0]

        if city_name_coll.count_documents({'city_name_ch': city_name_ch}) == 0:
            city_name_coll.insert_one({'city_name': city_name, 'city_name_ch': city_name_ch})
        city_data_coll = db[city_name_ch]
        with open(file, 'r') as f:
            reader = csv.reader(f)
            datas = []
            for row in reader:
                low = row[1]
                hight = row[2]
                if row[2] and row[1]:
                    hight = int(row[2])
                    low = int(row[1])
                    if low >= hight:
                        low, hight = hight, low
                dic = {'date': row[0].replace('-', ''), 'low': low, 'hight': hight,
                       'weather': row[3], 'windirction': row[4], 'windlevel': row[5]}
                datas.append(dic)
            if datas:
                city_data_coll.insert_many(datas)
    # city_data_coll = db


if __name__ == '__main__':
    # client()
    # select()
    # update()
    insert_city_data()
    # test()