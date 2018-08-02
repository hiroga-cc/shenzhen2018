ps aux | grep python | grep -v grep | awk '{ print "kill -9", $2 }' | sh
