public interface ISudokuGrid {
    void initializeGrid(int[][] grid);

    int getValue(int row, int col);

    boolean setValue(int row, int col, int value);

    boolean isValid();

    boolean isSolved();

    void resetGrid();

    void displayGrid();
}
