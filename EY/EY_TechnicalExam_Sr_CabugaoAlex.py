# 1. Load Grid
#   a. Based on the given character sequence below, create a data table of file that
#       handles the value.
            # XXOOXOXOXO
            # XOOXOXOXOX
            # OXX XOOXOX
            # OXXXOOX XO
            # XOOXOXOXXO
            # XOX XXO OX
            # XXOOXOXOXO
            # XO OXOOXOO
            # OXXXOO OXO
            # OOOOOOOXOX
        
#   b. Load the data into a grid as input to create a Two-dimensional array that
#       ensures a rectangular form and validates every character.

# Input length
INPUT_LENGTH = 100
# Row length
ROW_LENGTH = 10
# Valid character inputs
ValidInputs = ('X', 'O', ' ')
# Valid categories for Index of Dissimilarity
ValidCategories = ('X', 'O')

# Name: check_values
# Returns: Boolean
# Desc: Validates input values
def check_values(inputVal):
    if inputVal.upper() not in ValidInputs:
        print("ERROR: Invalid character input")
        return False
        
    return True


# Name: display_list
# Returns: None
# Desc: Prints list
def display_list(inputList):
    for i in inputList:
        print(i)

 
# Name: load_grid
# Returns: Array, empty array for exception
# Desc: Takes a character sequence as input and returns a two-dimensional 10x10 array
def load_grid(charSequence):
    gridOutput = []
    rowOutput = []
    
    if len(charSequence) == INPUT_LENGTH:
        for c in charSequence:
            c = c.upper()
            # Append to the row array if c is valid character        
            if check_values(c):
                if len(rowOutput) < ROW_LENGTH:
                    rowOutput.append(c)
                else:
                    # Append row to grid if already meets row length
                    gridOutput.append(rowOutput)
                    # Create a new row to append value to
                    rowOutput = []
                    rowOutput.append(c)
            else:
                return gridOutput.clear()
        # Append final row
        gridOutput.append(rowOutput)
    else:
        print("ERROR: Invalid length of input sequence (" + str(len(charSequence)) + ")")
            
    return gridOutput



# 2. Dissimilarity (Segregation Model)
#   a. Based on the grid (2D array) create, write a function to get specific value of row
#       and column to create a smaller 2D array.

#   b. After creating the new two-dimensional array, group the grid by each characters
#       given and implement the measure of segregation and isolation model to calculate
#       the index of dissimilarity 

#           Value of index represents the proportion of a group that would need to
#           move in order create a uniform distribution of population.

#           The value of the index is a maximum when each tract contains only one
#           group; it is minimized (0) when the proportion of each group in each tract
#           is the same as the proportion in the population as a whole

# Name: get_value_from_grid
# Returns: Value, -1 for exception
# Desc: Gets value given the source grid, row, and column
def get_value_from_grid(source, row, column):
    # Validate source
    if not source:
        print("ERROR: Invalid source")
        return -1
    # Try-except to catch IndexError
    try:
        retVal = source[row][column]
    except IndexError:
        return -1
    
    return retVal


# Name: create_subgrid
# Returns: Array, empty array for exception
# Desc: Create a subgrid given the source grid, row, and column
def create_subgrid(source, startRow, startColumn, rowSize, columnSize):
    # Initialize output grid
    subGrid = []
    
    # Validate source
    if not source:
        print("ERROR: Invalid source or destination")
        return subGrid
    
    # Loop through row and column from starting position indicated
    for rowCount in range(rowSize):
        subGridRow = []
        for columnCount in range(columnSize):
            cellValue = get_value_from_grid(source, startRow + rowCount, startColumn + columnCount)
            # Invalid value, return empty grid
            if cellValue == -1:
                print ("ERROR: No subgrid created")
                return subGrid.clear();
            # Append value to row
            else:
                subGridRow.append(cellValue)
        # Append row to subgrid
        subGrid.append(subGridRow)
         
    return subGrid


