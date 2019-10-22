import pytest
import function

def test_add():
    assert function.addiere(3,4) == 7
    a = [
          [2,3,5],
          [-1002,3,-999],
        ]
    
    for c in a:
        assert function.addiere(c[0],c[1]) == c[2]