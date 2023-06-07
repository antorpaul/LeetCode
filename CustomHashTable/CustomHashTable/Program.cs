public class CustomHashTable
{
    public static void Main(string[] args)
    {
        // Write Test Cases Here

        // New solution object to run
        CustomHashTable sol = new CustomHashTable(new int[]{3, 4, 5});

        // Do something with the solution object here:
    }

    private IList<LinkedList> indices = new List<LinkedList>(10);

    public CustomHashTable(int[] data)
    {
        // indicides will point to linked list of keys
        
    }

    /// <summary>
    /// Basic hash function to determine the index to place key
    /// </summary>
    /// <param name="k">key</param>
    /// <returns></returns>
    private int HashFunction(int k)
    {
        return k % indices.Count;
    }
    
    /// <summary>
    /// Look-up algorithm to get key
    /// </summary>
    /// <param name="k">key</param>
    /// <returns></returns>
    public int GetKey(int k)
    {
        // get index from hashfunction
        int index = HashFunction(k);
        LinkedList curr = indices[index];
        while (curr != null)
        {
            if (curr.Value == k)
            {
                return curr.Value;
            }
            
            curr = curr.Next;
        }
        return -1;
    }

    /// <summary>
    /// Algorithm to insert key into linked list at index
    /// </summary>
    /// <param name="k">key</param>
    /// <returns>Boolean status of insertion</returns>
    public bool InsertKey(int k)
    {
        if (GetKey(k) != -1)
        {
            // insert the key
        }
        return false;
    }

    /// <summary>
    /// Algorithm to remove key from hash table
    /// </summary>
    /// <param name="k"></param>
    /// <returns>Boolean status of insertion</returns>
    public bool RemoveKey(int k)
    {
        return false;
    }
}

public class LinkedList
{
    private int value;
    private LinkedList next;

    public LinkedList(int value = 0, LinkedList next = null)
    {
        this.value = value;
        this.next = next;
    }

    public int Value
    {
        get => value;
        set => this.value = value;
    }

    public LinkedList Next
    {
        get => next;
        set => next = value ?? throw new ArgumentNullException(nameof(value));
    }

    public static void PrintLinkedList(LinkedList head)
    {
        LinkedList curr = head;
        Console.Write("[");
        while (curr != null)
        {
            Console.Write($"{curr.value}");
            curr = curr.next;
            if (curr != null)
            {
                Console.Write(", ");
            }
        }
        Console.Write("]\n");
    }
}