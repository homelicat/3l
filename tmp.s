section .data
	txt db "Hi",0xa
section .text
global _start
_start:
	xor ebx,ebx
	mov ecx,txt
	mov eax,4
	inc ebx
	mov edx,3
	int 80h
	
	mov eax,1
	xor ebx,ebx
	int 80h
