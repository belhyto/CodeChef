1. Decimal to Binary, Hexadecimal, and Octal
 ```cpp
#include <iostream>
using namespace std;

void decimalToBinary(int n) {
    int binary[32];
    int i = 0;
    while (n > 0) {
        binary[i] = n % 2;
        n = n / 2;
        i++;
    }
    cout << "Binary: ";
    for (int j = i - 1; j >= 0; j--)
        cout << binary[j];
    cout << endl;
}

void decimalToHexadecimal(int n) {
    char hexa[100];
    int i = 0;
    while (n != 0) {
        int temp = n % 16;
        if (temp < 10)
            hexa[i] = temp + 48; // Convert integer to character (0-9)
        else
            hexa[i] = temp + 55; // Convert integer to character (A-F)
        i++;
        n = n / 16;
    }
    cout << "Hexadecimal: ";
    for (int j = i - 1; j >= 0; j--)
        cout << hexa[j];
    cout << endl;
}

void decimalToOctal(int n) {
    int octal[100];
    int i = 0;
    while (n != 0) {
        octal[i] = n % 8;
        n = n / 8;
        i++;
    }
    cout << "Octal: ";
    for (int j = i - 1; j >= 0; j--)
        cout << octal[j];
    cout << endl;
}

int main() {
    int n;
    cout << "Enter a decimal number: ";
    cin >> n;
    decimalToBinary(n);
    decimalToHexadecimal(n);
    decimalToOctal(n);
    return 0;
}
 ```

1. Question 1 A password string, pwd, consists of binary characters (Os and 1s). A cyber security expert is trying to determine the minimum number of changes required to make the password secure. To do so, it must be divided into substrings of non-overlapping, even length substrings. Each substring can only contain 1s or Os, not a mix. This helps to ensure that the password is strong and less vulnerable to hacking attacks. Find the minimum number of characters that must be flipped in the password string, i.e. changed from 0 to 1 or 1 to o to allow the string to be divided as described.


 ```cpp

#include <iostream>
#include <string>
using namespace std;

int minFlips(string pwd) {
    int n = pwd.length();
    if (n % 2 != 0) {
        return -1; // Length is odd, not possible to divide into even-length substrings
    }

    int flips = 0;
    for (int i = 0; i < n; i += 2) {
        // Check pairs of characters
        if (pwd[i] != pwd[i + 1]) {
            flips++; // One flip needed to make the pair homogeneous
        }
    }
    
    return flips;
}

int main() {
    string pwd;
    cout << "Enter the password string (binary): ";
    cin >> pwd;

    int result = minFlips(pwd);
    if (result == -1) {
        cout << "The length of the password string must be even." << endl;
    } else {
        cout << "Minimum number of flips required: " << result << endl;
    }

    return 0;
}
 ```

2. Question 2 For each element of an array, a counter is set to 0. The element is compared to each element to its left. If the element to the left is greater, the absolute difference is subtracted from the counter. If the element to the left is less, the absolute difference is added to the counter. For each element of the array, determine the value of the counter. These values should be stored in an array and returned. Example n=3, the number of elements arr = [24.3] For arr[0] 2. counter starts at 0 and there are no elements to the left so counter = 0. For arr[1]-4, counter starts at 0 and then increases by /4-2/-2 at the first and only comparison: counter = 2. • Testing arr[2]-3, first against 4, counter-0-13- 4/--1, and then against 2. counter-113-21- a • The answer array is [0, 2.0).


 ```cpp 

#include <iostream>
#include <vector>
#include <cmath>
using namespace std;

vector<int> calculateCounters(const vector<int>& arr) {
    int n = arr.size();
    vector<int> result(n, 0);

    for (int i = 1; i < n; i++) {
        int counter = 0;
        for (int j = 0; j < i; j++) {
            if (arr[j] > arr[i]) {
                counter -= abs(arr[j] - arr[i]);
            } else {
                counter += abs(arr[j] - arr[i]);
            }
        }
        result[i] = counter;
    }

    return result;
}

int main() {
    vector<int> arr = {2, 4, 3};
    vector<int> result = calculateCounters(arr);

    cout << "Resultant array: ";
    for (int val : result) {
        cout << val << " ";
    }
    cout << endl;

    return 0;
}
 ```

