.PHONY: default clean

default: Curriculum.html

%.html: %.md
	marp -o $@ $< 

clean:
	rm -f Curriculum.html