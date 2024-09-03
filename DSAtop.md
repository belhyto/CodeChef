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


