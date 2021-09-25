#include <algorithm>
#include <cstddef>
#include <iostream>
#include <string>
#include <vector>

int main(int argc, char** argv) {
  const std::string chars{argv[1]};
  std::cout << chars << "\n";

  size_t i = 0;
  std::vector<int> word{};
  for (const char& c: chars) {
    i += 1;
    word.push_back(static_cast<int>(c));
    if (i > 0 and i % 8 == 0) {
      std::reverse(word.begin(), word.end());
      for (const int& b: word) {
        std::cout << std::hex << b;
      }
      word.clear();
      if (i % 32 == 0) {
        std::cout << "\n";
      } else {
        std::cout << " ";
      }
    }
  }
  while (i % 8 != 0) {
    i += 1;
    std::cout << "00";
  }
  std::reverse(word.begin(), word.end());
  for (const int& b: word) {
      std::cout << std::hex << b;
  }
  std::cout << "\n";
  return 0;
}