#pragma once
#include <vector>

// Function prototype for ATR Band Strategy signal generator
// Parameters: 
//   closingPrices -> vector of closing prices
//   lowerATRBand  -> vector of lower ATR band values
// Returns: 
//   vector of signals (1 = Buy, 0 = No Action)
std::vector<int> generateATRBandSignals(const std::vector<double>& closingPrices, 
                                        const std::vector<double>& lowerATRBand);