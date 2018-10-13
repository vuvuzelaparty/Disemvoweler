EXE = disemvoweler*

.PHONY : build clean

build : $(EXE)
	@echo "Adding execute permissions to disemvoweler.py and disemvoweler_alt.py..."
	chmod +x $(EXE)

clean:
	@echo "Removing execute permissions for disemvoweler.py and disemvoweler_alt.py..."
	chmod -x $(EXE)
