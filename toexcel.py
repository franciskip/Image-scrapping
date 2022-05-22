import urllib.request
import xlwt
from ast import literal_eval
import urllib.request

#####################################################################################
#[KEYWORD] should be replaced with the name of the txt document you are going to run#
#####################################################################################

wb = xlwt.Workbook()
ws = wb.add_sheet('[KEYWORD]')
row_num = 0
columns = ['id','width','height''url','photographer','original_url']
for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num])
with open('[KEYWORD].txt', 'r') as people:
    for person in people:
        pers = literal_eval(person)
        for i in range(len(pers['photos'])):
            row_num += 1
            id = pers['photos'][i]['id']
            width = pers['photos'][i]['width']
            height = pers['photos'][i]['height']
            url = pers['photos'][i]['url']
            photographer = pers['photos'][i]['photographer']
            original_url = pers['photos'][i]['src']['original']
            ls = [id,width,height,url,photographer,original_url]
            imgURL = f"{original_url}"
            urllib.request.urlretrieve(imgURL,f"./[KEYWORD]/{id}.png")

            for col_num in range(len(ls)):
                ws.write(row_num, col_num, ls[col_num])
        wb.save('[KEYWORD].xls')

