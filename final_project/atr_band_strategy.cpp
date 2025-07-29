#include "atr_band_strategy.h"
#include <cstddef>
#include <vector>

// Function: generateATRBandSignals
// Purpose: Produce trading signals based on closing price relative to ATR lower band
// Output: 1 = Buy, 0 = No Action
std::vector<int> generateATRBandSignals(const std::vector<double>& closingPrices, 
                                        const std::vector<double>& lowerATRBand) {
    
    // Initialize all signals as 0 (No Action)
    std::vector<int> tradeSignals(closingPrices.size(), 0);

    for (size_t idx = 0; idx < closingPrices.size(); ++idx) {
        // Buy signal when the price drops below the lower ATR band
        if (closingPrices[idx] < lowerATRBand[idx]) {
            tradeSignals[idx] = 1;
        }
    }
    return tradeSignals;
}