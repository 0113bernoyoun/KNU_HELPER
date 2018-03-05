# -*- coding: utf-8 -*-
import urllib2
from bs4 import BeautifulSoup
import pymysql
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

html=urllib2.urlopen("http://www.kunsan.ac.kr/dormi/index.kunsan?menuCd=DOM_000000704006000000")#
soup = BeautifulSoup(html, 'html.parser')
data= soup.prettify()

#print data[76000:79001]
data2=data[47400:53880]
data3=data2

# replace_result=replace_result.replace("<br/>","")
# replace_result=replace_result.replace("</tr>","")
# replace_result=replace_result.replace("</tr>","")
# replace_result=replace_result.replace("</tr>","")
# replace_result=replace_result.replace("</div>","")
# replace_result=replace_result.replace("</body>","")
# replace_result=replace_result.replace("</html>","")
# replace_result=replace_result.replace("</th>","")
# replace_result=replace_result.replace("</tbody>","")
# replace_result=replace_result.replace("</table>","")
# replace_result=replace_result.replace("<td style=","")
# replace_result=replace_result.replace("""text-align:left">""","")
# replace_result=replace_result.replace("<tr>","")
# replace_result=replace_result.replace("""<th scope="row">""","")
# replace_result=replace_result.replace('"',"")
# replace_result=replace_result.replace(" <th rowspan=2 scope=row>","")
# replace_result=replace_result.replace("amp;","")
# replace_result=replace_result.replace("             ","")
# replace_result=replace_result.replace(" ","")
# replace_result=replace_result.replace("<td>","")

data3=data3.replace("<br/>","")
data3=data3.replace("</td>","")
data3=data3.replace("</tr>","")
data3=data3.replace("<tr>","")
data3=data3.replace("""<th scope="row">""","")
data3=data3.replace("점심","")
data3=data3.replace("저녁","")
data3=data3.replace("</th>","")
data3=data3.replace("</tbody>","")
data3=data3.replace("</table>","")
data3=data3.replace("</div>","")
data3=data3.replace("<h4>","")
data3=data3.replace("""<div class="bbs_list01" style="border-bottom-color: currentColor; border-bottom-width: medium; border-bottom-style: none;">""","")
data3=data3.replace("<p>","")
data3=data3.replace("</p>","")
data3=data3.replace(" 원산지 표기사항입니다.","")
data3=data3.replace("<strong>","")
data3=data3.replace("</strong>","")
data3=data3.replace("<tab","")
data3=data3.replace("</h4>","")
data3=data3.replace("식단 알림사항","")

data3=data3.split("<td>")

day_list=['월','화','수','목','금','토','일']
sr_time=['아침','점심','저녁']

conn=pymysql.connect(host='localhost',user='root',password='1234',db='school_food',charset='utf8',port=3307)
curs=conn.cursor()
sql1="""delete from domitory_restaurant"""

curs.execute(sql1)
sql=""" insert into domitory_restaurant(sr_time,daily,menu) values (%s, %s, %s)"""
curs.execute(sql,(day_list[0],sr_time[0],data3[1]))
curs.execute(sql,(day_list[1],sr_time[0],data3[2]))
curs.execute(sql,(day_list[2],sr_time[0],data3[3]))
curs.execute(sql,(day_list[3],sr_time[0],data3[4]))
curs.execute(sql,(day_list[4],sr_time[0],data3[5]))
curs.execute(sql,(day_list[5],sr_time[0],data3[6]))
curs.execute(sql,(day_list[6],sr_time[0],data3[7]))
curs.execute(sql,(day_list[0],sr_time[1],data3[8]))
curs.execute(sql,(day_list[1],sr_time[1],data3[9]))
curs.execute(sql,(day_list[2],sr_time[1],data3[10]))
curs.execute(sql,(day_list[3],sr_time[1],data3[11]))
curs.execute(sql,(day_list[4],sr_time[1],data3[12]))
curs.execute(sql,(day_list[5],sr_time[1],data3[13]))
curs.execute(sql,(day_list[6],sr_time[1],data3[14]))
curs.execute(sql,(day_list[0],sr_time[2],data3[15]))
curs.execute(sql,(day_list[1],sr_time[2],data3[16]))
curs.execute(sql,(day_list[2],sr_time[2],data3[17]))
curs.execute(sql,(day_list[3],sr_time[2],data3[18]))
curs.execute(sql,(day_list[4],sr_time[2],data3[19]))
curs.execute(sql,(day_list[5],sr_time[2],data3[20]))
curs.execute(sql,(day_list[6],sr_time[2],data3[21]))

conn.commit()
conn.close()


print data3[1]