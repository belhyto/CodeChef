Linked List

Insert

#include <iostream>
using namespace std;

struct Node {
    int data;
    Node* next;
};

// Function to insert at the beginning
void insertAtBeginning(Node** head_ref, int new_data) {
    Node* new_node = new Node(); // Allocate memory for new node
    new_node->data = new_data;   // Assign data to new node
    new_node->next = (*head_ref); // Make next of new node as head
    (*head_ref) = new_node;      // Move the head to point to the new node
}

// Function to print the linked list
void printList(Node* node) {
    while (node != nullptr) {
        cout << node->data << " ";
        node = node->next;
    }
    cout << endl;
}

int main() {
    Node* head = nullptr;

    insertAtBeginning(&head, 1);
    insertAtBeginning(&head, 2);
    insertAtBeginning(&head, 3);

    cout << "Linked list after insertion at the beginning: ";
    printList(head);

    return 0;
}

Delete

#include <iostream>
using namespace std;

// Define the structure for the linked list node
struct Node {
    int data;
    Node* next;
};

// Function to delete the head node
void deleteHead(Node** head_ref) {
    // If the linked list is empty, there's nothing to delete
    if (*head_ref == nullptr) {
        cout << "The list is empty, nothing to delete." << endl;
        return;
    }

    // Store the current head node
    Node* temp = *head_ref;

    // Move the head pointer to the next node
    *head_ref = temp->next;

    // Free the memory of the old head node
    delete temp;
}

// Function to add a new node at the end of the linked list
void append(Node** head_ref, int new_data) {
    Node* new_node = new Node();
    Node* last = *head_ref;

    new_node->data = new_data;
    new_node->next = nullptr;

    // If the linked list is empty, make the new node the head
    if (*head_ref == nullptr) {
        *head_ref = new_node;
        return;
    }

    // Traverse to the last node
    while (last->next != nullptr) {
        last = last->next;
    }

    // Insert the new node at the end
    last->next = new_node;
}

// Function to print the linked list
void printList(Node* node) {
    while (node != nullptr) {
        cout << node->data << " ";
        node = node->next;
    }
    cout << endl;
}

// Main function to demonstrate deleting the head node
int main() {
    Node* head = nullptr;

    // Creating the linked list 1 -> 2 -> 3 -> 4 -> 5
    append(&head, 1);
    append(&head, 2);
    append(&head, 3);
    append(&head, 4);
    append(&head, 5);

    cout << "Original Linked List: ";
    printList(head);

    // Delete the head node
    deleteHead(&head);

    cout << "Linked List after deleting the head node: ";
    printList(head);

    return 0;
}

Here are some important DSA (Data Structures and Algorithms) questions on linked lists that are commonly asked in coding interviews, including for companies like IBM. I've provided solutions and explanations to help you understand the concepts.

### 1. **Reverse a Linked List**
   - **Problem**: Given the head of a singly linked list, reverse the list and return the reversed list's head.
   - **Example**:
     ```cpp
     Input: 1 -> 2 -> 3 -> 4 -> 5 -> nullptr
     Output: 5 -> 4 -> 3 -> 2 -> 1 -> nullptr
     ```
   - **Solution**:
     ```cpp
     Node* reverseList(Node* head) {
         Node* prev = nullptr;
         Node* current = head;
         Node* next = nullptr;

         while (current != nullptr) {
             next = current->next;
             current->next = prev;
             prev = current;
             current = next;
         }

         return prev;
     }
     ```

### 2. **Detect a Cycle in a Linked List**
   - **Problem**: Given the head of a linked list, determine if the linked list has a cycle in it.
   - **Example**:
     ```cpp
     Input: 3 -> 2 -> 0 -> -4 -> 2 (cycle)
     Output: true
     ```
   - **Solution**:
     ```cpp
     bool hasCycle(Node* head) {
         Node* slow = head;
         Node* fast = head;

         while (fast != nullptr && fast->next != nullptr) {
             slow = slow->next;
             fast = fast->next->next;
             if (slow == fast) {
                 return true;
             }
         }

         return false;
     }
     ```

### 3. **Merge Two Sorted Linked Lists**
   - **Problem**: Merge two sorted linked lists and return it as a new sorted list. The new list should be made by splicing together the nodes of the first two lists.
   - **Example**:
     ```cpp
     Input: 1 -> 2 -> 4, 1 -> 3 -> 4
     Output: 1 -> 1 -> 2 -> 3 -> 4 -> 4
     ```
   - **Solution**:
     ```cpp
     Node* mergeTwoLists(Node* l1, Node* l2) {
         if (!l1) return l2;
         if (!l2) return l1;

         if (l1->data < l2->data) {
             l1->next = mergeTwoLists(l1->next, l2);
             return l1;
         } else {
             l2->next = mergeTwoLists(l1, l2->next);
             return l2;
         }
     }
     ```

