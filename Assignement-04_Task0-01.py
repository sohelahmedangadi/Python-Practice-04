try:
    with open("sample.txt", "r") as f:
        lines = f.readlines()

    print("Reading file content:")
    count = 1
    for line in lines:
        print(f"Line{count}: {line.strip()}")
        count += 1

except FileNotFoundError:
    print("Error: The file 'sample.txt' was not found.")

