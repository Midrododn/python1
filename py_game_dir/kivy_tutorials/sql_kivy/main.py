from kivy.app import App
from kivy.uix.behaviors import button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
import os
import sqlite3
import sys

class Prnt_dir:
    def __init__(self):
        self.txt = ""

    def p_dir(self):
	    app_folder = os.path.dirname(os.path.abspath(__file__))
	    return app_folder

class MainApp(App):
    def build(self):
        self.work_dir = app_folder = os.path.dirname(os.path.abspath(__file__))
        self.operators = ["/", "*", "+", "-"]
        self.last_was_operator = None
        self.last_button = None
        main_layout = BoxLayout(orientation="vertical")
        self.out_put = TextInput(
            multiline=True, readonly=True, halign="left", font_size=20
        )
        main_layout.add_widget(self.out_put)
        self.in_put = TextInput(
            multiline=True, readonly=False, halign="left", font_size=20
        )
        main_layout.add_widget(self.in_put)
        buttons = [
            ["Write", "Read", "SQLite"],
            ["Create Table", "Save", "Load"],
        ]
        for row in buttons:
            h_layout = BoxLayout()
            for label in row:
                button = Button(
                    text=label,
                    pos_hint={"center_x": 0.5, "center_y": 0.5},
                )
                button.bind(on_press=self.on_button_press)
                h_layout.add_widget(button)
            main_layout.add_widget(h_layout)

        return main_layout

    def on_button_press(self, instance):
        current = self.out_put.text
        button_text = instance.text

        if button_text == "Write":
            txt = self.work_dir + "/t_file.txt"
            f = open(txt, "a")
            f.write("New file\n")
            f.close()
        elif button_text == "Read":
            txt = self.work_dir + "/t_file.txt"
            f = open(txt, "r")
            self.out_put.text = txt
            txt += "\n"
            txt += f.readline()
            self.out_put.text = txt
        elif button_text == "SQLite":
            db_path = self.work_dir + "/test.db"
            conn = sqlite3.connect(db_path)
            self.out_put.text = db_path
            conn.close()
        elif button_text == "Create Table":
            db_path = self.work_dir + "/test.db"
            conn = sqlite3.connect(db_path)
            sql_command = '''
                CREATE TABLE IF NOT EXISTS test_table (
                    id INTEGER PRIMARY KEY AUTOINCREMENT , 
                    text_line TEXT 
                );
            '''
            conn.execute(sql_command)
            conn.close()
        elif button_text == "Save":
            db_path = self.work_dir + "/test.db"
            conn = sqlite3.connect(db_path)
            content = self.in_put.text
            sql_command = "INSERT INTO test_table (text_line) VALUES ('" + \
            content + "');"
            conn.execute(sql_command)
            conn.commit()
            conn.close()
        elif button_text == "Load":
            db_path = self.work_dir + "/test.db"
            conn = sqlite3.connect(db_path)
            sql_command = "SELECT * FROM test_table;"
            cursor = conn.execute(sql_command)
            out_txt = ""
            for row in cursor:
                out_txt += "ID= " + str(row[0]) + " |text= " + row[1] + "\n"
            self.out_put.text= out_txt
            conn.close()

    def on_solution(self, instance):
        text = self.solution.text
        if text:
            solution = str(eval(self.solution.text))
            self.solution.text = solution


def main():
    app = MainApp()
    app.run()

if __name__ == "__main__":
    main()
