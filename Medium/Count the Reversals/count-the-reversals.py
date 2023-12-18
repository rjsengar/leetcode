def countRev (s):
    c=0
    c1=0
    if len(s)%2:
        return -1
    for i in s:
        if i=="{":
            c+=1
        elif c:
            c-=1
        else:
            c1+=1
            c+=1
    return c1+c//2





#{ 
 # Driver Code Starts
t = int (input ())
for tc in range (t):
    s = input ()
    print (countRev (s))

# Contributed By: Pranay Bansal

# } Driver Code Ends