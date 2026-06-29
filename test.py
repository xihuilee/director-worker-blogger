from pdf_ingest import extract_text

text = extract_text(
    "input/00001_excerpt.pdf"
)

print(text[:1000])