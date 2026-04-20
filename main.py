import json
import uuid

class URLShortener:
    def __init__(self, filename='urls.json'):
        self.filename = filename
        self.urls = self.load_urls()

    def load_urls(self):
        try:
            with open(self.filename, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return {}

    def save_urls(self):
        with open(self.filename, 'w') as f:
            json.dump(self.urls, f)

    def shorten(self, url):
        short_code = str(uuid.uuid4())[:6]
        self.urls[short_code] = url
        self.save_urls()
        return short_code

    def expand(self, short_code):
        return self.urls.get(short_code)

# Misol:
shortener = URLShortener()
url = 'https://www.example.com'
short_code = shortener.shorten(url)
print(f'Qisqa kod: {short_code}')
print(f'Uzun URL: {shortener.expand(short_code)}')
```

Bu kodda biz URLShortener klassini yaratdik, u quyidagi metodlarni o'z ichiga oladi:

- `__init__`: klassni yaratishda fayl nomini va URLlar ro'yxatini yuklash uchun foydalaniladi.
- `load_urls`: faylda saqlangan URLlar ro'yxatini yuklaydi.
- `save_urls`: URLlar ro'yxatini faylga saqlaydi.
- `shorten`: URLni qisqa kodga aylantiradi.
- `expand`: qisqa kodni uzun URLga aylantiradi.

Misolni ko'rish uchun, biz URLShortener klassining obyekti yaratdik, uzun URLni qisqa kodga aylantirdik va keyin qisqa kodni uzun URLga aylantirdik.