# Name: compute_dissimilarity_index
# Returns: Float
# Desc: Calculates Dissimilarity Index of a grid and its subgrids
def compute_dissimilarity_index(grid, subGridList):
    # Output value
    indexOfDissimilarity = 0;
    
    # List of proportions per category
    proportionList = [ ]
    
    # Loop through valid categories to compute for proportions
    for cat in ValidCategories:
        # Create an output list per category
        # First element on the list is the category value
        # catOutputList = [cat, ]
        catOutputList = []
        # Count for total occurrences of a given category in grid
        catTotal = sum(row.count(cat) for row in grid)
        # Count for occurrences of a category in subGrid
        for subGrid in subGridList:
            catGridTotal = sum(innerRow.count(cat) for innerRow in subGrid)
            # Compute for subGrid category proportion
            gridProportion = 0.00            
            gridProportion = float("%0.2f" % (catGridTotal/catTotal))
            # Add proportion to category output list for later computation
            catOutputList.append(gridProportion)
        
        # Add to proportionList
        proportionList.append(catOutputList)
        
    # List to hold all the absoulte differences between categories
    absoluteDiffList = []
    
    # Compute for absolute difference among categories 
    for cat in proportionList:
        # Pop first category that will be computed for difference
        currentList = proportionList.pop(0)
        
        # List for absolute difference of a category
        # This will contain absolute differences per each grid as elements
        catAbsoluteDiffList = []
        
        for remainingCategory in proportionList:
            for elem in range(len(remainingCategory)):
                absDiff = abs(currentList[elem] - remainingCategory[elem])
                # Format to decimal places
                absDiff = float("%0.2f" % absDiff)
                catAbsoluteDiffList.append(absDiff)
                
        absoluteDiffList.append(catAbsoluteDiffList)
        
    # Compute for the final value (Index of Dissimilarity)
    # 1/2 of the summation of all absolute of the value differences 
    for c in absoluteDiffList:
        summation = sum(elem for elem in c)
    indexOfDissimilarity = summation / 2
    
    return indexOfDissimilarity
    

# 3. Schelling Model
#   a. Based on the grid (2D array) created, write a program that will implement the
#       schelling model for segregation and integration.

#   b. Write a function that inputs a threshold for the neighboring population
#       and calculate the satisfied characters.

#   c. Generate a new two-dimensional array to represent the satisfied neighboring
#       characters

    
    
##########    



def main():
    # Sample flow
    
    # Character sequence input
    charSequence = "XXOOXOXOXOXOOXOXOXOXOXX XOOXOXOXXXOOX XOXOOXOXOXXOXOX XXO OXXXOOXOXOXOXO OXOOXOOOXXXOO OXOOOOOOOOXOX"
    print("Input character sequence: ")
    print(charSequence)
    
    # Call to load_grid
    inputGrid = load_grid(charSequence)
    print("Grid: ")
    display_list(inputGrid)
    
    # Manual creation of smaller grids
    # For the given input, we try four 5x5 subgrids
    subGridList = [ ]
    
    subGrid = create_subgrid(inputGrid, 0, 0, 5, 5)
    subGridList.append(subGrid)
    
    subGrid = create_subgrid(inputGrid, 5, 0, 5, 5)
    subGridList.append(subGrid)
    
    subGrid = create_subgrid(inputGrid, 0, 5, 5, 5)
    subGridList.append(subGrid)
    
    subGrid = create_subgrid(inputGrid, 5, 5, 5, 5)
    subGridList.append(subGrid)
    
    print("SubgridList: ")
    display_list(subGridList)
    
    index = compute_dissimilarity_index(inputGrid, subGridList)
    print("Index of Dissimilarity: " + str(index))


if __name__ == "__main__":
    main()
    
    
##########



# TEST CASES
#
# checkValuesTestCase = ['X', 'O', ' ', 'x', 'o', '1', "A Test Case"]
# # Run test cases for check_values()
# for cvts in checkValuesTestCase:
#     result = check_values(cvts)
#     print("Input: " + str(cvts) + " Output: " + str(result))
#
# loadGridTestCase = ["XXOOXOXOXOXOOXOXOXOXOXX XOOXOXOXXXOOX XOXOOXOXOXXOXOX XXO OXXXOOXOXOXOXO OXOOXOOOXXXOO OXOOOOOOOOXOX",
#                     "XXOOXOXOXOXOOXOXOXOXOXX XOOXOXOXXXOOX XOXOOXOXOXXOXOX XXO OXXXOOXOXOXOXO OXOOXOOOXXXOO OXOOOOOOOOXO",
#                     "XX1OXOXOXOXOOXOXOXOXOXX XOOXOXOXXXOOX XOXOOXOXOXXOXOX XXO OXXXOOXOXOXOXO OXOOXOOOXXXOO OXOOOOOOOOXOX",]
# # Run test cases for load_grid()
# for lgts in loadGridTestCase:
#     print("Input: " + lgts)
#     result = load_grid(lgts)
#     print(result)
#
