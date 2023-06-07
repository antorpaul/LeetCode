public class Solution {
    public static void Main(string[] args)
    {
        // Write Test Cases Here
        int test1 = 3;
        int test2 = 58;
        int test3 = 1994;
        int test4 = 200;
        
        // New solution object to run
        Solution sol = new Solution();

        // Do something with the solution object here:
        // Console.WriteLine($"{sol.IntToRoman(test1)}");
        // Console.WriteLine($"{sol.IntToRoman(test2)}");
        // Console.WriteLine($"{sol.IntToRoman(test3)}");
        Console.WriteLine($"{sol.IntToRoman(test4)}");
    }
    
    public readonly static Dictionary<int, string> Symbols = new Dictionary<int, string>() {
        {1, "I"},
        {5, "V"},
        {10, "X"},
        {50, "L"},
        {100, "C"},
        {500, "D"},
        {1000, "M"}
    };
    
    public readonly static Dictionary<int, string> SpecialCases = new Dictionary<int, string>() {
        {4, "IV"},
        {9, "IX"},
        {40, "XL"},
        {90, "XC"},
        {400, "CD"},
        {900, "CM"},
    };

    public string IntToRoman(int num) {
        // Split integer into place value
        int number = num;
        int place = 1;
        Dictionary<int, string> placeToRoman = new Dictionary<int, string>(); // k = place value, v = roman numeral

        string result;

        if (Symbols.TryGetValue(num, out result))
        {
            return result;
        }

        result = "";

        // populate dictionary with place values (key)
        while(number != 0)
        {
            int placeValue = (number % 10) * place;
            if (placeValue != 0)
            {
                placeToRoman.Add(placeValue, "");
            }
            place *= 10;
            number = number / 10;
        }

        foreach (var kvp in placeToRoman)
        {
            result = result.Insert(0, KeyToRoman(kvp.Key));
        }
    
        return result;
    }

    // converts a key to roman numeral
    public static string KeyToRoman(int key)
    {
        // Roman Numerals have no 0
        if (key == 0)
        {
            return "";
        }
        
        // special cases:
        string result = "";
        if(SpecialCases.TryGetValue(key, out result) || Symbols.TryGetValue(key, out result))
        {
            return result;
        }
        
        // calculate regular cases
        while (key != 0)
        {
            int closestRoman = GetClosestRoman(key);
            int numClosestRoman = key / closestRoman;
            IEnumerable<string> romanValue = Enumerable.Repeat(Symbols[closestRoman], numClosestRoman);
            result += String.Join("", romanValue);
            key %= closestRoman;
        }
        
        return result;
    }

    public static int GetClosestRoman(int num)
    {
        int closestValue = 0;
        int prevValue = 0;
        foreach(var kvp in Symbols)
        {
            if(num >= kvp.Key)
            {
                closestValue = Math.Max(closestValue, kvp.Key);
            }
            
            // if the value didn't change, we've reached the max
            if (closestValue == prevValue)
            {
                return closestValue;
            }
            
            prevValue = closestValue;
        }

        return closestValue;
    }
}