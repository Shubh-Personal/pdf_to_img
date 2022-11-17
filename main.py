import os
import pypdfium2 as pdfium


def __convert_pdf_to_image(file_path):
    file_path = "./BMO/RATE_RESET (1).pdf"
    dpi = 300  # choose desired dpi here
    zoom = dpi / 72  # zoom factor, standard: 72 dpi
    magnify = fitz.Matrix(zoom, zoom)  # magnifies in x, resp. y direction
    doc = fitz.open(file_path)  # open document
    os.mkdir("BMO_IMG")
    for page in doc:
        pix = page.get_pixmap(matrix=magnify)  # render page to an image
        pix.save(f"./BMO_IMG/page-{page.number}.png")

def __convert_to_img_pypdf(pdfPath):
    splittedName = pdfPath.split("/")
    fileName = splittedName[2].split(".")[0]
    dirName = splittedName[1]
    pdf = pdfium.PdfDocument(pdfPath)
    page = pdf.get_page(0)
    pil_image = page.render_topil(
        scale=1,
        rotation=0,
        crop=(0, 0, 0, 0),
        greyscale=False,
        optimise_mode=pdfium.OptimiseMode.NONE,
    )
    
    if not os.path.exists(f"./images"):
        os.mkdir(f"./images")

    if not os.path.exists(f"./images/{dirName}_Image"):
        os.mkdir(f"./images/{dirName}_Image")
    print(f"./images/{dirName}_Image/{dirName}_{fileName}.png file created!")
    pil_image.save(f"./images/{dirName}_Image/{dirName}_{fileName}.png")

dir = os.listdir()

for i in dir:
    if os.path.isdir(i):
        fullDir = next(os.walk(i))
        for j in fullDir[2]:
            pdfFile = f"./{fullDir[0]}/{j}"
            __convert_to_img_pypdf(pdfFile)