### 4. **Remove Nth Node from End of List**
   - **Problem**: Given the head of a linked list, remove the nth node from the end of the list and return its head.
   - **Example**:
     ```cpp
     Input: 1 -> 2 -> 3 -> 4 -> 5, n = 2
     Output: 1 -> 2 -> 3 -> 5
     ```
   - **Solution**:
     ```cpp
     Node* removeNthFromEnd(Node* head, int n) {
         Node* dummy = new Node(0);
         dummy->next = head;
         Node* fast = dummy;
         Node* slow = dummy;

         for (int i = 1; i <= n + 1; i++) {
             fast = fast->next;
         }

         while (fast != nullptr) {
             slow = slow->next;
             fast = fast->next;
         }

         slow->next = slow->next->next;
         return dummy->next;
     }
     ```

### 5. **Find the Intersection of Two Linked Lists**
   - **Problem**: Given the heads of two singly linked lists, return the node at which the two lists intersect. If the two linked lists have no intersection, return `nullptr`.
   - **Example**:
     ```cpp
     Input: List A: 1 -> 9 -> 1 -> 2 -> 4
            List B: 3 -> 2 -> 4
            Intersection at node with value 2.
     Output: Node with value 2
     ```
   - **Solution**:
     ```cpp
     Node* getIntersectionNode(Node* headA, Node* headB) {
         Node* a = headA;
         Node* b = headB;

         while (a != b) {
             a = a ? a->next : headB;
             b = b ? b->next : headA;
         }

         return a;
     }
     ```

### 6. **Palindrome Linked List**
   - **Problem**: Given the head of a singly linked list, return true if it is a palindrome.
   - **Example**:
     ```cpp
     Input: 1 -> 2 -> 2 -> 1
     Output: true
     ```
   - **Solution**:
     ```cpp
     bool isPalindrome(Node* head) {
         if (!head) return true;

         Node* slow = head;
         Node* fast = head;
         Node* prev = nullptr;

         while (fast && fast->next) {
             fast = fast->next->next;
             Node* temp = slow->next;
             slow->next = prev;
             prev = slow;
             slow = temp;
         }

         if (fast) slow = slow->next;

         while (slow) {
             if (slow->data != prev->data) return false;
             slow = slow->next;
             prev = prev->next;
         }

         return true;
     }
     ```

### 7. **Remove Duplicates from Sorted Linked List**
   - **Problem**: Given the head of a sorted linked list, delete all duplicates such that each element appears only once.
   - **Example**:
     ```cpp
     Input: 1 -> 1 -> 2 -> 3 -> 3
     Output: 1 -> 2 -> 3
     ```
   - **Solution**:
     ```cpp
     Node* deleteDuplicates(Node* head) {
         Node* current = head;

         while (current && current->next) {
             if (current->data == current->next->data) {
                 Node* temp = current->next;
                 current->next = current->next->next;
                 delete temp;
             } else {
                 current = current->next;
             }
         }

         return head;
     }
     ```

### 8. **Rotate Linked List**
   - **Problem**: Given the head of a linked list, rotate the list to the right by `k` places.
   - **Example**:
     ```cpp
     Input: 1 -> 2 -> 3 -> 4 -> 5, k = 2
     Output: 4 -> 5 -> 1 -> 2 -> 3
     ```
   - **Solution**:
     ```cpp
     Node* rotateRight(Node* head, int k) {
         if (!head || !head->next) return head;

         int length = 1;
         Node* tail = head;
         while (tail->next) {
             tail = tail->next;
             length++;
         }

         tail->next = head;
         k = k % length;
         k = length - k;

         while (k--) {
             tail = tail->next;
         }

         head = tail->next;
         tail->next = nullptr;

         return head;
     }
     ```

### 9. **Flatten a Multilevel Doubly Linked List**
   - **Problem**: Given a doubly linked list where in addition to the next and previous pointers, each node has a child pointer, flatten the list.
   - **Example**:
     ```cpp
     Input: 1 - 2 - 3
             |   
             4 - 5
     Output: 1 -> 4 -> 5 -> 2 -> 3
     ```
   - **Solution**:
     ```cpp
     Node* flatten(Node* head) {
         if (!head) return head;

         Node* curr = head;
         while (curr) {
             if (curr->child) {
                 Node* next = curr->next;
                 Node* child = flatten(curr->child);

                 curr->next = child;
                 child->prev = curr;
                 curr->child = nullptr;

                 while (curr->next) curr = curr->next;

                 curr->next = next;
                 if (next) next->prev = curr;
             }

             curr = curr->next;
         }

         return head;
     }
     ```

### 10. **Add Two Numbers Represented by Linked Lists**
   - **Problem**: Given two non-empty linked lists representing two non-negative integers, add the two numbers and return it as a linked list.
   - **Example**:
     ```cpp
     Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
     Output: 7 -> 0 -> 8
     ```
   - **Solution**:
     ```cpp
     Node* addTwoNumbers(Node* l1, Node* l2) {
         Node* dummy = new Node(0);
         Node* p = l1;
         Node* q = l2;
         Node* curr = dummy;
         int carry = 0;

         while (p || q) {
             int x = (p != nullptr) ? p

->data : 0;
             int y = (q != nullptr) ? q->data : 0;
             int sum = carry + x + y;

             carry = sum / 10;
             curr->next = new Node(sum % 10);
             curr = curr->next;

             if (p) p = p->next;
             if (q) q = q->next;
         }

         if (carry > 0) {
             curr->next = new Node(carry);
         }

         return dummy->next;
     }
     ```

