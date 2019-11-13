# MongoDB数据库

from pymongo import MongoClient
import csv


def client():
    # dbclient = MongoClient('mongodb://localhost:27017')
    dbclient = MongoClient(host='localhost', port=27017)
    db = dbclient.mongodb_study
    # db.authenticate('fwzhang', 'fwzhang')
    cityurlcoll = db.cityurl
    # collection.insert_one({'dbname': 'mongodb', 'user': 'admin', 'password': '123456'})
    with open('D:/python/data/weather/matplot_data/city_url/citys_url_L.csv', 'r') as file:
        reader = csv.reader(file)
        datas = []
        for row in reader:
            dic = {'url': row[0], 'city_name': row[1]}
            datas.append(dic)
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


if __name__ == '__main__':
    client()
    # select()
    # update()
