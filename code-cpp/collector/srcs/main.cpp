#include <iostream>
#include <string>
#include <limits>

#include "Collector.hpp"

int main(int argc, char **argv) {
  if (argc < 2) {
    std::cout << "Error: no arguments" << std::endl;
    exit(1);
  }
  Collector colletor(argv[1]);
  // collector.run() // start loop
  return (0);
}
