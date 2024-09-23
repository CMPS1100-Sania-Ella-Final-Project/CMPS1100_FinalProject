#this is our test suite
import SaniaAndEllasCode
import Sudoku_Examples
def testing(grid):
    if (SaniaAndEllasCode.solveSudoku(grid, 0, 0)):
        SaniaAndEllasCode.printing(grid)
    else:
        print('no solution exists.')

#works
testing(Sudoku_Examples.puzzle)
print('----')
testing(Sudoku_Examples.puzzle1)
print('----')
testing(Sudoku_Examples.puzzle2)
print('----')
testing(Sudoku_Examples.puzzle3)
print('----')

print('----')

print('----')
#Prints Wrong
testing(Sudoku_Examples.puzzle6)

print('----')
testing(Sudoku_Examples.puzzle7)

#works (prints no solution)
print('----')
testing(Sudoku_Examples.puzzle8)

#puzzle 4 and 5 overwhelm it
