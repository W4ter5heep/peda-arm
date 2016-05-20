kSmiTag = 0
kSmiTagSize = 1
kSmiTagMask = (1 << kSmiTagSize) - 1
kHeapObjectTag = 1
kHeapObjectTagSize = 2
kHeapObjectTagMask = (1 << kHeapObjectTagSize) - 1
kFailureTag = 3
kFailureTagSize = 2
kFailureTagMask = (1 << kFailureTagSize) - 1
kSmiShiftSize32 = 0
kSmiValueSize32 = 31
kSmiShiftBits32 = kSmiTagSize + kSmiShiftSize32
kSmiShiftSize64 = 31
kSmiValueSize64 = 32
kSmiShiftBits64 = kSmiTagSize + kSmiShiftSize64
kAllBits = 0xFFFFFFFF
kTopBit32 = 0x80000000
kTopBit64 = 0x8000000000000000
# t_u32 = gdb.lookup_type('unsigned int')
# t_u64 = gdb.lookup_type('unsigned long long')

KB = 1024
MB = KB * KB
GB = KB * KB * KB
kMaxInt = 0x7FFFFFFF
kMinInt = -kMaxInt - 1
kMaxInt8 = (1 << 7) - 1
kMinInt8 = -(1 << 7)
kMaxUInt8 = (1 << 8) - 1
kMinUInt8 = 0
kMaxInt16 = (1 << 15) - 1
kMinInt16 = -(1 << 15)
kMaxUInt16 = (1 << 16) - 1
kMinUInt16 = 0
kMaxUInt32 = 0xFFFFFFFF

kCharSize = 1
kShortSize = 2
kIntSize = 4
kInt32Size = 4
kInt64Size = 8
kDoubleSize = 8
kIntptrSize = 4
kPointerSize = 4

kRegisterSize = kPointerSize
kPCOnStackSize = kRegisterSize
kFPOnStackSize = kRegisterSize

kDoubleSizeLog2 = 3
kPointerSizeLog2 = 2
kIntptrSignBit = 0x80000000
kUintptrAllBitsSet = 0xFFFFFFFF
kRequiresCodeRange = False
kMaximalCodeRangeSize = 0 * MB

kBitsPerByte = 8
kBitsPerByteLog2 = 3
kBitsPerPointer = kPointerSize * kBitsPerByte
kBitsPerInt = kIntSize * kBitsPerByte

# IEEE 754 single precision floating point number bit layout.
kBinary32SignMask = 0x80000000
kBinary32ExponentMask = 0x7f800000
kBinary32MantissaMask = 0x007fffff
kBinary32ExponentBias = 127
kBinary32MaxExponent = 0xFE
kBinary32MinExponent = 0x01
kBinary32MantissaBits = 23
kBinary32ExponentShift = 23

# Quiet NaNs have bits 51 to 62 set, possibly the sign bit, and no
# other bits set.
kQuietNaNMask = (1 << 64 - 1) & (0xfff << 51)

# Latin1/UTF-16 constants
# Code-point values in Unicode 4.0 are 21 bits wide.
# Code units in UTF-16 are 16 bits wide.

kOneByteSize = kCharSize
kUC16Size = 2

# We use the full 8 bits of the instance_type field to encode heap object
# instance types.  The high-order bit (bit 7) is set if the object is not a
# string, and cleared if it is a string.
kIsNotStringMask = 0x80
kStringTag = 0x0
kNotStringTag = 0x80

# Bit 6 indicates that the object is an internalized string (if set) or not.
# Bit 7 has to be clear as well.
kIsNotInternalizedMask = 0x40
kNotInternalizedTag = 0x40
kInternalizedTag = 0x0

# If bit 7 is clear then bit 2 indicates whether the string consists of
# two-byte characters or one-byte characters.
kStringEncodingMask = 0x4
kTwoByteStringTag = 0x0
kOneByteStringTag = 0x4

# If bit 7 is clear, the low-order 2 bits indicate the representation
# of the string.
kStringRepresentationMask = 0x03

