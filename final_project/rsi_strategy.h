#pragma once
#include <vector>

// Function prototype for RSI strategy signal generator
// Parameters:
//   rsiValues -> vector containing RSI values
// Returns:
//   vector<int> -> 1 = Buy, 0 = No Action
std::vector<int> generateRSISignals(const std::vector<double>& rsiValues);