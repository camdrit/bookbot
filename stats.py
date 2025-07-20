def count_words(text):
    return len(text.split())

def count_char_occurances(text):
    chars = {}
    words = text.lower()
    for char in words:
        if char not in chars:
            chars[char] = 1
        else:
            chars[char] += 1
    return chars

def sort_on(items):
    return items["num"]

def make_report(stats):
    sorted = []
    for char, count in stats.items():
        sorted.append({ "char": char, "num": count })
    sorted.sort(reverse=True, key=sort_on)
    return sorted