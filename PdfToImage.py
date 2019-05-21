#Python file to compare pdf docs 

import pdf2image

#comparing images
def pdf2img(src,dst="imgOut"):
    """
    (pdf file) -> jpg
    This functions returns image file of the give pdf file.
    pdf full path has to be given
    default output folder is imgOut
    """
    src = src.replace('/','\\')
    imgs = pdf2image.convert_from_path(src,100)
    i = 1
    for img in imgs:
        img.save(dst+"\\"+src[src.rfind('\\'):src.rfind('.pdf')]+str(i)+'.jpg')
        i+=1

pdf2img("data/prototype.pdf") #source file
pdf2img("data/sample.pdf") #test file