1. Question 1 An English lecture at Hacker Elementary School is aimed at teaching students the letters of the alphabet. The students are provided with a string word that consists of lowercase English letters. in one move. they can choose any index & and let the character at that index be c. Then, the first occurrence of c to the left of and the first occurrence of to the right of /are deleted (Note the operation can still be carried out even if either the left or right occurrence doesn't exist). For example, if word "adabacaea", and if index 4 is chosen (0-based), the first occurrence of 'a' to the left and right of index 4 (bold, indices 2 and 6) are deleted leaving word "adbaces" Find the minimum number of moves the students need to perform in order to get a word of minimal length Example Consider word "baabacaa" The following moves are optimal. 1. Choose index Q basbucar", then word "bhaaacar. Delete the to its right at index 3. There is no & to its left so the operation is finished. 2. Now choose index 2. Danacar", then word "baca" 3. Now choose index 3 "bacar then word "ba"

 ```cpp

def min_moves_to_reduce_string(word):
    word = list(word)
    moves = 0
    
    while True:
        found = False
        for i in range(len(word)):
            left_idx = None
            right_idx = None
            
            # Find first occurrence to the left
            for j in range(i - 1, -1, -1):
                if word[j] == word[i]:
                    left_idx = j
                    break
            
            # Find first occurrence to the right
            for k in range(i + 1, len(word)):
                if word[k] == word[i]:
                    right_idx = k
                    break
            
            # If both left and right occurrences are found
            if left_idx is not None or right_idx is not None:
                # Delete the occurrences
                if left_idx is not None:
                    word[left_idx] = ''
                if right_idx is not None:
                    word[right_idx] = ''
                
                word[i] = ''
                moves += 1
                word = [char for char in word if char != '']  # Clean up
                found = True
                break
        
        if not found:
            break
    
    return moves

# Test example
word = "baabacaa"
result = min_moves_to_reduce_string(word)
print(f"Minimum moves: {result}")

 ```

1. Question 1 The cost of a stock on each day is given in an array, arr. An investor wants to buy the stocks in triplets such that the sum of the cost for three days is divisible by d. The goal is to find the number of distinct triplets (j, k) such that / <j<k and the sum (a[i]+a[j]+a[k]) is divisible by d. Example Let arr, prices of stock = [3, 3, 4, 7, 8] and d = 5. Following are the triplets whose sum is divisible by d (1-based indexing): • Triplet with indices-(1, 2, 3), sum = 3+3+4 which is equal to 10 Triplet with indices-(1, 3, 5), sum = 3+4+8 which is equal to 15 • Triplet with indices-(2, 3, 4), sum = 3+4+8 which is equal to 15 Hence the answer is 3.

 ```
#include <iostream>
#include <vector>

using namespace std;

int countDivisibleTriplets(vector<int>& arr, int d) {
    int n = arr.size();
    int count = 0;

    // Brute-force check for all triplets (i, j, k)
    for (int i = 0; i < n - 2; ++i) {
        for (int j = i + 1; j < n - 1; ++j) {
            for (int k = j + 1; k < n; ++k) {
                int sum = arr[i] + arr[j] + arr[k];
                if (sum % d == 0) {
                    count++;
                }
            }
        }
    }

    return count;
}

int main() {
    vector<int> arr = {3, 3, 4, 7, 8};
    int d = 5;

    int result = countDivisibleTriplets(arr, d);
    cout << "Number of triplets: " << result << endl;

    return 0;
}
 ```
Fizzbuzz 
```cpp

#include <iostream>
using namespace std;

void fizzBuzz(int n) {
    for (int i = 1; i <= n; i++) {
        if (i % 3 == 0 && i % 5 == 0) {
            cout << "FizzBuzz" << endl;  // Multiple of both 3 and 5
        } else if (i % 3 == 0) {
            cout << "Fizz" << endl;  // Multiple of 3
        } else if (i % 5 == 0) {
            cout << "Buzz" << endl;  // Multiple of 5
        } else {
            cout << i << endl;  // Just print the number
        }
    }
}

int main() {
    int n;
    cout << "Enter the value of n: ";
    cin >> n;
    fizzBuzz(n);
    return 0;
}

```


Question 1
Given a string that consists of left and right parentheses, '(' and ')', balance the parentheses by inserting parentheses as necessary. Determine the minimum number of characters that must be inserted.
Example:
1. s = (()))
Insert 1 left parenthesis at the left end of the string to get '((()))'. The string is balanced after 1 insertion.
```cpp
int minInsertions(string s) {
    int leftBalance = 0;   // Number of unmatched '('
    int rightBalance = 0;  // Number of unmatched ')'

    for (char c : s) {
        if (c == '(') {
            leftBalance++;  // Every '(' needs a ')' to balance
        } else {
            if (leftBalance > 0) {
                leftBalance--;  // A ')' balances one '('
            } else {
                rightBalance++;  // No '(' to balance this ')', so we need a '('
            }
        }
    }

    // Total number of insertions needed is the sum of remaining unmatched '(' and ')'
    return leftBalance + rightBalance;
}
```

