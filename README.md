La idea de esto, es que leer un archivo excel donde estan cargadas todas las EUIs, de ese archivo tomar el campo de EUI y de index serial. Con estos dos campos se arma un script.sh
En este script se graba fila a fila la misma estrucuta de comando, agregando cada EUI del excel.
Despues se correrá el script, el cual apunta al server de chirpstack, a la carpeta de devices.
