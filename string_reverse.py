def string_reverse(s1):
    s2=''
    for i in range(len(s1)-1,-1,-1):
        s2=s2+s1[i]
    print(s2)
s="1234abcd"
string_reverse(s)
