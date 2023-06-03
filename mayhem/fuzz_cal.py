#!/usr/bin/env python3
import atheris
import sys
import fuzz_helpers


with atheris.instrument_imports():
    from aicsimageio import AICSImage
def TestOneInput(data):
    fdp = fuzz_helpers.EnhancedFuzzedDataProvider(data)
    AICSImage(fdp.ConsumeRemainingString())

def main():
    atheris.Setup(sys.argv, TestOneInput)
    atheris.Fuzz()


if __name__ == "__main__":
    main()
