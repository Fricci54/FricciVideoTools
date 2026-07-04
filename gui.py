import os
from tkinter import filedialog

import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")
from ffmpeg_runner import burn_subtitles

class FricciApp(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title("🎬 Fricci Video Tools v1.0")
        self.geometry("1000x720")
        self.minsize(900, 650)

        self.video_path = ctk.StringVar()
        self.subtitle_path = ctk.StringVar()
        self.output_path = ctk.StringVar(value=os.getcwd())

        self.nvenc = ctk.BooleanVar(value=True)
        self.subtitle_position = ctk.StringVar(value="bottom")

        self.create_header()
        self.create_main()

    # --------------------------------------------------

    def create_header(self):

        header = ctk.CTkFrame(self, height=70, corner_radius=0)
        header.pack(fill="x")

        title = ctk.CTkLabel(
            header,
            text="🎬 Fricci Video Tools",
            font=("Segoe UI", 28, "bold"),
        )

        title.pack(pady=(12, 0))

        version = ctk.CTkLabel(
            header,
            text="Version 1.0",
            font=("Segoe UI", 13),
        )

        version.pack()

    # --------------------------------------------------

    def create_main(self):

        self.main = ctk.CTkFrame(self)
        self.main.pack(fill="both", expand=True, padx=20, pady=20)

        self.create_video_selector()
        self.create_subtitle_selector()
        self.create_output_selector()
        self.create_options()
        self.create_progress()
        self.create_log()
        self.create_buttons()

    # --------------------------------------------------

    def create_video_selector(self):

        label = ctk.CTkLabel(
            self.main,
            text="Videó",
            font=("Segoe UI", 16, "bold"),
        )

        label.pack(anchor="w", pady=(10, 5))

        frame = ctk.CTkFrame(self.main, fg_color="transparent")
        frame.pack(fill="x")

        entry = ctk.CTkEntry(
            frame,
            textvariable=self.video_path,
            height=40,
        )

        entry.pack(side="left", fill="x", expand=True)

        button = ctk.CTkButton(
            frame,
            text="Tallózás",
            width=120,
            command=self.select_video,
        )

        button.pack(side="left", padx=10)

    # --------------------------------------------------

    def create_subtitle_selector(self):

        label = ctk.CTkLabel(
            self.main,
            text="Felirat",
            font=("Segoe UI", 16, "bold"),
        )

        label.pack(anchor="w", pady=(15, 5))

        frame = ctk.CTkFrame(self.main, fg_color="transparent")
        frame.pack(fill="x")

        entry = ctk.CTkEntry(
            frame,
            textvariable=self.subtitle_path,
            height=40,
        )

        entry.pack(side="left", fill="x", expand=True)

        button = ctk.CTkButton(
            frame,
            text="Tallózás",
            width=120,
            command=self.select_subtitle,
        )

        button.pack(side="left", padx=10)

    # --------------------------------------------------

    def create_output_selector(self):

        label = ctk.CTkLabel(
            self.main,
            text="Kimeneti mappa",
            font=("Segoe UI", 16, "bold"),
        )

        label.pack(anchor="w", pady=(15, 5))

        frame = ctk.CTkFrame(self.main, fg_color="transparent")
        frame.pack(fill="x")

        entry = ctk.CTkEntry(
            frame,
            textvariable=self.output_path,
            height=40,
        )

        entry.pack(side="left", fill="x", expand=True)

        button = ctk.CTkButton(
            frame,
            text="Tallózás",
            width=120,
            command=self.select_output,
        )

        button.pack(side="left", padx=10)

    # --------------------------------------------------

    def create_options(self):

        options = ctk.CTkFrame(self.main)
        options.pack(fill="x", pady=20)

        switch = ctk.CTkSwitch(
            options,
            text="NVENC hardveres gyorsítás",
            variable=self.nvenc,
        )

        switch.pack(anchor="w", padx=20, pady=15)

        label = ctk.CTkLabel(
            options,
            text="Felirat pozíció",
            font=("Segoe UI", 15, "bold"),
        )

        label.pack(anchor="w", padx=20)

        rb1 = ctk.CTkRadioButton(
            options,
            text="Alsó",
            value="bottom",
            variable=self.subtitle_position,
        )

        rb1.pack(anchor="w", padx=35)

        rb2 = ctk.CTkRadioButton(
            options,
            text="Közép",
            value="middle",
            variable=self.subtitle_position,
        )

        rb2.pack(anchor="w", padx=35)

        rb3 = ctk.CTkRadioButton(
            options,
            text="Felső",
            value="top",
            variable=self.subtitle_position,
        )

        rb3.pack(anchor="w", padx=35, pady=(0, 15))

    # --------------------------------------------------

    def create_progress(self):

        self.progress = ctk.CTkProgressBar(self.main)
        self.progress.pack(fill="x", pady=(10, 5))

        self.progress.set(0)

        self.status = ctk.CTkLabel(
            self.main,
            text="Készen áll.",
        )

        self.status.pack(anchor="w")

    # --------------------------------------------------

    def create_log(self):

        label = ctk.CTkLabel(
            self.main,
            text="Napló",
            font=("Segoe UI", 16, "bold"),
        )

        label.pack(anchor="w", pady=(20, 5))

        self.log = ctk.CTkTextbox(
            self.main,
            height=170,
        )

        self.log.pack(fill="both", expand=True)

        self.write_log("Fricci Video Tools elindult.")

    # --------------------------------------------------

    def create_buttons(self):

        frame = ctk.CTkFrame(self.main, fg_color="transparent")
        frame.pack(fill="x", pady=20)

        start = ctk.CTkButton(
            frame,
            text="🎬 Videó elkészítése",
            height=45,
            command=self.start,
        )

        start.pack(side="left", fill="x", expand=True)

    # --------------------------------------------------

    def write_log(self, text):

        self.log.insert("end", text + "\n")
        self.log.see("end")

    # --------------------------------------------------

    def set_status(self, text):

        self.status.configure(text=text)

    # --------------------------------------------------

    def select_video(self):

        file = filedialog.askopenfilename(
            filetypes=[
                ("Video", "*.mp4 *.mkv *.avi *.mov"),
                ("Minden", "*.*"),
            ]
        )

        if file:
            self.video_path.set(file)
            self.write_log("Videó: " + file)

    # --------------------------------------------------

    def select_subtitle(self):

        file = filedialog.askopenfilename(
            filetypes=[
                ("Subtitle", "*.srt"),
                ("Minden", "*.*"),
            ]
        )

        if file:
            self.subtitle_path.set(file)
            self.write_log("Felirat: " + file)

    # --------------------------------------------------

    def select_output(self):

        folder = filedialog.askdirectory()

        if folder:
            self.output_path.set(folder)
            self.write_log("Kimenet: " + folder)

    # --------------------------------------------------

    def start(self):

        if not self.video_path.get():
            self.write_log("Nincs videó kiválasztva.")
            return

        if not self.subtitle_path.get():
            self.write_log("Nincs felirat kiválasztva.")
            return

        self.progress.set(0)
        self.set_status("FFmpeg indítása...")

        self.write_log("")
        self.write_log("========== ÚJ FELADAT ==========")
        self.write_log(f"Videó: {self.video_path.get()}")
        self.write_log(f"Felirat: {self.subtitle_path.get()}")
        self.write_log(f"Kimenet: {self.output_path.get()}")

        try:

            output = burn_subtitles(
                self.video_path.get(),
                self.subtitle_path.get(),
                self.output_path.get(),
                self.nvenc.get()
            )

            self.progress.set(1)

            self.set_status("Kész.")

            self.write_log("")
            self.write_log("Videó elkészült:")
            self.write_log(output)

        except Exception as e:

            self.set_status("HIBA")

            self.write_log("")
            self.write_log("FFmpeg hiba:")
            self.write_log(str(e))