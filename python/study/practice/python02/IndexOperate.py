#索引操作列表
# 将以数指定的年月日打印出来

# 月份列表
months = ['January','February','March','April','May','June','July',
         'August','September','October','November','December']

# 日期结尾列表（1-31）
endings = ['st','nd','rd'] + 17 * ['th'] + ['st','nd','rd'] + 7 * ['th'] + ['st']

year = input('Year: ')
month = input('Month: ')
day = input('Day: ')

month_number = int(month) - 1
day_number = int(day) - 1

print('{} {}{} {}'.format(months[month_number],day,endings[day_number],year))