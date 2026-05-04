import os
from converter.converter import Converter

def main():
    try:
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))

        input_path = os.path.join(BASE_DIR, "files", "input", "teste.pdf")
        output_path = os.path.join(BASE_DIR, "files", "output", "teste.docx")

        os.makedirs(os.path.dirname(output_path), exist_ok=True)

        # 🔥 modo: "text", "image", "hybrid"
        converter = Converter(mode="hybrid")

        converter.convert(input_path, output_path)

        print("Conversão realizada com sucesso!")
        print(f"Arquivo gerado em: {output_path}")

    except Exception as e:
        print("Erro durante a conversão:")
        print(e)

if __name__ == "__main__":
    main()