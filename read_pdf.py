from PyPDF2 import PdfReader
reader = PdfReader("resources/docs-pytest-org-en-latest.pdf")
number_of_pages = len(reader.pages)
print(number_of_pages)
page = reader.pages[0]
text = page.extract_text()
print(text)
assert "2022" in text