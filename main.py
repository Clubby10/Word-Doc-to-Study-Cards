import docx
from collections import defaultdict

def convert_to_flashcards(filepath):
    flashcards = defaultdict(list)
    doc = docx.Document(filepath)
    question = ""
    answer = ""
    for para in doc.paragraphs:
        if para.style.name == "List Number":
            if question:
                flashcards[question] = answer
            question = para.text
            answer = ""
        else:
            if question:
                answer += para.text
    return flashcards

filepath = input("Enter the path to the word document:")
flashcards = convert_to_flashcards(filepath)

for question, answer in flashcards.items():
    print("Question: ", question)
    print("Answer: ", answer)
