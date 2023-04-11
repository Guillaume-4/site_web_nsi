dico_alpha = {'a': 1,'b': 2,'c': 3,'d': 4,'e': 5,'f': 6,'g': 7,'h': 8,'i': 9,'j': 10,'k': 11,'l': 12,'m': 13,'n': 14, 'o': 15,'p': 16,'q':17,'r': 18,'s': 19,'t': 20,'u': 21,'v': 22,'w': 23,'x': 24,'y': 25,'z': 26, ' ': " "}

def coder(phrase):
    phrase_terminer = ""
    phrase_code = []
    for i in range(len(phrase)):
        for ele in dico_alpha.items():
                if phrase[i] == " " :
                    v = " "
                elif phrase[i] == ele[0] and phrase[i]!= " ":
                    v = ele[1] + x
                    if v > 26:
                        v = v - 26
        for ele in dico_alpha.items():
            if v == ele[1]:
                phrase_code.append(ele[0])
    print(phrase_code)
    for j in phrase_code:
        phrase_terminer = phrase_terminer + j

    return phrase_terminer

def decoder(phrase_terminer):
    phrase_deco = ""
    temp = []
    w = 1000
    for i in range(len(phrase_terminer)):
        for ele in dico_alpha.items():
            if phrase_terminer[i] == " ":
                w = " "
            elif phrase_terminer[i] == ele[0] and phrase_terminer[i] != " ":
                w = ele[1] - x
            elif w == 0 :
                w = w + 26
        for ele in dico_alpha.items():
            if w == ele[1]:
                temp.append(ele[0])
    for j in temp:
        phrase_deco = phrase_deco + j
    return phrase_deco



x = int(input("chiffre"))
phrase = 'j aime manzez'
phrase2 = coder(phrase)
print(coder(phrase))
print(decoder(phrase2))