def vigenere_encode(message, key):
    encoded_message = ""
    key_index = 0
    
    for char in message:
        if char.isalpha():  # Vérifie si le caractère est une lettre
            # Convertit la lettre en majuscule pour faciliter le chiffrement
            char = char.upper()
            
            # Calcule le décalage correspondant à la lettre de la clé
            shift = ord(key[key_index].upper()) - ord('A')
            
            # Applique le décalage à la lettre du message
            encoded_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            
            key_index = (key_index + 1) % len(key)  # Passe à la lettre suivante de la clé
        else:
            encoded_char = char  # Conserve les caractères non alphabétiques inchangés
        
        encoded_message += encoded_char
    
    return encoded_message


def vigenere_decode(encoded_message, key):
    decoded_message = ""
    key_index = 0
    
    for char in encoded_message:
        if char.isalpha():
            char = char.upper()
            shift = ord(key[key_index].upper()) - ord('A')
            decoded_char = chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
            key_index = (key_index + 1) % len(key)
        else:
            decoded_char = char
        
        decoded_message += decoded_char
    
    return decoded_message


# Exemple d'utilisation :
message = "test si ' ' ' ca marche pour le francais"
key = "l'aluminium"

encoded_message = vigenere_encode(message, key)
print("Message encodé:", encoded_message)

decoded_message = vigenere_decode(encoded_message, key)
print("Message décodé:", decoded_message)
