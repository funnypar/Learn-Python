n_1=1
n_2=1
count=1
while len(str(n_1))!=1001:
        print(n_1,len(str(n_1)),count )
        nth=n_1+n_2
        n_1=n_2
        n_2=nth
        count+=1
