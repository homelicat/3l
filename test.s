section .text
global _start
test:
	push ebp
	mov ebp,esp
	push 1
	push 2
	pop eax
	pop ebx
	add eax,ebx
	push eax
	pop eax
	mov esp,ebp
	pop ebp
	ret
_start:
	push ebp
	mov ebp,esp
	call test
	push eax
	mov eax,1
	pop ebx
	int 80h
	pop eax
	mov esp,ebp
	pop ebp
	ret
