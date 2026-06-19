cmake_minimum_required(VERSION 3.20)

project(MonteCarloStockSimulator)

set(CMAKE_CXX_STANDARD 20)
set(CMAKE_EXPORT_COMPILE_COMMANDS ON)

find_package(cpr REQUIRED)
find_package(nlohmann_json REQUIRED)
find_package(gRPC CONFIG REQUIRED)
find_package(Protobuf REQUIRED)

add_executable(
  MonteCarloStockSimulator
  src/cpp/main.cpp
)

target_link_libraries(
  MonteCarloStockSimulator
  PRIVATE
  cpr::cpr
  nlohmann_json::nlohmann_json
  gRPC::grpc
  protobuf::libprotobuf
)

add_custom_target(run
    COMMAND $<TARGET_FILE:MonteCarloStockSimulator>
    DEPENDS MonteCarloStockSimulator
    WORKING_DIRECTORY ${CMAKE_SOURCE_DIR}
)

add_custom_target(gen_proto_cpp
    COMMAND protobuf::protoc
        -I ${CMAKE_SOURCE_DIR}/proto
        --grpc_out=${CMAKE_SOURCE_DIR}/src/generated
        --cpp_out=${CMAKE_SOURCE_DIR}/src/generated
        --plugin=protoc-gen-grpc=`which grpc_cpp_plugin`
        ${CMAKE_SOURCE_DIR}/proto/stock.proto
)

add_custom_target(gen_proto_py
    COMMAND python3
     -m grpc_tools.protoc
     -I ${CMAKE_SOURCE_DIR}/proto
     --python_out=${CMAKE_SOURCE_DIR}/src/generated
     --pyi_out=${CMAKE_SOURCE_DIR}/src/generated
     --grpc_python_out=${CMAKE_SOURCE_DIR}/src/generated
     ${CMAKE_SOURCE_DIR}/proto/stock.proto
)
