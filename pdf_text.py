import pdfplumber  # Import the pdfplumber library
import re  # Regular expressions
import csv

def clean_text(words: list) -> str:
    # Join words into a single string
    cleaned_content = ' '.join(word['text'] for word in words)
    
    # Remove special characters
    special_chars = [
        '!', '"', '#', '$', '%', '&', "'", '(', ')', '*',
        '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', 
        '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~',
        '§', '©', '®', '™'
    ]
    translation_table = str.maketrans('', '', ''.join(special_chars))
    
    # Clean the content
    cleaned_content = cleaned_content.translate(translation_table).lower()
    
    # Remove extra spaces
    cleaned_content = re.sub(r'\s+', ' ', cleaned_content).strip()
    
    return cleaned_content

def pdf_to_text(pdf_file: str) -> str:
    text = ""
    #text = []
    with pdfplumber.open(pdf_file) as pdf:
        # for page in pdf.pages:
        #    content = page.extract()
        #    cleaned_content = clean_text(content)
        #     text.append(cleaned_content)
        if len(pdf.pages) > 0:  
            first_page = pdf.pages[0]  
            words = first_page.extract_words()  
            if words:  
                cleaned_content = clean_text(words)
                text = cleaned_content
    return text

# save text to text file
def save_text_to_file(text: str, filename: str):
    with open(filename, mode="w",encoding='utf-8') as file:
        file.write(text)


def save_to_csv(text: str, csv_file: str):
    # Optionally, you can split the text into multiple lines for better readability
    # Here, we split by sentences or paragraphs based on punctuation
    # You can adjust the regex to fit your needs
    text_with_line_breaks = re.sub(r'(?<=[.!?]) +', '\n', text)  # Add line breaks after sentences

    with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Extracted Text'])  # Write header
        writer.writerow([text_with_line_breaks])

if __name__ == '__main__':
    extract_text = pdf_to_text('Programming_Assignment_1.pdf')
    print(extract_text)
    #print(f"The output_file is {} saved in .csv format")  

    pdf_file = 'Programming_Assignment_1.pdf'
    #csv_file = 'extracted_text.csv'
    text_file = 'extracted_text.txt'
    
    #extract_text = pdf_to_text(pdf_file)
    #save_to_csv(extract_text, csv_file)
    
    #print(f"Extracted text saved to {csv_file}")

    save_text_to_file(extract_text, text_file)  # Save the extracted text to a text file
    
    print(f"Extracted text saved to {text_file}")