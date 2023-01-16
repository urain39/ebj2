# Embedded Binary JSON

### What is EBJ?

EBJ is a format that focuses on storing binary json use RIGHT size.

### Byte Order

EBJ always use little-endian. It is more friendly for morden CPU to parse.

### Type Codes

```txt
0x00 int8
0x01 int16
0x02 int32
0x03 int64
0x04 float32
0x05 float64
0x06 str8 (uint8 length)
0x07 str32 (uint32 length)
0x08 ref8 (str only)
0x09 ref32 (str only)
0x0A true
0x0B false
0x0C null
0x0D array
0x0E end (array, object)
0x0F object
0x10 0
0x11 1
0x12 2
...
0xFF 239
```

> EBJ strXX should be encoded as UTF-8 bytes.

### How to use EBJ?

This repo contains a basic Python version EBJ implementation called `ebj2`. The
following lines show how to use `ebj2` to dump and load EBJ bytes.

Install:
```sh
pip install ebj2
```

Usage:
```py
# Load module
import ebj2

# Dump EBJ
byts = ebj2.dumps(['ebj2 is awesome!'])

# Load EBJ
msgs = ebj2.loads(byts)

# Dump to fp
ebj2.dump([], fp)

# Load from fp
ebj2.load(fp)
```

### Why should i use EBJ?

At least EBJ will save your 33% disk space to store json. Also it is very fast.
(`ebj2` maybe very slow, because it use pure-python, but still usable)
