#ifndef COLLECTOR_H
#define COLLECTOR_H

#include <fstream>
#include <iostream>
#include<sstream>
#include <ctime>

class Collector {
 private:
  std::ofstream fs;
  Collector();
  Collector(Collector const &);
  Collector &operator=(Collector const &);
  int openLogfile(std::string &filename);

 public:
  ~Collector();
  Collector(char *logFileName);
};

#endif
