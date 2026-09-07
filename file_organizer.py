from pathlib import Path
import shutil
import json

class FileOrganiser:
    def __init__(self,src_path):

        self.src_path = Path(src_path)

        self.history_file = self.src_path/"move_history.json"

        self.file_categories = {
            "Images": [".jpg", ".jpeg", ".png", ".gif"],
            "Documents": [".pdf", ".docx", ".txt"],
            "Videos": [".mp4", ".mkv", ".avi"],
            "Audio": [".mp3", ".wav"],
            "Archives": [".zip", ".rar", ".7z"],
        }


    def get_unique_path(self,path):
        if not path.exists():
            return path
        counter = 1

        while True:
            unique_name = f"{path.stem} ({counter}){path.suffix}"
            unique_path = path.with_name(unique_name)

            if not unique_path.exists():
                return unique_path
            counter += 1



    def create_plan(self):

        planned_moves = []
        skipped_files = []

        for file in self.src_path.iterdir():
            if not file.is_file():
                continue

            extension = file.suffix.lower()
            organised = False

            for cat,exn in self.file_categories.items():
                if extension in exn:
                    desti_folder = self.src_path/cat
                    desti_file = self.get_unique_path(desti_folder/file.name)
                    planned_moves.append([file,desti_file])
                    organised = True
                    break

            if not organised:
                skipped_files.append(file.name)

        return (planned_moves,skipped_files)
                


    def preview_plan(self,planned_moves,skipped_files):
        print(f"---------------ORGANIZATION PREVIEW----------------")

        for file,desti_file in planned_moves:
            print(f"{file.name}")
            print(f"-> {desti_file}\n")
            

        print(f"---------------------------------------------------")

        print(f"Files to be organised: {len(planned_moves)}")
        print(f"Files skipped: {len(skipped_files)}")
        print(f"-----------------------------------------")


    def execute_plan(self,planned_moves):
        errors = []
        move_history = []
        print(f"Moved: ")

        for file,desti_file in planned_moves:
            try: 
                desti_folder = desti_file.parent
                desti_folder.mkdir(exist_ok=True)
                shutil.move(file,desti_file)
                move_history.append([file,desti_file])
                print(f"{file.name} -> {desti_file}")
            except Exception as error:
                print(f"Failed to move {file.name}: {error}")
                errors.append({
                    "file": file,
                    "error": str(error)
                })
        return move_history,errors

    def execution_report(self,planned_moves,skipped_files,move_history,errors):
        print("===================EXECUTION REPORT===================")
        print(f"Files planned: {len(planned_moves)}")
        print(f"Files moved: {len(move_history)}")
        print(f"Files skipped: {len(skipped_files)}")
        print(f"Errors: {len(errors)}")
        print("======================================================\n") 
        if errors:
            print(f"Errors:\n")
            for error_info in errors:
                print(f"{error_info['file'].name}:\n-> {error_info['error']}")
        else:
            print("No errors occuured")
        print("======================================================\n")


    def save_history(self,move_history):
        operation_data = []

        if self.history_file.exists():

            with open(self.history_file,"r") as file:
                history_data=json.load(file)
        else:
            history_data = []

        for source,destination in move_history:
            source = str(source)
            destination = str(destination)
            operation_data.append({"source":source,
                                "destination":destination})
            
        history_data.append(operation_data)
            
        with open(self.history_file,"w") as file:
                json.dump(history_data,file,indent=4)


    def load_history(self):


        if self.history_file.exists():
            with open(self.history_file,"r") as file:
                history_data=json.load(file)
        else:
            return []

        if not history_data:
            return []
        
        last_operation = history_data[-1]

        move_history = []

        for move in last_operation:
            source = Path(move["source"])
            destination = Path(move["destination"])
            move_history.append([source,destination])

        return move_history
        


    def undo(self, move_history):

        failed_undos = []
        errors = []

        for source, destination in reversed(move_history):

            try:

                if not destination.exists():
                    raise FileNotFoundError(
                        f"{destination} does not exist"
                    )

                shutil.move(destination, source)

                print(f"{destination} -> {source}")

            except Exception as error:

                failed_undos.append({
                    "source": str(source),
                    "destination": str(destination)
                })

                errors.append(str(error))

                print(f"Failed to undo {destination}: {error}")

        return failed_undos, errors



    def show_menu(self):
        print("==========FILE ORGANIZER==========\n")
        print("1. Organise Files")
        print("2. Undo Last Operation")
        print("3. Exit\n")

        choice = (input("Enter choice: ")).lower()
        while choice not in ("1","2","3"):
            choice = (input("Enter 1/2/3:")).lower()

        return(choice)

    
    def update_last_operation(self, remaining_moves):
        if not self.history_file.exists():
            return
                
        with open(self.history_file,"r") as file:
            history_data=json.load(file)

        if not history_data:
            return
        
        if not remaining_moves:
            history_data.pop()
        else:
            history_data[-1] = remaining_moves

        with open(self.history_file,"w") as file:
            json.dump(history_data,file,indent=4)
        


    def run(self):
        while True:

            choice = self.show_menu()

            if choice == "1":
                planned_moves,skipped_files = self.create_plan()
                if not planned_moves:
                    print("No files to organise")
                    continue
                self.preview_plan(planned_moves,skipped_files)
                choice = (input("Continue (y/n)?")).lower()
                while choice not in ("y","n"):
                    choice = (input("Continue (y/n)?")).lower()

                if choice == "y":
                    move_history,errors=self.execute_plan(planned_moves)
                    if move_history:
                        self.save_history(move_history)
                        
                    self.execution_report(planned_moves,skipped_files,move_history,errors)
                else:
                    print("Operation Cancelled\n")

            elif choice == "2":
                move_history = self.load_history()
                if not move_history:
                    print("No recorded history exists.")
                else:
                    failed_undos,undo_errors=self.undo(move_history)
                    self.update_last_operation(failed_undos)
                                                                
            elif choice == "3":
                print("Goodbyee!!")
                break
            









