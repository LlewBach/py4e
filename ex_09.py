fname = input('Enter File: ')
if len(fname) < 1 : fname = 'clown.txt'
hand = open(fname)

di = dict()
for line in hand :
    line = line.rstrip()
    # print(line) 
    wds = line.split()
    # print(wds)
    # for w in wds :
    #     print('**',w,di.get(w,-99))
    #     if w in di :
    #         di[w] = di[w] + 1
    #     else: 
    #         di[w] = 1
    #     print(w, di[w])
    for w in wds :
        # if the key is not there, count = 0
        # idiom: retrieve/create/update counter
        di[w] = di.get(w,0) + 1
        # print(w,'new',di[w])
# print(di)

# now we want to find most common word
largest = -1
theword = None
for k,v in di.items() :
    if v > largest :
        largest = v
        theword = k # capture/remember the key  that was largest

print(theword, largest)