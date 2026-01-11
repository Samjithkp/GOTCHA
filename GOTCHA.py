import os
import subprocess

# ANSI Colors
RED = "\033[91m"
WHITE = "\033[97m"
CYAN = "\033[96m"
RESET = "\033[0m"

def banner():
    print()
    print(
        RED +
        " ██████╗  ██████╗ ████████╗" +
        WHITE +
        "  ██████╗ ██╗  ██╗ █████╗ "
    )
    print(
        RED +
        "██╔════╝ ██╔═══██╗╚══██╔══╝" +
        WHITE +
        " ██╔════╝ ██║  ██║██╔══██╗"
    )
    print(
        RED +
        "██║  ███╗██║   ██║   ██║   " +
        WHITE +
        " ██║      ███████║███████║"
    )
    print(
        RED +
        "██║   ██║██║   ██║   ██║   " +
        WHITE +
        " ██║      ██╔══██║██╔══██║"
    )
    print(
        RED +
        "╚██████╔╝╚██████╔╝   ██║   " +
        WHITE +
        " ╚██████╗ ██║  ██║██║  ██║"
    )
    print(
        RED +
        " ╚═════╝  ╚═════╝    ╚═╝   " +
        WHITE +
        "  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝"
    )
    print(
        CYAN +
        "\n        File Type Identification Tool"
        "\n   Detecting Disguised & Suspicious Files\n" +
        RESET
    )

def get_magic_hex(file_path):
    with open(file_path, "rb") as f:
        return f.read(16).hex()

def detect_magic_type(hexdata):
    if hexdata.startswith("7f454c46"):
        return "ELF Executable"
    elif hexdata.startswith("2321"):
        return "Script / Text File"
    elif hexdata.startswith("ffd8ff"):
        return "JPEG Image"
    elif hexdata.startswith("89504e47"):
        return "PNG Image"
    elif hexdata.startswith("25504446"):
        return "PDF Document"
    else:
        return "Unknown or Text File"

def get_file_command_output(file_path):
    result = subprocess.run(
        ["file", file_path],
        capture_output=True,
        text=True
    )
    return result.stdout.strip()

def determine_status(detected, extension):
    status = "SAFE"
    risk = "LOW"

    if detected == "ELF Executable" and extension in [".jpg", ".png", ".pdf", ".txt"]:
        status = "DISGUISED EXECUTABLE"
        risk = "HIGH"
    elif detected == "ELF Executable" and extension == ".sh":
        status = "EXECUTABLE WITH MISLEADING EXTENSION"
        risk = "MEDIUM"
    elif detected == "Unknown or Text File" and extension in [".txt", ".md", ".log"]:
        status = "SAFE TEXT FILE"
        risk = "LOW"
    elif detected == "Unknown or Text File":
        status = "UNKNOWN FILE TYPE"
        risk = "MEDIUM"

    return status, risk

def main():
    banner()
    file_path = input("Enter file path to analyze: ").strip()

    if not os.path.isfile(file_path):
        print("\n[!] File not found!")
        return

    magic_hex = get_magic_hex(file_path)
    detected = detect_magic_type(magic_hex)
    extension = os.path.splitext(file_path)[1]

    print("\nMagic Number Analysis:")
    print("Raw hex:", magic_hex)
    print("Detected:", detected)

    print("\nFile extension:", extension if extension else "None")

    print("\nFile command output:")
    print(get_file_command_output(file_path))

    status, risk = determine_status(detected, extension)

    print("\nStatus:", status)
    print("Risk Level:", risk)

    print("\nNote: Check if magic number matches the extension!")
    input("Press Enter to continue ...")

if __name__ == "__main__":
    main()
