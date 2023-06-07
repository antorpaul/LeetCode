public class Solution
{
    public static void Main(string[] args)
    {
        // Write Test Cases Here
        int[] caseOne = new[] { -1, 0, 3, 5, 9, 12 };   // target = 9
        int[] caseTwo = new[] { -1, 0, 3, 5, 9, 12 };   // target = 2
        int[] caseThree = new[] { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 };   // target = 3
        int[] caseFour = new[] { -1, 0, 5 };
        int[] caseFive = new[] { 2, 5 };

        // New solution object to run
        Solution sol = new Solution();

        // Do something with the solution object here:
        Console.WriteLine($"caseOne: {sol.Search(caseOne, 9)}");
        Console.WriteLine($"caseTwo: {sol.Search(caseTwo, 2)}");
        Console.WriteLine($"caseThree: {sol.Search(caseThree, 3)}");
        Console.WriteLine($"caseFour: {sol.Search(caseFour, 2)}");
        Console.WriteLine($"caseFive: {sol.Search(caseFive, 0)}");
    }

    // Solution Function Goes Here:
    public int Search(int[] nums, int target)
    {
        // Two pointers start at the ends of the array 
        int L = 0;
        int R = nums.Length - 1;

        if (R == 0)
        {
            return nums[L] == target ? 0 : -1;
        }
        
        // run until L and R are consecutive
        while (L <= R)
        {
            int M = (L + R) / 2;
            
            if (nums[M] == target)
            {
                return M;
            }

            if (nums[M] < target)
            {
                L = M + 1;
            }
            else
            {
                R = M - 1;
            }
        }

        return -1;
    }

    // Helper Functions Go Here
}