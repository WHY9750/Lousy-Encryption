# Encryption Program

# Just some empty variables to store things later!
raw_text = str(input("Key in something you want to encrpyt please!"))
strlistRMV = ""
strlistRMV2 = ""
conversion_5 = ""
aaff = 0
count = 0
count2 = 0
count3 = 0
numdigit = len(str((len(raw_text))))
lent = ["@", numdigit, "@", len(raw_text)]
iterstring = ""
abc122 = []
abc123 = []
concat_noise = ""
final_muladd = []
final_3digi = []
final_listRMV = []
final_listRMV_3 = []
final_listRMV_4 = []
encry = []
crap = []
finally222 = []
finalMAN = ""

# This does multiplication and addition to the ASCII number.
for i in raw_text:
    conversion_1 = i
    conversion_2 = ord(conversion_1)
    conversion_2 = (conversion_2 * 7) + 23
    final_muladd.append(conversion_2)

print(final_muladd)

# This part ensures that each characters will have 3 digits no matter what.
for ii in final_muladd:
    conversion_4 = str(int(ii))
    if len(conversion_4) < 2:
        conversion_5 = "00" + conversion_4
        final_3digi.append(conversion_5)
    elif len(conversion_4) < 3:
        conversion_5 = "0" + conversion_4
        final_3digi.append(conversion_5)
    else:
        final_3digi.append(conversion_4)

print(final_3digi)

# Swap the first and the last character (remember that each character takes up 3 numbers which is in the form of encrypted ASCII), and then we will take the [(length of string) - 2] and divide by 2 in the form of integer. That number obtained will be the character that will be swapped with the second character of the list...
if len(final_3digi) >= 4:
    length_swap = len(final_3digi) - 2
    length_swap = int(length_swap / 2)
    if length_swap <= 1:
        length_swap += 1
    aa = final_3digi[0]
    bb = final_3digi[len(final_3digi) - 1]
    final_3digi[0] = bb
    final_3digi[len(final_3digi) - 1] = aa
    cc = final_3digi[1]
    dd = final_3digi[length_swap]
    final_3digi[length_swap] = cc
    final_3digi[1] = dd
    print(final_3digi)

else:
    print("Please enter longer text!")  # This will be printed when there isn't enough characters in the raw text to perform the full encryption...

# This creates a stream of number with no comma or space...
for iii in final_3digi:
    strlistRMV += str(int(iii))

for iic in strlistRMV:
    final_listRMV.append(int(iic))

print(strlistRMV)
print(final_listRMV)

# Traverse through the entire string and look for 3 distinct numbers, and we need at most 3 digits and then use that 3 digits each as an index to the list of encrypted ASCII say the 3 digits are 2, 3, 4 then we will swap index 2 with 3, index 3 with 4 and index 4 with 5 sequentially...
for u1 in final_listRMV:
    if count == 3:
        break
    elif count < 3:
        if count == 1:
            if u1 == abc122[0]:
                pass
            else:
                abc122.append(u1)
                count += 1
        if count == 2:
            if u1 == abc122[0]:
                pass
            elif u1 == abc122[1]:
                pass
            else:
                abc122.append(u1)
                count += 1
        else:
            abc122.append(u1)
            count += 1

print(abc122)

if len(raw_text) >= 4:  # We have to ensure that the length of the final_listRMV is at least 11 because the highest index is 9 which will trigger out of range at line 112 (9 + 1) when the list is insufficiently long.
    if len(abc122) >= 3:    # This checks the number of swap index.
        key1 = abc122[0]
        key2 = abc122[1]
        key3 = abc122[2]

        at = final_listRMV[key1]
        at1 = final_listRMV[key1 + 1]
        final_listRMV[key1 + 1] = at
        final_listRMV[key1] = at1

        at = final_listRMV[key2]
        at1 = final_listRMV[key2 + 1]
        final_listRMV[key2 + 1] = at
        final_listRMV[key2] = at1

        at = final_listRMV[key3]
        at1 = final_listRMV[key3 + 1]
        final_listRMV[key3 + 1] = at
        final_listRMV[key3] = at1

        print(final_listRMV)

    elif len(abc122) == 2:  # This checks the number of swap index.
        key1 = abc122[0]
        key2 = abc122[1]

        at = final_listRMV[key1]
        at1 = final_listRMV[key1 + 1]
        final_listRMV[key1 + 1] = at
        final_listRMV[key1] = at1

        at = final_listRMV[key2]
        at1 = final_listRMV[key2 + 1]
        final_listRMV[key2 + 1] = at
        final_listRMV[key2] = at1

        print(strlistRMV)

    elif len(abc122) == 1:  # This checks the number of swap index.
        key1 = abc122[0]

        at = final_listRMV[key1]
        at1 = final_listRMV[key1 + 1]
        final_listRMV[key1 + 1] = at
        final_listRMV[key1] = at1

        print(final_listRMV)

    else:   # This is actually impossible to trigger since there had to be at least 1 single swap index.
        print("Bruhh!")

else:   # If there isn't at least 4 characters in the raw text, this will be trigger and the swapping will not occur!
    print("Bruhh!")

# This is the hint to the 3 distinct number index which we do the swapping and to the original number of characters in the raw text. The first number between the 2 '@' indicates the number of digit of the number of characters in the raw string, so the following numbers after the second '@' are the total number of digit. Then the last 3 character is the index which the swapping occurs and that the index is zero at the number indicating the number of characters in the raw text!
final_listRMV_2 = lent + final_listRMV + abc122

print(final_listRMV_2)

# This is to do a negative indexing to sequentially get 2 digit numbers with a step of -1 and then take these 2 digit numbers and convert to their ASCII equivalent but however it cannot be numbers neither can it be '@'.
for gghh in range(-4, -len(final_listRMV_2) + 2, -1):
    if count3 >= 2:
        iterstring = ""
        iterstring += str(final_listRMV_2[gghh])
        count3 = 1
    elif count3 == 1:
        iterstring += str(final_listRMV_2[gghh])
        count3 += 1
        if int(iterstring) < 33:
            pass
        elif 47 < int(iterstring) < 58:
            pass
        elif int(iterstring) == 64:
            pass
        else:
            final_listRMV_3.append(chr(int(iterstring)))
            count2 += 1
    else:
        iterstring += str(final_listRMV_2[gghh])
        count3 += 1

print(final_listRMV_3)

# Taking the encrypted number starting from 4th index to the last before we add the ASCII noise...
final_listRMV_4 = final_listRMV_2
for iif in range(0, 4):
    crap.append(final_listRMV_4[0])
    del final_listRMV_4[0]
for jjh in final_listRMV_4:
    strlistRMV2 += str(jjh)

print(crap)
print(strlistRMV2)

# Combining the index of ASCII noise into a number which we will subtract from the strlistRMV2...
for utt in final_listRMV_3:
    concat_noise += str(ord(utt))

print(concat_noise)
newstrlistRMV2 = int(strlistRMV2) - int(concat_noise)
print(newstrlistRMV2)

# Combining the abomination!
finally222 += crap
FINALE_1 = str(newstrlistRMV2)

if int(strlistRMV2[0:1]) == 0:
    finally222.append(0)

for itit in FINALE_1:
    finally222.append(itit)

finally222 += final_listRMV_3

print(finally222)

for nga in finally222:
    finalMAN += str(nga)

print(f"Final Encrypted Text: {finalMAN}")
