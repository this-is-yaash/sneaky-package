import pytest
from unittest.mock import patch
from package.models import display 

@patch("builtins.print")
def test_modelsDisplay(mock_print):
    display("test")

    mock_print.assert_called_once_with("""print("If it's visible, then it's good to go!")""")
