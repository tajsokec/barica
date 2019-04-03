
import urllib.request

from bs4 import BeautifulSoup

import codecs

def scrapProfessors(user_name):

    print('--> SCRAP PROFESSOR')

    urlpage =  (str('https://nastava.foi.hr/?username=') + str(user_name))

    page = urllib.request.urlopen(urlpage)

    soup = BeautifulSoup(page, 'html.parser')

    user_image = soup.find('img', {'alt': 'Slika nastavnika'})

    info = soup.findAll('div', {'class': 'col-md-12 col-sm-4'})
    
    lokacija = soup.findAll('div', {'class': 'col-md-6'})
    odjel = lokacija[0].findAll('p')
    odjel_text = ''
    for p in odjel:
        odjel_text += p.get_text()
    kabinet = lokacija[1].findAll('p')
    kabinet_text = ''
    for p in kabinet:
        kabinet_text += p.get_text() + '<br>'
        
    konzultacije = soup.findAll('div', {'class': 'col-md-4 col-sm-6 col-xs-6'})
    konzultacije_text = '<table><tbody><tr>'
    for kon in konzultacije:
        konzultacije_text += '<td>' + str(kon) + '</td>'
    konzultacije_text += '</tr></tbody></table>'

    html = """
<table>
<tbody>
<tr>
<td rowspan="4">
<table>
<tbody>
<tr>
<td>{str1}</td>
</tr>
<tr>
<td>{str2}</td>
</tr>
<tr>
<td>{str3}</td>
</tr>
</tbody>
</table>
</td>
<td>Odjel</td>
<td>Lokacija</td>
</tr>
<tr>
<td>{str4}</td>
<td>{str5}</td>
</tr>
<tr>
<td colspan="2">Konzultacije</td>
</tr>
<tr>
<td colspan="2">{str6}</td>
</tr>
</tbody>
</table>""".format(str1=info[0], str2=info[1], str3=info[2], str4=odjel_text,
                   str5=kabinet_text, str6=konzultacije_text)

    f = codecs.open('build/index.html','a', 'utf-8')
    f.write(html)
    f.close()
