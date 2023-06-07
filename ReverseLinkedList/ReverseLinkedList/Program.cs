public class Solution
{
    public static void Main(string[] args)
    {
        // New solution object to run
        Solution sol = new Solution();
        
        // Test cases
        int[] nums = new[] { 1, 2, 3, 4, 5 };
        ListNode head = sol.CreateLinkedList(nums);
        sol.PrintLinkedList(head, "Nums normal");
        
        // Do something with the solution object here:
        head = sol.ReverseList(head);
        sol.PrintLinkedList(head, "Nums reversed");
    }

    // Solution Function Goes Here:
    public ListNode ReverseList(ListNode head) {
        ListNode current = head;
        ListNode previous = null;
        while(current != null)
        {
            ListNode next = current.next;
            current.next = previous;
            previous = current;
            if (next == null)
            {
                head = current;
            }
            current = next;
        }

        return head;
    }
    
    // Helper functions
    public ListNode CreateLinkedList(int[] nums)
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

    public void PrintLinkedList(ListNode head, string name)
    {
        ListNode curr = head;
        Console.Write($"LinkedList {name}: [");
        while (curr != null)
        {
            Console.Write($"{curr.val}");
            curr = curr.next;
            if (curr == null)
            {
                Console.Write("]");
            }
            else
            {
                Console.Write(", ");
            }
        }

        Console.WriteLine();
    }
}

public class ListNode {
    public int val;
    public ListNode next;
    public ListNode(int val=0, ListNode next=null) {
       this.val = val;
       this.next = next;
    }
}