These questions cover a wide range of concepts related to linked lists, including reversing, detecting cycles, merging, and other common operations. Practicing these problems will help you prepare for coding interviews at IBM and similar companies.




ARRAYS

Here are some DSA (Data Structures and Algorithms) questions on arrays that are commonly asked in coding interviews, including for companies like IBM. I've included answers and explanations to help you understand the concepts.

### 1. **Find the Maximum Subarray Sum (Kadane’s Algorithm)**
   - **Problem**: Given an array of integers, find the contiguous subarray which has the largest sum.
   - **Example**:
     ```cpp
     Input: arr = [-2,1,-3,4,-1,2,1,-5,4]
     Output: 6
     Explanation: The subarray [4,-1,2,1] has the largest sum = 6.
     ```
   - **Solution**:
     ```cpp
     int maxSubArraySum(vector<int>& arr) {
         int max_sum = arr[0];
         int current_sum = arr[0];

         for (int i = 1; i < arr.size(); i++) {
             current_sum = max(arr[i], current_sum + arr[i]);
             max_sum = max(max_sum, current_sum);
         }

         return max_sum;
     }
     ```

### 2. **Two Sum Problem**
   - **Problem**: Given an array of integers, return the indices of the two numbers such that they add up to a specific target.
   - **Example**:
     ```cpp
     Input: arr = [2, 7, 11, 15], target = 9
     Output: [0, 1]
     Explanation: Because arr[0] + arr[1] = 2 + 7 = 9.
     ```
   - **Solution**:
     ```cpp
     vector<int> twoSum(vector<int>& nums, int target) {
         unordered_map<int, int> mp;
         for (int i = 0; i < nums.size(); i++) {
             int complement = target - nums[i];
             if (mp.find(complement) != mp.end()) {
                 return {mp[complement], i};
             }
             mp[nums[i]] = i;
         }
         return {};
     }
     ```

### 3. **Move Zeros to End**
   - **Problem**: Move all zeroes in an array to the end while maintaining the relative order of the non-zero elements.
   - **Example**:
     ```cpp
     Input: arr = [0,1,0,3,12]
     Output: [1,3,12,0,0]
     ```
   - **Solution**:
     ```cpp
     void moveZeroes(vector<int>& nums) {
         int nonZeroPos = 0;
         for (int i = 0; i < nums.size(); i++) {
             if (nums[i] != 0) {
                 swap(nums[i], nums[nonZeroPos]);
                 nonZeroPos++;
             }
         }
     }
     ```

### 4. **Find the Missing Number**
   - **Problem**: Given an array containing `n` distinct numbers taken from `0, 1, 2, ..., n`, find the one that is missing from the array.
   - **Example**:
     ```cpp
     Input: arr = [3,0,1]
     Output: 2
     Explanation: n = 3, so the numbers are [0,1,2,3], and 2 is missing.
     ```
   - **Solution**:
     ```cpp
     int missingNumber(vector<int>& nums) {
         int n = nums.size();
         int sum = (n * (n + 1)) / 2;
         for (int num : nums) {
             sum -= num;
         }
         return sum;
     }
     ```

### 5. **Find the Duplicate Number**
   - **Problem**: Given an array of `n+1` integers where each integer is between `1` and `n` (inclusive), find the duplicate number.
   - **Example**:
     ```cpp
     Input: arr = [1,3,4,2,2]
     Output: 2
     ```
   - **Solution**:
     ```cpp
     int findDuplicate(vector<int>& nums) {
         int slow = nums[0];
         int fast = nums[0];

         do {
             slow = nums[slow];
             fast = nums[nums[fast]];
         } while (slow != fast);

         fast = nums[0];
         while (slow != fast) {
             slow = nums[slow];
             fast = nums[fast];
         }

         return slow;
     }
     ```

### 6. **Merge Intervals**
   - **Problem**: Given a collection of intervals, merge all overlapping intervals.
   - **Example**:
     ```cpp
     Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
     Output: [[1,6],[8,10],[15,18]]
     ```
   - **Solution**:
     ```cpp
     vector<vector<int>> merge(vector<vector<int>>& intervals) {
         if (intervals.empty()) return {};

         sort(intervals.begin(), intervals.end());
         vector<vector<int>> merged;

         merged.push_back(intervals[0]);
         for (int i = 1; i < intervals.size(); i++) {
             if (merged.back()[1] >= intervals[i][0]) {
                 merged.back()[1] = max(merged.back()[1], intervals[i][1]);
             } else {
                 merged.push_back(intervals[i]);
             }
         }

         return merged;
     }
     ```

### 7. **Best Time to Buy and Sell Stock**
   - **Problem**: Given an array `prices` where `prices[i]` is the price of a given stock on the `i`th day, find the maximum profit you can achieve by buying and then selling one share of the stock.
   - **Example**:
     ```cpp
     Input: prices = [7,1,5,3,6,4]
     Output: 5
     Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
     ```
   - **Solution**:
     ```cpp
     int maxProfit(vector<int>& prices) {
         int min_price = INT_MAX;
         int max_profit = 0;

         for (int price : prices) {
             min_price = min(min_price, price);
             max_profit = max(max_profit, price - min_price);
         }

         return max_profit;
     }
     ```

