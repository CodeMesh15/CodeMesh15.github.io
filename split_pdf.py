try:
    from pypdf import PdfReader, PdfWriter
except ImportError:
    import subprocess, sys
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'pypdf'])
    from pypdf import PdfReader, PdfWriter

reader = PdfReader('Notes - SDTBI.pdf')
writer = PdfWriter()

# User wants page 46 onwards. Index is 0-based, so page 46 is index 45.
for i in range(45, len(reader.pages)):
    writer.add_page(reader.pages[i])

output_filename = 'Notes - SDTBI_pg46_to_end.pdf'
with open(output_filename, 'wb') as f:
    writer.write(f)
print(f'Successfully split the PDF into {output_filename}.')
