#include <iostream>
#include <vector>
#include <map>

using namespace std;

int main() {
    int n; // Number of elements in the array
    cout << "Enter the number of elements: ";
    cin >> n;

    vector<int> arr(n); // Create a vector to hold the integers
    cout << "Enter the elements: ";
    for (int i = 0; i < n; ++i) {
        cin >> arr[i]; // Input the elements into the array
    }

    map<int, int> countMap; // Map to store the count of each integer

    // Count occurrences of each integer
    for (int num : arr) {
        countMap[num]++;
    }

    // Print the occurrences
    for (const auto& pair : countMap) {
        cout << pair.first << " occurs " << pair.second << " times" << endl;
    }

    return 0;
}