Question 2
A palindrome reads the same from left or right, mom for example. There is a palindrome which must be modified, if possible. Change exactly one character of the string to another character in the range ascii[a-z] so that the string meets the following three conditions:
1. The new string is lower alphabetically than the initial string.
2. The new string is the lowest value string alphabetically that can be created from the original palindrome after making only one change.
3. The new string is not a palindrome.
Return the new string, or, if it not possible to create a string meeting the criteria, return the string IMPOSSIBLE

```cpp
#include <iostream>
#include <string>
using namespace std;

string breakPalindrome(string palindrome) {
    int n = palindrome.length();
    
    // If the length of the string is 1, it's impossible to create a non-palindrome
    if (n == 1) return "IMPOSSIBLE";
    
    // Traverse only half of the palindrome (since it's symmetric)
    for (int i = 0; i < n / 2; i++) {
        // If we find a character that is not 'a', change it to 'a' and return the string
        if (palindrome[i] != 'a') {
            palindrome[i] = 'a';
            return palindrome;
        }
    }

    // If the string consists entirely of 'a's, change the last character to 'b'
    palindrome[n - 1] = 'b';
    return palindrome;
}

int main() {
    string s = "abba";
    cout << breakPalindrome(s) << endl;  // Output should be "aaba"
    
    s = "aaaa";
    cout << breakPalindrome(s) << endl;  // Output should be "aaab"
    
    s = "a";
    cout << breakPalindrome(s) << endl;  // Output should be "IMPOSSIBLE"
    
    return 0;
}

```

