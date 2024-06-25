main:
	java -jar ../antlr4_13_1.jar -Dlanguage="Python3" -visitor -o out Slang.g4

test:
	python3 compiler.py SlangCode/smileyEat.s code.asm
	ln -f code.asm ../Assembler/build/main.asm
	scripts/assembler.sh
	scripts/runEmu.sh

tree:
	java -jar ../antlr4_13_1.jar Slang.g4 -o out
	javac -cp "./out:../antlr4_13_1.jar" Slang*.java -d ./out
	java -cp "./out:../antlr4_13_1.jar" org.antlr.v4.gui.TestRig Slang code.s -tree -startRuleName=start

clean:
	rm -f out/*.tokens
	rm -f out/*.interp
	rm -f out/*.java
	rm -f out/*.class
	rm -f Slang*.interp
	rm -f Slang*.tokens
	rm -f Slang*.java
	rm -f Slang*.class
	rm -f code.asm
	scripts/cleanAssembler.sh