### 8. **Rotate Array**
   - **Problem**: Rotate an array to the right by `k` steps, where `k` is non-negative.
   - **Example**:
     ```cpp
     Input: nums = [1,2,3,4,5,6,7], k = 3
     Output: [5,6,7,1,2,3,4]
     ```
   - **Solution**:
     ```cpp
     void rotate(vector<int>& nums, int k) {
         k = k % nums.size();
         reverse(nums.begin(), nums.end());
         reverse(nums.begin(), nums.begin() + k);
         reverse(nums.begin() + k, nums.end());
     }
     ```

### 9. **Find the Intersection of Two Arrays**
   - **Problem**: Given two arrays, find their intersection.
   - **Example**:
     ```cpp
     Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
     Output: [4,9]
     ```
   - **Solution**:
     ```cpp
     vector<int> intersection(vector<int>& nums1, vector<int>& nums2) {
         unordered_set<int> set(nums1.begin(), nums1.end());
         vector<int> result;
         
         for (int num : nums2) {
             if (set.erase(num)) {
                 result.push_back(num);
             }
         }
         
         return result;
     }
     ```

### 10. **Find the Majority Element**
   - **Problem**: Given an array of size `n`, find the majority element. The majority element is the element that appears more than `n/2` times.
   - **Example**:
     ```cpp
     Input: nums = [2,2,1,1,1,2,2]
     Output: 2
     ```
   - **Solution**:
     ```cpp
     int majorityElement(vector<int>& nums) {
         int count = 0;
         int candidate = 0;

         for (int num : nums) {
             if (count == 0) {
                 candidate = num;
             }
             count += (num == candidate) ? 1 : -1;
         }

         return candidate;
     }
     ```

These questions cover a variety of concepts related to arrays, such as searching, sorting, manipulation, and optimization techniques. Practicing these problems will help you prepare for coding interviews at IBM and similar companies.

Here are some essential DSA questions and answers focused on hashmaps, which are frequently asked in coding interviews, including at IBM. These questions will help you strengthen your understanding and application of hashmaps in solving various problems.

### 1. **Two Sum Problem**
   - **Problem**: Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to `target`.
   - **Example**:
     ```cpp
     Input: nums = [2, 7, 11, 15], target = 9
     Output: [0, 1]
     ```
   - **Solution**:
     ```cpp
     vector<int> twoSum(vector<int>& nums, int target) {
         unordered_map<int, int> map;
         for (int i = 0; i < nums.size(); i++) {
             int complement = target - nums[i];
             if (map.find(complement) != map.end()) {
                 return {map[complement], i};
             }
             map[nums[i]] = i;
         }
         return {};
     }
     ```

### 2. **Subarray Sum Equals K**
   - **Problem**: Given an array of integers `nums` and an integer `k`, find the total number of continuous subarrays whose sum equals `k`.
   - **Example**:
     ```cpp
     Input: nums = [1, 1, 1], k = 2
     Output: 2
     ```
   - **Solution**:
     ```cpp
     int subarraySum(vector<int>& nums, int k) {
         unordered_map<int, int> map;
         map[0] = 1;
         int count = 0, sum = 0;

         for (int num : nums) {
             sum += num;
             if (map.find(sum - k) != map.end()) {
                 count += map[sum - k];
             }
             map[sum]++;
         }

         return count;
     }
     ```

### 3. **Longest Consecutive Sequence**
   - **Problem**: Given an unsorted array of integers `nums`, return the length of the longest consecutive elements sequence.
   - **Example**:
     ```cpp
     Input: nums = [100, 4, 200, 1, 3, 2]
     Output: 4 (because the longest sequence is [1, 2, 3, 4])
     ```
   - **Solution**:
     ```cpp
     int longestConsecutive(vector<int>& nums) {
         unordered_set<int> numSet(nums.begin(), nums.end());
         int longestStreak = 0;

         for (int num : nums) {
             if (!numSet.count(num - 1)) {
                 int currentNum = num;
                 int currentStreak = 1;

                 while (numSet.count(currentNum + 1)) {
                     currentNum += 1;
                     currentStreak += 1;
                 }

                 longestStreak = max(longestStreak, currentStreak);
             }
         }

         return longestStreak;
     }
     ```

### 4. **Group Anagrams**
   - **Problem**: Given an array of strings, group anagrams together.
   - **Example**:
     ```cpp
     Input: strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
     Output: [["eat","tea","ate"],["tan","nat"],["bat"]]
     ```
   - **Solution**:
     ```cpp
     vector<vector<string>> groupAnagrams(vector<string>& strs) {
         unordered_map<string, vector<string>> map;
         for (string s : strs) {
             string key = s;
             sort(key.begin(), key.end());
             map[key].push_back(s);
         }

         vector<vector<string>> anagrams;
         for (auto& pair : map) {
             anagrams.push_back(pair.second);
         }

         return anagrams;
     }
     ```
     Full code

