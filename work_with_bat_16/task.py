"""
создает документ и пихает туда текст
"""
import docx

user_text = input("Введите текст который хотите сохронить в Файле: ")

filename = "file.docx"

doc = docx.Document()        #создает документ

doc.add_paragraph(user_text) #добовляет туда текст

doc.save(filename)           # сохроняет документ

print(f"текст сохронён в фале {filename}")