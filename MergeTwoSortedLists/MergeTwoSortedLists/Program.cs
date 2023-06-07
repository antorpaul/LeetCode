public class Solution
{
    public static void Main(string[] args)
    {
        // New solution object to run
        Solution sol = new Solution();
        int[] nums1 = new[] { 1, 2, 3 };
        int[] nums2 = new[] { 1, 4, 6 };

        ListNode list1 = ListNode.CreateLinkedList(nums1);
        ListNode list2 = ListNode.CreateLinkedList(nums2);
        Console.WriteLine("List 1:");
        ListNode.PrintLinkedList(list1);
        
        Console.WriteLine("List 2:");
        ListNode.PrintLinkedList(list2);
        
        // Do something with the solution object here:
        ListNode merged = sol.MergeTwoLists(list1, list2);
        Console.WriteLine("Merged:");
        ListNode.PrintLinkedList(merged);
    }

    // Solution Function Goes Here:
    public ListNode MergeTwoLists(ListNode list1, ListNode list2)
    {
        ListNode result = new ListNode();
        ListNode resultPtr = result;

        while (list1 != null && list2 != null)
        {
            if (list1.val < list2.val)
            {
                resultPtr.next = list1;
                list1 = list1.next;
            }
            else
            {
                resultPtr.next = list2;
                list2 = list2.next;
            }

            resultPtr = resultPtr.next;
        }

        if (list1 == null)
        {
            resultPtr.next = list2;
        }

        if (list2 == null)
        {
            resultPtr.next = list1;
        }

        return result.next;
    }

    // Helper Functions Go Here
    public static string SortString(string input)
    {
        char[] characters = input.ToCharArray();
        Array.Sort(characters);
        return new string(characters);
    }
}

public class ListNode {
    public int val;
    public ListNode next;
    
    public ListNode(int val=0, ListNode next=null) {
        this.val = val;
        this.next = next;
    }
    
    public static ListNode CreateLinkedList(int[] nums)
    {
        ListNode curr = new ListNode();
        ListNode head = curr;
        for (int i = 0; i < nums.Length; i++)
        {
            ListNode next = new ListNode();
            curr.val = nums[i];
            if (i == nums.Length - 1)
            {
                curr.next = null;
            }
            else
            {
                curr.next = next;
            }
            curr = next;
        }

        return head;
    }

    public static string PrintLinkedList(ListNode head)
    {
        ListNode curr = head;
        string result = "[";
        Console.Write("[");
        while (curr != null)
        {
            Console.Write($"{curr.val}");
            result.Insert(result.Length-1, $"{curr.val}");
            if (curr.next != null)
            {
                Console.Write(", ");
                result.Insert(result.Length-1, ", ");
            }
            else
            {
                Console.Write("]\n");
                result.Insert(result.Length-1, "]\n");
            }

            curr = curr.next;
        }

        return result;
    }
}