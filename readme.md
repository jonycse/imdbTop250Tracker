From my own interest I am tracking imdb top 250 movies each day

## Some information:
"imdbtop250.txt" contains latest 250's and "all_file/" directory contains each day's update.
By using configure file "config.py" you will be able to block/unblock some feature.

## Requirements
+ Python 2.7+
+ Beautiful Soap
+ html5lib

## [Crontab][1] settings
```javascript
0 16 * * * cd "/home/jony/Developer/python/imdb_top_250_tracker" && ./auto_script.sh
```

### Edit
+ crontab -e

### Remove 
+ crontab -r

### List
+ crontab -l


[1]: https://www.computerhope.com/unix/ucrontab.htm

