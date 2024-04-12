continue_info = True
dataLs = []
import os

while continue_info == True :
  print('_'*20, 'NILAI MEAN', '_'*20)
  angka = int(input('Masukkan angka : '))
  info_lanjut = input('Lanjut (Y/N) : ')
  if info_lanjut == 'y' : 
    dataLs.append(angka)
    print(dataLs)
    continue_info = True
    os.system('cls')
    continue
  elif info_lanjut == 'n' :
    dataLs.append(angka)
    print(dataLs)
    continue_info = False
    os.system('cls')
    break
  if info_lanjut == 'Y' : 
    dataLs.append(angka)
    print(dataLs)
    continue_info = True
    os.system('cls')
    continue
  elif info_lanjut == 'N' :
    dataLs.append(angka)
    print(dataLs)
    continue_info = False
    os.system('cls')
    break
  else : 
    print('Tidak Valid')
    break

def Mean () :
  Rata_rata = 0
  Rata_rata = sum(dataLs) / len(dataLs)
  return Rata_rata

def Median () :
  if len(dataLs) % 2 == 0:
    x = dataLs[len(dataLs) // 2]
    y = dataLs[len(dataLs) // 2 - 1]
    median = (x + y) / 2
  else : 
    median = dataLs[len(dataLs) // 2]
  return median

def Modus () :
  frekuensi = [0] * (max(dataLs) + 1)

  for i in dataLs :
    frekuensi[i] += 1

  frekuensi_max = max(frekuensi)
  modus = []
  for i in dataLs:
    if frekuensi[i] == frekuensi_max:
      modus.append(i)
  modus.pop()
  return modus 

print('_'*20, 'NILAI MEAN', '_'*20)
print(f'Hasil mean dari data : {dataLs} = {Mean()}')
print('_'*20, 'NILAI MEDIAN', '_'*20)
print(f'Hasil median dari data : {dataLs} = {Median()}')
print('_'*20, 'NILAI MODUS', '_'*20)
print(f'Hasil modus dari data : {dataLs} = {Modus()}')