while True:
    n = input()
    if n == '.':
        break
    new_string = ''.join(char for char in n if char.isalnum()==0)
    result=new_string.replace(" ","")
    result2=result[:-1]
    for _ in range(len(result2)//2):
        if '()' in result2:
            result2=result2.replace('()','')
        elif '[]' in result2:
            result2=result2.replace('[]','')
    if len(result2)==0:
        print('yes')
    else:
        print('no')