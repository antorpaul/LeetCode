namespace GroupAnagrams.Algos;

public class ShellSort
{
    private int[] array;

    public ShellSort(int[] array)
    {
        this.array = array;
    }

    public int[] Sort()
    {
        int[] result = new int[array.Length];
        array.CopyTo(result, 0);
        int n = array.Length;

        if (result.Length == 1)
        {
            return result;
        }

        // because c# is type safe, we can ignore the floor function
        for (int gap = n / 2; gap > 0; gap /= 2)
        {
            for (int i = gap; i < n; i++)
            {
                int gapValue = result[i];
                int j = i - gap;
                while (j >= 0 && result[j] > gapValue)
                {
                    result[j + gap] = result[j];
                    j = j - gap;
                }

                result[j + gap] = gapValue;
            }
        }

        return result;
    }
}