from kivy.lang import Builder
from kivymd.app import MDApp
import mysql.connector


class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Blue"

        # conn = sqlite3.connect("backend.db")
        mydb = mysql.connector.connect(
            host='localhost',
            user='root',
            passwd='Kavin@2211',
            database='backenddb'
        )
        c = mydb.cursor()
        c.execute("CREATE DATABASE IF NOT EXISTS backenddb")
        c.execute("""CREATE TABLE if not exists customers(name VARCHAR(50))""")
        mydb.commit()
        mydb.close()

        return Builder.load_file("main.kv")

    def submit(self):
        mydb = mysql.connector.connect(
            host='localhost',
            user='root',
            passwd='Kavin@2211',
            database='backenddb'
        )
        c = mydb.cursor()
        sql_command = 'INSERT INTO customers (name) VALUES (%s)'
        values = (self.root.ids.word_input.text,)
        c.execute(sql_command, values)
        self.root.ids.word_label.text = f'{self.root.ids.word_input.text} Added'
        self.root.ids.word_input.text = ''
        mydb.commit()
        mydb.close()

    def show_records(self):
        mydb = mysql.connector.connect(
            host='localhost',
            user='root',
            passwd='Kavin@2211',
            database='backenddb'
        )
        c = mydb.cursor()
        c.execute("SELECT * FROM customers")
        records = c.fetchall()
        word = ''
        for record in records:
            word = f"{word}\n{record[0]}"
            self.root.ids.word_label.text = f'{word}'
        mydb.commit()
        mydb.close()


MainApp().run()
