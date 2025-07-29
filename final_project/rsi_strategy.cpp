#include "rsi_strategy.h"
#include <vector>

// Function: generateRSISignals
// Purpose: Generate Buy signals when RSI value enters oversold territory (<30)
// Returns: Vector<int> where 1 = Buy, 0 = No Action
std::vector<int> generateRSISignals(const std::vector<double>& rsiValues) {
    
    // Initialize signals with 0 (No Action)
    std::vector<int> tradeSignals(rsiValues.size(), 0);

    for (size_t idx = 0; idx < rsiValues.size(); ++idx) {
        // Buy signal when RSI is below 30 (oversold condition)
        if (rsiValues[idx] < 30.0) {
            tradeSignals[idx] = 1;
        }
    }
    return tradeSignals;
}