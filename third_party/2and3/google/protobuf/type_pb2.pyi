from google.protobuf.any_pb2 import (
    Any,
)
from google.protobuf.internal.containers import (
    RepeatedCompositeFieldContainer,
    RepeatedScalarFieldContainer,
)
from google.protobuf.message import (
    Message,
)
from google.protobuf.source_context_pb2 import (
    SourceContext,
)
from typing import (
    Iterable,
    List,
    Optional,
    Text,
    Tuple,
    cast,
)


class Syntax(int):

    @classmethod
    def Name(cls, number: int) -> bytes: ...

    @classmethod
    def Value(cls, name: bytes) -> Syntax: ...

    @classmethod
    def keys(cls) -> List[bytes]: ...

    @classmethod
    def values(cls) -> List[Syntax]: ...

    @classmethod
    def items(cls) -> List[Tuple[bytes, Syntax]]: ...


SYNTAX_PROTO2: Syntax
SYNTAX_PROTO3: Syntax


class Type(Message):
    name: Text
    oneofs: RepeatedScalarFieldContainer[Text]
    syntax: Syntax

    @property
    def fields(self) -> RepeatedCompositeFieldContainer[Field]: ...

    @property
    def options(self) -> RepeatedCompositeFieldContainer[Option]: ...

    @property
    def source_context(self) -> SourceContext: ...

    def __init__(self,
                 name: Optional[Text] = ...,
                 fields: Optional[Iterable[Field]] = ...,
                 oneofs: Optional[Iterable[Text]] = ...,
                 options: Optional[Iterable[Option]] = ...,
                 source_context: Optional[SourceContext] = ...,
                 syntax: Optional[Syntax] = ...,
                 ) -> None: ...

    @classmethod
    def FromString(cls, s: bytes) -> Type: ...


class Field(Message):

    class Kind(int):

        @classmethod
        def Name(cls, number: int) -> bytes: ...

        @classmethod
        def Value(cls, name: bytes) -> Field.Kind: ...

        @classmethod
        def keys(cls) -> List[bytes]: ...

        @classmethod
        def values(cls) -> List[Field.Kind]: ...

        @classmethod
        def items(cls) -> List[Tuple[bytes, Field.Kind]]: ...
    TYPE_UNKNOWN: Kind
    TYPE_DOUBLE: Kind
    TYPE_FLOAT: Kind
    TYPE_INT64: Kind
    TYPE_UINT64: Kind
    TYPE_INT32: Kind
    TYPE_FIXED64: Kind
    TYPE_FIXED32: Kind
    TYPE_BOOL: Kind
    TYPE_STRING: Kind
    TYPE_GROUP: Kind
    TYPE_MESSAGE: Kind
    TYPE_BYTES: Kind
    TYPE_UINT32: Kind
    TYPE_ENUM: Kind
    TYPE_SFIXED32: Kind
    TYPE_SFIXED64: Kind
    TYPE_SINT32: Kind
    TYPE_SINT64: Kind

    class Cardinality(int):

        @classmethod
        def Name(cls, number: int) -> bytes: ...

        @classmethod
        def Value(cls, name: bytes) -> Field.Cardinality: ...

        @classmethod
        def keys(cls) -> List[bytes]: ...

        @classmethod
        def values(cls) -> List[Field.Cardinality]: ...

        @classmethod
        def items(cls) -> List[Tuple[bytes, Field.Cardinality]]: ...
    CARDINALITY_UNKNOWN: Cardinality
    CARDINALITY_OPTIONAL: Cardinality
    CARDINALITY_REQUIRED: Cardinality
    CARDINALITY_REPEATED: Cardinality
    kind: Field.Kind
    cardinality: Field.Cardinality
    number: int
    name: Text
    type_url: Text
    oneof_index: int
    packed: bool
    json_name: Text
    default_value: Text

    @property
    def options(self) -> RepeatedCompositeFieldContainer[Option]: ...

    def __init__(self,
                 kind: Optional[Field.Kind] = ...,
                 cardinality: Optional[Field.Cardinality] = ...,
                 number: Optional[int] = ...,
                 name: Optional[Text] = ...,
                 type_url: Optional[Text] = ...,
                 oneof_index: Optional[int] = ...,
                 packed: Optional[bool] = ...,
                 options: Optional[Iterable[Option]] = ...,
                 json_name: Optional[Text] = ...,
                 default_value: Optional[Text] = ...,
                 ) -> None: ...

    @classmethod
    def FromString(cls, s: bytes) -> Field: ...


class Enum(Message):
    name: Text
    syntax: Syntax

    @property
    def enumvalue(self) -> RepeatedCompositeFieldContainer[EnumValue]: ...

    @property
    def options(self) -> RepeatedCompositeFieldContainer[Option]: ...

    @property
    def source_context(self) -> SourceContext: ...

    def __init__(self,
                 name: Optional[Text] = ...,
                 enumvalue: Optional[Iterable[EnumValue]] = ...,
                 options: Optional[Iterable[Option]] = ...,
                 source_context: Optional[SourceContext] = ...,
                 syntax: Optional[Syntax] = ...,
                 ) -> None: ...

    @classmethod
    def FromString(cls, s: bytes) -> Enum: ...


class EnumValue(Message):
    name: Text
    number: int

    @property
    def options(self) -> RepeatedCompositeFieldContainer[Option]: ...

    def __init__(self,
                 name: Optional[Text] = ...,
                 number: Optional[int] = ...,
                 options: Optional[Iterable[Option]] = ...,
                 ) -> None: ...

    @classmethod
    def FromString(cls, s: bytes) -> EnumValue: ...


class Option(Message):
    name: Text

    @property
    def value(self) -> Any: ...

    def __init__(self,
                 name: Optional[Text] = ...,
                 value: Optional[Any] = ...,
                 ) -> None: ...

    @classmethod
    def FromString(cls, s: bytes) -> Option: ...
