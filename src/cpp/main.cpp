#include <cmath>
#include <cpr/cpr.h>
#include <fstream>
#include <iostream>
#include <nlohmann/json.hpp>
#include <numbers>
#include <random>
#include <vector>

using json = nlohmann::json;
std::random_device rd{};
std::mt19937 gen{rd()};
std::normal_distribution<double> d{0, 1};

struct StockStats {
    double drift;
    double volatility;
};

StockStats calculateDirft(std::vector<double> closingStockHistory) {
    double avgReturn = 0.0;
    std::vector<double> logReturns;
    for (int i{1}; i < closingStockHistory.size(); ++i) {
        double ln = std::log(closingStockHistory[i] / closingStockHistory[i - 1]);
        logReturns.push_back(ln);
        avgReturn += ln;
    }
    avgReturn /= closingStockHistory.size() - 1;

    std::cout << avgReturn << std::endl;

    double sum = 0;
    for (double s: logReturns) {
        sum += std::pow(s - avgReturn, 2);
    }

     double variance = sum / (closingStockHistory.size() - 1);

     return {
         avgReturn,
         std::sqrt(variance)
     };
}


std::vector<std::vector<double>> simulatePaths(std::vector<double>& closingStockHistory, int numPaths, int numSteps, StockStats stats) {
 std::vector<std::vector<double>> paths;
    for (int i = 0; i < numPaths; ++i) {
        std::vector<double> predictedPrices;
        double price = closingStockHistory.back();
        for (int j = 0; j < numSteps; ++j) {
            double z = d(gen);
            price *= std::exp(stats.drift + stats.volatility * (1.0/6) * z);
            predictedPrices.push_back(price);
        }
        paths.push_back(predictedPrices);
    }

    return paths;
}

int main() {
    std::ifstream stockFile("stocks/AAPL.json");
    json stockJson = json::parse(stockFile);

    std::vector<double> returnStockHistory;
    for (auto& elem : stockJson) {
        returnStockHistory.push_back(elem["Close"]);
    }

    std::cout << "Enter number of simulated paths: ";
    int numPaths;
    std::cin >> numPaths;

    std::cout << "Enter number of predicted prices per path: ";
    int numSteps;
    std::cin >> numSteps;
    StockStats stats = calculateDirft(returnStockHistory);

    auto paths = simulatePaths(returnStockHistory, numPaths, numSteps, stats);

    for (int i = 0; i < numPaths; ++i) {
        std::cout << "Path " << i + 1 << ": " << std::endl;
        for (int j = 0; j < numSteps; ++j) {
            std::cout << "Price: " << paths[i][j] << std::endl;
        }
        std::cout << std::endl;
    }

    return 0;
}
