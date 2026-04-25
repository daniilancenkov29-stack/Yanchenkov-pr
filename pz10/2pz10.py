with open("text18-24.txt", "r", encoding="utf-8") as f:
    content = f.read()

print(content)
letter_count = sum(1 for ch in content if ch.isalpha())
print(f"\n{letter_count}")

with open("poem_upper.txt", "w", encoding="utf-8") as f:
    f.write(content.upper())