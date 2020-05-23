def StringRotation(s1:str, s2:str)->bool:
    if len(s1) == len(s2) and len(s1) > 0:
        newS1 = s1 + s1
        return isSubstring(newS1, s2)
    return False