```cpp
#include <iostream>
#include <vector>
#include <unordered_map>
#include <algorithm>

using namespace std;

vector<vector<string>> groupAnagrams(vector<string>& strs) {
    unordered_map<string, vector<string>> map;
    
    // Step 1: Group words by their sorted version
    for (string s : strs) {
        string key = s;
        sort(key.begin(), key.end());  // Sort the string to create the key
        map[key].push_back(s);         // Group anagrams together
    }
    
    // Step 2: Prepare the result vector
    vector<vector<string>> anagrams;
    for (auto& pair : map) {
        anagrams.push_back(pair.second);  // Collect all anagram groups
    }
    
    return anagrams;  // Return the final grouped anagrams
}

int main() {
    // Test input
    vector<string> strs = {"eat", "tea", "tan", "ate", "nat", "bat"};
    
    // Group anagrams
    vector<vector<string>> result = groupAnagrams(strs);
    
    // Print the result
    for (const auto& group : result) {
        cout << "[";
        for (const auto& word : group) {
            cout << word << " ";
        }
        cout << "]\n";
    }
    
    return 0;
}

```
### 5. **Find All Duplicates in an Array**
   - **Problem**: Given an integer array `nums` of length `n` where all the integers of nums are in the range `[1, n]` and some elements appear twice while others appear once, return an array of all the integers that appear twice.
   - **Example**:
     ```cpp
     Input: nums = [4,3,2,7,8,2,3,1]
     Output: [2,3]
     ```
   - **Solution**:
     ```cpp
     vector<int> findDuplicates(vector<int>& nums) {
         unordered_map<int, int> map;
         vector<int> result;

         for (int num : nums) {
             map[num]++;
         }

         for (auto& pair : map) {
             if (pair.second == 2) {
                 result.push_back(pair.first);
             }
         }

         return result;
     }
     ```

### 6. **Top K Frequent Elements**
   - **Problem**: Given a non-empty array of integers, return the `k` most frequent elements.
   - **Example**:
     ```cpp
     Input: nums = [1,1,1,2,2,3], k = 2
     Output: [1, 2]
     ```
   - **Solution**:
     ```cpp
     vector<int> topKFrequent(vector<int>& nums, int k) {
         unordered_map<int, int> map;
         for (int num : nums) {
             map[num]++;
         }

         priority_queue<pair<int, int>> pq;
         for (auto& pair : map) {
             pq.push({pair.second, pair.first});
         }

         vector<int> result;
         for (int i = 0; i < k; i++) {
             result.push_back(pq.top().second);
             pq.pop();
         }

         return result;
     }
     ```

### 7. **Intersection of Two Arrays**
   - **Problem**: Given two arrays, return their intersection. Each element in the result must be unique.
   - **Example**:
     ```cpp
     Input: nums1 = [1,2,2,1], nums2 = [2,2]
     Output: [2]
     ```
   - **Solution**:
     ```cpp
     vector<int> intersection(vector<int>& nums1, vector<int>& nums2) {
         unordered_set<int> set1(nums1.begin(), nums1.end());
         unordered_set<int> resultSet;

         for (int num : nums2) {
             if (set1.count(num)) {
                 resultSet.insert(num);
             }
         }

         return vector<int>(resultSet.begin(), resultSet.end());
     }
     ```

### 8. **Longest Substring Without Repeating Characters**
   - **Problem**: Given a string, find the length of the longest substring without repeating characters.
   - **Example**:
     ```cpp
     Input: s = "abcabcbb"
     Output: 3 ("abc")
     ```
   - **Solution**:
     ```cpp
     int lengthOfLongestSubstring(string s) {
         unordered_map<char, int> map;
         int maxLength = 0, start = 0;

         for (int end = 0; end < s.size(); end++) {
             if (map.find(s[end]) != map.end()) {
                 start = max(map[s[end]] + 1, start);
             }
             map[s[end]] = end;
             maxLength = max(maxLength, end - start + 1);
         }

         return maxLength;
     }
     ```

### 9. **Ransom Note**
   - **Problem**: Given two strings `ransomNote` and `magazine`, return `true` if `ransomNote` can be constructed by using the letters from `magazine` and `false` otherwise.
   - **Example**:
     ```cpp
     Input: ransomNote = "a", magazine = "b"
     Output: false
     ```
   - **Solution**:
     ```cpp
     bool canConstruct(string ransomNote, string magazine) {
         unordered_map<char, int> map;
         for (char c : magazine) {
             map[c]++;
         }

         for (char c : ransomNote) {
             if (map[c] == 0) {
                 return false;
             }
             map[c]--;
         }

         return true;
     }
     ```

### 10. **Find the Difference**
   - **Problem**: You are given two strings `s` and `t`, where `t` is generated by shuffling `s` and then adding one more letter at a random position. Return the letter that was added to `t`.
   - **Example**:
     ```cpp
     Input: s = "abcd", t = "abcde"
     Output: "e"
     ```
   - **Solution**:
     ```cpp
     char findTheDifference(string s, string t) {
         unordered_map<char, int> map;

         for (char c : s) {
             map[c]++;
         }

         for (char c : t) {
             if (map[c] == 0) {
                 return c;
             }
             map[c]--;
         }

         return '\0';
     }
     ```

