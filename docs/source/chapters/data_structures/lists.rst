.. index:: list

Utilisation des listes
-----------------------

Certainement l'un des objets les plus utilisé. Les listes ne sont pas des tableaux, et elles peuvent contenir des items de différents types.
Il existe un type d'objet :py:class:`array.array` qui lui ne contient que des éléments d'un même type. Ce dernier est peu utilisé, pour des tableaux puissants il faut s'appuyer sur la bibliothèque scientifique `numpy <http://www.numpy.org/>`_  utilisée par la biblitothèque à usage scientifique `scipy <http://www.scipy.org/>`_.

.. code:: python

    >>> fruits = ['bananes', 'pommes', 'fraises']
    >>> #help(fruits)
    Help on list object:
    <BLANKLINE>
    class list(object)
     |  list() -> new empty list
     |  list(iterable) -> new list initialized from iterable's items
     |
     |  Methods defined here:
     |
     ...
     |  append(...)
     |      L.append(object) -- append object to end
     |
     |  count(...)
     |      L.count(value) -> integer -- return number of occurrences of value
     |
     |  extend(...)
     |      L.extend(iterable) -- extend list by appending elements from the iterable
     |
     |  index(...)
     |      L.index(value, [start, [stop]]) -> integer -- return first index of value.
     |      Raises ValueError if the value is not present.
     |
     |  insert(...)
     |      L.insert(index, object) -- insert object before index
     |
     |  pop(...)
     |      L.pop([index]) -> item -- remove and return item at index (default last).
     |      Raises IndexError if list is empty or index is out of range.
     |
     |  remove(...)
     |      L.remove(value) -- remove first occurrence of value.
     |      Raises ValueError if the value is not present.
     |
     |  reverse(...)
     |      L.reverse() -- reverse *IN PLACE*
     |
     |  sort(...)
     |      L.sort(cmp=None, key=None, reverse=False) -- stable sort *IN PLACE*;
     |      cmp(x, y) -> -1, 0, 1
     |
     |  ----------------------------------------------------------------------
     ...
    <BLANKLINE>

.. warning:: Une liste est un objet muable, c'est à dire modifiable 'IN PLACE'     

.. exo:: Ajouter des "mangues" aux fruits

.. exo:: supprimer les mangues

.. exo:: dire si les bananes sont présentes

.. exo:: rajouter les mangues

.. exo:: trier les fruits par ordre alphabétique décroissant

.. exo:: donner le nombre de fruits

.. exo:: expliquer la différence entre append et extend

.. exo:: Ajouter à nouveau les mangues

.. exo:: inverser l'ordre de la liste 

Résultat final ['mangues', 'bananes', 'fraises', 'pommes']

.. code:: python

    >>> fruits
    ['bananes', 'pommes', 'fraises']

.. code:: python

    >>> fruits.append('mangues')
    >>> fruits
    ['bananes', 'pommes', 'fraises', 'mangues']

.. code:: python
    
    >>> fruits.pop()
    'mangues'
    >>> fruits
    ['bananes', 'pommes', 'fraises']


.. code:: python
    
    >>> #help(fruits.pop)
    Help on built-in function pop:
    <BLANKLINE>
    pop(...)
        L.pop([index]) -> item -- remove and return item at index (default last).
        Raises IndexError if list is empty or index is out of range.
    <BLANKLINE>

.. code:: python
    
    >>> 'bananes' in fruits
    True



.. code:: python
    
    >>> fruits.sort(reverse=True)
    >>> fruits
    ['pommes', 'fraises', 'bananes']



.. code:: python
    
    >>> len(fruits)
    3



.. code:: python
    
    >>> fruits.extend('mangues')
    >>> fruits
    ['pommes', 'fraises', 'bananes', 'm', 'a', 'n', 'g', 'u', 'e', 's']



.. code:: python
    
    >>> fruits = fruits [:3]
    >>> fruits
    ['pommes', 'fraises', 'bananes']



.. code:: python
    
    >>> fruits.append('mangues')
    >>> fruits.reverse()
    >>> fruits
    ['mangues', 'bananes', 'fraises', 'pommes']

