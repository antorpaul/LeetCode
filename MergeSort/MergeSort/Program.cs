class MergeSort
{
    public static void Main(string[] args)
    {
        int[] nums = new[] { 2, 5, 6, 8, 12, 0, 3, 41, 2 };
        int[] numsEdges = new[] { 1, 0, -1, -30, 0, 40, -2, 1 };
        
        Console.WriteLine($"nums: {PrintNumsArray(nums)}\nnumsEdges: {PrintNumsArray(numsEdges)}");
        
        MergeSort.Sort(nums);
        MergeSort.Sort(numsEdges);
        
        Console.WriteLine($"sorted nums: {PrintNumsArray(nums)}\nsorted numsEdges: {PrintNumsArray(numsEdges)}");
    }

    public static string PrintNumsArray(int[] nums)
    {
        string result = $"[{string.Join(", ", nums)}]";
        return result;
    }

    public static void Sort(int[] nums)
    {
        // an array with 1 element is already sorted
        if (nums.Length < 2)
        {
            return;
        }
        
        int MidPoint = nums.Length / 2;
        
        // start by splitting
        int[] left = new int[nums.Length/2];
        int[] right = new int[nums.Length - nums.Length/2]; // account for possibility of odd numbered array
        
        // copy array
        Array.Copy(nums, left, MidPoint);
        Array.Copy(nums, MidPoint, right, 0, right.Length);
        
        // keep sorting until we have 1 element arrays to merge
        Sort(left);
        Sort(right);
        
        // merge in the arrays
        Merge(left, right, nums);
    }

    public static void Merge(int[] left, int[] right, int[] original)
    {
        // All of the elements of the original are either in L or R, we can just change the entries in the original
        int l = 0;  // index of left array
        int r = 0;  // index of right array
        int i = 0;  // index of original array to update
        // compare through both arrays
        while (l < left.Length && r < right.Length)
        {
            if (left[l] < right[r])
            {
                original[i] = left[l];
                l++;
            }
            else
            {
                original[i] = right[r];
                r++;
            }
            i++;
        }
        
        // compare leftover elements in L
        while (l < left.Length)
        {
            original[i] = left[l];
            i++;
            l++;
        }
        
        // compare leftover elements in R
        while (r < right.Length)
        {
            original[i] = right[r];
            i++;
            r++;
        }
    }
}