spam = ['apples','bananas','tofu','cats']

def fruits(buket):
    output = ''
    for i in range(len(buket)):
        if i != len(buket)-1:
              output += str(buket[i])+', '
        else:
            output +='and '+ str(buket[i])
    return output


print(fruits(spam))
    
