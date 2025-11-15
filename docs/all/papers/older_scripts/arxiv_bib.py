#!/usr/bin/python3
import arxiv
import sys
from os.path import exists

if len(sys.argv) < 2:
    print("Usage: ./arxiv_bib.py arxiv_number [article_name]")
    exit(0)

eprint = sys.argv[1]

article_label = ""
if len(sys.argv) > 2: 
    article_label = sys.argv[2]

# Look up paper through the arxiv Python library
search = arxiv.Search(id_list=[eprint])
paper = next(search.results())

# Extract properties
year = paper.published.strftime("%Y")

authors = ""
for a in paper.authors:
    authors += str(a) + " and "
authors = authors[0:len(authors)-5] #trim initial ' ' and final 'and '

if paper.doi != None:
    print(f"NOTE: paper has a DOI https://doi.org/{paper.doi}")

if paper.journal_ref != None:
    print(f"NOTE: paper has a journal reference: {paper.journal_ref}\n")

bib_entry = f"""
@article{{{article_label},
title={{{paper.title}}},
author={{{authors}}},
year={{{year}}},
eprint={{{eprint}}},
archivePrefix={{arXiv}},
primaryClass={{{paper.primary_category}}},
url={{https://arxiv.org/abs/{eprint}}}
}}
        """

print(bib_entry)

