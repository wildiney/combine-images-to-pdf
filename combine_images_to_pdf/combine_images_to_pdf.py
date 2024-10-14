import os
from PIL import Image
from reportlab.pdfgen import canvas


def combine_images_to_pdf(image_folder, output_pdf_path):
    # Obtém a lista de arquivos JPEG no diretório
    image_files = [f for f in os.listdir(image_folder) if f.endswith('.jpg')]
    image_files.sort()  # Ordena as imagens numericamente (se necessário)

    # Cria um objeto Canvas para o PDF
    c = canvas.Canvas("output/"+output_pdf_path)

    for image_file in image_files:
        image_path = os.path.join(image_folder, image_file)

        # Abre a imagem usando Pillow
        with Image.open(image_path) as img:
            # Converte a imagem para RGB (se necessário)
            img = img.convert('RGB')

            # Adiciona a imagem ao PDF
            c.setPageSize((img.width, img.height))
            c.drawImage(image_path, 0, 0, width=img.width, height=img.height)
            c.showPage()  # Avança para a próxima página do PDF

    # Salva o PDF
    c.save()
    print(f"PDF criado em: {output_pdf_path}")


# Exemplo de uso
if __name__ == "__main__":
    # Altere para o caminho onde suas imagens estão localizadas
    image_folder = input("Insert the path for the images folder: ")
    output_pdf_path = input("Save as: ") + ".pdf"

    combine_images_to_pdf(image_folder, output_pdf_path)
