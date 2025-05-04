from pdf2image import convert_from_path
import pytesseract
import os
import time

pytesseract.pytesseract.tesseract_cmd = "/opt/homebrew/bin/tesseract"

def ocr_pdf(pdf_path, output_txt_path, dpi=300, lang='hin+san'):
    start_time = time.time()

    temp_dir = 'temp_pages'
    os.makedirs(temp_dir, exist_ok=True)

    print("Converting PDF pages to images...")
    pages = convert_from_path(pdf_path, dpi=dpi, poppler_path="/opt/homebrew/bin"

    image_paths = []
    for i, page in enumerate(pages):
        image_path = os.path.join(temp_dir, f"page_{i+1}.png")
        page.save(image_path, 'PNG')
        image_paths.append(image_path)

    print("Running OCR on images...")
    ocr_text = ""
    for image_path in image_paths:
        text = pytesseract.image_to_string(image_path, lang=lang)
        ocr_text += text + "\n\n"

    with open(output_txt_path, 'w', encoding='utf-8') as f:
        f.write(ocr_text)

    for image_path in image_paths:
        os.remove(image_path)
    os.rmdir(temp_dir)

    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"OCR complete! Text saved to {output_txt_path}")
    print(f"Total time taken: {elapsed_time:.2f} seconds")

if __name__ == "__main__":
    input_file = input("Enter the input PDF filename (with .pdf extension): ").strip()
    output_file = input("Enter the desired output TXT filename (with .txt extension): ").strip()

    pdf_file_path = os.path.join(os.getcwd(), input_file)
    output_text_file = os.path.join(os.getcwd(), output_file)

    ocr_pdf(pdf_file_path, output_text_file)
