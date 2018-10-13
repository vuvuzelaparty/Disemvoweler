EXE = disemvoweler*

.PHONY : build clean

build : $(EXE)
	@echo "Adding execute permissions to disemvoweler and disemvoweler_alt..."
	chmod +x $(EXE)

clean:
	@echo "Removing execute permissions for disemvoweler and disemvoweler_alt..."
	chmod -x $(EXE)
