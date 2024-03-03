from docx import Document

def extract_text_from_docx(docx_path):
    # Load the .docx file
    document = Document(docx_path)
    
    # Initialize an empty list to hold all the text
    full_text = []

    # Iterate through each paragraph in the document and append its text to the list
    for para in document.paragraphs:
        full_text.append(para.text)
    
    # Join all the text pieces into a single string
    return '\n'.join(full_text)