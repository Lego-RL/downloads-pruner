import os
import shutil

AUTO_DEL_EXTS: list[str] = ["jar", "exe", "webm", "ini", "crdownload", "msi"]
DOCUMENT_EXTS: list[str] = ["xls", "xlsx", "txt", "docx", "pdf", "djvu", "zip"]
MEDIA_EXTS: list[str] = ["png", "gif", "jpg", "mp4"]

DOWNLOADS_PATH: str = r"C:\Users\drleg\Downloads"
DOCUMENTS_PATH: str = r"C:\Users\drleg\OneDrive\Documents\Downloads\Files"
MEDIA_PATH: str = r"C:\Users\drleg\OneDrive\Documents\Downloads\Media"
FOLDER_PATH: str = r"C:\Users\drleg\OneDrive\Documents\Downloads"


def main() -> None:
    """
    Move and delete files in downloads folder.
    """
    files: list[str] = os.listdir(DOWNLOADS_PATH)
    for file in files:

        # if file, not folder
        if os.path.isfile(rf"{DOWNLOADS_PATH}/{file}"):
            ext: str = os.path.splitext(file)[1]
            ext = ext.strip(".")  # remove period on front

            if ext in AUTO_DEL_EXTS:
                del_file(file)

            elif ext in DOCUMENT_EXTS:
                move_item(file, DOCUMENTS_PATH)

            elif ext in MEDIA_EXTS:
                move_item(file, MEDIA_PATH)

        # move folders to documents/downloads folder
        elif os.path.isdir(rf"{DOWNLOADS_PATH}/{file}"):
            move_item(file, FOLDER_PATH)


def log_event(event: str) -> None:
    """
    Write even that occurred into log file.
    """

    with open("log.txt", "a") as f:
        f.write(f"{event}\n")


def move_item(item: str, move_to: str) -> None:
    """
    Move item to proper directory & log said action.
    """
    shutil.move(rf"{DOWNLOADS_PATH}/{item}", rf"{move_to}")
    log_event(f"MOVED item: {item} to {move_to}")


def del_file(file: str) -> None:
    """
    Delete given file & log said action.
    """
    os.remove(rf"{DOWNLOADS_PATH}/{file}")
    log_event(f"REMOVED file: {file}")


if __name__ == "__main__":
    main()
