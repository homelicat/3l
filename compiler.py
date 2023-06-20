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
			f.write("\tpush eax\n\tmov eax,"+com+"\n")
		elif com=="+":
			f.write("\tpop edx\n\tadd eax,edx\n")
		elif com=="-":
			f.write("\tmov edx,eax\n\tpop eax\n\tsub eax,edx\n")
		elif com=="=":
			f.write("\txor ecx,ecx\n\tmov ebx,-1\n\tpop edx\n\tcmp edx,eax\n\tmov eax,ecx\n\tcmove eax,ebx\n")
		elif com==">":
			f.write("\txor ecx,ecx\n\tmov ebx,-1\n\tpop edx\n\tcmp edx,eax\n\tmov eax,ecx\n\tcmovg eax,ebx\n")
		elif com=="<":
			f.write("\txor ecx,ecx\n\tmov ebx,-1\n\tpop edx\n\tcmp edx,eax\n\tmov eax,ecx\n\tcmovl eax,ebx\n")
		elif com=="&":
			f.write("\tpop edx\n\tand eax,edx\n")
		elif com=="|":
			f.write("\tpop edx\n\tor eax,edx\n")
		elif com=="~":
			f.write("\tnot eax\n")
		elif com=="?":
			f.write("\tcmp eax,0\n\tje if"+str(ifs)+"\n")
		elif com==".":
			f.write("if"+str(ifs)+":\n")
			ifs+=1
		elif com==",":
			f.write("\tjmp if"+str(ifs+1)+"\nif"+str(ifs)+":\n")
			ifs+=1
		elif com=="a":
			pass
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
			f.write("\tpop edx\n\tmov esp,ebp\n\tpop ebp\n\tret\n")
		elif com=="exit":
			f.write("\tmov ebx,eax\n\tmov eax,1\n\tint 80h\n")
		else:
			if (func==2) and (com in funcs):
				f.write("\tpush eax\n\tcall "+com+"\n")
			elif func==1:
				funcs.append(com)
				f.write(com+":\n\tpush ebp\n\tmov ebp,esp\n")
				func=2
			else:
				print("Error: "+com)