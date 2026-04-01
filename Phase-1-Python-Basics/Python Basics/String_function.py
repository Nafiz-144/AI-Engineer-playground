# ==============================
# Python String Functions Demo
# ==============================

text = "  hello world  "
name = "john123"

# 🔹 Case Conversion
print("upper():", text.upper())
print("lower():", text.lower())
print("title():", text.title())
print("capitalize():", text.capitalize())

# 🔹 Searching & Checking
print("find('o'):", text.find("o"))
# print("index('x'):", text.index("x"))  # Will give error if not found
print("startswith('  he'):", text.startswith("  he"))
print("endswith('ld  '):", text.endswith("ld  "))
print("'he' in text:", "he" in text)

# 🔹 Modifying Strings
print("replace('l','x'):", text.replace("l", "x"))
print("strip():", text.strip())
print("lstrip():", text.lstrip())
print("rstrip():", text.rstrip())

# 🔹 Splitting & Joining
data = "a,b,c"
split_data = data.split(",")
print("split():", split_data)
print("join():", ",".join(split_data))

# 🔹 Checking String Content
print("isalpha():", name.isalpha())
print("isdigit():", name.isdigit())
print("isalnum():", name.isalnum())
print("isspace():", text.isspace())

# 🔹 Formatting Strings
print("format():", "My name is {}".format("John"))

person = "John"
print("f-string:", f"My name is {person}")

# 🔹 Length & Counting
print("len():", len(text))
print("count('l'):", text.count("l"))

# 🔹 Other Useful Functions
print("swapcase():", text.swapcase())
print("center(20):", text.center(20, "*"))
print("ljust(20):", text.ljust(20, "-"))
print("rjust(20):", text.rjust(20, "-"))
print("zfill(10):", "123".zfill(10))

# ==============================
# End of Program
# ==============================