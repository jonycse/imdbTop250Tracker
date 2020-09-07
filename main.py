__author__ = 'AbuZahedJony'

print "Staring Main"

from config import *
from util_file import *
from util_url import *
from imdb_parser import *
from datetime import datetime
import tag
import os

html = None

# decide read content from file or url
if READ_FROM_FILE:
    html = read_from_file(HTML_CONTENT_FILE_NAME)
else:
    html = get_url_content(URL_IMDB_TOP_250)
    # Keep backup of latest html content into file
    write_to_file(HTML_CONTENT_FILE_NAME, html)


# parsing data
data = top_250_movie_data(html)

# writing movie data
f = open(OUT_FILE, 'w')
for m in data:
    line = m[tag.SERIAL_NUMBER].ljust(10," ")+m[tag.RATING].ljust(10," ")+m[tag.YEAR].ljust(10," ")+m[tag.NAME].ljust(10," ")
    #print "Line: ",line
    f.write(line+"\n\n")
f.write("\nDate: "+str(datetime.now()))
f.close()

c_date = datetime.now().date()
dir = BACKUP_DIR+str(c_date.year)+"/"+str(c_date.month)+"/"

if not os.path.exists(dir):
    print "Dir: "+dir
    os.makedirs(dir)
# Backup current file if required
if BACKUP_FILE:
    backup_file(OUT_FILE, str(dir+str(datetime.now().date()))+".txt")

print datetime.now().date()
print "End main"