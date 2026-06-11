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
