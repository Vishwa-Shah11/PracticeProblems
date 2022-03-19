def list_to_dict(L):
    """
    List to dict

    Argument:
        L: list of lists
    Return:
        D: dict
            key: int
            value: list
    """
    D = {}
    for i in range(len(L)):
        #if (i not in D.keys()):
        D[i] = L[i]
        
        
    return D
    
def dict_to_list(D):
    """
    Dict to list
	
    Argument:
        D: dict
            key: int
            value: list
    Return:
        L: list of lists
    """
    L = []
    for i in D:
        L.append(D[i])
        
    return L


print(list_to_dict([[1, 2, 3], [4, 5, 6]]))
print(dict_to_list({0: [1, 2, 3], 1: [4, 5, 6]}))