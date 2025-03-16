import time
from ppadb.client import Client

client = Client(host="127.0.0.1",port=5037)
devices = client.devices()

device_0 = devices[0]

#abrir instagram
device_0.shell('am start -n com.instagram.android/com.instagram.android.activity.MainTabActivity   ')
time.sleep(2)
#boton buscar
device_0.shell('input touchscreen swipe 329 2310 0 0 1')
time.sleep(2)
#boton en linea de escritura
device_0.shell('input touchscreen swipe 570 210 0 0 1')
time.sleep(3)
#escribir
device_0.shell('input text "la_principal_farma"')
time.sleep(2)
#boton buscar
device_0.shell('input touchscreen swipe 981 2206 0 0 1')
time.sleep(2)
#boton cuentas
device_0.shell('input touchscreen swipe 333 360 0 0 1')
time.sleep(2)
#clickear cuenta
device_0.shell('input touchscreen swipe 371 525 0 0 1')
time.sleep(5)
#mensaje
device_0.shell('input touchscreen swipe 245 917 0 0 1')
time.sleep(2)

#cerrar aplicacion
device_0.shell('am force-stop com.instagram.android')