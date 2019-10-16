
# 6
# 3 + 2 + 1 + -4 * -5 + 1
# 2 + 3 + 1 + -4 * -5 + 1
# 1 + 2 + 3 + -5 * -4 + 1


#n=int(input())
#s=list(input().split(" "))

n = 6
s = ['2','+','3','+','1','+','-4','*','-5','+','1']

for i in range(len(s)):
    if s[i] in ['+','-','*','/']:
        new_s=s[:]
        for j in range(i,0,-2):
            if int(new_s[j+1])>int(new_s[j-1]):
                break
            new_s[j+1],new_s[j-1]=new_s[j-1],new_s[j+1]
            if eval("".join(new_s))==eval("".join(s)):
                s=new_s[:]
            else:
                break


if __name__ == "__main__":
    print(" ".join(s))
