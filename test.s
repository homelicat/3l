section .text
global _start
test:
	push ebp
	mov ebp,esp
	push eax
	mov eax,3
	pop edx
	mov esp,ebp
	pop ebp
	ret
_start:
	push ebp
	mov ebp,esp
	push eax
	mov eax,4
	push eax
	call test
	pop edx
	add eax,edx
	push eax
	mov eax,6
	xor ecx,ecx
	mov ebx,-1
	pop edx
	cmp edx,eax
	mov eax,ecx
	cmove eax,ebx
	cmp eax,0
	je if0
	push eax
	mov eax,0
	jmp if1
if0:
	push eax
	mov eax,1
if1:
	mov ebx,eax
	mov eax,1
	int 80h
	pop edx
	mov esp,ebp
	pop ebp
	ret
