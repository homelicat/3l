#!/bin/bash
./tmp.py
nasm -f elf test.s
ld -m elf_i386 test.o