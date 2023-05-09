#!/usr/bin/python3
src = list()

with open("test.3l") as f:
	for line in f:
		src.extend(line.split())
with open("test.s","w") as f:
	ifs = 0
	func = 0
	funcs = list()
	f.write("section .text\nglobal _start\n")
	for com in src:
		if com.isdecimal():
			f.write("\tpush "+com+"\n")
		elif com=="+":
			f.write("\tpop eax\n\tpop ebx\n\tadd eax,ebx\n\tpush eax\n")
		elif com=="-":
			f.write("\tpop eax\n\tpop ebx\n\tsub ebx,eax\n\tpush ebx\n")
		elif com=="=":
			f.write("\txor ecx,ecx\n\tmov edx,-1\n\tpop eax\n\tpop ebx\n\tcmp eax,ebx\n\tcmove ecx,edx\n\tpush ecx\n")
		elif com==">":
			f.write("\txor ecx,ecx\n\tmov edx,-1\n\tpop eax\n\tpop ebx\n\tcmp ebx,eax\n\tcmovg ecx,edx\n\tpush ecx\n")
		elif com=="<":
			f.write("\txor ecx,ecx\n\tmov edx,-1\n\tpop eax\n\tpop ebx\n\tcmp ebx,eax\n\tcmovl ecx,edx\n\tpush ecx\n")
		elif com=="&":
			f.write("\tpop eax\n\tpop ebx\n\tand eax,ebx\n\tpush eax\n")
		elif com=="|":
			f.write("\tpop eax\n\tpop ebx\n\tor eax,ebx\n\tpush eax\n")
		elif com=="~":
			f.write("\tpop eax\n\tnot eax\n\tpush eax\n")
		#elif com=="if":
		#	f.write("\tpop eax\n\tcmp eax,0\n\tje if"+str(ifs)+"\n")
		#elif com=="then":
		#	f.write("if"+str(ifs)+":\n")
		#	ifs+=1
		#elif com=="else":
		#	f.write("\tjmp if"+str(ifs+1)+"\nif"+str(ifs)+":\n")
		#	ifs+=1
		elif com==":":
			if func:
				print("Error: already defining")
				break
			func=1
		elif com==";":
			if not func:
				print("Error: not defining")
				break
			func=0
			f.write("\tpop eax\n\tmov esp,ebp\n\tpop ebp\n\tret\n")
		elif com=="exit":
			f.write("\tmov eax,1\n\tpop ebx\n\tint 80h\n")
		else:
			if (func==2) and (com in funcs):
				f.write("\tcall "+com+"\n\tpush eax\n")
			elif func==1:
				funcs.append(com)
				f.write(com+":\n\tpush ebp\n\tmov ebp,esp\n")
				func=2
			else:
				print("Error: "+com)