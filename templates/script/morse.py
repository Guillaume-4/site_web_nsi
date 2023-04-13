morse = {'A': '.-','B': '-...','C': '-.-.','D': '-..','E': '.','F': '..-.','G': '--.','H': '....','I': '..','J': '.---','K': '-.-','L': '.-..','M': '--','N': '-.','O': '---','P': '.--.','Q': '--.-','R': '.-.','S': '...','T': '-','U': '..-','V': '...-','W': '.--','X': '-..-','Y': '-.--','Z': '--..','1': '.----','2': '..---','3': '...--','4': '....-','5': '.....','6': '-....','7': '--...','8': '---..','9': '----.','0': '-----','.': '.-.-.-',',': '--..--','?': '..--..','\'': '·−−−−·','!': '−·−·−−','/': '−··−·','(': '−·−−·',')': '−·−−·−','&': '·−···',':': '−−−···',';': '−·−·−·','=': '−···−','+': '·−·−·','-': '−····−','_': '··−−·−','"': '·−··−·','$': '···−··−','@': '·−−·−·',' ':'.---.'}

def morse_encode(phrase):
    phrase_morse = ""
    for i in phrase:
        i = i.upper()
        for key, value in morse.items():
            if key == i:
                phrase_morse = phrase_morse + value + "/"
    return phrase_morse


def morse_decode(phrase_morse):
    phrase = ""
    ph_morse_split = phrase_morse.split("/")
    for i in ph_morse_split:
        for key, value in morse.items():
            if value == i:
                phrase = phrase + key.lower()
    return phrase

