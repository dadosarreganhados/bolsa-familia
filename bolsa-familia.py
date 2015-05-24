# coding: utf-8

import csv

from slugify import slugify

# ['UF', 'C\xf3digo SIAFI Munic\xedpio', 'Nome Munic\xedpio', 'C\xf3digo Fun\xe7\xe3o', 'C\xf3digo Subfun\xe7\xe3o', 'C\xf3digo Programa', 'C\xf3digo A\xe7\xe3o', 'NIS Favorecido', 'Nome Favorecido', 'Fonte-Finalidade', 'Valor Parcela', 'M\xeas Compet\xeancia']
# ['PE', '2471', 'LAGOA DO OURO', '08', '244', '1335', '8442', '00012422856057', 'MARCIA VITAL DE ARAUJO', 'CAIXA - Programa Bolsa Fam\xedlia', '185.00', '04/2015']


with open('files/2015-04.csv', 'rb') as csvfile:
    spamreader = csv.reader(csvfile, delimiter='\t', quotechar='|')
    for row in spamreader:
        file_name_slug = "{0}-{1}-{2}".format(row[0], row[8], row[10])
        file_name_slug = slugify(unicode(file_name_slug))
        file_name = file_name_slug + ".md"
        file_md = "UF: {0}\nNOME_MUNICIPIO: {1}\nCPF: {2}\nNOME: {3}\nVALOR: {4}\nTitle: {5} Date: {6}\n {7}".format(
            row[0],
            row[2],
            row[7],
            row[8],
            row[10],
            file_name_slug,
            "2015-01-01 00:00",
            row,
        )
        print("Gerando arquivo {0}".format(file_name))
        file_object = open("content/" + file_name, "w")
        file_object.write(file_md)
        file_object.close()