kSeqStringTag = 0x0
kConsStringTag = 0x1
kExternalStringTag = 0x2
kSlicedStringTag = 0x3

kIsIndirectStringMask = 0x1
kIsIndirectStringTag = 0x1
# Use this mask to distinguish between cons and slice only after making
# sure that the string is one of the two (an indirect string).
kSlicedNotConsMask = kSlicedStringTag & ~kConsStringTag

# If bit 7 is clear, then bit 3 indicates whether this two-byte
# string actually contains one byte data.
kOneByteDataHintMask = 0x08
kOneByteDataHintTag = 0x08

# If bit 7 is clear and string representation indicates an external string,
# then bit 4 indicates whether the data pointer is cached.
kShortExternalStringMask = 0x10
kShortExternalStringTag = 0x10

# A ConsString with an empty string as the right side is a candidate
# for being shortcut by the garbage collector. We don't allocate any
# non-flat internalized strings, so we do not shortcut them thereby
# avoiding turning internalized strings into strings. The bit-masks
# below contain the internalized bit as additional safety.
# See heap.cc, mark-compact.cc and objects-visiting.cc.
kShortcutTypeMask = kIsNotStringMask | kIsNotInternalizedMask | kStringRepresentationMask
kShortcutTypeTag = kConsStringTag | kNotInternalizedTag


