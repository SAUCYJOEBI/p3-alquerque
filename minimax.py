from board import Board, legal_moves
from move import Move

@dataclass
class _Node:
    """Nodes of the tree, carying all sorts of information of relations with it 
    """
    children: list  #:list[_Node]
    permutation: Board
    player1: bool #kan laves med board, hvad er nemmest?

@dataclass
class Tree:
    """Holds link to the first _Node of the tree
       Automatically deletes tree once link is cut (in python) 
    """
    trunk: _Node

def next_move(b: Board, depth: int) -> Move:
    """Finds the best move for 
       the next player/the algorithm 
    """
    ###

def make_tree() -> Tree:
    """returns empty tree"""
    return Tree(None)

def add(t: Tree, #input#) -> None:
    """adds a new row of arrays of leaves(move permutations) to pre-existing leaves(simulated board states)
    """
    ###

def _add(n: _Node #,input#) -> None:
    if n.children == []:
        
    else:
        for Node in n.children:
            _add(Node)


def reroot(t:Tree,m:Board) -> None:
    """changees the root of the given tree to one of 
       it's children
    """
    for N1 in t.trunk:
        for N2 in N1:
            if N2 == M:
                t.trunk = N2

def _size(n:_Node) -> int:
    """returns the total amount of children and subchildren of the given Node
    """
    sum = 1:
    for Node in n.children:
        sum = sum + _size(Node)
    return sum
