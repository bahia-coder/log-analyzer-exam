import re
from collections import Counter
from colorama import Fore, Style, init
from datetime import datetime

init(autoreset=True)

def log(message):
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(Fore.CYAN + f"[{now}] {message}")

def analyze_log(file_path):
    log(f"Lecture du fichier : {file_path}")
    with open(file_path, 'r') as file:
        log_data = file.read()

    stats = Counter()
    stats["ERROR"] = len(re.findall(r"\bERROR\b", log_data))
    stats["WARNING"] = len(re.findall(r"\bWARNING\b", log_data))
    stats["INFO"] = len(re.findall(r"\bINFO\b", log_data))

    log("Analyse terminée.")
    return stats

def export_report(stats, output_file):
    log(f"Export des résultats dans {output_file}")
    with open(output_file, 'w') as f:
        f.write("Statistiques du fichier log :\n")
        for level, count in stats.items():
            f.write(f"{level}: {count}\n")
    log("Export terminé.")

if __name__ == "__main__":
    log("Lancement de l'analyse des logs.")
    stats = analyze_log("log.txt")
    export_report(stats, "rapport.txt")

    print(Fore.RED + f"ERROR: {stats['ERROR']}")
    print(Fore.YELLOW + f"WARNING: {stats['WARNING']}")
    print(Fore.GREEN + f"INFO: {stats['INFO']}")
