using GroupAnagrams.Algos;

public class Solution
{
    public static void Main(string[] args)
    {
        // Write Test Cases Here
        int[] aOne = new[] { 3, 5, 8, 9, 5, 2 };
        int[] aTwo = new[] { 3, 5, 8, 6, 2, 9 };
        int[] aThree = new[] { 1, 2, 3, 4, 8, 3, 4, 9, 8 };
        
        // Do something with the solution object here
        // Selection Sort
        // SelectionSort selectionSort1 = new SelectionSort(aOne);
        // SelectionSort selectionSort2 = new SelectionSort(aTwo);
        // SelectionSort selectionSort3 = new SelectionSort(aThree);
        // Console.WriteLine($"SelectionSort: [{String.Join(", ", aOne)}], sorted: [{String.Join(", ", selectionSort1.Sort())}]");
        // Console.WriteLine($"SelectionSort: [{String.Join(", ", aTwo)}], sorted: [{String.Join(", ", selectionSort2.Sort())}]");
        // Console.WriteLine($"SelectionSort: [{String.Join(", ", aThree)}], sorted: [{String.Join(", ", selectionSort3.Sort())}]");
        
        // Insertion Sort
        // InsertionSort insertionSort1 = new InsertionSort(aOne);
        // InsertionSort insertionSort2 = new InsertionSort(aTwo);
        // InsertionSort insertionSort3 = new InsertionSort(aThree);
        // Console.WriteLine($"InsertionSort: [{String.Join(", ", aOne)}], sorted: [{String.Join(", ", insertionSort1.Sort())}]");
        // Console.WriteLine($"InsertionSort: [{String.Join(", ", aTwo)}], sorted: [{String.Join(", ", insertionSort2.Sort())}]");
        // Console.WriteLine($"InsertionSort: [{String.Join(", ", aThree)}], sorted: [{String.Join(", ", insertionSort3.Sort())}]");
        
        // Bubble Sort
        BubbleSort bubbleSort1 = new BubbleSort(aOne);
        BubbleSort bubbleSort2 = new BubbleSort(aTwo);
        BubbleSort bubbleSort3 = new BubbleSort(aThree);
        Console.WriteLine($"BubbleSort: [{String.Join(", ", aOne)}], sorted: [{String.Join(", ", bubbleSort1.SortV2())}]");
        Console.WriteLine($"BubbleSort: [{String.Join(", ", aTwo)}], sorted: [{String.Join(", ", bubbleSort2.SortV2())}]");
        Console.WriteLine($"BubbleSort: [{String.Join(", ", aThree)}], sorted: [{String.Join(", ", bubbleSort3.SortV2())}]");
        
        // Shell Sort
        // ShellSort shellSort1 = new ShellSort(aOne);
        // ShellSort shellSort2 = new ShellSort(aTwo);
        // ShellSort shellSort3 = new ShellSort(aThree);
        // Console.WriteLine($"ShellSort: [{String.Join(", ", aOne)}], sorted: [{String.Join(", ", shellSort1.Sort())}]");
        // Console.WriteLine($"ShellSort: [{String.Join(", ", aTwo)}], sorted: [{String.Join(", ", shellSort2.Sort())}]");
        // Console.WriteLine($"ShellSort: [{String.Join(", ", aThree)}], sorted: [{String.Join(", ", shellSort3.Sort())}]");
    }
}