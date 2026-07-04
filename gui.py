import customtkinter as ctk


class FricciVideoToolsApp(ctk.CTk):

    def __init__(self):
        super().__init__()

        # Ablak beállítások
        self.title("Fricci Video Tools v1.0")
        self.geometry("1000x650")
        self.minsize(900, 600)

        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        # ---------- Cím ----------
        title = ctk.CTkLabel(
            self,
            text="🎬 Fricci Video Tools v1.0",
            font=("Segoe UI", 24, "bold")
        )
        title.pack(pady=20)

        # ---------- Fő keret ----------
        main_frame = ctk.CTkFrame(self)
        main_frame.pack(fill="both", expand=True, padx=20, pady=10)

        # Bal oldal
        left_frame = ctk.CTkFrame(main_frame, width=420)
        left_frame.pack(side="left", fill="y", padx=10, pady=10)

        # Jobb oldal
        right_frame = ctk.CTkFrame(main_frame)
        right_frame.pack(side="right", fill="both", expand=True, padx=10, pady=10)

        # -----------------------------
        # Videó
        # -----------------------------
        ctk.CTkLabel(left_frame, text="🎬 Videó").pack(anchor="w", padx=15, pady=(15, 5))

        self.video_entry = ctk.CTkEntry(left_frame, width=350)
        self.video_entry.pack(padx=15)

        ctk.CTkButton(
            left_frame,
            text="Tallózás"
        ).pack(padx=15, pady=8)

        # -----------------------------
        # Felirat
        # -----------------------------
        ctk.CTkLabel(left_frame, text="💬 Felirat").pack(anchor="w", padx=15, pady=(10, 5))

        self.subtitle_entry = ctk.CTkEntry(left_frame, width=350)
        self.subtitle_entry.pack(padx=15)

        ctk.CTkButton(
            left_frame,
            text="Tallózás"
        ).pack(padx=15, pady=8)

        # -----------------------------
        # Kimenet
        # -----------------------------
        ctk.CTkLabel(left_frame, text="💾 Kimeneti fájl").pack(anchor="w", padx=15, pady=(10, 5))

        self.output_entry = ctk.CTkEntry(left_frame, width=350)
        self.output_entry.pack(padx=15)

        ctk.CTkButton(
            left_frame,
            text="Tallózás"
        ).pack(padx=15, pady=8)

        # -----------------------------
        # NVENC
        # -----------------------------
        self.nvenc = ctk.CTkCheckBox(
            left_frame,
            text="NVIDIA NVENC használata"
        )
        self.nvenc.select()
        self.nvenc.pack(anchor="w", padx=15, pady=20)

        # -----------------------------
        # Gombok
        # -----------------------------
        ctk.CTkButton(
            left_frame,
            text="▶ INDÍTÁS",
            height=40
        ).pack(fill="x", padx=15, pady=(20, 8))

        ctk.CTkButton(
            left_frame,
            text="■ LEÁLLÍTÁS",
            fg_color="firebrick"
        ).pack(fill="x", padx=15)

        # -----------------------------
        # Jobb oldal
        # -----------------------------

        ctk.CTkLabel(
            right_frame,
            text="Állapot"
        ).pack(anchor="w", padx=15, pady=(15, 5))

        self.progress = ctk.CTkProgressBar(right_frame)
        self.progress.pack(fill="x", padx=15)

        self.progress.set(0)

        self.status = ctk.CTkLabel(
            right_frame,
            text="Várakozás..."
        )
        self.status.pack(anchor="w", padx=15, pady=10)

        ctk.CTkLabel(
            right_frame,
            text="Napló"
        ).pack(anchor="w", padx=15)

        self.log = ctk.CTkTextbox(
            right_frame,
            height=350
        )

        self.log.pack(fill="both", expand=True, padx=15, pady=(5, 15))

        self.log.insert("end", "Fricci Video Tools v1.0 elindult...\n")