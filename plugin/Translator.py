from reverso_api.context import ReversoContextAPI
from googletrans import Translator as TranslatorGoogle


class Translator():
    def __init__(self, first_lang, second_lang):
        self.language_code_by_language_name = {
            "English": "en",
            "Russian":"ru",
            "Hungarian":"hu",
            "Dutch":"nl",
            "Greek":"el",
            "Danish":"da",
            "Hebrew":"he",
            "Spanish":"es",
            "Italian":"it",
            "Chinese":"zh",
            "Arabic":"ar",
            "Korean":"ko",
            "German":"de",
            "Persian":"fa",
            "Polish":"pl",
            "Portuguese":"pt",
            "Romanian":"ro",
            "Slovak":"sk",
            "Thai":"th",
            "Turkish":"tr",
            "Ukrainian":"uk",
            "French":"fr",
            "Hindi":"hi",
            "Czech":"cs",
            "Swedish":"sv",
            "Japanese":"ja"}
        
        self.first_lang_code = self.language_code_by_language_name[first_lang]
        self.second_lang_code = self.language_code_by_language_name[second_lang]
    

    def get_translation(self, query: str):
        source_lang, target_lang = self.get_source_target_lang(query) 
        result = []

        if(len(query.strip().split(" ")) <= 1):
            translations = ReversoContextAPI(source_lang=source_lang, target_lang=target_lang, source_text=query).get_translations()
            for translation in translations:
                result.append([translation.translation, 
                               translation.frequency,
                               f"https://www.reverso.net#sl={source_lang}&tl={target_lang}&text={query}"])
        else:
            translator = TranslatorGoogle()
            translation = translator.translate(query, dest=target_lang, src=source_lang)
            url_query = query.replace(" ", "%2520")
            result.append([translation.text, 
                           1,
                           f"https://www.reverso.net#sl={source_lang}&tl={target_lang}&text={url_query}"])
        
        return sorted(result, key=lambda x:x[1], reverse=True)


    def get_source_target_lang(self, text):
        translator = TranslatorGoogle()
        detect_lang = translator.detect(text).lang
        
        if detect_lang == self.first_lang_code:
            return self.first_lang_code, self.second_lang_code
        else:
            return self.second_lang_code, self.first_lang_code