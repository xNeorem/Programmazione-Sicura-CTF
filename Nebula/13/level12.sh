# -shared: genera un oggetto linkabile a tempo di
# esecuzione e condivisibile con altri oggetti
# -fPIC: genera codice indipendente dalla posizione
# (Position Independent Code), rilocabile ad un
# indirizzo di memoria arbitrario 
cp /home/flag13/flag13 /tmp/13
ls -l /tmp/13/
gcc -shared -fPIC -o getuid.so getuid.c
LD_PRELOAD="./getuid.so" ./flag13