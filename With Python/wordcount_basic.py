import re
from collections import Counter

def word_count(file_path):
    word_counts = Counter()
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:  # 'ignore' ile hatalı karakterleri yoksay
        for line in file:
            words = re.findall(r'\w+', line.lower())  # Satır satır kelimeleri ayıkla
            word_counts.update(words)
    return word_counts

if __name__ == '__main__':
    file_path = '1GB.txt'  # Dosyanın yolu
    word_counts = word_count(file_path)

    # Sonuçları output.txt dosyasına yazdır
    with open('output.txt', 'w', encoding='utf-8') as output_file:
        for word, count in word_counts.items():

            output_file.write(f"{word}: {count}\n")  # Sonuçları dosyaya yaz










