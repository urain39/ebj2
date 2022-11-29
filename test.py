import io
import ebj2


def test(x):
  buf = io.BytesIO()
  ebj2.dump(x, buf)
  buf.seek(0)
  assert ebj2.load(buf) == x
  assert ebj2.loads(ebj2.dumps(x)) == x


# INT8
for n in range(-128, 127):
  test(n)


# INT16
for n in range(-32768, 32767, 256):
  test(n)


# INT32
for n in range(-2147483648, 2147483647, 268435456):
  test(n)


# INT64
for n in range(-9223372036854775808, 9223372036854775807, 1152921504606846976):
  test(n)


# XXX: FLOAT32


# FLOAT64
for n in range(-9223372036854775808, 9223372036854775807, 1152921504606846976):
  test(1/(n-1))


# STR8
for n in range(0, 255):
  test('\x00' * n)


# STR32
for n in range(0, 65536, 256):
  test('\x00' * n)


# REF8
for n in range(0, 255):
  test(['\x00'] * n)


# REF32
for n in range(0, 512, 256):
  test(['\x00'] * n)


# True, False and None
for n in (True, False, None):
  test(n)


# ARRAY
test([])
test([1, 2, 3])
test([True, False, None])
test(['abc', True, None, 1, -2, 3.0, {}, []])
test([[1], [1], [[2], [[{0: []}], [0, [789922]]]]])


# OBJECT
test({})
test({'abc': []})
test({'abc': [], 'cba': {False: None}})
test([{'abc': []}, {None: [{}]}])
test({3.0: [{999: {'b': 'b'}}, 'b', {}]})
