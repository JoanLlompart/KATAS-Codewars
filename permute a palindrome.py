def permute_a_palindrome (word): 

    unique = False

    for letter in word:
        letter_counter = word.count(letter)
        if letter_counter == 1 and not unique:
            unique = True
        elif letter_counter %2 !=  0:   #si es igual a letter_counter,residuo de la division de 2 , es igual a 0 entonces es True i entra para devolver False, ya que solo puede haber un valor unico.
            return False
    return True #si la condicion no se cumple entonces es un palindromo, como la condicion no se ha cumplido sal i devuelve True