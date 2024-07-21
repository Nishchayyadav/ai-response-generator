import markdown
import pdfkit

# Read the Markdown file
with open('input.txt', 'r') as md_file:
    md_content = md_file.read()

# Convert Markdown to HTML
html_content = markdown.markdown(md_content)

# Convert HTML to PDF
pdfkit.from_string(html_content, 'output.pdf')

print("Markdown has been converted to PDF successfully.")