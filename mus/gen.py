import random
import numpy
import os

def makemydir(whatever):
  try:
    os.makedirs(whatever)
  except OSError:
    pass



notes=["DO","RE","MI","FA","SOL","LA","SI","DOd","REd","FAd","SOLd","Lad"]

notes=["DO","FAd","SI","LAd"]

notes=["DO","MI","SOL"]


notes=["DO","RE","MI","FA","SOL","LA","SI"]


voisins=[8,10, 14,15,7,1,2]

currnote=0

rythmes=[0.25, 0.5, 0.75, 1, 1.5, 2]


min_duree=0.1
max_duree=4.0
min_octave=2
max_octave=2
min_tempo=130
max_tempo=180
nb_temps=4
ln="\n"
sep="_____________________"

name=["blip","blop","ting","hey","swag","camille","la","chenille","mynamejeff","augustinboloss","alexiz","kameliaz","danyz","bricez","yes","salamandre","stagiaire","laputaindetarace","lapureesamere"]

folder="mus"
path=folder+"/"


def rand_name(part=4):
	file=random.choice(name)
	part=part-1
	for i in range(part):
		file+="_"+random.choice(name)
	file+=".mus"
	return file

def rand_note():
    global currnote
    idx = []
    l=0
    for x in voisins:
        l+=x
        idx.append(l)
    c = random.uniform(0,idx[-1]);
    i=0
    while i+1 < len(idx) and not ( idx[i] < c and c < idx[i+1]):
        i+=1
    currnote += i;
    currnote %= len(notes)
    return notes[currnote]

def rand_duration():
	duree = random.uniform(min_duree,max_duree)
	duree = numpy.random.normal(2,1.5)
	duree = random.choice(rythmes)
	return round(duree,2)

def make_line(note,duree):
	line=str(note)+":"+str(duree)+ln
	return line

def rand_line():
	line=make_line(rand_note(),rand_duration())
	return line

def rand_octave():
	return str(random.randint(min_octave,max_octave))

def rand_tempo():
	return str(random.randint(min_tempo,max_tempo))

def rand_mesure():
	temps_restants=nb_temps
	lines=""
	while(temps_restants != 0):
		note=rand_note()
		duree=rand_duration()
		if(temps_restants < duree):
			duree=temps_restants
		temps_restants-=duree
		line=make_line(note,duree)
		lines+=line
	return lines

def var_octave():
 	return random.random()<0.1



def build_file(file,nb_notes=100,tempo=rand_tempo(),octave=rand_octave()):
	file.write("tempo:"+tempo+ln)
	file.write("octave:"+octave+ln)

	for i in range(nb_notes):
		if(var_octave()):
			new_oct=rand_octave()
			print("NEW OCTAVE : "+new_oct)
			file.write("octave:"+new_oct+ln)
		#file.write(rand_line())
		file.write(rand_mesure())
	return file


def new_file():
	file_name=rand_name()
	#makemydir(folder)

	file=open(file_name,"w+")
	build_file(file)
	file.close()
	return file_name

def play(mus_file=new_file(),args=''):
	print(ln+ln+sep+ln+ln+"Hey !"+ln+ln+"Random Music !"+ln+ln+ln+"--> "+mus_file+ln+ln+sep+ln+ln)
	os.system(args+'music '+mus_file)


play()
