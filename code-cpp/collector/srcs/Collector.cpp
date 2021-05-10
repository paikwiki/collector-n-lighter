#include "Collector.hpp"

// helper starts
std::string getZeroPaddedNumString(int nbr) {
  std::ostringstream ss;

  if (nbr < 10)
    ss << "0";
  ss << nbr;

  return (ss.str());
}

std::string getFormattedLogTime(char const delemeter) {
  std::ostringstream ss;
  time_t rawTime;
  struct tm *ptm;

  time(&rawTime);
  ptm = gmtime(&rawTime);
  ss << (ptm->tm_year + 1900) << delemeter
     << getZeroPaddedNumString((ptm->tm_mon + 1)) << delemeter
     << getZeroPaddedNumString(ptm->tm_mday) << delemeter
     << getZeroPaddedNumString((ptm->tm_hour + 9) % 24) << delemeter
     << getZeroPaddedNumString(ptm->tm_min) << delemeter
     << getZeroPaddedNumString(ptm->tm_sec);

  return (ss.str());
}
// helper ends

Collector::Collector(char *logFileName) : isFileClose(false) {
  std::string fileName = logFileName;

  if (this->openLogfile(fileName) == true) {
    this->fs << getFormattedLogTime('-')
             << ": Write the word, \"" << fileName
             << "\" in a file called \"" << fileName << "\"" << std::endl;
  }
}

Collector::~Collector() {
  this->closeLogfile();
}

bool Collector::closeLogfile() {
  if (isFileClose != false)
    return (false);

  try {
    this->fs.close();
    isFileClose = true;
  } catch (std::exception &e) {
    std::cerr << "Error: " << e.what() << std::endl;
  }

  return (true);
}

bool Collector::openLogfile(std::string &fileName) {
  try {
    this->fs.open(fileName, std::fstream::out | std::fstream::app);
  } catch (std::exception &e) {
    std::cerr << "Error: " << e.what() << std::endl;
  }

  if (!(fs.is_open())) {
    this->isFileClose = true;
    return (false);
  }

  return (true);
}
