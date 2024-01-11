import pywhatkit
import pyautogui
import time

pywhatkit.sendwhatmsg("Isi Nomor Telepon yang dituju", "Pesan Kamu", 23,23) 
time.sleep(1)
pyautogui.click()
time.sleep(1)
pyautogui.press('enter')

#Step 1 : Melakukan instalasi di terminal command = pip install pywhatkit 
#Step 2 : Melakukan instalasi di terminal command = pip install flask
#Step 3 : Melakukan instalasi di terminal command = pip install pyautogui
#Step 4 : Isi Nomor Telepon yang dituju dan Isi Pesan kamu serta isi jam kamu sebagai contoh 23, 23 -> Jam 23 Menit 23
#Step 5 : Run File kalau tidak ada icon Run Code (Ctrl+Alt+N) bisa install extensions Code Runner
#@IgnatiusFarel_ 11 Januari 2024 