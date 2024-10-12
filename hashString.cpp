#include <iostream>
#include <string>
using namespace std;

std::string moveHashesToFront(const std::string& input) {
    std::string hashes;
    std::string nonHashes;

    for (char c : input) {
        if (c == '#') {
            hashes += c;
        } else {
            nonHashes += c;
        }
    }

    return hashes + nonHashes;
}

int main() {
    std::string input;
    std::cout << "Enter a string: ";
    std::getline(std::cin, input);

    std::string result = moveHashesToFront(input);
    std::cout << "Result: " << result << std::endl;

    return 0;
}
