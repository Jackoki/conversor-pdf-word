from pdf2docx import Converter as PDFConverter
import os

class Converter:
    def convert(self, input_path, output_path):
        if not os.path.exists(input_path):
            raise FileNotFoundError(f"Arquivo de entrada não encontrado: {input_path}")

        if not input_path.lower().endswith(".pdf"):
            raise ValueError("O arquivo de entrada deve ser um PDF")

        cv = PDFConverter(input_path)

        try:
            cv.convert(output_path, start=0, end=None, layout=True)
        finally:
            cv.close()