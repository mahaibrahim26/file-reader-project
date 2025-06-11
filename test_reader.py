import os
from reader import FileReader

def test_get_content():
    
    test_file = "files/test_file.txt"
    with open(test_file, "w") as f:
        f.write("line 1\nline 2")

    reader = FileReader(test_file)
    content = reader.get_content()

    assert content == "line 1\nline 2"

    
    os.remove(test_file)
