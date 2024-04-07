import os

def find_pdf_size(top):
    total_size = 0
    for root, dirs, files in os.walk(top):
        for file in files:
            if file.endswith('.pdf'):
                filepath = os.path.join(root, file)
                total_size += os.path.getsize(filepath)
    return total_size

# Example:
print(f"Total size of PDF files in current directory is {find_pdf_size('.')} bytes.")
