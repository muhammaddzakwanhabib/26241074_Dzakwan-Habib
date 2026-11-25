a = int(input("Digit A: "))
b = int(input("Digit B: "))

kondisi1 = a >= 5
kondisi2 = b >= 5

print("Kondisi 1:", kondisi1)
print("Kondisi 2:", kondisi2)
print("NOT:", not kondisi1)
print("AND:", kondisi1 and kondisi2)
print("OR :", kondisi1 or kondisi2)
print("XOR:", kondisi1 ^ kondisi2)

# OR bernilai True jika minimal satu kondisi True (termasuk keduanya True),
# sedangkan XOR hanya True jika tepat satu kondisi True, sehingga
# saat kedua kondisi True, OR = True tetapi XOR = False.