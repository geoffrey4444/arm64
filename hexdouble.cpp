#include <bitset>
#include <cstdint>
#include <cstring>
#include <iomanip>
#include <iostream>
#include <string>

int main(int argc, char** argv) {
  double x = 0.0;
  const uint64_t bits = std::stoull(argv[1], nullptr, 16);
  std::memcpy(&x, &bits, sizeof(bits));
  std::cout << std::setprecision(15) << x << "\n";
  std::cout << std::dec << bits << "\n";
  std::cout << std::hex << bits << "\n";
  std::cout << std::bitset<64>{bits} << "\n";
}
