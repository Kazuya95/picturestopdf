# junta as imagens e salva em um unico pdf
from PIL import Image
from pathlib import Path

# funcao para juntar imagens e converter em pdf
def pic_pdf(directory,picture_list,final_name):
    # onde serao salvos as imagens no formato rgb
    imagelist=[]
    # abre imagens
    image1 = Image.open(r'{}/{}'.format(directory,picture_list[0]))
    # converte em rgb
    im1 = image1.convert('RGB')
    for i in range(1,len(picture_list)):
        # abre imagens
        image = Image.open(r'{}/{}'.format(directory,picture_list[i]))
        # converte em rgb
        im = image.convert('RGB')
        # salva na lista imagelist
        imagelist.append(im)
    # salva no formato pdf
##    directory2 = Path('C:/Users/Johnny/Desktop/')
    directory2 = directory
    im1.save(r'{}/{}'.format(directory2,final_name),save_all=True, append_images=imagelist)


picture_list = ['horarios_2sem2020.jpeg']
directory =Path('C:/Users/oijkn_000/Desktop/conteiner/12sem')
final_name = 'teste_pdf.pdf'
pic_pdf(directory,picture_list,final_name)

##picture_list = ['WhatsApp Image 2021-03-03 at 12.04.48.jpeg','WhatsApp Image 2021-03-03 at 12.05.05.jpeg','WhatsApp Image 2021-03-03 at 12.05.19.jpeg','WhatsApp Image 2021-03-03 at 12.05.33.jpeg']
##directory =Path('C:/Users/Johnny/Desktop/12sem/I1/2020/p2')
##final_name = 'resolucao_prova2_Intalacoes_Johnny_Kazuya_Nakazono_RA15101421.pdf'
##pic_pdf(directory,picture_list,final_name)

##picture_list = ['WhatsApp Image 2021-03-01 at 16.34.51.jpeg','WhatsApp Image 2021-03-01 at 16.35.19.jpeg','WhatsApp Image 2021-03-01 at 16.35.32.jpeg','WhatsApp Image 2021-03-01 at 16.35.44.jpeg','WhatsApp Image 2021-03-01 at 16.36.03.jpeg']
##directory =Path('C:/Users/Johnny/Desktop/12sem/SEP/2020/p2')
##final_name = 'resolucao_prova_28_Johnny_Kazuya_Nakazono_RA15101421.pdf'
##pic_pdf(directory,picture_list,final_name)

##picture_list = ['51_enunciado.JPG', '52a_enunciado.JPG', '52b_enunciado.JPG', '53_enunciado.JPG', '54_enunciado.JPG']
##directory =Path('C:/Users/Johnny/Desktop/12sem/SEP/2020/exercicios_resolvidos_2/cap5_resolucao')
##final_name = 'enunciados_cap5_2020.pdf'
##pic_pdf(directory,picture_list,final_name)

### lista de imagens
##picture_list = ['51a.jpg', '51b.jpg', '51c.jpg', '51d.jpg', '51e.jpg', '52a.jpg', '52b.jpg', '52c.jpg', '52d.jpg', '52e.jpg', '52f.jpg', '52g.jpg', '52h.jpg', '52i.jpg', '53a.jpg', '53b.jpg', '53c.jpg', '53d.jpg', '53e.jpg', '53f.jpg', '53g.jpg', '54a.jpg', '54b.jpg', '54c.jpg', '54d.jpg', '54e.jpg', '54f.jpg']
##directory =Path('C:/Users/Johnny/Desktop/12sem/SEP/2020/exercicios_resolvidos_2/cap5_resolucao')
##final_name = 'cap5_resolucao.pdf'
##pic_pdf(directory,picture_list,final_name)

##picture_list = ['ted_mes01.jpeg', 'ted_mes03.jpeg', 'ted_mes04.jpeg', 'ted_mes05.jpeg', 'ted_mes07.jpeg', 'ted_mes09.jpeg', 'ted_mes10.jpeg']
##directory =Path('C:/Users/Johnny/Desktop/conteiner/contrato e recibos/2020/envio')
##final_name = 'comprovantes_ted2020.pdf'
##pic_pdf(directory,picture_list,final_name)

