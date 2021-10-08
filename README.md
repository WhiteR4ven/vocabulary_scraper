# Vocabulary Scraper

**Python script to webscrape vocabulary conjugations.**

__Idea:__
Goal of the project is, to supply a script with a own list of vocabularies.
Afterwards the script webscrapes all the vocabulary conjugations and writes them into an export file, that is easy to import into Excel.

__How-To:__
- Supply a vocab_input.txt
  containing the base forms of your search vocabulary
- The script uses the online website of "Cooljugator"
  https://cooljugator.com/ro/
  change the URL if necessary
- the script extracts the conjugations defined in the search list.
  For this example as present conjugations 
  search = ["present1", "present2", "present3", "present4", "present5", "present6"]
  simply add all your needed conjugations.
  To find them out, go on cooljugator website an inspect the appropriate field with the browser-dev-tools.
- the script creates a "vocab_output.txt" with all the conjugations seperated by tabs.
- Import the textfile to Excel or a similar tool for further data handling
