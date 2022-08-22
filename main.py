import numpy as np
import pandas as pd

def check(board,row,col,N):
    for i in range(0,col) :
        if(board[row][i]):
            return False

    for i,j in range(row,0) and range(col,0):
        if(board[i][j]):
            return False
    for i,j in range(0,N) and range(col,0):
        if(board[i][j]):
            return False


    return True

def solve(board,col,N):
    if(col>=N):
        return True
    for i in range(0,N):
        if(check(board,i,col,N)):
            board[i][col] = 1

            if(solve(board,col + 1,N)):
                return True

    return False

def printBoard(board,N):
    for i in range(0,N):
        for j in range(0,N):
            print(board[i][j])
        print()

def solveQ(N):
    board = [ [ 0, 0, 0, 0 ],[ 0, 0, 0, 0 ],[ 0, 0, 0, 0 ],[ 0, 0, 0, 0 ] ]
    if (solve(board,0,N)==False):
        print("Solution doesn't exist.")
        return False
    printBoard(board,N)

N = 4
solveQ(N)