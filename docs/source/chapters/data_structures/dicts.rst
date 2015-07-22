
.. index:: dict

Usage des Dictionnaires
~~~~~~~~~~~~~~~~~~~~~~~~~


Les dictionnaires sont souvent considérés comme des "tableaux" associatifs. Ils sont implémentés via des "hash-table".

Les clefs peuvent être un objet immuable et hashable(qui a un __hash__) soit une string, int (ces deux premiers sont les plus utilisés), un tuple, un décimal (float). Les valeurs peuvent contenir n'importe quel autre objet.

.. warning:: Un dictionnaire est un objet muable, c'est à dire modifiable 'IN PLACE'     

.. code:: python

    >>> formateur = {'nom': 'Skywaleker', 'âge': 42, 'addresse': 'Tatooine', 'profession': 'Jedi', 'prénom': 'Luc', 'hobbies': ['Open|FreeBSD', 'PauLLA', 'Python', 'Chess']}


.. code:: python

    >>> from pprint import pprint
    >>> pprint(formateur)
    {'addresse': 'Tatooine',
     'hobbies': ['Open|FreeBSD', 'PauLLA', 'Python', 'Chess'],
     'nom': 'Skywaleker',
     'profession': 'Jedi',
     'pr\xc3\xa9nom': 'Luc',
     '\xc3\xa2ge': 42}
    

Comme on le voit, les clefs ne sont pas ordonnées, et l'ordre d'insertion n'est pas respecté. Tout dépend de l'évaluation des fonctions de hashage interne, on ne peut prédire l'ordre d'un dictionnaire. Depuis Python 2.7 sont disponibles des  :py:class:`collections.OrderedDict` dans le module collection de la stdlib.

.. code:: python

    >>> len(formateur)
    6



.. code:: python

    >>> formateur.keys()
    ['nom', 'profession', '\xc3\xa2ge', 'hobbies', 'pr\xc3\xa9nom', 'addresse']



.. code:: python

    >>> pprint(formateur.values())
    ['Skywaleker',
     'Jedi',
     42,
     ['Open|FreeBSD', 'PauLLA', 'Python', 'Chess'],
     'Luc',
     'Tatooine']

.. code:: python

    >>> formateur['hobbies']
    ['Open|FreeBSD', 'PauLLA', 'Python', 'Chess']



.. code:: python

    >>> 'nom' in formateur
    True



.. code:: python

    >>> formateur['nom'] = 'Skywalker'

.. code:: python

    >>> pprint(formateur.items())
    [('nom', 'Skywalker'),
     ('profession', 'Jedi'),
     ('\xc3\xa2ge', 42),
     ('hobbies', ['Open|FreeBSD', 'PauLLA', 'Python', 'Chess']),
     ('pr\xc3\xa9nom', 'Luc'),
     ('addresse', 'Tatooine')]



.. code:: python

    >>> #help(formateur)
    Help on dict object:
    <BLANKLINE>
    class dict(object)
     |  dict() -> new empty dictionary
     |  dict(mapping) -> new dictionary initialized from a mapping object's
     |      (key, value) pairs
     |  dict(iterable) -> new dictionary initialized as if via:
     |      d = {}
     |      for k, v in iterable:
     |          d[k] = v
     |  dict(**kwargs) -> new dictionary initialized with the name=value pairs
     |      in the keyword argument list.  For example:  dict(one=1, two=2)
     |
     |  Methods defined here:
     |
     ...
     |  clear(...)
     |      D.clear() -> None.  Remove all items from D.
     |
     |  copy(...)
     |      D.copy() -> a shallow copy of D
     |
     |  fromkeys(...)
     |      dict.fromkeys(S[,v]) -> New dict with keys from S and values equal to v.
     |      v defaults to None.
     |
     |  get(...)
     |      D.get(k[,d]) -> D[k] if k in D, else d.  d defaults to None.
     |
     |  has_key(...)
     |      D.has_key(k) -> True if D has a key k, else False
     |
     |  items(...)
     |      D.items() -> list of D's (key, value) pairs, as 2-tuples
     |
     |  iteritems(...)
     |      D.iteritems() -> an iterator over the (key, value) items of D
     |
     |  iterkeys(...)
     |      D.iterkeys() -> an iterator over the keys of D
     |
     |  itervalues(...)
     |      D.itervalues() -> an iterator over the values of D
     |
     |  keys(...)
     |      D.keys() -> list of D's keys
     |
     |  pop(...)
     |      D.pop(k[,d]) -> v, remove specified key and return the corresponding value.
     |      If key is not found, d is returned if given, otherwise KeyError is raised
     |
     |  popitem(...)
     |      D.popitem() -> (k, v), remove and return some (key, value) pair as a
     |      2-tuple; but raise KeyError if D is empty.
     |
     |  setdefault(...)
     |      D.setdefault(k[,d]) -> D.get(k,d), also set D[k]=d if k not in D
     |
     |  update(...)
     |      D.update([E, ]**F) -> None.  Update D from dict/iterable E and F.
     |      If E present and has a .keys() method, does:     for k in E: D[k] = E[k]
     |      If E present and lacks .keys() method, does:     for (k, v) in E: D[k] = v
     |      In either case, this is followed by: for k in F: D[k] = F[k]
     |
     |  values(...)
     |      D.values() -> list of D's values
     |
     |  viewitems(...)
     |      D.viewitems() -> a set-like object providing a view on D's items
     |
     |  viewkeys(...)
     |      D.viewkeys() -> a set-like object providing a view on D's keys
     |
     |  viewvalues(...)
     |      D.viewvalues() -> an object providing a view on D's values
     |
     |  ----------------------------------------------------------------------
     ...
    <BLANKLINE>


