#include <iostream>
#include <vector>

class MergeSort {
public:
    MergeSort(std::vector<int>& arr) : array(arr) {}

    void sort() {
        mergeSort(0, array.size() - 1);
    }

    void display() {
        for (int num : array) {
            std::cout << num << " ";
        }
        std::cout << std::endl;
    }

private:
    std::vector<int>& array;

    void merge(int left, int middle, int right) {
        int n1 = middle - left + 1;
        int n2 = right - middle;

        std::vector<int> leftArray(n1);
        std::vector<int> rightArray(n2);

        for (int i = 0; i < n1; i++) {
            leftArray[i] = array[left + i];
        }

        for (int i = 0; i < n2; i++) {
            rightArray[i] = array[middle + 1 + i];
        }

        int i = 0, j = 0, k = left;

        while (i < n1 && j < n2) {
            if (leftArray[i] <= rightArray[j]) {
                array[k++] = leftArray[i++];
            } else {
                array[k++] = rightArray[j++];
            }
        }

        while (i < n1) {
            array[k++] = leftArray[i++];
        }

        while (j < n2) {
            array[k++] = rightArray[j++];
        }
    }

    void mergeSort(int left, int right) {
        if (left < right) {
            int middle = left + (right - left) / 2;

            mergeSort(left, middle);
            mergeSort(middle + 1, right);

            merge(left, middle, right);
        }
    }
};

int main() {
    int n;
    std::cout << "Enter the number of elements: ";
    std::cin >> n;

    std::vector<int> arr(n);

    std::cout << "Enter " << n << " elements: ";
    for (int i = 0; i < n; i++) {
        std::cin >> arr[i];
    }

    MergeSort mergeSort(arr);
    mergeSort.sort();

    std::cout << "Sorted array: ";
    mergeSort.display();

    return 0;
}
