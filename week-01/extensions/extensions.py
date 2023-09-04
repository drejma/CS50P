# https://cs50.harvard.edu/python/2022/psets/1/extensions/
# Prints MIME type of a given file's extension

# Prompt user to input file
file = input("File name: ")

# Remove leading and trailing spaces, make it lowercase
file = file.strip().lower()

# Print extension's MIME type
if file.endswith(".gif"):
    print("image/gif")
elif file.endswith(".jpg") or file.endswith(".jpeg"):
    print("image/jpeg")
elif file.endswith(".png"):
    print("image/png")
elif file.endswith(".pdf"):
    print("application/pdf")
elif file.endswith(".txt"):
    print("text/plain")
elif file.endswith(".zip"):
    print("application/zip")
else:
    print("application/octet-stream")