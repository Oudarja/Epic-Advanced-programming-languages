.PHONY: build clean

build:
	antlr4 Calc.g4 -Dlanguage=Python3 -visitor

clean:
	$(RM) -r .antlr
	$(RM) -r __pycache__
	$(RM) *.tokens *.interp CalcListener.py CalcParser.py CalcVisitor.py CalcLexer.py
