#include <bitset>
#include <cstdint>
#include <cstring>
#include <iomanip>
#include <iostream>
#include <string>

int main(int argc, char** argv) {
  const double x = std::stod(argv[1]);
  uint64_t bits;
  std::memcpy(&bits, &x, sizeof(x));
  std::cout << x << "\n";
  std::cout << std::dec << bits << "\n";
  std::cout << std::hex << bits << "\n";
  std::cout << std::bitset<64>{bits} << "\n";
}
