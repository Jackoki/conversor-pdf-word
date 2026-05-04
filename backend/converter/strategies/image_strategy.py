import os
from docx.shared import Inches
from converter.strategies.base_strategy import BaseStrategy

class ImageStrategy(BaseStrategy):
    def process(self, page, doc, index):
        pix = page.get_pixmap()
        path = f"temp_page_{index}.png"
        pix.save(path)

        doc.add_picture(path, width=Inches(6))

        # limpa arquivo temporário
        os.remove(path)