# Diego Seisdedos Stoz
# BARB27 - Equipe 11.74
# Fait avec Adrien Sillis


import mission8 as m

# CLASS DUREE TEST

def test_to_secondes_():
    
    duree1 = m.Duree(0, 59, 0)
    duree2 = m.Duree(0, 20, 34)
    
    assert duree1.to_secondes() == 3540 , "Test 1"
    assert duree2.to_secondes() == 1234 , "Test 2"
    
test_to_secondes_()

def test_delta():
    
    duree1 = m.Duree(0, 59, 0)
    duree2 = m.Duree(0, 20, 34)
    
    assert duree1.delta(duree2) == 2306 , "Test 1"
    assert duree2.delta(duree1) == -2306 , "Test 2"
    
test_delta()

def test_apres():
    
    duree1 = m.Duree(0, 59, 0)
    duree2 = m.Duree(0, 20, 34)
    
    assert duree1.apres(duree2) == True, "Test 1"
    assert duree2.apres(duree1) == False, "Test 2"
    
test_apres()

def test_ajouter():
    
    duree1 = m.Duree(0, 59, 0)
    duree2 = m.Duree(0, 1, 0)
    duree1.ajouter(duree2)
    duree2.ajouter(duree2)
    
    assert duree1.heure == 1, "Test 1"
    assert duree1.minute == 0, "Test 2"
    assert duree1.seconde == 0, "Test 3"
    assert duree2.heure == 0, "Test 4"
    assert duree2.minute == 2, "Test 5"
    assert duree2.seconde == 0, "Test 6"
    
test_ajouter()
    
def test___str__1():
    
    duree1 = m.Duree(0, 59, 0)
    duree2 = m.Duree(0, 20, 34)
    
    assert duree1.__str__() == "00:59:00" , "Test 1"
    assert duree2.__str__() == "00:20:34" , "Test 2"
    
test___str__1()

# CLASS CHANSON TEST

def test___str__2():
    
    duree1 = m.Duree(0, 59, 0)
    duree2 = m.Duree(0, 20, 34)
    chanson1 = m.Chanson("Title1", "Author1", duree1)
    chanson2 = m.Chanson("Title2", "Author2", duree2)
    
    assert chanson1.__str__() == "Title1 - Author1 - 00:59:00", "Test 1"
    assert chanson2.__str__() == "Title2 - Author2 - 00:20:34", "Test 2"
    
test___str__2()
    
# CLASS ALBUM TEST

def test_add():
    
    duree1 = m.Duree(0, 59, 0)
    duree2 = m.Duree(0, 20, 34)
    chanson1 = m.Chanson("Title1", "Author1", duree1)
    chanson2 = m.Chanson("Title2", "Author2", duree2)
    album1 = m.Album(1)
    
    assert album1.add(chanson1) == True, "Test 1"
    assert album1.add(chanson2) == False, "Test 2"
    
test_add()

def test___str__():
    
    duree1 = m.Duree(0, 59, 0)
    duree2 = m.Duree(0, 1, 34)
    chanson1 = m.Chanson("Title1", "Author1", duree1)
    chanson2 = m.Chanson("Title2", "Author2", duree2)
    album1 = m.Album(1)
    album1.add(chanson1)
    album1.add(chanson2)
    
    assert album1.__str__() == "Album 1 (2 chansons, 01:00:34)\n01: Title1 - Author1 - 00:59:00\n02: Title2 - Author2 - 00:01:34"
    
test___str__()