##path ='C:/Users/Johnny/Desktop/12sem/SEP/2020/lista1/'
##total_path = lambda imagem:f'{path}{imagem}'
##image1 = Image.open(r'C:/Users/Johnny/Desktop/12sem/SEP/2020/lista1/WhatsApp Image 2021-02-05 at 09.20.17.jpeg')
##image2 = Image.open(r'C:/Users/Johnny/Desktop/12sem/SEP/2020/lista1/WhatsApp Image 2021-02-05 at 09.20.39.jpeg')
##image3 = Image.open(r'C:/Users/Johnny/Desktop/12sem/SEP/2020/lista1/WhatsApp Image 2021-02-05 at 09.20.51.jpeg')
##image4 = Image.open(r'C:/Users/Johnny/Desktop/12sem/SEP/2020/lista1/WhatsApp Image 2021-02-05 at 09.21.09.jpeg')
##image5 = Image.open(r'C:/Users/Johnny/Desktop/12sem/SEP/2020/lista1/WhatsApp Image 2021-02-05 at 09.21.37.jpeg')
##image6 = Image.open(r'C:/Users/Johnny/Desktop/12sem/SEP/2020/lista1/WhatsApp Image 2021-02-05 at 09.21.56.jpeg')
##image7 = Image.open(r'C:/Users/Johnny/Desktop/12sem/SEP/2020/lista1/WhatsApp Image 2021-02-05 at 09.22.15.jpeg')
##image8 = Image.open(r'C:/Users/Johnny/Desktop/12sem/SEP/2020/lista1/WhatsApp Image 2021-02-05 at 09.22.42.jpeg')
##image9 = Image.open(r'C:/Users/Johnny/Desktop/12sem/SEP/2020/lista1/WhatsApp Image 2021-02-05 at 09.23.05.jpeg')
##image10 = Image.open(r'C:/Users/Johnny/Desktop/12sem/SEP/2020/lista1/WhatsApp Image 2021-02-05 at 09.23.30.jpeg')
##image11 = Image.open(r'C:/Users/Johnny/Desktop/12sem/SEP/2020/lista1/WhatsApp Image 2021-02-05 at 09.23.56.jpeg')
##image12 = Image.open(r'C:/Users/Johnny/Desktop/12sem/SEP/2020/lista1/WhatsApp Image 2021-02-05 at 09.24.55.jpeg')
##image13 = Image.open(r'C:/Users/Johnny/Desktop/12sem/SEP/2020/lista1/WhatsApp Image 2021-02-05 at 09.25.15.jpeg')
##image14 = Image.open(r'C:/Users/Johnny/Desktop/12sem/SEP/2020/lista1/WhatsApp Image 2021-02-05 at 09.25.50.jpeg')
##image15 = Image.open(r'C:/Users/Johnny/Desktop/12sem/SEP/2020/lista1/WhatsApp Image 2021-02-05 at 09.26.38.jpeg')
##image16 = Image.open(r'C:/Users/Johnny/Desktop/12sem/SEP/2020/lista1/WhatsApp Image 2021-02-05 at 09.27.03.jpeg')
##image17 = Image.open(r'C:/Users/Johnny/Desktop/12sem/SEP/2020/lista1/WhatsApp Image 2021-02-05 at 09.27.20.jpeg')
##image18 = Image.open(r'C:/Users/Johnny/Desktop/12sem/SEP/2020/lista1/WhatsApp Image 2021-02-05 at 09.27.42.jpeg')
##image19 = Image.open(r'C:/Users/Johnny/Desktop/12sem/SEP/2020/lista1/WhatsApp Image 2021-02-05 at 09.27.59.jpeg')
##image20 = Image.open(r'C:/Users/Johnny/Desktop/12sem/SEP/2020/lista1/WhatsApp Image 2021-02-05 at 09.28.25.jpeg')
##image21 = Image.open(r'C:/Users/Johnny/Desktop/12sem/SEP/2020/lista1/WhatsApp Image 2021-02-05 at 09.28.53.jpeg')
##image22 = Image.open(r'C:/Users/Johnny/Desktop/12sem/SEP/2020/lista1/WhatsApp Image 2021-02-05 at 09.29.23.jpeg')
##image23 = Image.open(r'C:/Users/Johnny/Desktop/12sem/SEP/2020/lista1/WhatsApp Image 2021-02-05 at 09.29.45.jpeg')
##image24 = Image.open(r'C:/Users/Johnny/Desktop/12sem/SEP/2020/lista1/WhatsApp Image 2021-02-05 at 09.30.09.jpeg')
##image25 = Image.open(r'C:/Users/Johnny/Desktop/12sem/SEP/2020/lista1/WhatsApp Image 2021-02-05 at 09.30.25.jpeg')
##image26 = Image.open(r'C:/Users/Johnny/Desktop/12sem/SEP/2020/lista1/WhatsApp Image 2021-02-05 at 09.30.49.jpeg')
##image27 = Image.open(r'C:/Users/Johnny/Desktop/12sem/SEP/2020/lista1/WhatsApp Image 2021-02-05 at 09.31.13.jpeg') 
## 
##im1 = image1.convert('RGB')
##im2 = image2.convert('RGB')
##im3 = image3.convert('RGB')
##im4 = image4.convert('RGB')
##im5 = image5.convert('RGB')
##im6 = image6.convert('RGB')
##im7 = image7.convert('RGB')
##im8 = image8.convert('RGB')
##im9 = image9.convert('RGB')
##im10 = image10.convert('RGB')
##im11 = image11.convert('RGB')
##im12 = image12.convert('RGB')
##im13 = image13.convert('RGB')
##im14 = image14.convert('RGB')
##im15 = image15.convert('RGB')
##im16 = image16.convert('RGB')
##im17 = image17.convert('RGB')
##im18 = image18.convert('RGB')
##im19 = image19.convert('RGB')
##im20 = image20.convert('RGB')
##im21 = image21.convert('RGB')
##im22 = image22.convert('RGB')
##im23 = image23.convert('RGB')
##im24 = image24.convert('RGB')
##im25 = image25.convert('RGB')
##im26 = image26.convert('RGB')
##im27 = image27.convert('RGB')
##
##imagelist = [im2, im3, im4, im5, im6, im7, im8, im9, im10, im11, im12, im13, im14, im15, im16, im17, im18, im19, im20, im21, im22, im23, im24, im25, im26, im27]
##
##im1.save(r'C:/Users/Johnny/Desktop/12sem/SEP/2020/lista1/lista1_JohnnyKazuyaNakazonoRA151010421.pdf',save_all=True, append_images=imagelist)


