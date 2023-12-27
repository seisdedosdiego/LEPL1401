# Diego Seisdedos Stoz
# BARB27 - Equipe 11.74

import search

def test_readfile():
    """ Fonction test de la fonction readfile(filename) """
    assert search.readfile("test_example_1.txt") == ["abc efg", "hij klm"], "test 1"
    assert search.readfile(" ") == "An error occured", "test 2"
    
# test_readfile()

def test_get_words():
    """ Fonction test de la fonction get_words(line) """
    assert search.get_words("abc Diego. ?haK ans") == ['abc', 'diego', 'hak', 'ans'], "test 1"
    assert search.get_words('ceci . est , un test ?') == ['ceci', 'est', 'un', 'test'], "test 2"
    
# test_get_words()

def test_create_index():
    """ Fonction test de la fonction create_index(filename) """
    assert search.create_index("test_example_2.txt") == {'while': [0], 'the': [0, 1], 'congress': [0], 'of': [0, 1], 'republic': [0], 'endlessly': [0], 'debates': [0], 'this': [1], 'alarming': [1], 'chain': [1], 'events': [1], 'supreme': [1], 'chancellor': [1], 'has': [1], 'secretly': [2], 'dispatched': [2], 'two': [2], 'jedi': [2], 'knights': [2]}, "test 1"
    assert search.create_index(" ") == "An error occured", "test 2"
    
# test_create_index()

def test_get_lines():
    """ Fonction test de la fonction get_lines(words, index) """
    assert search.get_lines(["the", "while", "of"], {'while': [0], 'the': [0, 1], 'congress': [0], 'of': [0, 1], 'republic': [0], 'endlessly': [1] }) == [0], "test 1"
    assert search.get_lines(["the", "while", "endlessly"], {'while': [0], 'the': [0, 1], 'congress': [0], 'of': [0, 1], 'republic': [0], 'endlessly': [1] }) == [], "test 2"
    assert search.get_lines(["coucou"], {'while': [0], 'the': [0, 1], 'congress': [0], 'of': [0, 1], 'republic': [0], 'endlessly': [1] }) == [], "test 3"

test_get_lines()

