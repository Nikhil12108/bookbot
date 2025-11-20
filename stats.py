def word_count(text):
    words = text.split()
    return len(words)

def character_count(text):
    char_counts = {}
    for char in text:
        char = char.lower()
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    return char_counts

__all__ = ["word_count", "character_count"]