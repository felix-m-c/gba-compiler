# SLANG compiler
this repo contains a compiler that compiles *Slang* files to *Gameboy Assembly*.
this code was written for the *Compiler Development* lecture at my university. 

## getting things to work
to compile a sourcefile to gameboy asm run 
```
cd main/Compiler
python3 compiler.py <input file> <output file>

e.g.
python3 compiler.py SlangCode/consoleTest.s out/code.asm
```
The assembler expects *customMagic.asm* and *framework.asm* to be one folder above the compiled assembly. 


## Slang
### Language Features
*Slang* looks somewhat like python, but with brackets instead of indents.
Examples of Slang code may be found in main/Compiler/SlangCode.

---

## actually getting things to work (WIP)
### Prerequisites
- The python code expects antlr4 to be installed
- the makefiles and scripts expect the assembler from the lecure at main/Assembler

### Running
the main code is in main/Compiler
to get started just run
```
cd main/Compiler
```
to let antlr build the language lexer and parser run
```
make
```
and to run your program
```
make run
```
