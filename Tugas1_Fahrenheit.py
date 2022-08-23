#Program Konversi FAHRENHEIT 

print("\nPROGRAM KONVERSI SATUAN TEMPRATUR\n")
print("\n=======================================")
print("=====PRAMUDYA PANGESTU=====")
fahrenheit = float(input("Masukan suhu dalam Fahrenheit : "))
print("Suhu dalam adalah", fahrenheit, 'Fahrenheit')

#Celcius
celcius = (5/9) * (fahrenheit-32)
print("Suhu dalam adalah", celcius, 'Celcius')

# Reamur
reamur = (4/9) * (fahrenheit-32)
print("Suhu dalam adalah", reamur, 'Reamur')

#Kelvin
kelvin = (5/9) * (fahrenheit-32)+273
print("Suhu dalam adalah", kelvin, 'Kelvin')
