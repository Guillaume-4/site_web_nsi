dico = {'a': 1,'b': 2,'c': 3,'d': 4,'e': 5,'f': 6,'g': 7,'h': 8,'i': 9,'j': 10,'k': 11,'l': 12,'m': 13,'n': 14, 'o': 15,'p': 16,'q':17,'r': 18,'s': 19,'t': 20,'u': 21,'v': 22,'w': 23,'x': 24,'y': 25,'z': 26, ' ': 27}
dico_carac = {1 :'_|', 2 : '|_|', 3 : '|_', 4 : ']', 5 : '[]', 6 : '[', 7 : '-|', 8 : '|-|', 9 : '|-', 10 : '.|', 11 : '|.|', 12 : '|.', 13 : '.]', 14 : '[.]', 15 : '[.', 16 : '-.|', 17 : '|.-|', 18 : '|.-', 19 : '>', 20 : '>-', 21 : '<', 22 : '-<', 23 : '.>', 24 : '.>-', 25 : '<.', 26 : '-<.', 27: '[-.]'}

def pigpen_encode(phrase):
    carac = []
    code = ""
    for i in range(len(phrase)) :
        for ele in dico.items() :
            if phrase[i] == ele[0] :
                x = ele[1]
        for ele in dico_carac.items():
            if x == ele[0] :
                carac.append(ele[1])
    for j  in carac:
        code = code + j + "/"
    return code

def pigpen_decode(code):
    liste_temp = []
    decode = ""
    ph_code_split = code.split("/")
    for i in ph_code_split:
        for ele in dico_carac.items():
            if i == ele[1]:
                temp1 = ele[0]
        for ele in dico.items():
            if temp1 == ele[1]:
                liste_temp.append(ele[0])
    for j in liste_temp :
        decode = decode + j
    decode = decode[:-1]
    return decode