#pragma once
#include <vector>
#include <string>

// Structure to hold all relevant market data fields
struct PriceData {
    std::vector<std::string> tradeDates;    // List of dates
    std::vector<double> openPrices;         // Opening prices
    std::vector<double> highPrices;         // Highest prices
    std::vector<double> lowPrices;          // Lowest prices
    std::vector<double> closePrices;        // Closing prices
    std::vector<double> tradeVolume;        // Volume traded
};
