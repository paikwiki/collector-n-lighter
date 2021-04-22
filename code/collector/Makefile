NAME		=	collector

SRCS		=	./srcs/main.cpp ./srcs/Collector.cpp
OBJS		=	$(SRCS:.cpp=.o)
INCS		=	-I./

CXX			=	clang++
RM			=	rm -f
FLAGS		=	-Wall -Wextra -Werror -std=c++98 # Do not use "nullptr"
LEAKS		=	-g -fsanitize=address -fsanitize=undefined

%.o:		%.cpp
			$(CXX) $(FLAGS) -c $< -o $@

all:		$(NAME)
$(NAME):	$(OBJS)
			$(CXX) $(FLAGS) $(INCS) $(OBJS) -o $(NAME)
clean:
			$(RM) $(OBJS)
fclean:		clean
			$(RM) $(NAME)
debug:		fclean $(OBJS)
			$(CXX) $(FLAGS) $(LEAKS) $(INCS) $(OBJS) -o $(NAME)
re:			fclean all

.PHONY:		all clean fclean debug re