Odd-Even-Transform Problem works on an array of integers (both positive, negative, and zero), by taking in a value (a whole number) that specifies the number of times the transformation has to be applied.
On an array of integers, the transformation that n number of times needs to occur:
- Adds three (+3) to each odd integer.
- Subtracts three (-3) from each even integer.
Example:
[3, 4, 9] means the array with integers 3, 4, 9 has to undergo transformation 3 times.
[3, 4, 9]->[6, 1, 12] -> [3,4,9]→[6, 1, 12]. So the result is [6, 1, 121.


```cpp
#include <iostream>
#include <vector>
using namespace std;

vector<int> oddEvenTransform(vector<int>& arr, int n) {
    for (int i = 0; i < arr.size(); i++) {
        if (arr[i] % 2 != 0) {
            // If the number is odd, add 3 * n
            arr[i] += 3 * n;
        } else {
            // If the number is even, subtract 3 * n
            arr[i] -= 3 * n;
        }
    }
    return arr;
}

int main() {
    // Example input
    vector<int> arr = {3, 4, 9};
    int n = 3;  // Number of times to apply the transformation
    
    // Applying the transformation
    vector<int> result = oddEvenTransform(arr, n);
    
    // Output the result
    cout << "Transformed array: ";
    for (int i = 0; i < result.size(); i++) {
        cout << result[i] << " ";
    }
    cout << endl;

    return 0;
}

```

2. Question 2
In the assembly line, the factory assembles three parts 'a'b'c' of a triangle toy. A valid toy is one where the two shorter sides added together are greater in lengths than the longest side.
There are two forms of valid triangles to identify
If 2 parts are of equal length, the form is sosceles
if all 3 parts are of equal length, the form is Equilateral
If a toy is not valid or is not one of those 2 forms, it is None of these.
Example
mangle Toy [22.1333,345 1137
The fest triangle is valid and has 2 equal parts, in the form is sosceles
The second a sand and has 2 equal parts so the farm in Equiahma
The third is valid tur not one of me to specific forms
The fourstiev The sof

```cpp
#include <iostream>
#include <algorithm>
using namespace std;

string classifyToy(double a, double b, double c) {
    // Sort the sides to easily check for triangle validity
    double sides[3] = {a, b, c};
    sort(sides, sides + 3);  // Sorting ensures sides[2] is the largest side
    
    // Check for the triangle inequality (valid triangle)
    if (sides[0] + sides[1] > sides[2]) {
        // Check if all sides are equal -> Equilateral
        if (a == b && b == c) {
            return "Equilateral";
        }
        // Check if two sides are equal -> Isosceles
        else if (a == b || b == c || a == c) {
            return "Isosceles";
        } else {
            return "None of these";
        }
    } else {
        return "None of these";  // Not a valid triangle
    }
}

int main() {
    // Example 1
    double a1 = 22.1, b1 = 33.3, c1 = 34.5;
    cout << "Toy 1: " << classifyToy(a1, b1, c1) << endl;
    
    // Example 2
    double a2 = 11.3, b2 = 11.3, c2 = 11.3;
    cout << "Toy 2: " << classifyToy(a2, b2, c2) << endl;
    
    // Example 3
    double a3 = 11, b3 = 3, c3 = 7;
    cout << "Toy 3: " << classifyToy(a3, b3, c3) << endl;
    
    return 0;
}

```

1. Question 1
Given in request ids as an array of string requests, and an interger & after all requests are received, find the à most recent requests. Report the answer in order of most recent to least recent.
Example:
Suppose & requnststemt ten tem Stem", "item", and 3.
Starting from the right and moving left, collecting distinct requests, there is "tem" followed by "item" Skip the second instance of "tent3" and find "item". The answer is [item)", "item" tem2"]
Function Description
Complete the function getLatestRequests in the editor below.
getLatest Requests takes the following arguments str requestifol the request ids mrk the number of requests to report
 
``cpp
#include <iostream>
#include <vector>
#include <unordered_set>
using namespace std;

vector<string> getLatestRequests(vector<string>& requests, int k) {
    vector<string> result;              // Stores the final result
    unordered_set<string> seen;         // Tracks distinct requests
    
    // Traverse the requests from the last element to the first (right to left)
    for (int i = requests.size() - 1; i >= 0; i--) {
        if (seen.find(requests[i]) == seen.end()) {  // If it's a distinct request
            result.push_back(requests[i]);           // Add to the result
            seen.insert(requests[i]);                // Mark as seen
        }
        if (result.size() == k) {                    // Stop once we have k requests
            break;
        }
    }
    
    return result;  // Return the result in order from most recent to least recent
}

int main() {
    // Example input
    vector<string> requests = {"item1", "item2", "item3", "item2", "item1"};
    int k = 3;
    
    // Get the latest k distinct requests
    vector<string> latestRequests = getLatestRequests(requests, k);
    
    // Output the result
    cout << "Latest distinct requests: ";
    for (const string& request : latestRequests) {
        cout << request << " ";
    }
    cout << endl;

    return 0;
}

```

1. Question 1
Implement a simple prototype service to find the difference between two JSON (JavaScript Object Notation) objects.
To keep the prototype simple, a JSON will contain only key-value pairs and no nested objects or arrays in It. Given two JSON strings, json! and json2, find the list of keys for which the values are different. If a key is present in only one of the JSONs, it should not be considered in the result. The list of keys should be sorted in lexicographically ascending order.
Example: Suppose json?"("hello":"world", "hi":"hello", "you":"me")" and json2" ("hello":"world","hi":"helloo", "you": "me")"
The only common key where the values differ is "hi". Hence the answer is [hi].
Function Description
Complete the function get/SONDiff in the editor below.
get/SONDiff has the following parameter(s)
json 1: the first JSON string
json2: the second JSON string
Returns
string(): a sorted list of keys that have different associated values in the two JSONS

To solve the problem of finding the difference between two JSON objects, you need to:
1. Parse the JSON strings into a dictionary-like format.
2. Compare the values for the common keys.
3. Collect the keys where the values differ.
4. Sort the keys lexicographically and return them as a string.

Here’s a step-by-step implementation using C++:

### Solution:

1. **Parse JSON**: Use a library or method to parse JSON strings into a map or unordered_map. For simplicity, we will use C++ standard libraries and assume JSON-like format can be parsed into a `map<string, string>`.

2. **Compare Values**: Iterate through the keys in one JSON and check if the other JSON contains the same key with a different value.

3. **Collect and Sort Keys**: Collect the keys where values differ and sort them.

4. **Return Result**: Format the sorted keys into a string.

### Code Implementation in C++:

```cpp
#include <iostream>
#include <string>
#include <map>
#include <set>
#include <sstream>
#include <algorithm>

// Utility function to parse JSON-like string into a map
std::map<std::string, std::string> parseJson(const std::string& json) {
    std::map<std::string, std::string> jsonMap;
    std::string key, value;
    bool isKey = true;
    bool isValue = false;
    std::stringstream ss(json);

    char ch;
    while (ss >> ch) {
        if (ch == '{' || ch == '}') continue;  // Ignore braces
        if (ch == '"') {  // Start of key or value
            if (isKey) {
                while (ss >> ch && ch != '"') key += ch;
                isKey = false;
                isValue = true;
            } else if (isValue) {
                while (ss >> ch && ch != '"') value += ch;
                jsonMap[key] = value;
                key.clear();
                value.clear();
                isKey = true;
                isValue = false;
            }
        }
    }

    return jsonMap;
}

// Function to find the difference between two JSON strings
std::string getJsonDiff(const std::string& json1, const std::string& json2) {
    // Parse JSON strings
    std::map<std::string, std::string> map1 = parseJson(json1);
    std::map<std::string, std::string> map2 = parseJson(json2);

    std::set<std::string> diffKeys;

    // Find keys with differing values
    for (const auto& [key, value] : map1) {
        if (map2.count(key) > 0 && map2[key] != value) {
            diffKeys.insert(key);
        }
    }

    for (const auto& [key, value] : map2) {
        if (map1.count(key) > 0 && map1[key] != value) {
            diffKeys.insert(key);
        }
    }

    // Convert result to a string
    std::string result;
    for (const auto& key : diffKeys) {
        if (!result.empty()) result += ", ";
        result += key;
    }

    return result;
}

int main() {
    // Example JSON strings
    std::string json1 = R"({"hello":"world", "hi":"hello", "you":"me"})";
    std::string json2 = R"({"hello":"world","hi":"helloo", "you": "me"})";

    // Get the differing keys
    std::string diff = getJsonDiff(json1, json2);

    // Output the result
    std::cout << "Keys with differing values: [" << diff << "]" << std::endl;

    return 0;
}
```

### Explanation:
1. **Parse JSON**:
   - The `parseJson` function converts a JSON-like string into a `map<string, string>`. It handles keys and values while ignoring braces.

2. **Find Differences**:
   - The `getJsonDiff` function finds keys with differing values by comparing the two maps. It uses a `set` to ensure unique and sorted keys.

3. **Output**:
   - The `diff` string is constructed from the sorted set of differing keys.

### Example Output:
For `json1 = {"hello":"world", "hi":"hello", "you":"me"}` and `json2 = {"hello":"world","hi":"helloo", "you": "me"}`, the output will be:
```
Keys with differing values: [hi]
```

### Time Complexity:
- **O(n)** for parsing and finding differences where `n` is the number of key-value pairs in the JSON strings.

### Space Complexity:
- **O(n)** for storing the key-value pairs and the result set.


There is a shop with old-style cash regihters. Rather than scanning items and pulling the price from a Atabase, the price of each item is typed in manually. This method sometimes leads to errors. Given a Int of items and their comect prices compare the prices to those entered when nach item was d Determine the number of errors in selling prices
Example
products(egge, mik: cheese)
productPrices (232557号
productSoldeger lege cheer mik
solPrice(225328
Price
Product Actual Expected Error
2.99
2.09
2.89
3:29
The second sale of eggs has a wrong price, as does the sale of cheese. There are errors in priong
Function Description
Complete the function priceCheck in the editor belon

The problem involves comparing the prices of products sold with their correct prices, and determining how many errors occurred during the sales. We are given:
- A list of products,
- Their correct prices, 
- A list of products sold,
- The prices at which they were sold.

We need to count how many times a product was sold at the wrong price.

### Problem Breakdown:
1. **Input**:
   - `products`: A list of strings representing product names.
   - `productPrices`: A list of corresponding prices for the products in `products`.
   - `productSold`: A list of strings representing the products that were sold.
   - `soldPrices`: A list of prices at which each product was sold.

2. **Output**:
   - Return the number of errors where a product was sold at an incorrect price.

3. **Approach**:
   - First, we need to map each product to its correct price using a hash map (unordered_map in C++).
   - Then, for each product sold, compare its sold price with the correct price from the map.
   - Count the number of times there is a mismatch in the price.

### Solution in C++:

```cpp
#include <iostream>
#include <vector>
#include <unordered_map>
using namespace std;

int priceCheck(vector<string>& products, vector<float>& productPrices, vector<string>& productSold, vector<float>& soldPrices) {
    // Create a map to store the correct price for each product
    unordered_map<string, float> priceMap;
    for (int i = 0; i < products.size(); i++) {
        priceMap[products[i]] = productPrices[i];
    }

    int errorCount = 0;
    // Compare the sold prices with the correct prices
    for (int i = 0; i < productSold.size(); i++) {
        string soldProduct = productSold[i];
        float correctPrice = priceMap[soldProduct];
        if (soldPrices[i] != correctPrice) {
            errorCount++;  // Count an error if prices do not match
        }
    }

    return errorCount;  // Return the total number of pricing errors
}

int main() {
    // Example data
    vector<string> products = {"eggs", "milk", "cheese"};
    vector<float> productPrices = {2.99, 2.50, 5.99};
    vector<string> productSold = {"eggs", "eggs", "cheese", "milk"};
    vector<float> soldPrices = {2.99, 2.50, 3.29, 2.50};

    // Call the function to count pricing errors
    int errors = priceCheck(products, productPrices, productSold, soldPrices);
    
    // Output the number of errors
    cout << "Number of pricing errors: " << errors << endl;

    return 0;
}
```

### Explanation:
1. **Mapping products to prices**:
   - We create an `unordered_map` (`priceMap`) that maps each product to its correct price.
   
2. **Comparing sold prices**:
   - For each product in the `productSold` list, we check if the price at which it was sold matches the correct price from the `priceMap`.
   - If there is a mismatch, we increment the `errorCount`.

3. **Output**:
   - After iterating through all the sold products, we return the `errorCount`, which represents how many products were sold at the wrong price.

### Example:

#### Input:
```cpp
products = {"eggs", "milk", "cheese"}
productPrices = {2.99, 2.50, 5.99}
productSold = {"eggs", "eggs", "cheese", "milk"}
soldPrices = {2.99, 2.50, 3.29, 2.50}
```

#### Execution:
- The first and second sales of "eggs" are correct.
- The sale of "cheese" has an incorrect price (expected 5.99 but sold for 3.29).
- The sale of "milk" is correct.

#### Output:
```
Number of pricing errors: 1
```

### Time Complexity:
- **O(n + m)**, where `n` is the size of the `products` list and `m` is the size of the `productSold` list. We traverse both lists once to create the map and compare prices.

### Space Complexity:
- **O(n)**, where `n` is the size of the `products` list, due to the space needed for the map.

This solution efficiently counts pricing errors while maintaining clarity and simplicity.


1. Question 1
When multiple tasks are esecuted on a single threaded CPU, the tasks are scheduled based on the principle of pre- emption. When a higher-priority task arrives in the execution queue, then the lower priority task is pre-empted, Le. its execution is paused until the higher-priority task is complete.
There are n functions to be executed on a single-threaded CPU, with each function having a unique ID between 0 and n-1. Given an integer n, representing the number of functions to be executed, and an execution log as an array of strings, logs, of size m determine the exclusive times of each of the functions. Exclusive time is the sum of execution times for all calls to a

```cpp
#include <iostream>
#include <vector>
#include <stack>
#include <string>
#include <sstream>

using namespace std;

vector<int> exclusiveTime(int n, vector<string>& logs) {
    vector<int> result(n, 0);  // Array to store the exclusive time of each function
    stack<int> stk;  // Stack to store the function ids
    int previousTime = 0;  // Variable to store the time of the previous log entry

    for (const string& log : logs) {
        // Split the log into components
        stringstream ss(log);
        string id_str, type, time_str;
        getline(ss, id_str, ':');
        getline(ss, type, ':');
        getline(ss, time_str, ':');
        
        int id = stoi(id_str);
        int time = stoi(time_str);

        if (!stk.empty()) {
            result[stk.top()] += time - previousTime;
        }

        previousTime = time;

        if (type == "start") {
            stk.push(id);  // Push the function id onto the stack
        } else {  // If it's "end"
            result[stk.top()]++;  // Increase time for the current function
            stk.pop();  // Pop the current function
            previousTime++;
        }
    }

    return result;
}

int main() {
    // Example input
    int n = 2;
    vector<string> logs = {
        "0:start:0", "1:start:2", "1:end:5", "0:end:6"
    };
    
    // Call the function
    vector<int> result = exclusiveTime(n, logs);
    
    // Output the result
    for (int time : result) {
        cout << time << " ";
    }
    cout << endl;

    return 0;
}

```

1. Question 1
Prisoners are standing on a Cartesian condute system present ideja with both the coordrates (xy) beng megers. Each prsoner should be at with 3 other prisoners
More formally, every prisoner at a coordinates prxshould have
at least one prisoner standing at veneer oordrates at kast one prhionee standing toutes are ayy
Unfortunately, one prisoner has escaped. Find the coordinates of that p
Example
cations[1, 13

```cpp
#include <iostream>
#include <unordered_set>
#include <vector>

using namespace std;

typedef pair<int, int> pii;

// Helper function to check if a position exists in the set
bool exists(unordered_set<pii>& positionsSet, int x, int y) {
    return positionsSet.find(make_pair(x, y)) != positionsSet.end();
}

vector<int> findMissingPrisoner(vector<vector<int>>& positions) {
    unordered_set<pii> positionsSet;
    
    // Insert all given positions into the set
    for (auto& pos : positions) {
        positionsSet.insert(make_pair(pos[0], pos[1]));
    }
    
    // Check for the missing coordinate
    for (auto& pos : positions) {
        int x = pos[0];
        int y = pos[1];
        
        // Check all 4 possible neighbors (left, right, above, below)
        if (!exists(positionsSet, x - 1, y) ||
            !exists(positionsSet, x + 1, y) ||
            !exists(positionsSet, x, y - 1) ||
            !exists(positionsSet, x, y + 1)) {
            return {x, y};  // Return the missing prisoner coordinates
        }
    }

    return {};  // No missing prisoner found (fallback)
}

int main() {
    // Example input
    vector<vector<int>> positions = {{1, 1}, {1, 2}, {2, 1}};
    
    // Call the function to find the missing prisoner
    vector<int> result = findMissingPrisoner(positions);
    
    // Output the result
    if (!result.empty()) {
        cout << "[" << result[0] << ", " << result[1] << "]" << endl;
    } else {
        cout << "No missing prisoner found." << endl;
    }

    return 0;
}


```

1. Question 1
metaddresses which and then used by Impwsers to load tentures For quicker DNS lookups, browsers often stone a number of Fecere DNSi queries in a DNS cache. Retrieving data from the cache is offen faster than retrieving it from a DNS server. This task aims to simulate DINS resolution and determine the time taken to process zifferent URL
Assume that the DNS cache can store a maximare of the cache size most recent DNS requests, Le. URL-IP mappings. The cache is initially empty. It takes cache time units of time to fetch data from the DNS cache, and server time units of time to fetch data from the DNS server.
Given a list of in URLs visited as an array of strings, urls, determine the minimum time taken to resolve each DNS request.

```cpp
#include <iostream>
#include <unordered_set>
#include <list>
#include <vector>
#include <string>

using namespace std;

int resolveDNS(vector<string>& urls, int cacheSize, int cacheTime, int serverTime) {
    // LRU cache: List to store URLs in the order of their usage
    list<string> cache;
    // Set to check if a URL is in the cache
    unordered_set<string> cacheSet;
    
    int totalTime = 0;
    
    for (string& url : urls) {
        // If URL is in the cache
        if (cacheSet.find(url) != cacheSet.end()) {
            totalTime += cacheTime;
            
            // Move the URL to the most recent position in the cache
            cache.remove(url);
            cache.push_back(url);
        } else {
            // If URL is not in the cache
            totalTime += serverTime;
            
            // If the cache is full, remove the least recently used (LRU) item
            if (cache.size() == cacheSize && cacheSize > 0) {
                string leastUsed = cache.front();
                cache.pop_front();
                cacheSet.erase(leastUsed);
            }
            
            // Add the new URL to the cache
            if (cacheSize > 0) {
                cache.push_back(url);
                cacheSet.insert(url);
            }
        }
    }
    
    return totalTime;
}

int main() {
    // Example input
    vector<string> urls = {"google.com", "facebook.com", "google.com", "youtube.com", "facebook.com"};
    int cacheSize = 2;    // Maximum number of URLs that can be stored in the cache
    int cacheTime = 2;    // Time taken to fetch a URL from the cache
    int serverTime = 5;   // Time taken to fetch a URL from the server
    
    // Call the DNS resolver function
    int result = resolveDNS(urls, cacheSize, cacheTime, serverTime);
    
    // Output the result
    cout << "Total time taken to resolve DNS requests: " << result << " units" << endl;

    return 0;
}

```

1. Tracks in Hackathon
there is a hackathors organized by HackerRank which has 2 separate tracks, healthcare and e ce for track 1, the required team sur is mamdice & while for tack 2, the required tram size is amice 2. The socal number of participants
D
Find the minimum number of teatis into which the participants can be divided such that each patzipant belongs to exactly one team esther of track 1 or track 21, and each tam has a size equal to either teamSure, for teamsine 2 If no such division Is posadile, remum-1
Example
Comoder seamSor 1-2 mame 2-4 and numtier of participants-2
Ogitimullly there is 1 team of 3 and 1 traim of 4. The number of teams is 2.
Function Description
Complete the function the

```cpp
#include <iostream>
#include <algorithm>
using namespace std;

int minTeams(int n, int teamSize1, int teamSize2) {
    int minTeams = INT_MAX;  // Initialize with a large number
    bool possible = false;
    
    // Try to form teams with teamSize1 first and then see if the rest can be divided by teamSize2
    for (int x = 0; x * teamSize1 <= n; x++) {
        int remaining = n - x * teamSize1;
        // Check if remaining participants can be divided into teams of size teamSize2
        if (remaining % teamSize2 == 0) {
            int y = remaining / teamSize2;
            minTeams = min(minTeams, x + y);
            possible = true;
        }
    }

    // If a valid division was found, return the minimum number of teams
    if (possible) {
        return minTeams;
    }

    // If no valid division was found, return -1
    return -1;
}

int main() {
    int n = 10;        // Total number of participants
    int teamSize1 = 3; // Team size for track 1
    int teamSize2 = 4; // Team size for track 2

    int result = minTeams(n, teamSize1, teamSize2);
    
    if (result != -1) {
        cout << "Minimum number of teams: " << result << endl;
    } else {
        cout << "No valid division possible" << endl;
    }

    return 0;
}

```

There are n friends standing in a line, each numbered from I through ninclusive. The first one, friend 1, holds a baton. Each second, the baton is passed to the next friend in line. Once it reaches the end of the line, the direction of passing is reversed and passing continues. Determine who will pass and who will receive the baton at a given time.
Example
friends = 4
time -5
Friends are numbered 1 through 4. Friend 1 holds the baton at time 0. At time 7, it is passed to friend 2. Over 5 seconds, the baton is passed as 1-2-3-4>3>2. The friend passing the baton at time 5 is friend 3. The friend receiving the baton is friend 2. Return (3 21.
Function Description
Complete the function batonPass in the editor below. The function must return an integer array.
batonPlass has the following parameters:
int friends the number of friends
int time the time to report who on the batt
Returns
int[2] the friend who has the baton (index (0) and the friend who receives the baton (index 1)
Constraints
2x friends 2x10
Titimes1017
```cpp
#include <iostream>
#include <vector>
using namespace std;

vector<int> batonPass(int friends, int time) {
    // Calculate the length of one complete cycle (forward and backward)
    int cycleLength = 2 * (friends - 1);
    
    // Find the position in the current cycle
    int currentTime = time % cycleLength;
    
    // Determine whether the baton is moving forward or backward
    if (currentTime < friends - 1) {
        // Moving forward (1 -> 2 -> ... -> n)
        int passer = currentTime + 1;
        int receiver = passer + 1;
        return {passer, receiver};
    } else {
        // Moving backward (n -> n-1 -> ... -> 1)
        int passer = friends - (currentTime - (friends - 1));
        int receiver = passer - 1;
        return {passer, receiver};
    }
}

int main() {
    int friends = 4;
    int time = 5;
    
    vector<int> result = batonPass(friends, time);
    
    cout << "Friend passing the baton: " << result[0] << endl;
    cout << "Friend receiving the baton: " << result[1] << endl;
    
    return 0;
}

```
Given three integers, and a sequence sum to be the value of 110-20-0-3) (increment from/until it equals then decrement from/until it equals Given values and &, calculate the sequence sum as described
Example
1-5
k=6
Sum all the values from ito/and back to k: 5+6+ 7+8+9+8+7-6-56
Function Description
Complete the function get.SequenceSum in the editor below.
getSequenceSum has the following parameter(s): int int int k three integers
Return
long the value of the sequence sum
```cpp
#include <iostream>
using namespace std;

long getSequenceSum(int a, int b, int k) {
    long sum = 0;
    
    // Step 1: Sum from a to b
    for (int i = a; i <= b; i++) {
        sum += i;
    }
    
    // Step 2: Sum from b-1 back to k
    for (int i = b - 1; i >= k; i--) {
        sum += i;
    }
    
    return sum;
}

int main() {
    int a = 5;
    int b = 9;
    int k = 6;
    
    long result = getSequenceSum(a, b, k);
    cout << "Sequence sum: " << result << endl;
    
    return 0;
}

```

2. String Replacement
Two strings are given, worf and substr. Some of the characters in word are a question mark (7) Find the lexicographically smallest string that can be obtained by replacing 7 characters such thue subser appears at least once, if it is not possible to do so, return-1"
Note:
A substring is a contiguous sequence of characters within a string For example, "bed in a substring of abcde but ac is not
For two strings a and b of the same length, ass lexicographically smaller than bif abyfor some 0xfat and by for all
Example
word "as/ble substyb
Replace the 3 and 5th characters with th' and 'k' to get landbke which has subsarasa substring Replace the remaining 7 with a. The final string is Sandbag
```cpp
#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

string stringReplacement(string word, string substr) {
    int wordLen = word.length();
    int subLen = substr.length();
    string result = "";

    // Try to place the substring at each valid position in 'word'
    for (int i = 0; i <= wordLen - subLen; i++) {
        string temp = word; // Create a copy to try replacing

        // Check if we can replace the current window with 'substr'
        bool canReplace = true;
        for (int j = 0; j < subLen; j++) {
            if (temp[i + j] != '?' && temp[i + j] != substr[j]) {
                canReplace = false;
                break;
            }
        }

        if (canReplace) {
            // Replace the current window with 'substr'
            for (int j = 0; j < subLen; j++) {
                temp[i + j] = substr[j];
            }

            // Replace remaining '?' with 'a' to form lexicographically smallest string
            for (int k = 0; k < wordLen; k++) {
                if (temp[k] == '?') {
                    temp[k] = 'a';
                }
            }

            // Track the lexicographically smallest result
            if (result == "" || temp < result) {
                result = temp;
            }
        }
    }

    // If no valid replacement was found, return -1
    return result == "" ? "-1" : result;
}

int main() {
    string word = "a?b?le";
    string substr = "abk";
    
    string result = stringReplacement(word, substr);
    
    cout << "Result: " << result << endl;

    return 0;
}

```

