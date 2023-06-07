public class Solution {
    public static void Main(string[] args)
    {
        string[] strs = new string[] {"eat","tea","tan","ate","nat","bat"};
        
        Solution sol = new Solution();
        Console.WriteLine($"{sol.GroupAnagrams(strs)}");
    }
    
    
    public IList<IList<string>> GroupAnagrams(string[] strs) {
        IList<IList<string>> result = new List<IList<string>>();
        IDictionary<string, IList<int>> strIndices = new Dictionary<string, IList<int>>(); 
        if(strs.Length == 1)
        {
            result.Add(new List<string>() {strs[0]});
            return result;
        }

        for(int i = 0; i < strs.Length; i++)
        {
            string sortedString = SortString(strs[i]);
            if(strIndices.ContainsKey(sortedString))
            {
                strIndices[sortedString].Add(i);
            }
            else
            {
                strIndices[sortedString] = new List<int> {i};
            }
        }

        foreach (KeyValuePair<string, IList<int>> str in strIndices)
        {
            IList<string> groupedAnagrams = new List<string>();
            foreach (int i in str.Value)
            {
                groupedAnagrams.Add(strs[i]);
            }
            result.Add(groupedAnagrams);
        }
        return result;
    }

    public static string SortString(string input)
    {
        char[] characters = input.ToCharArray();
        Array.Sort(characters);
        return new string(characters);
    }
}