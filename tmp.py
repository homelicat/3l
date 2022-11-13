#!/usr/bin/python3
src = list()

with open("test.tmp") as f:
	for line in f:
		src.extend(line.split())
with open("test.s","w") as f:
	ifs = 0
	f.write("section .text\nglobal _start\n_start:\n")
	for com in src:
		if com.isdecimal():
			f.write("\tpush "+com+"\n")
		elif com=="+":
			f.write("\tpop eax\n\tpop ebx\n\tadd eax,ebx\n\tpush eax\n")
		elif com=="exit":
			f.write("\tmov eax,1\n\tpop ebx\n\tint 80h\n")
		elif com=="dup":
			f.write("\tpop eax\n\tpush eax\n\tpush eax\n")
		elif com=="-":
			f.write("\tpop eax\n\tpop ebx\n\tsub ebx,eax\n\tpush ebx\n")
		elif com=="drop":
			f.write("\tpop eax\n")
		elif com=="swap":
			f.write("\tpop eax\n\tpop ebx\n\tpush eax\n\tpush ebx\n")
		elif com=="over":
			f.write("\tpop eax\n\tpop ebx\n\tpush ebx\n\tpush eax\n\tpush ebx\n")
		elif com=="rot":
			f.write("\tpop eax\n\tpop ebx\n\tpop ecx\n\tpush ebx\n\tpush eax\n\tpush ecx\n")
		elif com=="=":
			f.write("\tmov ecx,0\n\tmov edx,-1\n\tpop eax\n\tpop ebx\n\tcmp eax,ebx\n\tcmove ecx,edx\n\tpush ecx\n")
		elif com==">":
			f.write("\tmov ecx,0\n\tmov edx,-1\n\tpop eax\n\tpop ebx\n\tcmp ebx,eax\n\tcmovg ecx,edx\n\tpush ecx\n")
		elif com=="<":
			f.write("\tmov ecx,0\n\tmov edx,-1\n\tpop eax\n\tpop ebx\n\tcmp ebx,eax\n\tcmovl ecx,edx\n\tpush ecx\n")
		elif com=="and":
			f.write("\tmov ecx,-1\n\tpop eax\n\tpop ebx\n\tcmp eax,0\n\tcmovne eax,ecx\n\tcmp ebx,0\n\tcmovne ebx,ecx\n\tand eax,ebx\n\tpush eax\n")
		elif com=="or":
			f.write("\tmov ecx,-1\n\tpop eax\n\tpop ebx\n\tcmp eax,0\n\tcmovne eax,ecx\n\tcmp ebx,0\n\tcmovne ebx,ecx\n\tor eax,ebx\n\tpush eax\n")
		elif com=="invert":
			f.write("\tpop eax\n\tmov ebx,-1\n\tcmp eax,0\n\tcmovne eax,ebx\n\tnot eax\n\tpush eax\n")
		elif com=="if":
			f.write("\tpop eax\n\tcmp eax,0\n\tje if"+str(ifs)+"\n")
		elif com=="then":
			f.write("if"+str(ifs)+":\n")
			ifs+=1
		else:
			print("Error: "+com)