def anagrams(word, words):
    list_anagrams =[]  #Aqui guardaremos los anagramas.
    for element in words:
        if sorted(word) == sorted(element): #sorted ordena las listas de menor a mayor , si la listas son iguales entra,si no return list_anagrams
            list_anagrams.append(element)
    return  list_anagrams