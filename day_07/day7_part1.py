""""--- Day 7: No Space Left On Device ---
--- Part One ---
https://adventofcode.com/2022/day/7
"""


def main():
    with open('input') as terminal_log:
        directories = parse_input(terminal_log)

        total_size = 0
        directories_in_scope = directories.get_directories_below(100000)
        for d in directories_in_scope:
            total_size += d.get_size()
        print('Total size:', total_size)


def parse_input(terminal_log):
    lines = list()

    current_depth = 0
    working_dir = Dir('')
    working_dir.add_directory(Dir('/', working_dir))

    for line in terminal_log:
        lines.append(line.split())

    ln = 0
    while ln < len(lines):
        if lines[ln][0] == '$':
            # Command executed on terminal
            if lines[ln][1] == 'cd':
                if lines[ln][2] == '..':
                    current_depth -= 1
                    working_dir = working_dir.parent
                else:
                    current_depth += 1
                    working_dir = working_dir.get_subdirectory(lines[ln][2])

            elif lines[ln][1] == 'ls':
                # The following lines will contain directories and files until the next '$'
                while (ln + 1) < len(lines) and lines[ln + 1][0] != '$':
                    # print('ln (from loop): ', ln + 1, 'first char is :', lines[ln + 1][0])
                    if lines[ln + 1][0] == 'dir':
                        working_dir.add_directory(Dir(lines[ln + 1][1], working_dir))
                    else:
                        working_dir.add_file([lines[ln + 1][1], int(lines[ln + 1][0])])
                    # print(working_dir.to_console(current_depth))
                    ln += 1
            else:
                print('Unknown command: ', lines[ln][1])
        else:
            print(lines[ln])
        ln += 1
    return working_dir.get_root()


class Dir:

    def __init__(self, name, parent=None):
        self.name = name
        self.parent = parent
        self.directories = list()
        self.files = list()

    def __lt__(self, other):
        return self.get_size() <= other.get_size()

    def add_directory(self, directory):
        # Double check that the directory does not yet exist
        existing_dirs = list()
        for existing_dir in self.directories:
            existing_dirs.append(existing_dir.name)
        assert directory.name not in existing_dirs

        self.directories.append(directory)

    def add_file(self, file):
        self.files.append(file)

    def get_subdirectory(self, dir_name):
        for directory in self.directories:
            if directory.name == dir_name:
                return directory

    def get_root(self):
        if self.parent is not None:
            return self.parent.get_root()
        else:
            return self

    def get_size(self):
        size = 0
        for directory in self.directories:
            size += directory.get_size()
        for file in self.files:
            size += file[1]
        return size

    def get_file_size(self):
        size = 0
        for file in self.files:
            size += file[1]
        return size

    def get_directories_below(self, size):
        dirs_in_scope = list()
        for directory in self.directories:
            if directory.get_size() <= size:
                dirs_in_scope.append(directory)

            # Recursively call all sub-directories
            dirs_in_scope.extend(directory.get_directories_below(size))

        return dirs_in_scope

    def get_directories_above(self, size):
        dirs_in_scope = list()
        for directory in self.directories:
            if directory.get_size() >= size:
                dirs_in_scope.append(directory)

            # Recursively call all sub-directories
            dirs_in_scope.extend(directory.get_directories_above(size))

        return dirs_in_scope

    def to_console(self, depth):
        print('  ' * depth, '* ', self.name, '(dir, size: ', self.get_size(), ')')
        for directory in self.directories:
            directory.to_console(depth + 1)
        for file in self.files:
            print('  ' * (depth + 1), '- ', file[0], ' (file, size: ', file[1], ')')


if __name__ == "__main__":
    main()
