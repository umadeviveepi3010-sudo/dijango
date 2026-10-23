from pathlib import Path
import PyPDF2

pdf_path = Path(r"c:/Users/veepi/Downloads/Umadevi_Veepi_CV.pdf")
out_path = Path(r"c:/Users/veepi/OneDrive/Desktop/Django portfolio/myportfolio/cv_text.txt")

with pdf_path.open('rb') as f:
    reader = PyPDF2.PdfReader(f)
    text = '\n\n'.join((page.extract_text() or '') for page in reader.pages)

out_path.write_text(text, encoding='utf-8')
print('written', out_path)
