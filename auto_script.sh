# cd "D:\WORKING\my_git\IMDB_TOP_250_TRACKER"
cd "/home/jony/Developer/python/imdb_top_250_tracker/"
python main.py
git add --all
git commit -m "`date`"
echo ""
echo "Information: "
echo "Pushing to remote, Please wait ....."
# showing remote
git remote -v
echo ""
git push origin master
echo ""
echo "                  End                  "
# 5 seconds sleep
sleep 10s