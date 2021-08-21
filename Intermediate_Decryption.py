# Decryption Program
# Do everything in reverse!

# Just some empty variables to store things later!
list_1 = []
list_2 = []
list_3 = []
list_4 = []
list_5 = []
swap_list = []
length_raw_text = ""
noise_text = ""
new_text = ""
new_text_1 = ""
new_digi = ""
Finale = ""
num_swap_digit = 0
count = 0
raw_text = str(input("Key in something you want to decrpyt please!"))

# This turns the raw text into a list of individual characters!
for i in raw_text:
    list_1.append(i)

# This just tells us how long is the original unencrypted raw text!
Num_Digit_length = int(list_1[1])
# print(f"Number of Digit for Length of Text: {Num_Digit_length}")

for ii in range(3, Num_Digit_length + 3):
    length_raw_text += str(list_1[ii])

# print(f"Length of Text: {length_raw_text}")

# This will remove the numbers that is used to describe on how long is the original unencrypted raw text.
for iii in range(0, Num_Digit_length + 3):
    del list_1[0]

# print(f"Length of List: {len(list_1)}")
# print(list_1)

list_1_len = len(list_1)

# This is there to read from the right most character to the leftmost, and this will read only letters excluding numbers or '@'. Then we will add each of these chracter to a new empty string.
for iii in range(-1, -(list_1_len), -1):
    chrlist_1 = ord(list_1[iii])
    if (33 <= chrlist_1 <= 47) or (chrlist_1 >= 58):
        if chrlist_1 == 64:
            pass
        else:
            noise_text += str(list_1[iii])
    else:
        pass

# After reading the characters from right to left, it will need to be inverted laterally back to normal...
noise_text_2 = noise_text[::-1]

# print(f"Length of Noise: {len(noise_text_2)}")
# print(noise_text_2)

# Then we remove all the letters of the list_1 until we are only left with numbers.
for iiii in range(0, len(noise_text_2)):
    list_1.pop()

# print(f"Length of List: {list_1_len}")
# print(list_1)

# Then convert that list_1 into a string of numbers without any commas or so.
for iv in list_1:
    new_text += str(iv)

# print(new_text)

# Convert the letters we gathered before into its ASCII equivalents.
for vi in noise_text_2:
    new_digi += str(ord(vi))

# print(new_digi)

# That number we obtained from the ASCII equivalents of those noise text will be added to the new_text.
new_digi_1 = int(new_text) + int(new_digi)

# This checks if the new_text have a number "0" at the leftmost side of the string. Because if there is, during the addition at line 80, the left most zero will be omitted...
if int(new_text[0:1]) == 0:
    new_digi_1 = "0" + str(new_digi_1)

# print(new_digi_1)

# This checks how many swap digits there are by seeing if it is a multiple of 3 under a certain condition!
length_digits = len(str(new_digi_1))

if length_digits % 3 == 0:
    num_swap_digit = 3
    # print("3 swap digit")
elif (length_digits - 2) % 3 == 0:
    num_swap_digit = 2
    # print("2 swap digit")
else:
    num_swap_digit = 1
    # print("1 swap digit")

# print(num_swap_digit)

# This converts new_digi_1 into a list.
for vtr in str(new_digi_1):
    list_2.append(vtr)

# print(list_2)

# This will store the the swap index in the form of a list!
for vvi in range(-1, -(num_swap_digit) - 1, -1):
    nig = list_2[vvi]
    swap_list.append(nig)

# print(swap_list)

# Only if the length of original raw text is more than or equal to 4 characters long then will we do the swapping...
if int(length_raw_text) >= 4:
    for vvti in swap_list:
        aa = list_2[int(vvti)]
        bb = list_2[int(vvti) + 1]
        list_2[int(vvti)] = bb
        list_2[int(vvti) + 1] = aa
else:   # If no swapping is required, then this executes.
    print("Too Short!")

# print(list_2)

# This removes the swap index from the list_2... Which is at the rightmost side of the list. So we can use .pop() method!
for vvvv in range(0, num_swap_digit):
    list_2.pop()

# print(list_2)

# This generates a list of 3 digits from list_2...
for vvti in list_2:
    if count < 3:
        new_text_1 += str(vvti)
        count += 1
    elif count == 3:
        list_3.append(new_text_1)
        new_text_1 = ""
        new_text_1 += str(vvti)
        count = 1

list_3.append(new_text_1)

# print(list_3)

# If the length of original raw text is less than 4, no further action is required... Just minus 23 and divide by 7...
if int(length_raw_text) < 4:
    for ix in list_3:
        list_4.append(int((int(ix) - 23) / 7))

    for iz in list_4:
        strtxt = chr(int(iz))
        Finale += str(strtxt)

    print(Finale)

# Else we will need to find out the last swapping required which is the index of the (length_raw_text - 2) / 2
else:
    midswap = int((int(length_raw_text) - 2) / 2)

    if midswap == 1:    # This is only applicable for the case where the original raw text is exactly 4 characters long...
        midswap += 1
    # else:
        # print("I'm a Failure!")

    ax = list_3[1]
    bx = list_3[midswap]

    list_3[1] = bx
    list_3[midswap] = ax

    cx = list_3[0]
    dx = list_3[-1]

    list_3[0] = dx
    list_3[-1] = cx

    # Convert back to ASCII index...
    for iix in list_3:
        list_4.append(int((int(iix) - 23) / 7))

    # print(list_4)

    # Convert back to ASCII characters.
    for iy in list_4:
        strtxt = chr(int(iy))
        Finale += str(strtxt)

    print(Finale)


