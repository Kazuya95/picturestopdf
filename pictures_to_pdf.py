from PIL import Image
from pathlib import Path

# merge pictures in an PDF file
def pic_pdf(directory,picture_list,final_name):
    # list used to save images in RGB format
    imagelist=[]
    # open first image from picture_list
    image1 = Image.open(r'{}/{}'.format(directory,picture_list[0]))
    # convert to rgb
    im1 = image1.convert('RGB')
    for i in range(1,len(picture_list)):
        # open each image from picture_list (after first)
        image = Image.open(r'{}/{}'.format(directory,picture_list[i]))
        # convert to rgb
        im = image.convert('RGB')
        # save in imagelist
        imagelist.append(im)
    # the destination folder
    # in this case, it will be kept in same folder
    directory2 = directory
    im1.save(r'{}/{}'.format(directory2,final_name),save_all=True, append_images=imagelist)

# example
##picture_list = ['image1.jpeg','image2.jpeg','image3.jpeg']
##directory =Path('C:/beginning')
##final_name = 'teste_pdf.pdf'
##pic_pdf(directory,picture_list,final_name)
