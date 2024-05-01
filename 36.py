class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)

        for c in range(9):
            for r in range(9):
                if board[c][r] == ".":
                    continue
                if board[c][r] in cols[c] or board[c][r] in rows[r] or board[c][r] in squares[(c//3,r//3)]:
                    return False
                cols[c].add(board[c][r])
                rows[r].add(board[c][r])
                squares[(c//3,r//3)].add(board[c][r])
        return True
# Time complexity: O(1) because of the fixed size of the board
# Space complexity: O(1) because of the fixed size of the board

'''
So basically we're gonna store the rows, columns and squares in a set.
But then there are separate rows, columns and squares.
So then we use hashmaps to organize the various rows, columns and squares.
Hashmaps because searching in hashmap also take constant time, and it's convenient. 


Now you can easily get the rows and columns but the questions is how would you get the squares. 
You can get the squares by dividing the row and column by 3 since each square is 3x3.
And then in the square hashmap you make the position calculated a tuple and then map them to their corresponding set

'''