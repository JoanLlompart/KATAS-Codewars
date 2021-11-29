#convertir un string a un nuevo string
#si un caracter solo aparece una vez "("
#si un caracter aparece mas veces ")".
#el caracter tiene que ignorar las mayusculas.

def duplicate_encode(word):

    word = word.lower()

    encoded = {}
     
    for character in word:
        if character in encoded:
            encoded[character] = ')'
        else:
            encoded[character] = '('

    orderedEncoder = ''        
    for character in word:
            orderedEncoder = orderedEncoder + encoded[character]
    
    return orderedEncoder