##path ='C:/Users/Johnny/Desktop/12sem/geracao/2020/aula9/'
##total_path = lambda imagem:f'{path}{imagem}'
##image1 = Image.open(r'C:/Users/Johnny/Desktop/12sem/geracao/2020/aula9/solar1de2.jpeg')
##image2 = Image.open(r'C:/Users/Johnny/Desktop/12sem/geracao/2020/aula9/solar2de2.jpeg')
##
##im1 = image1.convert('RGB')
##im2 = image2.convert('RGB')
##
##imagelist = [im2]
##
##im1.save(r'C:/Users/Johnny/Desktop/12sem/geracao/2020/aula9//lista_solar_JohnnyKazuyaNakazonoRA151010421.pdf',save_all=True, append_images=imagelist)

##path ='C:/Users/Johnny/Desktop/12sem/ME1/2020/segunda/p2'
##total_path = lambda imagem:f'{path}{imagem}'
##image1 = Image.open(r'C:/Users/Johnny/Desktop/12sem/ME1/2020/segunda/p2/WhatsApp Image 2021-02-26 at 11.52.14.jpeg')
##image2 = Image.open(r'C:/Users/Johnny/Desktop/12sem/ME1/2020/segunda/p2/WhatsApp Image 2021-02-26 at 11.52.29.jpeg')
##image3 = Image.open(r'C:/Users/Johnny/Desktop/12sem/ME1/2020/segunda/p2/WhatsApp Image 2021-02-26 at 11.52.43.jpeg')
##image4 = Image.open(r'C:/Users/Johnny/Desktop/12sem/ME1/2020/segunda/p2/WhatsApp Image 2021-02-26 at 11.52.59.jpeg')
##image5 = Image.open(r'C:/Users/Johnny/Desktop/12sem/ME1/2020/segunda/p2/WhatsApp Image 2021-02-26 at 11.53.30.jpeg')
##image6 = Image.open(r'C:/Users/Johnny/Desktop/12sem/ME1/2020/segunda/p2/WhatsApp Image 2021-02-26 at 11.53.46.jpeg')
##
##im1 = image1.convert('RGB')
##im2 = image2.convert('RGB')
##im3 = image3.convert('RGB')
##im4 = image4.convert('RGB')
##im5 = image5.convert('RGB')
##im6 = image6.convert('RGB')
##
##imagelist = [im2,im3,im4,im5,im6]
##
##im1.save(r'C:/Users/Johnny/Desktop/12sem/ME1/2020/segunda/p2/prova2_JohnnyKazuyaNakazonoRA151010421.pdf',save_all=True, append_images=imagelist)

