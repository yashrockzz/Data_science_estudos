import chardet

file_path = r"C:\Users\Miguel\Documents\GitHub\udemy_data\data\fifa.csv"

with open(file_path, "rb") as f:
    result = chardet.detect(f.read(100000))  # lê 100KB
    print(result)
