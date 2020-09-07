__author__ = 'AbuZahedJony'

from bs4 import BeautifulSoup
import tag

'''
    Get year from string
'''
def get_year(s):
    #print "Year: ",s
    sa = s.find("(", 0)
    sb = s.find(")", sa)
    if sa and sb:
        return s[sa+1:sb]
    return None

'''
    Parse top 250 movies information from html content
'''
def top_250_movie_data(html):
    a = []
    soup = BeautifulSoup(html)
    k = 0
    for name in soup.find_all('tr',limit=251):
        #print k," [:###] ",name

        #print 20*"=="
        k += 1
        if k>1:
            # print 20*"##"
            data_index = 0
            d = {}
            for column in name.find_all('td'):
                #print "data index ",data_index," : ",column
                if data_index == 0:
                    d[tag.SERIAL_NUMBER] = str(k - 1)
                if data_index == 2:
                    d[tag.RATING] = str(column.strong.string.encode('utf-8'))
                if data_index == 1:
                    #print "SPAN", column.findAll('span')
                    d[tag.YEAR] = get_year(str(column.findAll('span')[0]))
                    d[tag.NAME]= str(column.a.text.encode('utf-8'))
                    # print "NN: ",d[tag.NAME]
                #if data_index == 3:
                #    d[tag.VOTES] = str(column.font.string.encode('utf-8'))
                data_index += 1
                #print d
            #print (k-2), ":", d
            a.append(d)
            #raise BaseException
            #break
    return a
