a=98
while(a<123):
    a-=1
    for i in range(4):
        if a<123:
            print(chr(a),end='')
            a+=1
    print()
