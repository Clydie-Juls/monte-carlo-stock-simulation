cmake_minimum_required(VERSION 3.20)

project(MonteCarloStockSimulator)

set(CMAKE_CXX_STANDARD 20)

find_package(cpr REQUIRED)
find_package(nlohmann_json REQUIRED)

add_executable(
  MonteCarloStockSimulator
  main.cpp
)

target_link_libraries(
  MonteCarloStockSimulator
  PRIVATE
  cpr::cpr
  nlohmann_json::nlohmann_json
)

add_custom_target(run
    COMMAND $<TARGET_FILE:MonteCarloStockSimulator>
    DEPENDS MonteCarloStockSimulator
    WORKING_DIRECTORY ${CMAKE_SOURCE_DIR}
)
