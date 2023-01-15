#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
"""
    Un module documenté
    ===================
 
    IL s'agit d'un exemple pour tester et voir ce que l'on peut faire avec
    des docstrings
 
    :Example:
 
    >>> from docstr1 import ajoute
    >>> ajoute(1, 1)
    2
 
    On peut mettre des sous titres
    ------------------------------

    Si vous avez des précisions a apporter sur ce module
    c'est le bon endroit
 
 
    Encore un sous titre
    --------------------
 
    Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod
    tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,
    proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
 
"""
 
def ajoute(a, b):
    """
        Ajoute 2 nombres et retourne le resultat
 
        cette fonction ne fait rien de mieux que ce vieil opérateur
        '+' mais il s'agit d'un exemple de docstring d'accord
 
        :param a: Le premier argument
        :param b: Le deuxieme argument 
        :type a: int ou float
        :type b: int ou float
        :return: Le résultat de l'addition de a+b
        :rtype: int ou float
 
        :Example:
 
        >>> ajoute(1, 1)        # int
        2
        >>> ajoute(0.003, 0.12) # float
        0.123
 
        .. seealso:: PEP 257 qui vous décrit les bonnes pratiques pour les docstrings
        .. warning:: En aucun cas il ne s'agit d'un vrai module
                     C'est juste pour montrer ce que l'on peut faire 
                     avec des docstrings
        .. note:: Ajout d'une note 
        .. todo:: Si vous avez une todo concernant ce module
    """
    return a + b

if __name__ == '__main__':
    import doctest
    doctest.testmod()
