#include "macd_strategy.h"
#include <vector>

// Function: generateMACDSignals
// Purpose: Generate Buy signals based on MACD line crossing above Signal line
// Output: Vector<int> (1 = Buy, 0 = No Action)
std::vector<int> generateMACDSignals(const std::vector<double>& macdLine, 
                                     const std::vector<double>& signalLine) {
    
    // Initialize all signals as 0 (No Action)
    std::vector<int> tradeSignals(macdLine.size(), 0);

    // Start loop from 1 since we compare current and previous values
    for (size_t idx = 1; idx < macdLine.size(); ++idx) {
        bool currentCross = macdLine[idx] > signalLine[idx];
        bool prevCross = macdLine[idx - 1] <= signalLine[idx - 1];

        // Buy signal when MACD crosses above the signal line
        if (currentCross && prevCross) {
            tradeSignals[idx] = 1;
        }
    }
    return tradeSignals;
}