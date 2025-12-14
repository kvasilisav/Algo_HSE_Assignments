def rabin_karp(text: str, pattern: str) -> list[int]:
    if not pattern or not text or len(pattern) > len(text):
        return []
    
    base, mod = 256, 10**9 + 7
    pattern_hash = 0
    window_hash = 0
    h = 1

    for _ in range(len(pattern) - 1):
        h = (h * base) % mod
    
    for i in range(len(pattern)):
        pattern_hash = (base * pattern_hash + ord(pattern[i])) % mod
        window_hash = (base * window_hash + ord(text[i])) % mod
    
    result = []
    for i in range(len(text) - len(pattern) + 1):
        if window_hash == pattern_hash and text[i:i+len(pattern)] == pattern:
            result.append(i)
        if i < len(text) - len(pattern):
            window_hash = (base * (window_hash - ord(text[i]) * h) + ord(text[i + len(pattern)])) % mod
            window_hash = (window_hash + mod) % mod
    
    return result