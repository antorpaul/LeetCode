namespace GroupAnagrams.Algos;

public class MergeSort
{
    private int[] array;
    private int[] result;

    public MergeSort(int[] array)
    {
        this.array = array;
    }

    public int[] Sort(int left, int right)
    {
        if (left < right)
        {
            int mid = (left + right) / 2;
            Sort(left, mid);
            Sort(mid + 1, right);
            Merge(left, mid, right);
        }

        return result;
    }
    
    // Merge Function
    public void Merge(int left, int mid, int right)
    {
        
    }
}