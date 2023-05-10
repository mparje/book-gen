import streamlit as st
import sys
import os
import unicodedata
import datetime

# Global variables for settings:
OUTPUT_FILE = 'output.txt'

# helper functions
def addparagraphs(lines):
    """Put HTML paragraph tags around each paragraph"""
    st.write("Writing to file...", end='')
    with open(OUTPUT_FILE, mode='w', encoding='utf-8-sig') as output:
        for line in lines:
            line = line.rstrip('\n')
            output.write("<p>{}</p>\n".format(line))
    st.write("done.")
    return(0)

def main():
    """Run editing checks on a text document"""

    st.set_page_config(page_title="Generate an eBook and print-ready book format from a manuscript in Markdown",
                       page_icon=":books:",
                       layout="wide")

    st.title("Generate an eBook and print-ready book format from a manuscript in Markdown")

    # Check for proper command line usage
    if len(sys.argv) is not 2:
        st.error("Usage: generate.py text_file")
        st.stop()

    filename = sys.argv[1]
    if not os.path.isfile(filename):
        st.error("File path {} does not exist. Exiting...".format(filename))
        st.stop()

    st.write("Started at {}, checking file {}:".format(datetime.datetime.now(), filename))

    st.write("Reading file... ", end='')
    try:
        with open(filename, mode='r', encoding='utf-8-sig') as file:
            # CAUTION: reading the whole file into memory
            lines = file.readlines()
            st.write("done.\n")
    except IOError:
        st.error("Could not read {}".format(filename))
        st.stop()

    exitcode = addparagraphs(lines)
    if exitcode == 0:
        st.success("Finished with no errors.")
    st.stop()

if __name__ == "__main__":
    main()
