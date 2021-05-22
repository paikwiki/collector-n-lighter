NAME 	=	lighter
RM 		=	rm -rf
MYPY 	=	mypy

$(NAME):
			python3 main.py
all:		$(NAME)
clean:
			$(RM) __pycache__ **/__pycache__
			$(RM) *.pyc **/*.pyc
typecheck:
			$(MYPY) *.py **/*.py
.PHONY: 	all clean typecheck