### 11. **Isomorphic Strings**
   - **Problem**: Given two strings `s` and `t`, determine if they are isomorphic. Two strings are isomorphic if the characters in `s` can be replaced to get `t`.
   - **Example**:
     ```cpp
     Input: s = "egg", t = "add"


     Output: true
     ```
   - **Solution**:
     ```cpp
     bool isIsomorphic(string s, string t) {
         unordered_map<char, char> mapS, mapT;
         for (int i = 0; i < s.size(); i++) {
             if (mapS.find(s[i]) != mapS.end()) {
                 if (mapS[s[i]] != t[i]) return false;
             } else {
                 mapS[s[i]] = t[i];
             }

             if (mapT.find(t[i]) != mapT.end()) {
                 if (mapT[t[i]] != s[i]) return false;
             } else {
                 mapT[t[i]] = s[i];
             }
         }
         return true;
     }
     ```

### 12. **Word Pattern**
   - **Problem**: Given a pattern and a string `s`, find if `s` follows the same pattern.
   - **Example**:
     ```cpp
     Input: pattern = "abba", s = "dog cat cat dog"
     Output: true
     ```
   - **Solution**:
     ```cpp
     bool wordPattern(string pattern, string s) {
         unordered_map<char, string> mapP;
         unordered_map<string, char> mapS;
         vector<string> words;
         istringstream iss(s);
         string word;
         while (iss >> word) {
             words.push_back(word);
         }

         if (words.size() != pattern.size()) {
             return false;
         }

         for (int i = 0; i < pattern.size(); i++) {
             char p = pattern[i];
             string w = words[i];

             if (mapP.find(p) != mapP.end()) {
                 if (mapP[p] != w) return false;
             } else {
                 mapP[p] = w;
             }

             if (mapS.find(w) != mapS.end()) {
                 if (mapS[w] != p) return false;
             } else {
                 mapS[w] = p;
             }
         }

         return true;
     }
     ```

These questions cover a variety of scenarios where hashmaps are useful. Practicing them will help you build a strong foundation for solving hashmap-related problems in coding interviews, including those at IBM.

Here are some common DSA questions related to strings that are frequently asked in coding interviews, including at IBM. These questions will help you strengthen your understanding of string manipulation and algorithms.

### 1. **Reverse a String**
   - **Problem**: Write a function that reverses a string.
   - **Example**:
     ```cpp
     Input: "hello"
     Output: "olleh"
     ```
   - **Solution**:
     ```cpp
     string reverseString(string s) {
         int left = 0, right = s.length() - 1;
         while (left < right) {
             swap(s[left++], s[right--]);
         }
         return s;
     }
     ```

### 2. **Check if Two Strings are Anagrams**
   - **Problem**: Given two strings `s` and `t`, determine if they are anagrams of each other.
   - **Example**:
     ```cpp
     Input: s = "anagram", t = "nagaram"
     Output: true
     ```
   - **Solution**:
     ```cpp
     bool isAnagram(string s, string t) {
         if (s.length() != t.length()) return false;
         vector<int> count(26, 0);
         for (char c : s) count[c - 'a']++;
         for (char c : t) {
             if (--count[c - 'a'] < 0) return false;
         }
         return true;
     }
     ```

### 3. **Longest Palindromic Substring**
   - **Problem**: Given a string `s`, find the longest palindromic substring in `s`.
   - **Example**:
     ```cpp
     Input: "babad"
     Output: "bab" (Note: "aba" is also a valid answer.)
     ```
   - **Solution**:
     ```cpp
     string longestPalindrome(string s) {
         if (s.empty()) return "";
         int n = s.length(), start = 0, maxLen = 1;

         for (int i = 0; i < n; i++) {
             int l = i, r = i;
             while (l >= 0 && r < n && s[l] == s[r]) {
                 if (r - l + 1 > maxLen) {
                     start = l;
                     maxLen = r - l + 1;
                 }
                 l--;
                 r++;
             }

             l = i, r = i + 1;
             while (l >= 0 && r < n && s[l] == s[r]) {
                 if (r - l + 1 > maxLen) {
                     start = l;
                     maxLen = r - l + 1;
                 }
                 l--;
                 r++;
             }
         }

         return s.substr(start, maxLen);
     }
     ```

### 4. **String to Integer (atoi)**
   - **Problem**: Implement the `atoi` function, which converts a string to an integer.
   - **Example**:
     ```cpp
     Input: "42"
     Output: 42
     ```
   - **Solution**:
     ```cpp
     int myAtoi(string s) {
         int i = 0, sign = 1, result = 0;
         while (i < s.length() && s[i] == ' ') i++;

         if (i < s.length() && (s[i] == '+' || s[i] == '-')) {
             sign = (s[i++] == '-') ? -1 : 1;
         }

         while (i < s.length() && isdigit(s[i])) {
             int digit = s[i++] - '0';
             if (result > (INT_MAX - digit) / 10) {
                 return (sign == 1) ? INT_MAX : INT_MIN;
             }
             result = result * 10 + digit;
         }

         return result * sign;
     }
     ```

### 5. **Longest Substring Without Repeating Characters**
   - **Problem**: Given a string `s`, find the length of the longest substring without repeating characters.
   - **Example**:
     ```cpp
     Input: "abcabcbb"
     Output: 3 (The answer is "abc", with the length of 3.)
     ```
   - **Solution**:
     ```cpp
     int lengthOfLongestSubstring(string s) {
         unordered_map<char, int> map;
         int maxLength = 0, start = 0;

         for (int end = 0; end < s.size(); end++) {
             if (map.find(s[end]) != map.end()) {
                 start = max(map[s[end]] + 1, start);
             }
             map[s[end]] = end;
             maxLength = max(maxLength, end - start + 1);
         }

         return maxLength;
     }
     ```

