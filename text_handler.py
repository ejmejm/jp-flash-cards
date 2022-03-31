import nagisa
import ebooklib
from ebooklib import epub
from bs4 import BeautifulSoup

print('a')

book = epub.read_epub('data/mushoku_tensei_raw.epub')
items = list(book.get_items_of_type(ebooklib.ITEM_DOCUMENT))

def chapter_to_str(chapter):
    soup = BeautifulSoup(chapter.get_body_content(), 'html.parser')
    text = [para.get_text() for para in soup.find_all('p')]
    return ' '.join(text)

texts = {}
for item in items:
    print(item.get_name())
    if '0' not in item.get_name():
        continue
    texts[item.get_name()] = chapter_to_str(item)