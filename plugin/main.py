import pyperclip
from flox import Flox
from plugin.Translator import Translator

class App(Flox):
    def __init__(self):
        self.translator = Translator(self.settings.get("first_lang"), self.settings.get("second_lang"))
        
    
    def query(self, query):
        translations = self.translator.get_translation(query)
        method_name = 'copy_clipboard'
        for translation in translations:
            self.add_item(
                title = translation[0],
                subtitle= f"Frequency: {translation[1]}",
                icon = "Images/app.png",
                method = method_name,
                parameters = [translation[0]],
                context = [translation[2]]   
            )

    def context_menu(self, data):
        self.add_item(
                title="Open in Browser",
                subtitle=data[0],
                method="open_url",
                parameters=data
            )

    def copy_clipboard(self, word):
        pyperclip.copy(word)

    def open_url(self, url):
        self.browser_open(url)