O := build

all: html

html linkcheck::
	sphinx-build $(SPHINXFLAGS) -d $(O)/.doctrees -b $@ doc $(O)/$@

check: linkcheck

clean:
	rm -rf $(O)

.PHONY: all check clean html linkcheck
