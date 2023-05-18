objects = addition.o division.o main.o multiplication.o subtraction.o

calculator: $(objects)
	cc -o calculator $^

$(objects): operations.h

clean:
	rm -f calculator $(objects)

.PHONY: clean
