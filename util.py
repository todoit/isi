
from itertools import chain

def list_ret(g):
    """
    Exhaust a generator to a list, and additionally return its return value which normally you need to catch in an exception handler.
    returns: (list(g), return_value)
    
    As with regular functions, return_value will be None if there isn't one and/or if g isn't actually a generator.
    
    TODO: is this in stdlib somewhere?
    """
    L = []
    while True:
        try:
            L.append(next(g))
        except StopIteration as stop:
            return L, stop.value

            
def chomp(s):
	"remove trailing newline"
	"assumes universal newlines mode "
	if s.endswith("\n"): s = s[:-1]
	return s
	
	
def flatten(L):
    """
    flatten a nested list by one level
    """
    return list(chain.from_iterable(L))

