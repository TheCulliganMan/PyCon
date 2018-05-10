# Python Epiphanies

### What this is:

Jupyter Notebook files for 
presented at PyCon 2018 by Stuart Williams

This is an updated and reorganized version of the Python Epiphanies
O'Reilly video at http://shop.oreilly.com/product/06369200

This shows you all of pythons major quirks, how to intruduce them and thereby how to avoid running into them.  There aren't a whole lot of notes for this one, it is best to run in order and figure out what is happening by sight.

This in particular blew my mind.

```python

value = 4

def print_value():  
    print(value)
    
def test_local():  
    value = 'inner'
    print(value)

def test_local_unbound():  
    print(value)
    value = 'inner'

print_value()  # works
test_local()  # works
test_local_unbound()  # throws error (essentially a null pointer)

```

And this:

```python
>>> tuple_1 = ([12, 13],)
>>> tuple_1
([12, 13],)
>>> tuple_1[0] += [14]
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<input-16-cb9150723806> in <module>()
----> 1 tuple_1[0] += [14]

TypeError: 'tuple' object does not support item assignment

>>> tuple_1
([12, 13, 14],) 
>>> # ?!?!?!! https://docs.python.org/3/faq/programming.html#faq-augmented-assignment-tuple-error
```