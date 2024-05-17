def reverse_bin(n: int) -> int:
    results = 0x00000000
    getmask = 0x00000001
    setmask = 0x80000000

    for _ in range(32):
        if n & getmask:
            results |= setmask
        getmask <<= getmask
        setmask >>= setmask
    return results
