#!/bin/bash
./compiler.py
nasm -f elf test.s
ld -m elf_i386 -o test test.o
rm test.o