#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

// Structure for an item which stores weight & corresponding value of Item
struct Item {
    int value, weight;
    // Constructor
    Item(int value, int weight)
        : value(value), weight(weight)
    {
        
    }
};

// Comparison function to sort Item according to val/weight ratio
bool cmp(Item a, Item b)
{
    double r1 = (double)a.value / a.weight;
    double r2 = (double)b.value / b.weight;
    return r1 > r2;
}

// Main greedy function to solve the problem
double fractionalKnapsack(vector<Item>& items, int N)
{
    // Sort Items based on ratio
    sort(items.begin(), items.end(), cmp);

    // Current weight in knapsack
    int curWeight = 0;

    // Result (value in Knapsack)
    double finalvalue = 0.0;

    // Loop through all Items
    for (int i = 0; i < items.size(); i++) {

        // If adding Item won't overflow, add it completely
        if (curWeight + items[i].weight <= N) {
            curWeight += items[i].weight;
            finalvalue += items[i].value;
        }

        // If we can't add the current Item, add a fractional part of it
        else {
            int remain = N - curWeight;
            finalvalue += items[i].value * ((double)remain / items[i].weight);

            break;
        }
    }
    // Return the final value
    return finalvalue;
}

// Driver Code
int main()
{
    // Weight of knapsack - Accept user input
    int N;
    cout << "Enter the weight of the knapsack: ";
    cin >> N;

    // Accept user input for the number of items
    int size;
    cout << "Enter the number of items: ";
    cin >> size;

    // Given weights and values as pairs - Accept user input
    vector<Item> items;
    for (int i = 0; i < size; i++) {
        int value, weight;
        cout << "Enter value and weight for item " << i + 1 << ": ";
        cin >> value >> weight;
        items.push_back(Item(value, weight));
    }

    // Function Call
    cout << "Maximum profit earned = " << fractionalKnapsack(items, N);
    return 0;
}
