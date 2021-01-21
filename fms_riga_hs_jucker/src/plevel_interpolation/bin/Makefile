# Makefile created by mkmf $Id: mkmf,v 18.0 2010/03/02 23:26:08 fms Exp $ 


.DEFAULT:
	-echo $@ does not exist.
all: plev.x
SRC =
OBJ =
clean: neat
	-rm -f .plev.x.cppdefs $(OBJ) plev.x
neat:
	-rm -f $(TMPFILES)
TAGS: $(SRC)
	etags $(SRC)
tags: $(SRC)
	ctags $(SRC)
plev.x: $(OBJ) 
	$(LD) $(OBJ) -o plev.x  $(LDFLAGS)