### 6. **Count and Say**
   - **Problem**: The "Count and Say" sequence is a sequence of digit strings defined by the recursive formula:
     - `countAndSay(1) = "1"`
     - `countAndSay(n)` is the previous term (n-1) read out loud.
   - **Example**:
     ```cpp
     Input: 4
     Output: "1211"
     ```
   - **Solution**:
     ```cpp
     string countAndSay(int n) {
         if (n == 1) return "1";
         string prev = countAndSay(n - 1);
         string result = "";
         int count = 1;

         for (int i = 1; i < prev.length(); i++) {
             if (prev[i] == prev[i - 1]) {
                 count++;
             } else {
                 result += to_string(count) + prev[i - 1];
                 count = 1;
             }
         }
         result += to_string(count) + prev.back();
         return result;
     }
     ```

### 7. **Valid Anagram**
   - **Problem**: Given two strings `s` and `t`, write a function to determine if `t` is an anagram of `s`.
   - **Example**:
     ```cpp
     Input: s = "anagram", t = "nagaram"
     Output: true
     ```
   - **Solution**:
     ```cpp
     bool isAnagram(string s, string t) {
         if (s.length() != t.length()) return false;
         vector<int> count(26, 0);
         for (int i = 0; i < s.length(); i++) {
             count[s[i] - 'a']++;
             count[t[i] - 'a']--;
         }
         for (int c : count) {
             if (c != 0) return false;
         }
         return true;
     }
     ```

### 8. **Longest Common Prefix**
   - **Problem**: Write a function to find the longest common prefix string amongst an array of strings. If there is no common prefix, return an empty string "".
   - **Example**:
     ```cpp
     Input: ["flower", "flow", "flight"]
     Output: "fl"
     ```
   - **Solution**:
     ```cpp
     string longestCommonPrefix(vector<string>& strs) {
         if (strs.empty()) return "";
         string prefix = strs[0];
         for (int i = 1; i < strs.size(); i++) {
             while (strs[i].find(prefix) != 0) {
                 prefix = prefix.substr(0, prefix.length() - 1);
                 if (prefix.empty()) return "";
             }
         }
         return prefix;
     }
     ```

### 9. **Zigzag Conversion**
   - **Problem**: The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows. Write the code that will take a string and make this conversion.
   - **Example**:
     ```cpp
     Input: s = "PAYPALISHIRING", numRows = 3
     Output: "PAHNAPLSIIGYIR"
     ```
   - **Solution**:
     ```cpp
     string convert(string s, int numRows) {
         if (numRows == 1) return s;

         vector<string> rows(min(numRows, int(s.length())));
         int currRow = 0;
         bool goingDown = false;

         for (char c : s) {
             rows[currRow] += c;
             if (currRow == 0 || currRow == numRows - 1) goingDown = !goingDown;
             currRow += goingDown ? 1 : -1;
         }

         string result;
         for (string row : rows) result += row;
         return result;
     }
     ```

### 10. **Add Binary**
   - **Problem**: Given two binary strings, return their sum (also a binary string).
   - **Example**:
     ```cpp
     Input: a = "11", b = "1"
     Output: "100"
     ```
   - **Solution**:
     ```cpp
     string addBinary(string a, string b) {
         string result = "";
         int carry = 0, i = a.size() - 1, j = b.size() - 1;

         while (i >= 0 || j >= 0 || carry) {
             int sum = carry;
             if (i >= 0) sum += a[i--] - '0';
             if (j >= 0) sum += b[j--] - '0';
             result

 += (sum % 2) + '0';
             carry = sum / 2;
         }

         reverse(result.begin(), result.end());
         return result;
     }
     ```

These problems cover a range of string-related algorithms and data structures. Practicing these problems will help you prepare for string-related questions in coding interviews at IBM.

Here are some common Data Structures and Algorithms (DSA) questions related to queues that might be asked in IBM coding interviews. These problems cover various applications and implementations of queues.

### 1. **Implement a Queue using Stacks**
   - **Problem**: Implement a queue using two stacks. The queue should support the following operations:
     - `enqueue(x)`: Add element `x` to the queue.
     - `dequeue()`: Remove and return the element from the front of the queue.
     - `peek()`: Return the element at the front of the queue without removing it.
     - `empty()`: Return whether the queue is empty.
   - **Solution**:
     ```cpp
     class MyQueue {
     private:
         stack<int> s1, s2;

     public:
         void enqueue(int x) {
             s1.push(x);
         }

         int dequeue() {
             if (s2.empty()) {
                 while (!s1.empty()) {
                     s2.push(s1.top());
                     s1.pop();
                 }
             }
             int res = s2.top();
             s2.pop();
             return res;
         }

         int peek() {
             if (s2.empty()) {
                 while (!s1.empty()) {
                     s2.push(s1.top());
                     s1.pop();
                 }
             }
             return s2.top();
         }

         bool empty() {
             return s1.empty() && s2.empty();
         }
     };
     ```

