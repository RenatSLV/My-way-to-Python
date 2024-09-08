from itertools import permutations

def generate_words(sequence):
    # Подсчёт букв в нашой последовательности
    original_counts = {char: sequence.count(char) for char in set(sequence)}
    
    # Генерация всех возможных уникальных комбинаций букв разной длины
    valid_words = set()
    for r in range(1, len(sequence) + 1):
        for combo in permutations(sequence, r):
            word = ''.join(combo)
            word_counts = {char: word.count(char) for char in set(word)}
            if all(word_counts[char] <= original_counts[char] for char in word_counts):
                valid_words.add(word)
    
    # Сортируем слова по длине
    sorted_words = sorted(valid_words, key=len)
    
    return sorted_words, len(sorted_words)

# Пример использования
sequence = "abc"
words, count = generate_words(sequence)
print(f"Words: {words}")
print(f"Count: {count}")