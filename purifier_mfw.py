# -*- coding: utf-8 -*-
#skrypt zapisuje sparsowany plik xml na txt(http://www.mediawiki.org/wiki/Alternative_parsers, WikiParser C++) w formie 
#klucz
#Alergologia
#rak
#samochod
#itd
#do wczytania do bazy jako csv
#powstaje kolekcja:
#{_id : id, klucz: Alergologia }
import re
file=open("po.txt", "a")

with open("articles_in_plain_text.txt") as infile:
	for line in infile:
		tym=" ".join(line.split()).replace(',', '').replace('.', '').replace('”', '').replace('„', '').replace(':', '').replace(';', '').replace('{', '').replace('}', '').replace('-', '').replace('(', '').replace(')', '')
		file.write(tym.replace(' ', '\n'))