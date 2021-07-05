#-*-coding:utf8;-*-
#qpy:console
i=0
bd=""
search = input("write the word you want to search ")
direct = input("write direction "+ bd)
try:
    file = open(bd+direct,"r")
    for word in file:
        i +=1
        word =str(i) +" " + word
        if search in word:
            print(word)
        else:
            continue
except:
    print("directory must be wrong pls retry you have one more try ")
    direct= input("write direction "+ bd)
    file = open(bd+direct,"r")
    for word in file:
        i +=1
        word =str(i) +" " + word
        if search in word:
            print(word)
        else:
            continue