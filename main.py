from deep_translator import GoogleTranslator
import os
from colorama import Fore, init

init(autoreset=True)

# 🌍 Languages (including Telugu)
languages = {
    "hi": "Hindi",
    "te": "Telugu",
    "es": "Spanish",
    "fr": "French",
    "de": "German",
    "ja": "Japanese",
    "zh-cn": "Chinese",
    "ar": "Arabic",
    "ru": "Russian",
    "pt": "Portuguese",
    "it": "Italian"
}

print(Fore.CYAN + "=" * 60)
print(Fore.YELLOW + "- SUBTITLE TRANSLATOR TOOL")
print(Fore.GREEN + "- Created by: ABHIRAM")
print(Fore.MAGENTA + "- Instagram: themabhiram (https://www.instagram.com/themabhiram/)")
print(Fore.CYAN + "=" * 60)

while True:
    folder = input(Fore.WHITE + "\nEnter folder path (or type 'exit'): ").strip()

    if folder.lower() == "exit":
        print(Fore.YELLOW + "Exiting...")
        break

    if not os.path.isdir(folder):
        print(Fore.RED + "Invalid folder path ")
        continue

    # 📂 Get .srt files
    srt_files = [f for f in os.listdir(folder) if f.lower().endswith(".srt")]

    if not srt_files:
        print(Fore.RED + "No subtitle files found ")
        continue

    # 📋 Show files
    print(Fore.YELLOW + "\nAvailable Subtitle Files:")
    for i, file in enumerate(srt_files):
        print(Fore.CYAN + f"[{i}] {file}")

    # 🎯 Select file
    try:
        index = int(input(Fore.WHITE + "\nEnter file index: "))
        if index < 0 or index >= len(srt_files):
            print(Fore.RED + "Invalid index ")
            continue
        selected_file = srt_files[index]
    except:
        print(Fore.RED + "Invalid input ")
        continue

    srt_path = os.path.join(folder, selected_file)

    try:
        with open(srt_path, "r", encoding="utf-8") as f:
            lines = f.readlines()
    except:
        print(Fore.RED + "Failed to read file ")
        continue

    for lang_code, lang_name in languages.items():
        print(Fore.BLUE + f"\nTranslating to {lang_name}...")

        translated_lines = []

        for line in lines:
            stripped = line.strip()

            if stripped.isdigit() or "-->" in stripped or stripped == "":
                translated_lines.append(line)
            else:
                try:
                    translated_text = GoogleTranslator(
                        source='auto',
                        target=lang_code
                    ).translate(stripped)

                    translated_lines.append(translated_text + "\n")
                except:
                    translated_lines.append(stripped + "\n")

        output_file = os.path.join(
            folder,
            f"{os.path.splitext(selected_file)[0]}_{lang_code}.srt"
        )

        try:
            with open(output_file, "w", encoding="utf-8") as f:
                f.writelines(translated_lines)

            print(Fore.GREEN + f"Saved: {output_file} ")
        except:
            print(Fore.RED + f"Failed to save {lang_name} file ")

    print(Fore.CYAN + "\nexit All translations completed!")

input(Fore.MAGENTA + "\nPress Enter to exit...")