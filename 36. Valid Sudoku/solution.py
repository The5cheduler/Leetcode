import collections
class Solution:
    def isValidSudoku(self, board: List[List[str]]) ->  bool:
        # create hash set to stores the value of rows, columns and squares
        rows = collections.defaultdict(set)
        columns = collections.defaultdict(set)
        squares = collections.defaultdict(set) # key for the square will be (row // 3, column // 3)

        # traverse through the board
        for row in range(9):
            for column in range(9):
                # check if the value is empty than continue
                if board[row][column] == ".":
                    continue

                # check if the value already exists in any the hast sets of rows, columns or squares
                if board[row][column] in rows[row] or board[row][column] in columns[column] or board[row][column] in squares[(row // 3, column // 3)]:
                    return False

                # update the hash sets for rows, columns and squares
                rows[row].add(board[row][column])
                columns[column].add(board[row][column])
                squares[(row // 3, column // 3)].add(board[row][column])
        return True

