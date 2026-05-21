public class SudokuGrid implements ISudokuGrid{
    private static final int GRID_SIZE = 9;
    private int[][] grid;

    public SudokuGrid() {
        this.grid = new int[GRID_SIZE][GRID_SIZE];
    }

    private boolean validateIndices(int row, int col) {
        if (row >= 0 && col >= 0 && row < GRID_SIZE && col < GRID_SIZE) {
            return true;
        }
        return false;
    }

    public boolean setValue(int row, int col, int value) {
        if (validateIndices(row, col)) {
            grid[row][col] = value;
            return true;
        }
        return false;
    }

    public int getValue(int row, int col) {
        if (validateIndices(row, col)) {
            return grid[row][col];
        }
        return 0;
    }

    public boolean isValid() {
        return validateGrid();
    }

    public boolean isSolved() {
        return validateGrid() && !hasEmptyCells();
    }

    public void resetGrid() {
        grid = new int[GRID_SIZE][GRID_SIZE];
    }

    private boolean hasEmptyCells() {
        for (int[] row : grid) {
            for (int cell : row) {
                if (cell == 0) {
                    return true;
                }
            }
        }
        return false;
    }

    private boolean validateGrid() {
        int[] rowCheck = new int[9];
        int[] colCheck = new int[9];
        int[] subGridCheck = new int[9];

        for (int[] row : grid) {
            for (int cell : row) {
                // add implementation later
            }
        }
        return false;
    }

    public void displayGrid() {
        for (int[] row : grid) {
            for (int cell : row) {
                if (cell == 0) {
                    System.out.print(".");
                }
                else {
                    System.out.print(cell);
                }
                System.out.print(" ");
            }
            System.out.println();
        }
    }
}
