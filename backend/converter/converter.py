import os
import fitz
from docx import Document

from converter.strategies.text_strategy import TextStrategy
from converter.strategies.image_strategy import ImageStrategy
from converter.strategies.hybrid_strategy import HybridStrategy

class Converter:
    def __init__(self, mode="hybrid"):
        self.mode = mode

    def convert(self, input_path, output_path):
        if not os.path.exists(input_path):
            raise FileNotFoundError(f"Arquivo não encontrado: {input_path}")

        pdf = fitz.open(input_path)
        doc = Document()

        strategy = self._get_strategy()

        for i, page in enumerate(pdf):
            strategy.process(page, doc, i)

        doc.save(output_path)

    def _get_strategy(self):
        if self.mode == "text":
            return TextStrategy()
        elif self.mode == "image":
            return ImageStrategy()
        elif self.mode == "hybrid":
            return HybridStrategy()
        else:
            raise ValueError("Modo inválido")