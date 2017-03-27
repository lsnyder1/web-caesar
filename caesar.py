def encrypt(text,rot):
    ns=""
    for i in range(len(text)):
        char=text[i]
        ns=ns+rotate_character(char,rot)
    return ns

def alphabet_position(letter):
    alph=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q',
        'r','s','t','u','v','w','x','y','z']
    ALPH=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q',
        'R','S','T','U','V','W','X','Y','Z']
    pos= None

    if letter in alph:
        pos=alph.index(letter)

    elif letter in ALPH:
        pos=ALPH.index(letter)

    else:
        return 0

    return pos


def rotate_character(char,rot):
    alph=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q',
        'r','s','t','u','v','w','x','y','z']
    ALPH=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q',
        'R','S','T','U','V','W','X','Y','Z']
    newchar=""
    ap=alphabet_position(char)
    np=ap+rot
    if np>=26:
        np=np%26
    if char in alph:
        newchar=alph[np]
    elif char in ALPH:
        newchar=ALPH[np]
    else:
        newchar=char
    return newchar    
