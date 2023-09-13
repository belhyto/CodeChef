#include <iostream>
#include <vector>

class Quicksort {
public:
    void sort(std::vector<int>& arr) {
        quicksort(arr, 0, arr.size() - 1);
    }
private:
    void quicksort(std::vector<int>& arr, int left, int right) {
        if (left < right) {
            int pivotIndex = partition(arr, left, right);
            quicksort(arr, left, pivotIndex - 1);
            quicksort(arr, pivotIndex + 1, right);
        }
    }
    int partition(std::vector<int>& arr, int left, int right) {
        int pivot = arr[right];
        int i = left - 1;

        for (int j = left; j < right; j++) {
            if (arr[j] < pivot) {
                i++;
                std::swap(arr[i], arr[j]); 
            }
        }
        std::swap(arr[i + 1], arr[right]);
        return i + 1;
    }
};
int main() {
    int n;
    std::cout << "Enter the number of elements: ";
    std::cin >> n;

    std::vector<int> arr(n);

    std::cout << "Enter " << n << " integers: ";
    for (int i = 0; i < n; i++) {
        std::cin >> arr[i];
    }

    Quicksort quicksort;
    quicksort.sort(arr);

    std::cout << "Sorted array: ";
    for (int num : arr) {
        std::cout << num << " ";
    }
    std::cout << std::endl;

    return 0;
}
