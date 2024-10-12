#include <iostream>
#include <string>

std::string compressConsecutiveChars(const std::string& input) {
    std::string output;
    int count = 1;
   std::cout << "size: "<< input.size();
    for (int i = 1; i <= input.size(); i++) {
        if (i == input.size() || input[i] != input[i - 1]) {
            output += input[i - 1];
            output += std::to_string(count);
            count = 1;
        } else {
            ++count;
        }
    }

    return output;
}

int main() {
    std::string input;
    std::cout << "Enter a string: ";
    std::getline(std::cin, input);

    std::string result = compressConsecutiveChars(input);
    std::cout << "Result: " << result << std::endl;

    return 0;
}