.. code:: python

    >>> formateur.get('robot') is None
    True



.. exo:: ajouter des 'talents' à formateur : ('acteur', 'surfeur', 'codeur', 'administrateur') = True
.. exo:: modifier ses 'hobbies' : ajouter la pêche
.. exo:: modifier la clef 'addresse' en 'adresse'
.. exo:: fusionner formateur avec le dico {'robots': ['r2d2', 'sispeo']}
.. exo:: expliquer la différence entre items et iteritems
.. exo:: expliquer la différence entre dico['key'] et dico.get('key')
.. exo:: expliquer la méthode setdefault

.. code:: python

    >>> formateur[('acteur', 'surfeur', 'codeur', 'administrateur')] = True

.. code:: python

    >>> formateur['hobbies'].append('pêche')

.. code:: python
    
    >>> formateur['adresse'] = formateur['addresse']

.. code:: python
    
    >>> formateur.pop('addresse')
    'Tatooine'



.. code:: python

    >>> formateur.update({'robots':  ['r2d2', 'sispeo']})

.. code:: python

    >>> pprint(formateur)
    {'adresse': 'Tatooine',
     'hobbies': ['Open|FreeBSD', 'PauLLA', 'Python', 'Chess', 'p\xc3\xaache'],
     'nom': 'Skywalker',
     'profession': 'Jedi',
     'pr\xc3\xa9nom': 'Luc',
     'robots': ['r2d2', 'sispeo'],
     '\xc3\xa2ge': 42,
     ('acteur', 'surfeur', 'codeur', 'administrateur'): True}
     

.. code:: python

    >>> #help(formateur.iteritems)
    Help on built-in function iteritems:
    <BLANKLINE>
    iteritems(...)
        D.iteritems() -> an iterator over the (key, value) items of D
    <BLANKLINE>
    


.. code:: python

    >>> formateur['truc']
    Traceback (most recent call last):
    ...
        formateur['truc']
    KeyError: 'truc'

.. code:: python

    >>> formateur.get('truc', 'bidule')
    'bidule'



.. code:: python

    >>> formateur.setdefault('prénom', 'Anakin')
    'Luc'



.. code:: python

    >>> formateur.setdefault('key', 'value if key not in dict')
    'value if key not in dict'



.. code:: python

    >>> pprint(formateur)
    {'adresse': 'Tatooine',
     'hobbies': ['Open|FreeBSD', 'PauLLA', 'Python', 'Chess', 'p\xc3\xaache'],
     'key': 'value if key not in dict',
     'nom': 'Skywalker',
     'profession': 'Jedi',
     'pr\xc3\xa9nom': 'Luc',
     'robots': ['r2d2', 'sispeo'],
     '\xc3\xa2ge': 42,
     ('acteur', 'surfeur', 'codeur', 'administrateur'): True}

.. exo:: expliquer la  différence entre dict.keys et dict.viewkeys

.. code:: python
    
    >>> d_keys = formateur.keys()
    >>> pprint(d_keys)
    ['nom', 'adresse', 'profession', 'robots', '\xc3\xa2ge', 'key', 'hobbies', 'pr\xc3\xa9nom', ('acteur', 'surfeur', 'codeur', 'administrateur')]

    >>> v_keys = formateur.viewkeys()
    >>> pprint(v_keys)
    dict_keys(['nom', 'adresse', 'profession', 'robots', '\xc3\xa2ge', 'key', 'hobbies', 'pr\xc3\xa9nom', ('acteur', 'surfeur', 'codeur', 'administrateur')])

    >>> formateur['another_key'] = 'another value'

    >>> pprint(d_keys)
    ['nom', 'adresse', 'profession', 'robots', '\xc3\xa2ge', 'key', 'hobbies', 'pr\xc3\xa9nom', ('acteur', 'surfeur', 'codeur', 'administrateur')]

    >>> pprint(v_keys)
    dict_keys(['nom', 'adresse', 'another_key', 'profession', 'robots', '\xc3\xa2ge', 'key', 'hobbies', 'pr\xc3\xa9nom', ('acteur', 'surfeur', 'codeur', 'administrateur')])

    >>> 'another_key' in d_keys
    False

Disponibles à partir de python2.7 les méthodes avec view (viewkeys, viewitems, viewvalues) conservent les références vers le dictionnaire, ce qui n'est pas le cas de leur pendantes sans le prefixe view : keys, values, items qui elles retournent une séquence conforme à l'instant où elles sont évoquées.
