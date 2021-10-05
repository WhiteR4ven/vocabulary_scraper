# Vocabulary Scraper

**Python script to webscrape vocabulary conjugations.

Idea:
Goal of the project is, to supply the script with a list of vocabularies.
Afterwards the script webscrapes all the vocabulary confugations and writes them into an own file, that is easy to import into Excel.

How-To:
- Supply a vocab_input.txt
  containing the base forms of the search Vocabulary
- The script uses the online website of "Cooljugator"
  https://cooljugator.com/ro/
  change the URL if necessary
- the script extracts the conjugations defined in the search-list.
  For this example als present conjugations 
  search = ["present1", "present2", "present3", "present4", "present5", "present6"]
