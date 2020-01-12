def minion_game(s):
    vowel=['a','e','i','o','u']
    K,S=0,0
    sub=(s[i:j] for i in range(len(s)) for j in range(i+1,len(s)+1))
    
    while True:
        try:
            ns=next(sub)
            if ns[0] in vowel:
                K+=1
            else:
                S+=1
                
        except StopIteration:
            break
        
    if S>K:
        print("Stuart {}".format(S))
    elif K>S:
        print("Kevin {}".format(K))
    elif S==K:
        print("Draw")
            
if __name__=='__main__':
    s=input()
    import timeit
    start=timeit.default_timer()
    minion_game(s)
    end=timeit.default_timer()
    print("Time",end-start)
    