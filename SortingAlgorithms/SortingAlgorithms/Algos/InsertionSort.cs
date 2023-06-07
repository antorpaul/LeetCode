namespace GroupAnagrams.Algos;

public class InsertionSort
{
    private int[] array;

    public InsertionSort(int[] array)
    {
        this.array = array;
    }

    public int[] Sort()
    {
        int[] result = new int[array.Length];
        array.CopyTo(result, 0);

        for (int i = 0; i < result.Length; i++)
        {
            int curr = result[i];
            int ptr = i;

            while (ptr > 0 && result[ptr - 1] > curr)
            {
                // keep going down and swapping result values
                result[ptr] = result[ptr - 1];
                ptr = ptr - 1;
            }

            // finally put the current value where it belongs
            result[ptr] = curr;
        }

        return result;
    }
}