# -*- coding: utf-8 -*-  # Encoding belirtmesi

import re
from collections import Counter

# Stopwords dosyasını yükle
stopwords_file = '/home/hadoop/stopwords.txt'
with open(stopwords_file, 'r', encoding='utf-8') as f:
    stopwords = set(f.read().splitlines())

# Kelime sayımını yapacak bir sayaç
word_counts = Counter()

# Metin dosyasını satır satır oku
input_file = '/home/hadoop/10GB.txt'
with open(input_file, 'r', encoding='utf-8') as f:
    for line in f:
        # Noktalama işaretlerini temizle ve kelimeleri küçük harfe çevir
        line = re.sub(r'[^\w\s]', '', line)  # Noktalama işaretlerini kaldır
        words = line.lower().split()  # Kelimeleri ayır ve küçük harfe çevir

        # Stopwords olmayan kelimeleri say
        filtered_words = [word for word in words if word not in stopwords]
        word_counts.update(filtered_words)

# En yüksekten en aza doğru sıralama
sorted_word_counts = word_counts.most_common()

# Çıktıyı dosyaya yaz
output_file = '/home/hadoop/word_count_sorted.txt'
with open(output_file, 'w', encoding='utf-8') as f:
    for word, count in sorted_word_counts:
        f.write(f"{word}: {count}\n")

# Türkçe karakterlere uygun olarak format() kullanarak çıktıyı yaz
print("Kelimelerin sayısı hesaplandı ve sıralandı. Sonuçlar {} dosyasına kaydedildi.".format(output_file))
