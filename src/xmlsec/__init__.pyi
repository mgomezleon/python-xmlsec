from collections.abc import Callable, Iterable
from typing import Any, AnyStr, IO, TypeVar, overload
from _typeshed import GenericPath, Self, StrOrBytesPath

from lxml.etree import _Element

from xmlsec.constants import __KeyData as KeyData, __Transform as Transform

_E = TypeVar('_E', bound=_Element)

def enable_debug_trace(enabled: bool = ...) -> None: ...
def init() -> None: ...
def shutdown() -> None: ...
def cleanup_callbacks() -> None: ...
def register_default_callbacks() -> None: ...
def register_callbacks(
    input_match_callback: Callable[[bytes], bool],
    input_open_callback: Callable[[bytes], Any],
    input_read_callback: Callable[[Any, memoryview], int],
    input_close_callback: Callable[[Any], None],
) -> None: ...
@overload
def base64_default_line_size() -> int: ...
@overload
def base64_default_line_size(size: int) -> None: ...

class EncryptionContext:
    key: Key | None
    def __init__(self, manager: KeysManager | None = ...) -> None: ...
    def decrypt(self, node: _Element) -> _Element: ...
    def encrypt_binary(self, template: _E, data: bytes) -> _E: ...
    def encrypt_uri(self, template: _E, uri: str) -> _E: ...
    def encrypt_xml(self, template: _E, node: _Element) -> _E: ...
    def reset(self) -> None: ...

class Error(Exception): ...
class InternalError(Error): ...

class Key:
    name: str
    @classmethod
    def from_binary_data(cls: type[Self], klass: KeyData, data: AnyStr) -> Self: ...
    @classmethod
    def from_binary_file(cls: type[Self], klass: KeyData, filename: StrOrBytesPath) -> Self: ...
    @classmethod
    def from_file(cls: type[Self], file: GenericPath | IO[AnyStr], format: int, password: str | None = ...) -> Self: ...
    @classmethod
    def from_memory(cls: type[Self], data: AnyStr, format: int, password: str | None = ...) -> Self: ...
    @classmethod
    def generate(cls: type[Self], klass: KeyData, size: int, type: int) -> Self: ...
    def load_cert_from_file(self, file: GenericPath | IO[AnyStr], format: int) -> None: ...
    def load_cert_from_memory(self, data: AnyStr, format: int) -> None: ...
    def __copy__(self: Self) -> Self: ...
    def __deepcopy__(self: Self) -> Self: ...

class KeysManager:
    def add_key(self, key: Key) -> None: ...
    def load_cert(self, filename: StrOrBytesPath, format: int, type: int) -> None: ...
    def load_cert_from_memory(self, data: AnyStr, format: int, type: int) -> None: ...

class SignatureContext:
    key: Key | None
    def enable_reference_transform(self, transform: Transform) -> None: ...
    def enable_signature_transform(self, transform: Transform) -> None: ...
    def register_id(self, node: _Element, id_attr: str = ..., id_ns: str | None = ...) -> None: ...
    def set_enabled_key_data(self, keydata_list: Iterable[KeyData]) -> None: ...
    def sign(self, node: _Element) -> None: ...
    def sign_binary(self, bytes: bytes, transform: Transform) -> bytes: ...
    def verify(self, node: _Element) -> None: ...
    def verify_binary(self, bytes: bytes, transform: Transform, signature: bytes) -> None: ...

class VerificationError(Error): ...
