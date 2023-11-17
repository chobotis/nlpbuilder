from os import read


#this is where the cvs parser from NLPparser comes in

#summon NLPParser

#if job description includes keywords, parse keywords and print them into skills

#-------------------------------------------
def section3(resume_text):
    # Use the previously mentioned code to extract keywords from the job description
    text = read('../job_desc.txt')
    text = str(text)
    text = text.replace("\\n", "")
    text = text.lower()

    # below is the csv where we have all the keywords, you can customize your own
    keyword_dict = pd.read_csv('D:/Documents/resumes/template_new.csv')
    stats_words = [nlp(text) for text in keyword_dict['Statistics '].dropna(axis=0)]
    NLP_words = [nlp(text) for text in keyword_dict['NLP'].dropna(axis=0)]
    ML_words = [nlp(text) for text in keyword_dict['Machine Learning'].dropna(axis=0)]
    DL_words = [nlp(text) for text in keyword_dict['Deep Learning'].dropna(axis=0)]
    R_words = [nlp(text) for text in keyword_dict['R Language'].dropna(axis=0)]
    python_words = [nlp(text) for text in keyword_dict['Python Language'].dropna(axis=0)]
    Data_Engineering_words = [nlp(text) for text in keyword_dict['Data Engineering'].dropna(axis=0)]
    health_words =[nlp(text) for text in keyword_dict['Health'].dropna(axis=0)]

    matcher = PhraseMatcher(nlp.vocab)
    matcher.add('Stats', None, *stats_words)
    matcher.add('NLP', None, *NLP_words)
    matcher.add('ML', None, *ML_words)
    matcher.add('DL', None, *DL_words)
    matcher.add('R', None, *R_words)
    matcher.add('Python', None, *python_words)
    matcher.add('DE', None, *Data_Engineering_words)
    matcher.add('HE', None, *health_words)
    doc = nlp(text)

    d = []
    matches = matcher(doc)
    for match_id, start, end in matches:
        rule_id = nlp.vocab.strings[match_id]  # get the unicode ID, i.e. 'COLOR'
        span = doc[start: end]  # get the matched slice of the doc
        d.append((rule_id, span.text))
    keywords = "\n".join(f'{i[0]} {i[1]} ({j})' for i, j in Counter(d).items())


     # Return a list directly
    return [keywords]

# Example usage
resume_text = "Your resume text here"
skills = section3(resume_text)
print(skills)

from pathlib import Path
from os import read
import pandas as pd
from collections import Counter
from spacy.matcher import PhraseMatcher
import spacy


def section3(resume_text):
    # Use pathlib for file paths
    job_description_path = Path('C:/Users/rkimc/Documents/nlpbuilder/job_desc.txt')

    # Use with statement for file reading
    with job_description_path.open('r') as file:
        text = file.read()

    # Combine multiple replace operations into one
    text = text.replace("\\n", "").lower()

    # below is the csv where we have all the keywords, you can customize your own
    keyword_dict = pd.read_csv('D:/Documents/resumes/template_new.csv')

    # Create a dictionary to store lists of words
    word_categories = {
        'Stats': 'Statistics ',
        'NLP': 'NLP',
        'ML': 'Machine Learning',
        'DL': 'Deep Learning',
        'R': 'R Language',
        'Python': 'Python Language',
        'DE': 'Data Engineering',
        #  'HE': 'Health',
    }

    nlp = spacy.load("en_core_web_sm")
    matcher = PhraseMatcher(nlp.vocab)

    # Use a loop to add multiple categories to the matcher
    for category, column in word_categories.items():
        words = [nlp(text) for text in keyword_dict[column].dropna(axis=0)]
        matcher.add(category, None, *words)

    doc = nlp(text)

    d = []
    matches = matcher(doc)
    for match_id, start, end in matches:
        rule_id = nlp.vocab.strings[match_id]
        span = doc[start: end]
        d.append((rule_id, span.text))

    # Use f-strings for string formatting
    keywords = "\n".join(f'{i[0]} {i[1]} ({j})' for i, j in Counter(d).items())

    # Return a list directly
    return [keywords]


# Example usage
resume_text = "Your resume text here"
skills = section3(resume_text)
print(skills)


def compare_versions(version1, version2):
    # Split versions into major, minor, and revision numbers
    v1 = list(map(int, version1.split('.')))
    v2 = list(map(int, version2.split('.')))

    # Compare major, minor, and revision numbers
    for i in range(3):
        if v1[i] < v2[i]:
            return -1
        elif v1[i] > v2[i]:
            return 1

    return 0

def quicksort(versions):
    if len(versions) <= 1:
        return versions

    pivot = versions[len(versions) // 2]
    left = [x for x in versions if compare_versions(x, pivot) == -1]
    middle = [x for x in versions if compare_versions(x, pivot) == 0]
    right = [x for x in versions if compare_versions(x, pivot) == 1]

    return quicksort(left) + middle + quicksort(right)

# Example usage
versions = ["1.1.2", "1.0", "1.3.3", "1.0.12", "1.0.2"]
sorted_versions = quicksort(versions)
print(sorted_versions)
