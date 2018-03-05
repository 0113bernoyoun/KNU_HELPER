import urllib2
from bs4 import BeautifulSoup
html=urllib2.urlopen("http://www.kunsan.ac.kr/board/list.kunsan?boardId=BBS_0000641&menuCd=DOM_000000104002007000&contentsSid=3778&cpath=")
soup = BeautifulSoup(html, 'html.parser')
data= soup.prettify()

#print data[76000:79001]
data2=data[76420:79001]
data3=data2
replace_result=data3.replace("</td>","")
replace_result=replace_result.replace("<br/>","")
replace_result=replace_result.replace("</tr>","")
replace_result=replace_result.replace("</tr>","")
replace_result=replace_result.replace("</tr>","")
replace_result=replace_result.replace("</div>","")
replace_result=replace_result.replace("</body>","")
replace_result=replace_result.replace("</html>","")
replace_result=replace_result.replace("</th>","")
replace_result=replace_result.replace("</tbody>","")
replace_result=replace_result.replace("</table>","")
replace_result=replace_result.replace("<td style=","")
replace_result=replace_result.replace("""text-align:left">""","")
replace_result=replace_result.replace("<tr>","")
replace_result=replace_result.replace("""<th scope="row">""","")
replace_result=replace_result.replace('"',"")
replace_result=replace_result.replace(" <th rowspan=2 scope=row>","")
replace_result=replace_result.replace("amp;","")
replace_result=replace_result.replace("             ","")
replace_result=replace_result.replace(" ","")
#print replace_result[2]
print replace_result