class InstanceType:
    # String types.
    INTERNALIZED_STRING_TYPE = kTwoByteStringTag | kSeqStringTag | kInternalizedTag
    ONE_BYTE_INTERNALIZED_STRING_TYPE = kOneByteStringTag | kSeqStringTag | kInternalizedTag
    EXTERNAL_INTERNALIZED_STRING_TYPE = kTwoByteStringTag | kExternalStringTag | kInternalizedTag
    EXTERNAL_ONE_BYTE_INTERNALIZED_STRING_TYPE = kOneByteStringTag | kExternalStringTag | kInternalizedTag
    EXTERNAL_INTERNALIZED_STRING_WITH_ONE_BYTE_DATA_TYPE = EXTERNAL_INTERNALIZED_STRING_TYPE | kOneByteDataHintTag | kInternalizedTag
    SHORT_EXTERNAL_INTERNALIZED_STRING_TYPE = EXTERNAL_INTERNALIZED_STRING_TYPE | kShortExternalStringTag | kInternalizedTag
    SHORT_EXTERNAL_ONE_BYTE_INTERNALIZED_STRING_TYPE = EXTERNAL_ONE_BYTE_INTERNALIZED_STRING_TYPE | kShortExternalStringTag | kInternalizedTag
    SHORT_EXTERNAL_INTERNALIZED_STRING_WITH_ONE_BYTE_DATA_TYPE = EXTERNAL_INTERNALIZED_STRING_WITH_ONE_BYTE_DATA_TYPE | kShortExternalStringTag | kInternalizedTag
    STRING_TYPE = INTERNALIZED_STRING_TYPE | kNotInternalizedTag
    ONE_BYTE_STRING_TYPE = ONE_BYTE_INTERNALIZED_STRING_TYPE | kNotInternalizedTag
    CONS_STRING_TYPE = kTwoByteStringTag | kConsStringTag | kNotInternalizedTag
    CONS_ONE_BYTE_STRING_TYPE = kOneByteStringTag | kConsStringTag | kNotInternalizedTag
    SLICED_STRING_TYPE = kTwoByteStringTag | kSlicedStringTag | kNotInternalizedTag
    SLICED_ONE_BYTE_STRING_TYPE = kOneByteStringTag | kSlicedStringTag | kNotInternalizedTag
    EXTERNAL_STRING_TYPE = EXTERNAL_INTERNALIZED_STRING_TYPE | kNotInternalizedTag
    EXTERNAL_ONE_BYTE_STRING_TYPE = EXTERNAL_ONE_BYTE_INTERNALIZED_STRING_TYPE | kNotInternalizedTag
    EXTERNAL_STRING_WITH_ONE_BYTE_DATA_TYPE = EXTERNAL_INTERNALIZED_STRING_WITH_ONE_BYTE_DATA_TYPE | kNotInternalizedTag
    SHORT_EXTERNAL_STRING_TYPE = SHORT_EXTERNAL_INTERNALIZED_STRING_TYPE | kNotInternalizedTag
    SHORT_EXTERNAL_ONE_BYTE_STRING_TYPE = SHORT_EXTERNAL_ONE_BYTE_INTERNALIZED_STRING_TYPE | kNotInternalizedTag
    SHORT_EXTERNAL_STRING_WITH_ONE_BYTE_DATA_TYPE = SHORT_EXTERNAL_INTERNALIZED_STRING_WITH_ONE_BYTE_DATA_TYPE | kNotInternalizedTag

    # Non-string names
    SYMBOL_TYPE = kNotStringTag
    # FIRST_NONSTRING_TYPE, LAST_NAME_TYPE

    MAP_TYPE, \
    CODE_TYPE, \
    ODDBALL_TYPE, \
    CELL_TYPE, \
    PROPERTY_CELL_TYPE, \
 \
    HEAP_NUMBER_TYPE, \
    MUTABLE_HEAP_NUMBER_TYPE, \
    FOREIGN_TYPE, \
    BYTE_ARRAY_TYPE, \
    FREE_SPACE_TYPE, \
    EXTERNAL_INT8_ARRAY_TYPE, \
    EXTERNAL_UINT8_ARRAY_TYPE, \
    EXTERNAL_INT16_ARRAY_TYPE, \
    EXTERNAL_UINT16_ARRAY_TYPE, \
    EXTERNAL_INT32_ARRAY_TYPE, \
    EXTERNAL_UINT32_ARRAY_TYPE, \
    EXTERNAL_FLOAT32_ARRAY_TYPE, \
    EXTERNAL_FLOAT64_ARRAY_TYPE, \
    EXTERNAL_UINT8_CLAMPED_ARRAY_TYPE, \
    FIXED_INT8_ARRAY_TYPE, \
    FIXED_UINT8_ARRAY_TYPE, \
    FIXED_INT16_ARRAY_TYPE, \
    FIXED_UINT16_ARRAY_TYPE, \
    FIXED_INT32_ARRAY_TYPE, \
    FIXED_UINT32_ARRAY_TYPE, \
    FIXED_FLOAT32_ARRAY_TYPE, \
    FIXED_FLOAT64_ARRAY_TYPE, \
    FIXED_UINT8_CLAMPED_ARRAY_TYPE, \
    FIXED_DOUBLE_ARRAY_TYPE, \
    FILLER_TYPE, \
 \
    DECLARED_ACCESSOR_DESCRIPTOR_TYPE, \
    DECLARED_ACCESSOR_INFO_TYPE, \
    EXECUTABLE_ACCESSOR_INFO_TYPE, \
    ACCESSOR_PAIR_TYPE, \
    ACCESS_CHECK_INFO_TYPE, \
    INTERCEPTOR_INFO_TYPE, \
    CALL_HANDLER_INFO_TYPE, \
    FUNCTION_TEMPLATE_INFO_TYPE, \
    OBJECT_TEMPLATE_INFO_TYPE, \
    SIGNATURE_INFO_TYPE, \
    TYPE_SWITCH_INFO_TYPE, \
    ALLOCATION_SITE_TYPE, \
    ALLOCATION_MEMENTO_TYPE, \
    SCRIPT_TYPE, \
    CODE_CACHE_TYPE, \
    POLYMORPHIC_CODE_CACHE_TYPE, \
    TYPE_FEEDBACK_INFO_TYPE, \
    ALIASED_ARGUMENTS_ENTRY_TYPE, \
    BOX_TYPE, \
    DEBUG_INFO_TYPE, \
    BREAK_POINT_INFO_TYPE, \
    FIXED_ARRAY_TYPE, \
    CONSTANT_POOL_ARRAY_TYPE, \
    SHARED_FUNCTION_INFO_TYPE, \
 \
    JS_FUNCTION_PROXY_TYPE, \
    JS_PROXY_TYPE, \
    JS_VALUE_TYPE, \
    JS_MESSAGE_OBJECT_TYPE, \
    JS_DATE_TYPE, \
    JS_OBJECT_TYPE, \
    JS_CONTEXT_EXTENSION_OBJECT_TYPE, \
    JS_GENERATOR_OBJECT_TYPE, \
    JS_MODULE_TYPE, \
    JS_GLOBAL_OBJECT_TYPE, \
    JS_BUILTINS_OBJECT_TYPE, \
    JS_GLOBAL_PROXY_TYPE, \
    JS_ARRAY_TYPE, \
    JS_ARRAY_BUFFER_TYPE, \
    JS_TYPED_ARRAY_TYPE, \
    JS_DATA_VIEW_TYPE, \
    JS_SET_TYPE, \
    JS_MAP_TYPE, \
    JS_SET_ITERATOR_TYPE, \
    JS_MAP_ITERATOR_TYPE, \
    JS_WEAK_MAP_TYPE, \
    JS_WEAK_SET_TYPE, \
    JS_REGEXP_TYPE, \
    JS_FUNCTION_TYPE = range(SYMBOL_TYPE + 1, SYMBOL_TYPE + 1 + 78)

    # Pseudo-types
    FIRST_TYPE = 0x0
    LAST_TYPE = JS_FUNCTION_TYPE
    FIRST_NAME_TYPE = FIRST_TYPE
    LAST_NAME_TYPE = SYMBOL_TYPE
    FIRST_UNIQUE_NAME_TYPE = INTERNALIZED_STRING_TYPE
    LAST_UNIQUE_NAME_TYPE = SYMBOL_TYPE
    FIRST_NONSTRING_TYPE = SYMBOL_TYPE
    # Boundaries for testing for an external array.
    FIRST_EXTERNAL_ARRAY_TYPE = EXTERNAL_INT8_ARRAY_TYPE
    LAST_EXTERNAL_ARRAY_TYPE = EXTERNAL_UINT8_CLAMPED_ARRAY_TYPE
    # Boundaries for testing for a fixed typed array.
    FIRST_FIXED_TYPED_ARRAY_TYPE = FIXED_INT8_ARRAY_TYPE
    LAST_FIXED_TYPED_ARRAY_TYPE = FIXED_UINT8_CLAMPED_ARRAY_TYPE
    # Boundary for promotion to old data space/old pointer space.
    LAST_DATA_TYPE = FILLER_TYPE
    # Boundary for objects represented as JSReceiver (i.e. JSObject or JSProxy).
    # Note that there is no range for JSObject or JSProxy, since their subtypes
    # are not continuous in this enum! The enum ranges instead reflect the
    # external class names, where proxies are treated as either ordinary objects,
    # or functions.
    FIRST_JS_RECEIVER_TYPE = JS_FUNCTION_PROXY_TYPE
    LAST_JS_RECEIVER_TYPE = LAST_TYPE
    # Boundaries for testing the types represented as JSObject
    FIRST_JS_OBJECT_TYPE = JS_VALUE_TYPE
    LAST_JS_OBJECT_TYPE = LAST_TYPE
    # Boundaries for testing the types represented as JSProxy
    FIRST_JS_PROXY_TYPE = JS_FUNCTION_PROXY_TYPE
    LAST_JS_PROXY_TYPE = JS_PROXY_TYPE
    # Boundaries for testing whether the type is a JavaScript object.
    FIRST_SPEC_OBJECT_TYPE = FIRST_JS_RECEIVER_TYPE
    LAST_SPEC_OBJECT_TYPE = LAST_JS_RECEIVER_TYPE
    # Boundaries for testing the types for which typeof is "object".
    FIRST_NONCALLABLE_SPEC_OBJECT_TYPE = JS_PROXY_TYPE
    LAST_NONCALLABLE_SPEC_OBJECT_TYPE = JS_REGEXP_TYPE
    # Note that the types for which typeof is "function" are not continuous.
    # Define this so that we can put assertions on discrete checks.
    NUM_OF_CALLABLE_SPEC_OBJECT_TYPES = 2
