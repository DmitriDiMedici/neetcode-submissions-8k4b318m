class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        rows = len(board)
        columns = len(board[0])
        squares = {}

        for row in board:
            seen = set()
            for element in row:
                if element in seen and element != ".":
                    return False
                else:
                    seen.add(element)

        for c in range(columns):
            seen = set()
            for r in range(rows):
                element = board[r][c]
                if element in seen and element != ".":
                    return False
                else:
                    seen.add(element)

        for r in range(rows):
            for c in range(columns):
                element = board[r][c]

                if element != ".":
                    key = (r // 3, c // 3)

                    if key not in squares:
                        squares[key] = set()

                    if element in squares[key]:
                        return False
                    else:
                        squares[key].add(element)

        return True

        