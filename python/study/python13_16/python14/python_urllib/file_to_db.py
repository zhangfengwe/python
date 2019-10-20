# 将csv文件中的数据转移到数据库中

import csv
from python.study.other.config.logger import Logger
from python.study.other.config.readconfig import MyConfig
from os import path
import traceback
from python.study.other.util import fileutil, oracledb
from time import time


logger = Logger().get_logger()
# 根目录
base_path = MyConfig.get_value('path', 'base_path')
# 存储城市天气数据表，一个城市一张表
base_table_name = 'CITY_WEATHER_DATA'
# 插入语句
insert_sql = '''insert into city_weather_url(city_name, city_weather_month, city_weather_url, data_file_name)
values (:1, :2, :3, :4)
'''

create_table = '''
create table CITY_WEATHER_URL
(
  city_name          NVARCHAR2(50) not null,
  city_weather_month VARCHAR2(6) not null,
  city_weather_url   VARCHAR2(100),
  data_file_name     VARCHAR2(500)
);
-- Add comments to the columns 
comment on column CITY_WEATHER_URL.city_name
  is '城市名';
comment on column CITY_WEATHER_URL.city_weather_month
  is '月份';
comment on column CITY_WEATHER_URL.city_weather_url
  is 'url';
comment on column CITY_WEATHER_URL.data_file_name
  is '当月天气统计图片名称';
-- Create/Recreate primary, unique and foreign key constraints 
alter table CITY_WEATHER_URL
  add constraint PK_CITY_WEATHER_URL primary key (CITY_NAME, CITY_WEATHER_MONTH)'''

data_table_sql = '''create table CITY_WEATHER_DATA
(
  city_date VARCHAR2(10) not null,
  hight      VARCHAR2(5),
  low      VARCHAR2(5),
  weather   VARCHAR2(20),
  windirction      VARCHAR2(50),
  windlevel        VARCHAR2(50)
)
'''

alert_sql = '''alter table CITY_WEATHER_DATA add constraint PK_CITY_WEATHER_DATA primary key (CITY_DATE);
comment on column CITY_WEATHER_DATA.city_date
  is '日期';
comment on column CITY_WEATHER_DATA.low
  is '低温';
comment on column CITY_WEATHER_DATA.hight
  is '高温';
comment on column CITY_WEATHER_DATA.weather
  is '天气';
comment on column CITY_WEATHER_DATA.windirction
  is '风向';
comment on column CITY_WEATHER_DATA.windlevel
  is '风力' '''

data_insert_sql = '''
insert into CITY_WEATHER_DATA(city_date, hight, low, weather, windirction, windlevel) values (:1, :2, :3, :4, :5, :6)'''


def read_file(filepath):
    '''
    读取城市url数据文件
    :param filepath:
    :return:
    '''
    try:
        filedatas = []
        cityname = fileutil.get_file_name(filepath, endflag=False)[0]
        logger.info('cityname is {}'.format(cityname))
        with open(filepath, 'r', encoding='GBK') as file:
            reader = csv.reader(file)
            for row in reader:
                data = [cityname]
                url = row[0]
                month = url[-11:-5]
                # 气温走势图文件路径为：base_path + data/weather/matplot/ + 城市名/ + 城市名 + 月份 + 气温走势图.png
                file_name_png = base_path + 'data/weather/matplot/' + cityname +\
                                '/' + cityname + row[1] + '气温走势图.png'
                logger.debug('png file path is {}'.format(file_name_png))
                data.extend([month, url, file_name_png])
                # logger.info('data is {}'.format(data))
                filedatas.append(data)
            return filedatas
    except Exception:
        logger.error(traceback.format_exc())


def read_data_file(filepath):
    '''
    读取每月天气数据文件
    :param filepath: 
    :return: 
    '''
    try:
        filedatas = []
        with open(filepath, 'r', encoding='GBK') as file:
            reader = csv.reader(file)
            for row in reader:
                data = []
                # csv文件格式：日期(yyyy-mm-dd),高温,低温,天气,风向,风力
                for i in range(6):
                    if i == 0:
                        data.append(row[i].replace('-', ''))
                    else:
                        data.append(row[i])
                # logger.info('data is {}'.format(data))
                filedatas.append(data)
            return filedatas
    except Exception:
        logger.error(traceback.format_exc())


def file_to_db():
    conn, curs = oracledb.con()
    try:
        allstart = time()
        allfiles = fileutil.get_all_file(path.join(base_path, 'data/weather/matplot_data/city_url_month'))
        for file in allfiles:
            start = time()
            logger.info('start trans data from {} to db'.format(file))
            filedatas = read_file(file)
            # logger.info('文件总数据filedata is {}'.format(filedatas))
            oracledb.insert(conn, curs, filedatas, insert_sql)
            end = time()
            logger.info('trans data from {} to db is finish, cost is {}'.format(file, end-start))
        allend = time()
        logger.info('finish ......, allcost is {}'.format(allend - allstart))
        # 整体耗时6.5秒左右
    except Exception:
        logger.error(traceback.format_exc())
    finally:
        conn.close()


def data_to_db():
    '''
    插入每月天气数据
    :return:
    '''
    conn, curs = oracledb.con()
    citys = []
    try:
        allstart = time()
        allfiles = fileutil.get_all_file(path.join(base_path, 'data/weather/matplot_data/city_weather_data'))
        for file in allfiles:
            start = time()
            # 获取城市拼音
            cityname = fileutil.get_file_name(file, endflag=False)[0].split('_')[0]
            if cityname not in citys:
                table_name = base_table_name + '_' + cityname.upper()

                oracledb.create_table(conn, curs, [data_table_sql.replace(base_table_name, table_name)])
                # oracledb.create_table(conn, curs, [alert_sql.replace(base_table_name, table_name)])
                citys.append(cityname)
                logger.info('create table {}'.format(table_name))
            logger.info('start trans data from {} to db'.format(file))
            filedatas = read_data_file(file)
            # logger.info('文件总数据filedata is {}'.format(filedatas))
            oracledb.insert(conn, curs, filedatas, data_insert_sql.replace(base_table_name, table_name))
            end = time()
            logger.info('trans data from {} to db is finish, cost is {}'.format(file, end - start))
        allend = time()
        logger.info('finish ......, allcost is {}'.format(allend - allstart))
    except Exception:
        logger.error(traceback.format_exc())
    finally:
        conn.close()


if __name__ == '__main__':
    # file_to_db()
    data_to_db()
