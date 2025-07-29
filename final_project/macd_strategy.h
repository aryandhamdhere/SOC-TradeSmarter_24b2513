#pragma once
#include <vector>

// Function prototype for MACD strategy signal generator
// Parameters:
//   macdLine    -> vector containing MACD values
//   signalLine  -> vector containing Signal line values
// Returns:
//   vector<int> -> 1 = Buy, 0 = No Action
std::vector<int> generateMACDSignals(const std::vector<double>& macdLine, 
                                     const std::vector<double>& signalLine);