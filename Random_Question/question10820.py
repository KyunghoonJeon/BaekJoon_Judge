while True:
    try:
        s=input()
        lower=sum(i.islower() for i in s)
        upper=sum(i.isupper() for i in s)
        num=sum(i.isdigit() for i in s)
        blank=sum(i.isspace() for i in s)
        print(lower,upper,num,blank)
    except EOFError:
        break