def salaryPerHour(name, hour):
    if name == "jadi" :
        salary = hour * 16
        return ("Here you are my hero 😍😍😍  " , name, salary)
    if hour > 8 :
        return ("Too much work! You don't receive anythings 😂", name)    
    salary = hour * 8    
    return ("Here you are 😒😒😒  " , name , salary) 


print(salaryPerHour("jadi",16))    
print(salaryPerHour("mopano",16))    
print(salaryPerHour("mopano",7))    


        

