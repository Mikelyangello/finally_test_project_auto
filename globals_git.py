class MyCreds:

    def __init__(self):
        self.login = "youremailhere"
        self.password = "yourpasswordhere"
        self.user_email = 'testuser@test.com'
        self.user_password = '!TestPassword!'
        self.sel_login_window_btn = ".navbar__auth_login"
        self.sel_login_form = "#login_form"
        self.sel_login = "#id_login_email"
        self.sel_password = "#id_login_password"
        self.sel_submit_btn = 'button[type="submit"]'
        self.sel_auth_profile = '.navbar__profile-img[alt="User avatar"]'
        self.sel_for_answer = '[autocorrect="off"]'
        self.sel_btn_for_answer = 'button.submit-submission'
        self.sel_for_hint = 'p.smart-hints__hint'
        self.expecting_hint = "Correct!"
        self.real_answer = ''
        self.def_link = "https://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/"
        self.empty_basket_texts_dictionary = {
            "ar": "سلة التسوق فارغة",
            "ca": "La seva cistella està buida.",
            "cs": "Váš košík je prázdný.",
            "da": "Din indkøbskurv er tom.",
            "de": "Ihr Warenkorb ist leer.",
            "en": "Your basket is empty.",
            "el": "Το καλάθι σας είναι άδειο.",
            "es": "Tu carrito esta vacío.",
            "fi": "Korisi on tyhjä",
            "fr": "Votre panier est vide.",
            "it": "Il tuo carrello è vuoto.",
            "ko": "장바구니가 비었습니다.",
            "nl": "Je winkelmand is leeg",
            "pl": "Twój koszyk jest pusty.",
            "pt": "O carrinho está vazio.",
            "pt-br": "Sua cesta está vazia.",
            "ro": "Cosul tau este gol.",
            "ru": "Ваша корзина пуста",
            "sk": "Váš košík je prázdny",
            "uk": "Ваш кошик пустий.",
            "zh-cn": "Your basket is empty.",
        }
        self.empty_basket_texts = ' '.join([*self.empty_basket_texts_dictionary.values()])

    @staticmethod
    def answer():
        import time
        import math
        return math.log(int(time.time()))

    def assertion_msg(self, hint):
        self.real_answer += hint
        return f'Ошибка, ожидали подсказку "{self.expecting_hint}", а получили: "{hint}"'
