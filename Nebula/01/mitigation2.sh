gcc -o flag01-env level1-env.c
chown flag01:level01 ./flag01-env
chmod u+s ./flag01-env
PATH=/tmp:$PATH
./flag01-env
