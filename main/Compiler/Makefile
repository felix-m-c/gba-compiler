main:
	java -jar ../antlr4_13_1.jar -Dlanguage="Python3" -visitor -o out Slang.g4

run:
	python3 compiler.py SlangCode/game1.s out/code.asm
	ln -f out/code.asm ../Assembler/build/main.asm
	scripts/assembler.sh
	scripts/runEmu.sh

test:
	python3 compiler.py SlangCode/testAll.s out/code.asm
	ln -f out/code.asm ../Assembler/build/main.asm
	scripts/assembler.sh
	scripts/runTest.sh

tree:
	java -jar ../antlr4_13_1.jar Slang.g4 -o out
	javac -cp "./out:../antlr4_13_1.jar" Slang*.java -d ./out
	java -cp "./out:../antlr4_13_1.jar" org.antlr.v4.gui.TestRig Slang code.s -tree -startRuleName=start

clean:
	rm -f out/*.tokens
	rm -f out/*.interp
	rm -f out/*.java
	rm -f out/*.class
	rm -f out/*.asm
	rm -f Slang*.interp
	rm -f Slang*.tokens
	rm -f Slang*.java
	rm -f Slang*.class
	scripts/cleanAssembler.sh