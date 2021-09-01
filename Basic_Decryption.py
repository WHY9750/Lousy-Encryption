raw = input("Put in the encrpyted text!")
final_1 = []
text = ""

final = list(raw.split(","))
print(final)

for i in final:
    conversion_3 = int(i)
    conversion_4 = (conversion_3 - 23) / 7
    final_1.append(conversion_4)

for i2 in final_1:
    text += chr(int(i2))

print(text)