namespace GroupAnagrams.Algos;

public class SelectionSort
{
    private int[] array;

    public SelectionSort(int[] array)
    {
        this.array = array;
    }

    public int[] Sort()
    {
        int[] result = new int[array.Length];
        array.CopyTo(result, 0);

        for (int i = 0; i < result.Length; i++)
        {
            int minIndex = i;
            for (int j = i; j < result.Length; j++)
            {
                if (result[j] < result[minIndex])
                {
                    minIndex = j;
                }
            }

            int temp = result[i];
            result[i] = result[minIndex];
            result[minIndex] = temp;
        }

        return result;
    }
}