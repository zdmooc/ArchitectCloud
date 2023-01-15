## ---------------------
## Think / Edit / Make
## ---------------------

all: clean index table

.PHONY: clean
clean:
	rm -f *.html 

##
## HELLO
##
.PHONY: hello
hello:
	pug --pretty hello.pug


.PHONY: index
index: table
	pug --pretty index.pug

table:
	python gnr_table.py > table.pug
