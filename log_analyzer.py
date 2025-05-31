import re
from collections import Counter
from colorama import Fore, Style

def analyze_log(file_path):
    with open(file_path, 'r') as file:
        log_data = file.read()
    stats = Counter()
    stats["ERROR"] = len(re.findall(r"\bERROR\b", log_data))
    stats["WARNING"] = len(re.findall(r"\bWARNING\b", log_data))
    stats["INFO"] = len(re.findall(r"\bINFO\b", log_data))
    return stats

def export_report(stats, output_file):
    with open(output_file, 'w') as f:
        for key, value in stats.items():
            f.write(f"{key}: {value}\n")

if __name__ == "__main__":
    stats = analyze_log("log.txt")
    export_report(stats, "rapport.txt")
    print(Fore.RED + f"ERROR: {stats['ERROR']}" + Style.RESET_ALL)
    print(Fore.YELLOW + f"WARNING: {stats['WARNING']}" + Style.RESET_ALL)
    print(Fore.GREEN + f"INFO: {stats['INFO']}" + Style.RESET_ALL)
