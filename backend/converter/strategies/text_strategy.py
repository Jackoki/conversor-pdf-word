from converter.strategies.base_strategy import BaseStrategy

class TextStrategy(BaseStrategy):
    def process(self, page, doc, index):
        blocks = page.get_text("blocks")

        for block in blocks:
            text = block[4].strip()
            if text:
                doc.add_paragraph(text)