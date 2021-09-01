raw_text = str(input("Key in something you want to encrpyt please!"))
decoded = ""

final = []
final_1 = []

for i in raw_text:
    conversion_1 = i
    conversion_2 = ord(conversion_1)
    conversion_2 = (conversion_2 * 7) + 23
    final.append(conversion_2)

print(final)

for ii in final:
    conversion_3 = ii
    conversion_4 = (conversion_3 - 23) / 7
    final_1.append(conversion_4)

print(final_1)

for i in final_1:
    decoded += chr(int(i))

print(decoded)

