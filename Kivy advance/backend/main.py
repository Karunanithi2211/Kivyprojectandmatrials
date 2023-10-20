from kivy.lang import Builder
from kivymd.app import MDApp
import sqlite3


class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Blue"

        conn = sqlite3.connect("backend.db")
        c = conn.cursor()
        c.execute("""CREATE TABLE if not exists customers(name text)""")
        conn.commit()
        conn.close()

        return Builder.load_file("main.kv")

    def submit(self):
        conn = sqlite3.connect("backend.db")
        c = conn.cursor()
        c.execute("INSERT INTO customers VALUES (:first)", {
            'first': self.root.ids.word_input.text
        })
        self.root.ids.word_label.text = f'{self.root.ids.word_input.text} Added'
        self.root.ids.word_input.text = ''
        conn.commit()
        conn.close()

    def show_records(self):
        conn = sqlite3.connect("backend.db")
        c = conn.cursor()
        c.execute("SELECT * FROM customers")
        records = c.fetchall()
        word = ''
        for record in records:
            word = f"{word}\n{record[0]}"
            self.root.ids.word_label.text = f'{word}'
        conn.commit()
        conn.close()


MainApp().run()
