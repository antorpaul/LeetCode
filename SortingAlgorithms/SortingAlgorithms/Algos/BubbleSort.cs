namespace GroupAnagrams.Algos;

public class BubbleSort
{
    private int[] array;

    public BubbleSort(int[] array)
    {
        this.array = array;
    }

    public int[] Sort()
    {
        int[] result = new int[array.Length];
        array.CopyTo(result, 0);

        if (result.Length == 1)
        {
            return result;
        }
        
        bool swap = true;
        while (swap)
        {
            swap = false;
            for (int i = 0; i < result.Length-1; i++)
            {
                if (result[i] > result[i + 1])
                {
                    int temp = result[i];
                    result[i] = result[i + 1];
                    result[i + 1] = temp;
                    swap = true;
                }
            }
        }

        return result;
    }
    
    public int[] SortV2()
    {
        int[] result = new int[array.Length];
        array.CopyTo(result, 0);

        if (result.Length == 1)
        {
            return result;
        }
        
        for(int pass = array.Length - 1; pass >= 0; pass--)
        {
            // each pass will establish the largest element at the right place
            // so we only need to go to the ith value before that
            for (int i = 0; i < pass; i++)
            {
                if (result[i] > result[i + 1])
                {
                    int temp = result[i];
                    result[i] = result[i + 1];
                    result[i + 1] = temp;
                }
            }
        }

        return result;
    }
}