def balanced(word):
    """
    Determine if a string is balanced
    Argument:
        word: string
    Return:
        result: bool
    """
    w1 = '({['
    w2 = ')}]'
    if len(word) == 0:
        return True
    else:
        if (word[0] in w1):
            i = w1.index(word[0])
            if (word[-1] != w2[i]):
                return False
        else:
            return False
            
        return balanced(word[1:-1])
            
    
        