import tkinter as tk
import webbrowser
from generators import *
from tkinter import messagebox


class App:
    def __init__(self, master):
        self.master = master
        master.title("Генератор данных")
        master.geometry()

        self.fields = [
            ("ОКПО (Юр. лицо)", generate_okpo_for_juridical),
            ("ОКПО (Филиал)", generate_okpo_for_branch),
            ("ОГРН", generate_businesses_ogrn),
            ("ИНН", generate_businesses_inn),
            ("БИК", generate_businesses_bic),
            ("Серия паспорта", generate_passport_series),
            ("Номер", generate_number),
            ("ДР взрослый", generate_date_adult),
            ("Серия СоР", generate_sor_number),
            ("Номер", generate_number),
            ("ДР ребенок", generate_date_child),
            ("ДР подросток", generate_date_child_adult),
            ("Город", generate_name_city),
            ("KPP", generate_kpp),
            ("Телефон", generate_phone),
        ]

        self.result_texts = []

        for field_name, field_generator in self.fields:
            frame = tk.Frame(master)
            frame.pack(fill=tk.X)

            label = tk.Label(frame, text=field_name, width=20)
            label.pack(side=tk.LEFT)

            result_text = tk.Text(frame, height=1, width=30)
            result_text.pack(side=tk.LEFT)
            self.result_texts.append(result_text)

            generate_button = tk.Button(frame, text="g", command=lambda generator=field_generator, text=result_text: self.generate_field(generator, text))
            generate_button.pack(side=tk.LEFT)

            copy_button = tk.Button(frame, text="Копировать", command=lambda text=result_text: self.copy_to_clipboard(text))
            copy_button.pack(side=tk.LEFT)

        author_label = tk.Label(master, text="Автор: Sergey Salyk", fg="blue", cursor="hand2")
        author_label.pack()
        author_label.bind("<Button-1>", lambda e: self.open_linkedin_profile())

        self.pinned = False

        self.pin_button = tk.Button(master, text="Закрепить", command=self.toggle_pinning)
        self.pin_button.pack(side=tk.RIGHT)

        generate_button = tk.Button(master, text="Сгенерировать все", command=self.generate_fields)
        generate_button.pack()

    def generate_field(self, field_generator, result_text):
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, field_generator())

    def generate_fields(self):
        for i, (_, field_generator) in enumerate(self.fields):
            result_text = self.result_texts[i]
            result_text.delete(1.0, tk.END)
            result_text.insert(tk.END, field_generator())

    def copy_to_clipboard(self, text_widget):
        text = text_widget.get(1.0, tk.END).strip()
        if text:
            self.master.clipboard_clear()
            self.master.clipboard_append(text)

    def open_linkedin_profile(self):
        webbrowser.open("https://www.linkedin.com/in/sergeysalyk")

    def toggle_pinning(self):
        self.pinned = not self.pinned
        if self.pinned:
            self.pin_button.config(text="Открепить")
            self.master.wm_attributes("-topmost", 1)
        else:
            self.pin_button.config(text="Закрепить")
            self.master.wm_attributes("-topmost", 0)


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
