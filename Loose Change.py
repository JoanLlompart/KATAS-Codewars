
def loose_change(cents):
    money = {'Pennies': 1, 'Dimes': 10, 'Nickels': 5, 'Quarters': 25}

    ordenatedvalues = sorted(money.values(), reverse = True)
    change = []
    i = 0 

    while  cents > 0:           #si cents es mayor a 0 entra a nes bucle
        if cents < 1:       
            break
        elif cents >= ordenatedvalues[i]:
            cents -= ordenatedvalues[i]    #posa el contador a 1 en lloc de 0
            change.append(ordenatedvalues[i]) 
        else:
            i += 1 #suma 1 cada vegada que utilitza una moneda

    D_change = dict.fromkeys(['Nickels','Pennies','Dimes','Quarters'], 0)
    for value in money:
        for changevalue in change :
            if money[value] == changevalue :
                D_change[value] += 1
    return D_change


if __name__ == "__main__":
    assert loose_change(29) == {'Nickels': 0, 'Pennies': 4,'Dimes': 0, 'Quarters': 1}
    assert loose_change(-2) == {'Nickels': 0, 'Pennies': 0,'Dimes': 0, 'Quarters': 0}
    assert loose_change(3.9) == {'Nickels': 0, 'Pennies': 3,'Dimes': 0, 'Quarters': 0}