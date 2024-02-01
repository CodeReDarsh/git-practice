resident_str = """Ramisha
Janine
Alyssa
Rebecca
Nandita
Rosa
Yi
Nicholas
Matthew
Sean
Varun
Ansh
Mario
Aiden
Harrison
Avin
JasonZ
JasonC
Vincent
Huabin
Yaoting
Nisat
Caitlyn
Arin
Tiffany
Adrita
Sarah"""

gc_str = """Aanasa Nikhil Karkare
		
Adrita Arif
		
Aiden Latham
		
Alayna Garcia
		
Alo Chakravarty
		
Alyssa Cornell
		
Anastasia Karampimperis
		
Andrew Han
		
Angus Ning
		
Anjali Vishwanath
		
Ansh Garg
		
Anthony Lagano
		
Antim Baru
		
Arin Lee
		
Avin Mathew
		
Caitlyn Mark
		
Chris Tan
		
Daisy Buathatseephol
		
Daniel Yoo
		
Derrick Xie
		
Enya Myke
		
Eric Yang
		
Esther Kwon
		
Fanny Zheng
		
Gabriel O'Donnell
		
Gabriela Grajdianu
		
Gabriella Garber
		
Grace Wang
		
Harrison Bohrer
		
Helen Zeng
		
Huabin Ye
		
Isha Shah
		
Janine McKenzie
		
JasonC hen
		
JasonZ hen
		
Jeremy Cheung
		
Jimmy Chen
		
Johnny Chen
		
Jonathan Ng
		
Kashvi Khanchi
		
Katherine Moquete
		
Keyla Romero
		
Lingxi Chen
		
Lori Xia
		
Madeline Mulholland
		
Mario Reyes
		
Matthew Zhang
		
Maxim Savenkov
		
Megan Cheung
		
Nandita Das
		
Natalie Melendez
		
Nicholas Cipriano
		
Nicholas Desena
		
Nicole Hooshiari
		
Nisat Nosin
		
Ramisha Parvez
		
Rebecca Caliguiri
		
Rika Hayashi
		
Rosa Melendez
		
Saif Sahawneh
		
Sarah Chung
		
Sean Erfan
		
Steve Yang
		
Steven Chen
		
Tiffany Huang
		
Varun Dev
		
Vincent Dong
		
Weiyi Zhang
		
Yaoting Deng
		
Yi Xiao
		
Yoselin Garcia
		
Yuqing Yang
		
Yuxin Lin
		
Zehao Feng Feng"""

gc_set = set()

for name in gc_str.splitlines():
    if("\t" not in name):
        gc_set.add(name.split()[0])
    
    print("hello world my name is adarsh and I'm editing in vim wow.")
res_arr = resident_str.splitlines()

all_res_in = True

for fname in res_arr:
    if fname not in gc_set:
        all_res_in = False
        print(fname)

print("Are all residents in? ", all_res_in)
