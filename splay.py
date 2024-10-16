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

    def zig(self, treename: str, node: Node):
        if node == None:
            print("Oopsy! This shouldn't happen")
        parent = node.parent
        if node == parent.leftchild:
            if node.rightchild:
                node.rightchild.parent = parent
            parent.leftchild = node.rightchild
            node.rightchild = parent
        else:
            if node.leftchild:
                node.leftchild.parent = parent
            parent.rightchild = node.leftchild
            node.leftchild = parent
        if parent.parent:
            if parent == parent.parent.leftchild:
                parent.parent.leftchild = node
            else:
                parent.parent.rightchild = node
        else:
            self.roots[treename] = node
        node.parent = parent.parent
        parent.parent = node
        # self.dump()

    # Search:
    # Search for the key or the last node before we fall out of the tree.
    # Splay that node.
    def search(self,treename: str,key:int):
        node = self.roots[treename]
        if node != None:
            parent = None
            while node != key and node != None:
                parent = node
                if key < node.key:
                    node = node.leftchild
                else:
                    node = node.rightchild
            if node == None:
                node = parent
            # print(node.key)
            while node.parent != None and node.parent.parent != None: # while Node is not at root or child
                if (node == node.parent.leftchild and node.parent == node.parent.parent.leftchild) or \
                    (node == node.parent.rightchild and node.parent == node.parent.parent.rightchild):
                    # print("Zig zig")
                    self.zig(treename, node.parent)
                    self.zig(treename, node)
                else:
                    # print("Zig zag")
                    self.zig(treename, node)
                    self.zig(treename, node)
            if node.parent != None:
                # print("Zig")
                self.zig(treename, node)

    # Insert Type 1:
    # The key is guaranteed to not be in the tree.
    # Call splay(x) and respond according to whether we get the IOP or IOS.
    def insert(self,treename:str,key:int):
        # self.dump()
        self.search(treename, key)
        node = self.roots[treename]
        if node == None:
            self.roots[treename] = Node(key, None, None, None)
        elif node.key < key:
            node.parent = Node(key, node, node.rightchild, None)
            if node.rightchild:
                node.rightchild.parent = node.parent
            node.rightchild = None
            self.roots[treename] = node.parent
        else:
            node.parent = Node(key, node.leftchild, node, None)
            if node.leftchild:
                node.leftchild.parent = node.parent
            node.leftchild = None
            self.roots[treename] = node.parent

    # Delete Type 1:
    # The key is guarenteed to be in the tree.
    # Call splay(key) and then respond accordingly.
    # If key (now at the root) has two subtrees call splay(key) on the right one.
    def delete(self,treename:str,key:int):
        print('This is a place-holder')