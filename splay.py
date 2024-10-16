from __future__ import annotations
import json
from typing import List

verbose = False

# DO NOT MODIFY!
class Node():
    def  __init__(self,
                  key       : int,
                  leftchild  = None,
                  rightchild = None,
                  parent     = None,):
        self.key        = key
        self.leftchild  = leftchild
        self.rightchild = rightchild
        self.parent     = parent

class SplayForest():
    def  __init__(self,
                  roots : None):
        self.roots = roots

    def newtree(self,treename):
        self.roots[treename] = None

    # For the tree rooted at root:
    # Return the json.dumps of the object with indent=2.
    # DO NOT MODIFY!!!
    def dump(self):
        def _to_dict(node) -> dict:
            pk = None
            if node.parent is not None:
                pk = node.parent.key
            return {
                "key": node.key,
                "left": (_to_dict(node.leftchild) if node.leftchild is not None else None),
                "right": (_to_dict(node.rightchild) if node.rightchild is not None else None),
                "parentkey": pk
            }
        if self.roots == None:
            dict_repr = {}
        else:
            dict_repr = {}
            for t in self.roots:
                if self.roots[t] is not None:
                    dict_repr[t] = _to_dict(self.roots[t])
        print(json.dumps(dict_repr,indent = 2))

    # Search:
    # Search for the key or the last node before we fall out of the tree.
    # Splay that node.
    def search(self,treename: str,key:int):
        print('This is a place-holder')

    # Insert Type 1:
    # The key is guaranteed to not be in the tree.
    # Call splay(x) and respond according to whether we get the IOP or IOS.
    def insert(self,treename:str,key:int):
        print('This is a place-holder')

    # Delete Type 1:
    # The key is guarenteed to be in the tree.
    # Call splay(key) and then respond accordingly.
    # If key (now at the root) has two subtrees call splay(key) on the right one.
    def delete(self,treename:str,key:int):
        print('This is a place-holder')