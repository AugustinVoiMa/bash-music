import random
import os

def makemydir(whatever):
  try:
    os.makedirs(whatever)
  except OSError:
    pass



notes=["DO","RE","MI","FA","SOL","LA","SI","DOd","REd","FAd","SOLd","Lad"]

notes=["DO","FAd","SI","LAd"]

min_duree=0.1
max_duree=4.0
min_octave=2
max_octave=4
min_tempo=100
max_tempo=1000
ln="\n"

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
	return random.choice(notes)

def rand_duration():
	duree = random.uniform(min_duree,max_duree)
	return round(duree,2)

def rand_line():
	line=str(rand_note())+":"+str(rand_duration())
	return line

def rand_octave():
	return str(random.randint(min_octave,max_octave))

def rand_tempo():
	return str(random.randint(min_tempo,max_tempo))

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
		file.write(rand_line()+ln)
	return file


def new_file():
	file_name=rand_name()
	makemydir(folder)

	file=open(path+file_name,"w+")
	build_file(file)
	file.close()
	return file_name

def play(mus_file=new_file(),args=''):
	os.system(args+'./music '+mus_file)


play()
