# Given a 2D board and a word, find if the word exists in the grid.

# The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

# Example:

# board =
# [
#   ['A','B','C','E'],
#   ['S','F','C','S'],
#   ['A','D','E','E']
# ]

# Given word = "ABCCED", return true.
# Given word = "SEE", return true.
# Given word = "ABCB", return false.


class Solution(object):

    def exist(self, board, word):

        # dfs function within function 
        def dfs(board, i, j, pos, word):

        # if end of the word is reached
            if len(word) == pos:
                return True
        # check for boundary condiditions and if the word is found
            if i < 0 or j < 0 or i >= len(board) or j >= len(board[i]) or board[i][j] != word[pos]:
                return False

        # so that there is no word reused in the same recursion calls
            temp = word[pos]
            board[i][j] = ''
            found = dfs(board, i-1, j, pos+1, word) or dfs(board, i+1, j, pos+1,
                                                           word) or dfs(board, i, j-1, pos+1, word) or dfs(board, i, j+1, pos+1, word)
        # setting back the replaced value 
            board[i][j] = temp
            return found

        #  main loop

        for i_, b_i in enumerate(board):
            for j_, _, in enumerate(b_i):
                if board[i_][j_] == word[0] and dfs(board, i_, j_, 0, word):
                    return True
        return False

        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
# Runtime: 320 ms, faster than 76.81% of Python online submissions for Word Search.
# Memory Usage: 15 MB, less than 84.44% of Python online submissions for Word Search.
