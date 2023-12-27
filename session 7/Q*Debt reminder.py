def give_money(borrowed_money, from_person, to_person, amount):
    """ Voir au dessus """
    
    if (type(amount) != float and type(amount) != int)\
    or type(from_person) != str or type(to_person) != str\
    or type(borrowed_money) != dict or from_person == to_person:
        raise ValueError("mauvais arguments")
            
    if from_person in borrowed_money:
        pass
    else:
        borrowed_money[from_person] = {}

    if to_person in borrowed_money:
        pass
    else:
        borrowed_money[to_person] = {}

    borrowed_money[from_person][to_person] = borrowed_money[from_person].get(to_person, 0) - amount
    borrowed_money[to_person][from_person] = borrowed_money[to_person].get(from_person, 0) + amount
    
    return borrowed_money
        
    
def total_money_borrowed(borrowed_money):
    """ Voir au dessus """
    if not isinstance(borrowed_money, dict):
        raise ValueError
        
    total = 0
    for i in borrowed_money:
        for j in borrowed_money[i]:
            x = borrowed_money[i][j]
            if x > 0:
                total +=x
    return total
        
borrowed_money = {}
give_money(borrowed_money,"Mark","Bill",2000000)
give_money(borrowed_money,"Mark","Steve",2000000)
give_money(borrowed_money,"Serguei","Bill",5000000)
give_money(borrowed_money,"Bill","Larry",6000000)
give_money(borrowed_money,"Larry","Linus",5.5)
give_money(borrowed_money,"Steve","Mark",2000000)