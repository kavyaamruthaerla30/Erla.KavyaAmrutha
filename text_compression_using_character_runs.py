#Case Study 35: Text Compression Using Character Runswelc
def compress(text):
    if not text:
        return ""
    result, count = [], 1
    for index in range(1, len(text)):
        if text[index] == text[index - 1]:
            count += 1
        else:
            result.append(text[index - 1] + str(count))
            count = 1
    result.append(text[-1] + str(count))
    return "".join(result)

def main():
    original = input("Enter text to compress: ")
    encoded = compress(original)
    print("Compressed text:", encoded)
    print(f"Original length: {len(original)} | Compressed length: {len(encoded)}")

if __name__ == "__main__":
    main()
