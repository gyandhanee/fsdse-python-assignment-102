def is_rotation(s1, s2):
    if s1 is None or s2 is None:
        return False
    elif s1 == s2 or (s2 in s1*2 and len(s1) == len(s2)):
        return True
    else:
        return False
