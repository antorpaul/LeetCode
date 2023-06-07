using System;
using System.Collections.Generic;

public class Solution {
    static public void Main(String[] args)
    {
        string s = "anagram", t = "nagaram";
        if(IsAnagram(s, t))
        {
            Console.WriteLine("True");
        }
        else
        {
            Console.WriteLine("False");
        }
    }
    
    public static bool IsAnagram(string s, string t) {
        // if the lengths aren't the same, we can already count it out
        if(s.Length != t.Length)
        {
            return false;
        }

        // make a dictionary to hold characters in s
        IDictionary<char, int> sDict = new Dictionary<char, int>();
        foreach(char sChar in s)
        {
            if(sDict.ContainsKey(sChar))
            {
                sDict[sChar]++;
            } else {
                sDict.Add(sChar, 1);
            }
        }

        IDictionary<char, int> tDict = new Dictionary<char, int>();
        foreach(char tChar in t)
        {
            if(tDict.ContainsKey(tChar))
            {
                tDict[tChar]++;
            } else {
                tDict.Add(tChar, 1);
            }
        }

        return sDict.Keys.All(key => tDict.ContainsKey(key) && sDict[key] == tDict[key]);
    }
}