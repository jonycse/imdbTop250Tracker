__author__ = 'AbuZahedJony'

import urllib2
'''
    Read url content
'''
def get_url_content(site_url):
    try:
        request = urllib2.Request(site_url) 
        f=urllib2.urlopen(request)
        content=f.read()
        f.close()
    except urllib2.HTTPError, error:
        content=str(error.read())
    return content