from hello2 import hello

def test_default():
    assert hello("Apoorv") == "hello, Apoorv"
    

def test_arguments():
    assert hello() == "hello, world"
