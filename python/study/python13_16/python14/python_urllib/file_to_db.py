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


def read_file(filepath):
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


if __name__ == '__main__':
    file_to_db()
