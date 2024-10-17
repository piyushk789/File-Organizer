# Source Code (Organizer)
import os


class Extension:

    # Constructor
    def __init__(self):
        self.__file_path__: str | None = None
        self.list_dir: list = []
        self.moves = 0

    def filter_data(self):
        if not (os.path.exists(self.__file_path__)):
            return quit()

        self.identification(self.__file_path__)
        return self.list_dir

    def identification(self, location: str):
        ls = os.listdir(location)
        for in_dir in ls:
            loc = f"{location}/{in_dir}"
            if os.path.isfile(loc):
                self.list_dir.append(loc)

    def separate(self, extension: list | None = None):
        if extension is None:
            extension = []
            for value in self.filter_data():
                extension.append((value.split('/')[-1]).split('.')[-1])

        for data in self.list_dir:
            for ext in set(extension):
                if data.lower().endswith(ext.lower()):
                    file_name = data.split('/')[-1]
                    path = f"{self.__file_path__}/{ext.upper()}"
                    if os.path.exists(path) and os.path.isdir(path):
                        pass
                    else:
                        os.mkdir(f"{self.__file_path__}/{ext.upper()}")
                    try:
                        os.rename(data, f"{self.__file_path__}/{ext.upper()}/{file_name}")
                        self.moves += 1
                    except FileExistsError as exist_err:
                        print(f"File Error: {exist_err}")
                    except WindowsError:
                        # print(f"Replace Error: {rename}")
                        pass
