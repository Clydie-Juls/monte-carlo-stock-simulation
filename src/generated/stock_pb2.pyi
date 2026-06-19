from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class StockRequest(_message.Message):
    __slots__ = ("ticker", "interval", "num_paths", "num_steps")
    TICKER_FIELD_NUMBER: _ClassVar[int]
    INTERVAL_FIELD_NUMBER: _ClassVar[int]
    NUM_PATHS_FIELD_NUMBER: _ClassVar[int]
    NUM_STEPS_FIELD_NUMBER: _ClassVar[int]
    ticker: str
    interval: str
    num_paths: int
    num_steps: int
    def __init__(self, ticker: _Optional[str] = ..., interval: _Optional[str] = ..., num_paths: _Optional[int] = ..., num_steps: _Optional[int] = ...) -> None: ...

class StockInfo(_message.Message):
    __slots__ = ("close",)
    CLOSE_FIELD_NUMBER: _ClassVar[int]
    close: float
    def __init__(self, close: _Optional[float] = ...) -> None: ...

class StockHistory(_message.Message):
    __slots__ = ("timestamp", "stock_info")
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    STOCK_INFO_FIELD_NUMBER: _ClassVar[int]
    timestamp: str
    stock_info: StockInfo
    def __init__(self, timestamp: _Optional[str] = ..., stock_info: _Optional[_Union[StockInfo, _Mapping]] = ...) -> None: ...

class StockHistoryResponse(_message.Message):
    __slots__ = ("stock_histories",)
    STOCK_HISTORIES_FIELD_NUMBER: _ClassVar[int]
    stock_histories: _containers.RepeatedCompositeFieldContainer[StockHistory]
    def __init__(self, stock_histories: _Optional[_Iterable[_Union[StockHistory, _Mapping]]] = ...) -> None: ...

class Path(_message.Message):
    __slots__ = ("steps",)
    STEPS_FIELD_NUMBER: _ClassVar[int]
    steps: _containers.RepeatedScalarFieldContainer[float]
    def __init__(self, steps: _Optional[_Iterable[float]] = ...) -> None: ...

class StockResponse(_message.Message):
    __slots__ = ("paths",)
    PATHS_FIELD_NUMBER: _ClassVar[int]
    paths: _containers.RepeatedCompositeFieldContainer[Path]
    def __init__(self, paths: _Optional[_Iterable[_Union[Path, _Mapping]]] = ...) -> None: ...
