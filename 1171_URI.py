# Isabelly Santos Cavalcante
# UFCG
 
total = int(raw_input())
dic = {}
 
for i in range(total):
    number = int(raw_input())
    if (dic.has_key(number)):
        dic[number] = dic[number] + 1
    else:
        dic[number] = 1
list = dic.keys()
list.sort()
 
for i in list:
    print i, "aparece", dic[i], "vez(es)"