### 2. **Circular Queue**
   - **Problem**: Design and implement a circular queue with a fixed size. The circular queue should support the following operations:
     - `enqueue(x)`: Add an element `x` to the queue.
     - `dequeue()`: Remove and return the front element of the queue.
     - `isEmpty()`: Return whether the queue is empty.
     - `isFull()`: Return whether the queue is full.
   - **Solution**:
     ```cpp
     class CircularQueue {
     private:
         vector<int> arr;
         int front, rear, size, capacity;

     public:
         CircularQueue(int k) : capacity(k), size(0), front(0), rear(0) {
             arr.resize(k);
         }

         void enqueue(int x) {
             if (isFull()) return;
             arr[rear] = x;
             rear = (rear + 1) % capacity;
             size++;
         }

         int dequeue() {
             if (isEmpty()) return -1;
             int res = arr[front];
             front = (front + 1) % capacity;
             size--;
             return res;
         }

         bool isEmpty() {
             return size == 0;
         }

         bool isFull() {
             return size == capacity;
         }
     };
     ```

### 3. **Generate Binary Numbers from 1 to N**
   - **Problem**: Given an integer `N`, generate all binary numbers from `1` to `N` in a queue.
   - **Example**:
     ```cpp
     Input: N = 5
     Output: [1, 10, 11, 100, 101]
     ```
   - **Solution**:
     ```cpp
     vector<string> generateBinaryNumbers(int N) {
         vector<string> result;
         queue<string> q;
         q.push("1");

         for (int i = 0; i < N; i++) {
             string binary = q.front();
             q.pop();
             result.push_back(binary);
             q.push(binary + "0");
             q.push(binary + "1");
         }

         return result;
     }
     ```

### 4. **First Non-Repeating Character in a Stream**
   - **Problem**: Given a stream of characters, find the first non-repeating character in the stream at each point.
   - **Example**:
     ```cpp
     Input: "aabcc"
     Output: "a", "a", "b", "b", "#"
     ```
   - **Solution**:
     ```cpp
     vector<char> firstNonRepeating(string str) {
         vector<char> result;
         unordered_map<char, int> count;
         queue<char> q;

         for (char c : str) {
             count[c]++;
             q.push(c);
             
             while (!q.empty() && count[q.front()] > 1) {
                 q.pop();
             }
             
             if (q.empty()) {
                 result.push_back('#');
             } else {
                 result.push_back(q.front());
             }
         }

         return result;
     }
     ```

### 5. **Rearrange Characters in a String**
   - **Problem**: Given a string where each character appears exactly twice, rearrange the characters in such a way that no two identical characters are adjacent.
   - **Example**:
     ```cpp
     Input: "aabb"
     Output: "abab" or "baba"
     ```
   - **Solution**:
     ```cpp
     string rearrangeCharacters(string s) {
         unordered_map<char, int> count;
         for (char c : s) {
             count[c]++;
         }

         priority_queue<pair<int, char>> maxHeap;
         for (auto& kv : count) {
             maxHeap.push({kv.second, kv.first});
         }

         string result;
         while (maxHeap.size() >= 2) {
             auto [count1, char1] = maxHeap.top(); maxHeap.pop();
             auto [count2, char2] = maxHeap.top(); maxHeap.pop();
             
             result += char1;
             result += char2;
             
             if (--count1 > 0) maxHeap.push({count1, char1});
             if (--count2 > 0) maxHeap.push({count2, char2});
         }
         
         if (!maxHeap.empty()) {
             result += maxHeap.top().second;
         }

         return result;
     }
     ```

### 6. **Sliding Window Maximum**
   - **Problem**: Given an array and a window size `k`, find the maximum value in each sliding window of size `k`.
   - **Example**:
     ```cpp
     Input: [1,3,-1,-3,5,3,6,7], k = 3
     Output: [3,3,5,5,6,7]
     ```
   - **Solution**:
     ```cpp
     vector<int> maxSlidingWindow(vector<int>& nums, int k) {
         vector<int> result;
         deque<int> dq;

         for (int i = 0; i < nums.size(); i++) {
             if (!dq.empty() && dq.front() == i - k) {
                 dq.pop_front();
             }
             
             while (!dq.empty() && nums[dq.back()] < nums[i]) {
                 dq.pop_back();
             }
             
             dq.push_back(i);

             if (i >= k - 1) {
                 result.push_back(nums[dq.front()]);
             }
         }

         return result;
     }
     ```

### 7. **Reverse First K Elements of Queue**
   - **Problem**: Given a queue, reverse the first `k` elements of the queue.
   - **Example**:
     ```cpp
     Input: Queue = [1,2,3,4,5], k = 3
     Output: [3,2,1,4,5]
     ```
   - **Solution**:
     ```cpp
     void reverseFirstKElements(queue<int>& q, int k) {
         stack<int> s;
         for (int i = 0; i < k; i++) {
             s.push(q.front());
             q.pop();
         }

         while (!s.empty()) {
             q.push(s.top());
             s.pop();
         }

         for (int i = 0; i < q.size() - k; i++) {
             q.push(q.front());
             q.pop();
         }
     }
     ```

These questions and solutions should help you prepare for queue-related problems in coding interviews at IBM and other tech companies.