##path ='C:/Users/Johnny/Desktop/12sem/SEP/2020/lista2'
##total_path = lambda imagem:f'{path}{imagem}'
##image1 = Image.open(r'C:/Users/Johnny/Desktop/12sem/SEP/2020/lista2/lista2_1.jpeg')
##image2 = Image.open(r'C:/Users/Johnny/Desktop/12sem/SEP/2020/lista2/lista2_3.jpeg')
##image3 = Image.open(r'C:/Users/Johnny/Desktop/12sem/SEP/2020/lista2/lista2_5b.jpeg')
##image4 = Image.open(r'C:/Users/Johnny/Desktop/12sem/SEP/2020/lista2/lista2_12e13.jpeg')
##image5 = Image.open(r'C:/Users/Johnny/Desktop/12sem/SEP/2020/lista2/lista2_14.jpeg')
##image6 = Image.open(r'C:/Users/Johnny/Desktop/12sem/SEP/2020/lista2/lista2_15.jpeg')
##image7 = Image.open(r'C:/Users/Johnny/Desktop/12sem/SEP/2020/lista2/lista2_16.jpeg')
##image8 = Image.open(r'C:/Users/Johnny/Desktop/12sem/SEP/2020/lista2/lista2_17.jpeg')
##image9 = Image.open(r'C:/Users/Johnny/Desktop/12sem/SEP/2020/lista2/lista2_18.jpeg')
##image10 = Image.open(r'C:/Users/Johnny/Desktop/12sem/SEP/2020/lista2/lista2_19e20.jpeg')
##image11 = Image.open(r'C:/Users/Johnny/Desktop/12sem/SEP/2020/lista2/lista2_21e22.jpeg')
##image12 = Image.open(r'C:/Users/Johnny/Desktop/12sem/SEP/2020/lista2/lista2_22b.jpeg')
##
##im1 = image1.convert('RGB')
##im2 = image2.convert('RGB')
##im3 = image3.convert('RGB')
##im4 = image4.convert('RGB')
##im5 = image5.convert('RGB')
##im6 = image6.convert('RGB')
##im7 = image7.convert('RGB')
##im8 = image8.convert('RGB')
##im9 = image9.convert('RGB')
##im10 = image10.convert('RGB')
##im11 = image11.convert('RGB')
##im12 = image12.convert('RGB')
##
##imagelist = [im2,im3,im4,im5,im6,im7,im8,im9,im10,im11,im12]
##
##im1.save(r'C:/Users/Johnny/Desktop/12sem/SEP/2020/lista2/lista2_sep_JohnnyKazuyaNakazonoRA151010421.pdf',save_all=True, append_images=imagelist)


# lista de imagens
##picture_list = ['solar1de2.jpeg','solar2de2.jpeg']
##directory =Path('C:/Users/Johnny/Desktop/12sem/geracao/2020/aula9')
##final_name = 'lista_solar_test.pdf'
##pic_pdf(directory,picture_list,final_name)
