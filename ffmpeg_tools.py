from pathlib import Path
import subprocess


FFMPEG = Path("ffmpeg") / "ffmpeg.exe"


def burn_subtitles(video_file, subtitle_file, output_folder):

    video = Path(video_file)
    subtitle = Path(subtitle_file)
    output_dir = Path(output_folder)

    output_file = output_dir / f"{video.stem}_feliratos.mp4"

    subtitle_filter = (
        str(subtitle)
        .replace("\\", "/")
        .replace(":", "\\:")
    )

    cmd = [
        str(FFMPEG),
        "-y",
        "-i", str(video),

        "-vf",
        f"subtitles='{subtitle_filter}'",

        "-c:v", "h264_nvenc",
        "-preset", "p5",
        "-cq", "20",

        "-c:a", "copy",

        str(output_file)
    ]

    process = subprocess.run(
        cmd,
        capture_output=True,
        text=True
    )

    return (
        process.returncode == 0,
        process.stdout,
        process.stderr,
        str(output_file)
    )