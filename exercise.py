a = 65534  # FF FE
b = 65535  # FF FF
c = 65536  # 00 01 00 00
x = 2998302  # 00 2D C0 1E

with open("binary2", 'bw') as bin_file2:
    bin_file2.write(a.to_bytes(2, 'big'))
    bin_file2.write(b.to_bytes(2, 'big'))
    bin_file2.write(c.to_bytes(4, 'big'))
    bin_file2.write(x.to_bytes(4, 'big'))
    bin_file2.write(x.to_bytes(4, 'little'))


