with open("leetcode", "r") as file:
    header = file.readline()
    link = file.readline()
    code = file.read()


with open("result.txt", "w") as file:
    print("##", header, sep= " ", end= '\n', file = file)
    print(link, end='\n', file=file)
    print("```python", code, "```",  sep="\n", file = file)