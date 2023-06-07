public class Solution
{
    public static void Main(string[] args)
    {
        // Write Test Cases Here
        char[][] testcase1 = new char[9][] {
            new char[9] {'5','3','.','.','7','.','.','.','.'}, 
            new char[9] {'6','.','.','1','9','5','.','.','.'},
            new char[9] {'.','9','8','.','.','.','.','6','.'},
            new char[9] {'8','.','.','.','6','.','.','.','3'},
            new char[9] {'4','.','.','8','.','3','.','.','1'},
            new char[9] {'7','.','.','.','2','.','.','.','6'},
            new char[9] {'.','6','.','.','.','.','2','8','.'},
            new char[9] {'.','.','.','4','1','9','.','.','5'},
            new char[9] {'.','.','.','.','8','.','.','7','9'}
        };

    // New solution object to run
        Solution sol = new Solution();

        // Do something with the solution object here:
        sol.IsValidSudoku(testcase1);
    }
    
    public bool IsValidSudoku(char[][] board) {
        IDictionary<(int, int), string> subBox = new Dictionary<(int, int), string>(){
            {(0, 0), "000000000"}, 
            {(1, 0), "000000000"}, 
            {(2, 0), "000000000"}, 
            {(0, 1), "000000000"}, 
            {(1, 1), "000000000"}, 
            {(2, 1), "000000000"}, 
            {(0, 2), "000000000"}, 
            {(1, 2), "000000000"}, 
            {(2, 2), "000000000"}
        };

        String[] columns = new String[9] { 
            "000000000", "000000000", "000000000", "000000000", "000000000", 
            "000000000", "000000000", "000000000", "000000000"};

        for(int i = 0; i < 9; i++)
        {
            HashSet<int> rowNumbers = new HashSet<int>();
            for(int j = 0; j < 9; j++)
            {
                int rowLength = rowNumbers.Count;
                if(board[i][j] != '.')
                {
                    rowNumbers.Add(board[i][j]);
                    // check row
                    if(rowLength == rowNumbers.Count)
                    {
                        return false;
                    }
                    
                    // char to int
                    int num = board[i][j] - '0';
                    // insert into columns
                    if(columns[j][num-1] == board[i][j])
                    {
                        return false;
                    }
                    columns[j] = columns[j].Insert(num-1, board[i][j].ToString()).Remove(num, 1);

                    // insert into sub-box
                    if(subBox[GetSubBox(i, j)][num-1] == board[i][j])
                    {
                        return false;
                    }
                    
                    subBox[GetSubBox(i, j)] = subBox[GetSubBox(i, j)].Insert(num-1, board[i][j].ToString()).Remove(num, 1);
                }
            }
        }

        return true;
    }

    public (int, int) GetSubBox(int i, int j)
    {
        return (i/3, j/3);
    }
}