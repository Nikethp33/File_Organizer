from pathlib import Path
import shutil

src_path = Path("test_dir")

FILE_CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".txt"],
    "Videos": [".mp4", ".mkv", ".avi"],
    "Audio": [".mp3", ".wav"],
    "Archives": [".zip", ".rar", ".7z"],
}



def get_unique_path(path):
    if not path.exists():
        return path
    counter = 1

    while True:
        unique_name = f"{path.stem} ({counter}){path.suffix}"
        unique_path = path.with_name(unique_name)

        if not unique_path.exists():
            return unique_path
        counter += 1



# def organise(dry_run = False):
#     skipped_files = []
#     organised_count = 0
#     move_history = []

#     for file in src_path.iterdir():

#         if not file.is_file():
#             continue

#         extension = file.suffix.lower()
#         organised = False

#         for cat,extn in FILE_CATEGORIES.items():
#             if extension in extn:
#                 desti_folder = src_path / cat
#                 desti_file = get_unique_path(desti_folder / file.name)

#                 if dry_run:
#                     print(f"WOULD MOVE: {file} --> {cat} in {desti_file}")

#                 else:
#                     desti_folder.mkdir(exist_ok=True)
#                     shutil.move(file, desti_file)
#                     move_history.append([file, desti_file])
#                     print(f"MOVED: {file} --> {cat} in {desti_file}")

#                 organised_count += 1
#                 organised = True

#                 break


#         if not organised:
#             skipped_files.append(file.name)

#     return (organised_count,skipped_files,move_history,dry_run)

#organised_count,skipped_files,move_history,dry_run = organise(True)

def create_plan():

    planned_moves = []
    skipped_files = []

    for file in src_path.iterdir():
        if not file.is_file():
            continue

        extension = file.suffix.lower()
        organised = False

        for cat,exn in FILE_CATEGORIES.items():
            if extension in exn:
                desti_folder = src_path/cat
                desti_file = get_unique_path(desti_folder/file.name)
                planned_moves.append([file,desti_file])
                organised = True
                break

        if not organised:
            skipped_files.append(file.name)

    return (planned_moves,skipped_files)
            


def preview_plan(planned_moves,skipped_files):
    print(f"---------------ORGANIZATION PREVIEW----------------")

    for file,desti_file in planned_moves:
        print(f"{file.name}")
        print(f"-> {desti_file}")
        print(f"\n")

    print(f"---------------------------------------------------")

    print(f"Files to be organised: {len(planned_moves)}")
    print(f"Files skipped: {len(skipped_files)}")
    print(f"-----------------------------------------")


def execute_plan(planned_moves):
    move_history = []
    print(f"Moved: ")

    for file,desti_file in planned_moves:
        desti_folder = desti_file.parent
        desti_folder.mkdir(exist_ok=True)
        shutil.move(file,desti_file)
        move_history.append([file,desti_file])
        print(f"{file.name} -> {desti_file}")
    return move_history


def undo(move_history):
    print("Undo process!!")
    for file,desti_file in reversed(move_history):
        if desti_file.exists():
            shutil.move(desti_file,file)
            print(f"{desti_file} -> {file}")

planned_moves,skipped_files = create_plan()
preview_plan(planned_moves,skipped_files)

choice = input("Continue (y or n)?: ").lower()
while choice not in ("y","n"):
    choice = input("Continue (y or n)?: ").lower()

if choice == "y":
    move_history = execute_plan(planned_moves)
else:
    print("Operation cancelled!")
    move_history = []



# undo(move_history)