# #20
# name = input("Enter first name")
# nleng = len(name)
# print(nleng)

# #21
# fname = input("Enter first name")
# lname = input("Enter last name")
# fullname = fname + " " + lname
# print(fullname)

# #22
# lfname = input("Enter first name in lower case")
# llname = input("Enter last name in lower case")
# if lfname.islower() == True and llname.islower() == True:
#     lfname = lfname.upper()
#     llname = llname.upper()
#     hfullname = lfname + " " + llname
#     print(hfullname)
# else:
#     print("input is not in lower case")

# #23
# nrime = input("Input first line of nursery rime")
# nrimeleng = len(nrime)
# print(nrimeleng)
# snum = int(input("Enter starting number")) - 1
# enum = int(input("Enter ending number")) - 1
# print(nrime[snum:enum])

# #24
# lany = input("input a lowercase word")
# lany = lany.upper()
# print(lany)

# #25
# fname = input("Enter first name")
# if len(fname)<5:
#     lname = input("Enter last name")
#     fullname = fname + lname
#     print(fullname.upper())
# else:
#     print(fname.lower())

#26
iword = input("Input a word")
iword = iword.lower()
vow =["a","i","u","e","o"]
fcu = 0
for x in vow:
    print(x)
    if iword[1] == x:
        nword = iword + "way"
        fcu += 0
    else:
        fcu += 1
    if fcu == 5:
        nword = list(iword)
        nword.append(nword.pop(0))
        nword = "".join(nword)
        nword = nword + "ay"
print(nword)
        

    
    








