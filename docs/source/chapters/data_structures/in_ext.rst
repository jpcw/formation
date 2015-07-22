
Objects comprehensions
~~~~~~~~~~~~~~~~~~~~~~~~~

.. index:: list comprehension

listes
++++++++

.. exo:: fabriquer une liste des fruits de ['bananes', 'fraises', 'pommes'] qui contiennent un 'a'

.. code:: python

    >>> fruits = ['bananes', 'fraises', 'pommes']
    >>>
    >>> def get_fruits_with_a_letter(fruits):
    ...     fruits_with_a_letter = []
    ...     for fruit in fruits:
    ...         if 'a' in fruit:
    ...             fruits_with_a_letter.append(fruit)
    ...
    ...
    ...     return fruits_with_a_letter
    ...
    >>> get_fruits_with_a_letter(fruits)
    ['bananes', 'fraises']

En fait il y a une méthode bien plus rapide à l'écriture, mais aussi à l'exécution la voici, ce sont les list comprehensions parfois aussi appelées list in extensions


.. code:: python
            
     >>> fastest_way = [fruit for fruit in fruits if 'a' in fruit]
     >>> fastest_way    
     ['bananes', 'fraises']


Certaines personnes ont un peu de mal au début à décoder les objets in extensions.

Il suffit de décomposer de la façon suivante :

Je veux obtenir une liste, donc je commence par écrire les crochets [ ]

puis on réfléchit à ce que l'on veut y mettre dedans ::
 
 objet ajouté         | pour tout objet dans itérable | condition éventuelle
 Je veux chaque fruit | pour tout fruit dans fruits   | si un 'a' est présent dans fruit
 
                fruit | for       fruit in   fruits   | if    'a'             in   fruit


C'est aussi simple et lisible que ça. Si vous n'êtes pas encore convaincu, essayez d'en écrire deux ou trois, et vous verrez que vous allez très vite acquérir la chose.

Les listes comprehensions sont chaînables, mais il faut reconnaitre qu'au dessus de 2 on perd en lisibilité.

.. index:: generator expresion

generators 
++++++++++++

Avec la même syntaxe on peut aussi fournir un generator (qui pourra donc être consommé itération par itération), il suffit de subtituer les crochets par des parenthèses :

.. code:: python

    >>> fastest_way = (fruit for fruit in fruits if 'a' in fruit)
    >>> fastest_way
    <generator object <genexpr> at 0x...>

Disponibles uniquement dans python 2.7 et au dela il existe maintenant les sets comprehensions, et les dict comprehensions


.. index:: dict comprehension

dict comprehensions
+++++++++++++++++++ 

.. code:: python

    >>> from string import ascii_lowercase
    >>> {idx + 1: ascii_lowercase[idx] for idx in range(len(ascii_lowercase))}
    {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f', 7: 'g', 8: 'h', 9: 'i', 10: 'j', 11: 'k', 12: 'l', 13: 'm', 14: 'n', 15: 'o', 16: 'p', 17: 'q', 18: 'r', 19: 's', 20: 't', 21: 'u', 22: 'v', 23: 'w', 24: 'x', 25: 'y', 26: 'z'}

Ici on reprend le même raisonnement que pour les listes comprehensions :

On construit un dictionnaire donc on commence par les {}, puis on définit ce qu'on met comme couple **clef: valeur** pour tout parcours d'un itérable.

On peut aussi conditionner la sélection des éléments avec un if

.. code:: python

    >>> {idx + 1: ascii_lowercase[idx] for idx in range(len(ascii_lowercase)) if idx % 2 == 0}
    {1: 'a', 3: 'c', 5: 'e', 7: 'g', 9: 'i', 11: 'k', 13: 'm', 15: 'o', 17: 'q', 19: 's', 21: 'u', 23: 'w', 25: 'y'}

.. index:: set comprehension

set comprehensions
+++++++++++++++++++ 

C'est la même chose pour les sets :

.. code:: python

    >>> {elt for elt in range(20) if elt % 2 == 0 and elt not in [8, 14]}
    set([0, 2, 4, 6, 10, 12, 16, 18])
