from os.path import join


def valid_line(text):
    """ Returns true if doing a comparison to a checked markdown line would
    not cause and error condition"""
    if text == None:
        return False

    return len(text) >= 5

def is_whitespace(text):
    """ Returns true if text is whitespace"""
    if text == None:
        return True

    return text.strip() == ""

def checked_line(text):
    """Returns true if this is a line that is Markdown for a checked checkbox"""
    if valid_line(text):
        return text[:5].upper() == '- [X]'

    return False

def strip_tail(source_list):
    """ Takes a list and removes null and blank items from the tail """
    line = source_list.pop()

    while len(source_list) > 0 and is_whitespace(line):
        line = source_list.pop()

    if not is_whitespace(line):
        source_list.append(line)

    return source_list


def split_lines(source):
    """ Takes the source text and splits out any lines starting with the
    Markdown for a checked item and moves it to another list.  It
    returns the checked and then the unchecked items separately"""
    unchecked = []
    checked = []

    for line in source:
        is_unchecked = checked_line(line)

        if is_unchecked:
            checked.append(line)
        else:
            unchecked.append(line)

    checked = strip_tail(checked)
    unchecked = strip_tail(unchecked)

    return checked, unchecked


class WeeklyUpdate:
    def __init__(self,source_dir, source_file,
                 checked_target, unchecked_target):
        self._source_dir = source_dir
        self._source_file = source_file
        self._checked_target = checked_target
        self._unchecked_target = unchecked_target

    @property
    def source_dir(self):
        """Get the source directory"""
        return self._source_dir

    @property
    def source_file(self):
        """Get the source file"""
        return self._source_file

    @property
    def checked_target(self):
        """Get the checked target"""
        return self._checked_target

    @property
    def unchecked_target(self):
        """Get the unchecked target"""
        return self._unchecked_target

    def wrap_up_week(self):
        checked, unchecked = self.split_source()

        checked_text = "\n".join(checked)
        unchecked_text = "\n".join(unchecked)

        self.checked_target.write(checked_text)
        self.unchecked_target.write(unchecked_text)

    def source_file_n_path(self):
        return join(self._source_dir, self._source_file)

    def read_source_file(self):
        with open(self.source_file_n_path(), encoding='utf-8') as source:
            return source.read()

    def split_source(self):
        """Sends the source text to split_lines and returns the results"""
        source = self.read_source_file()
        return split_lines(source.split("\n"))

