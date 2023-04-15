import string 
def print_rangoli(size):
    # to get first size letters of the alphabet
    letters = string.ascii_lowercase[:size]    
    
    # creating an empty list to contain the first 'size' lines
    lines_list=[]
    
    for i in range(size):
        
        # selecting the letters in each line
        lineletters= letters[-i-1:]
        letters_list= list(lineletters)
        
        # hyphenating the selected letters
        hyphenated='-'.join(letters_list)
        
        
        # reversing and appending each line to get a palindrome/symmetric pattern 
        result=hyphenated[::-1]+hyphenated[1:]
        
        # centering the letters and filling the rest with hyphens 
        lines=result.center((4*size-3),"-")
        print(lines)
        
        # appending each line to the list created earlier
        lines_list.append(lines)
    
    # printing remaining lines
    for i in range(size-2,-1,-1):
        print(lines_list[i])
    
