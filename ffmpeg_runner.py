import os
import subprocess

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FFMPEG = os.path.join(BASE_DIR, "ffmpeg", "ffmpeg.exe")


def burn_subtitles(video, subtitle, output_folder, use_nvenc=True):

    # Abszolút útvonalak
    video = os.path.abspath(video)
    subtitle = os.path.abspath(subtitle)
    output_folder = os.path.abspath(output_folder)

    # Kimeneti fájl neve
    filename = os.path.splitext(os.path.basename(video))[0]
    output = os.path.join(output_folder, filename + "_sub.mp4")

    # Windows kompatibilis subtitle útvonal
    subtitle_filter = (
        subtitle
        .replace("\\", "/")
        .replace(":", "\\:")
    )

    # Videó codec
    codec = "h264_nvenc" if use_nvenc else "libx264"

    command = [
        FFMPEG,
        "-y",
        "-i", video,
        "-vf",
        f"subtitles='{subtitle_filter}'",
        "-c:v",
        codec,
        "-c:a",
        "copy",
        output
    ]

    print("FFmpeg parancs:")
    print(" ".join(command))

    result = subprocess.run(
        command,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        encoding="utf-8",
        errors="ignore"
    )

    if result.returncode != 0:
        raise Exception(result.stderr)

    return output