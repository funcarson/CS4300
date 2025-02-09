import os
import task7
import pytest

def test_triangle_image_created(tmp_path):
    #Define a temporary filename
    test_filename = tmp_path / "triangle_test.png"
    
    #Call the function to create the image, using the temporary filename.
    created_filename = task7.create_triangle_image(str(test_filename))
    
    #Check that the file exists.
    assert os.path.exists(created_filename), f"File {created_filename} does not exist."
    
    #Check that the file is not empty.
    file_size = os.path.getsize(created_filename)
    assert file_size > 0, "The created image file is empty."