import os
from converter.converter import Converter

def main():
    try:
    input_path = os.path.abspath("files/input/teste.pdf")
    output_path = os.path.abspath("files/output/teste.docx")


        # Garante que a pasta de saída existe
        os.makedirs(os.path.dirname(output_path), exist_ok=True)

        # Instancia o converter
        converter = Converter()

        # Executa a conversão
        converter.convert(input_path, output_path)

        print("Conversão realizada com sucesso!")
        print(f"Arquivo gerado em: {output_path}")

    except Exception as e:
        print("Erro durante a conversão:")
        print(e)

    if **name** == "**main**":
    main()
