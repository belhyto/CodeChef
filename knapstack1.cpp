#include <iostream>
#include <vector>
#include <algorithm>

struct Item {
    int weight;
    int value;
    double value_to_weight_ratio;
};

bool compareItems(Item item1, Item item2) {
    return item1.value_to_weight_ratio > item2.value_to_weight_ratio;
}

double fractional_knapsack(std::vector<Item>& items, int capacity) {
    int n = items.size();

    // Calculate the value-to-weight ratio for each item
    for (int i = 0; i < n; ++i) {
        items[i].value_to_weight_ratio = static_cast<double>(items[i].value) / items[i].weight;
    }

    // Sort the items in non-increasing order of value-to-weight ratio
    std::sort(items.begin(), items.end(), compareItems);

    double total_value = 0;
    int current_capacity = capacity;

    for (int i = 0; i < n; ++i) {
        if (current_capacity >= items[i].weight) {
            // Take the whole item as it can fit entirely into the knapsack
            current_capacity -= items[i].weight;
            total_value += items[i].value;
        } else {
            // Take a fraction of the item to fill the remaining capacity
            double fraction = static_cast<double>(current_capacity) / items[i].weight;
            total_value += fraction * items[i].value;
            break; // The knapsack is full, so no need to continue
        }
    }

    return total_value;
}

int main() {
    std::vector<Item> items = {
        {10, 60},
        {20, 100},
        {30, 120},
    };

    int knapsack_capacity = 50;

    double max_value = fractional_knapsack(items, knapsack_capacity);

    std::cout << "Maximum value that can be achieved: " << max_value << std::endl;

    return 0;
}
