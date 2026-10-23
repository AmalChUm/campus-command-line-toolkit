"""Check input validation and the example tool's complete launcher workflow.

Run from the repository root with:
    python -m unittest discover -s tests -p test_input_helpers.py -v

The helper tests cover valid input, empty and whitespace-only input, and
integer conversion failures. A launcher integration test exercises the full
sequence of invalid attempts followed by valid input.

patch("builtins.input") supplies simulated responses instead of reading from
the terminal. A side_effect list returns one response per input() call, so
call counts verify that rejected input causes another prompt. Each patch is
automatically removed when its with block exits.

StringIO and redirect_stdout capture printed messages for assertions without
cluttering the test output. Mocked input does not print its prompt or echo the
supplied response; prompt checks therefore inspect the mock's call arguments.
These tests exercise Python behavior, not terminal rendering or keyboard input.
"""

import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch

from main import discover_tools, main
from tools import example_tool
from tools.input_helpers import read_integer, read_nonempty_text


class InputHelpersTests(unittest.TestCase):
    """Verify helper return values, validation messages, and launcher integration.

    Each test creates its own simulated input and captured output. Parameterized
    cases use subTest so a failure identifies the specific input that caused it.
    """

    def test_accepts_name_and_trims_outer_whitespace(self):
        """Return 'Andrew' after removing spaces surrounding valid text."""
        with patch("builtins.input", return_value="  Andrew  "):
            self.assertEqual(read_nonempty_text("Name: "), "Andrew")

    def test_rejects_blank_name_then_accepts_valid_name(self):
        """Reject an empty response, print an error, and accept the next name."""
        output = io.StringIO()
        with patch("builtins.input", side_effect=["", "Andrew"]) as mock_input:
            with redirect_stdout(output):
                result = read_nonempty_text("Name: ")

        self.assertEqual(result, "Andrew")
        self.assertEqual(mock_input.call_count, 2)
        self.assertIn("Please enter text; the input cannot be blank.", output.getvalue())

    def test_rejects_whitespace_only_name(self):
        """Treat spaces as blank input and request a name a second time."""
        output = io.StringIO()
        with patch("builtins.input", side_effect=["   ", "Andrew"]) as mock_input:
            with redirect_stdout(output):
                result = read_nonempty_text("Name: ")

        self.assertEqual(result, "Andrew")
        self.assertEqual(mock_input.call_count, 2)
        self.assertIn("Please enter text; the input cannot be blank.", output.getvalue())

    def test_accepts_positive_negative_and_zero_integers(self):
        """Return integer values without imposing a positive-only restriction."""
        for entered, expected in [("5", 5), ("-7", -7), ("0", 0)]:
            with self.subTest(entered=entered):
                with patch("builtins.input", return_value=entered):
                    result = read_integer("Number: ")
                self.assertIsInstance(result, int)
                self.assertEqual(result, expected)

    def test_rejects_nonnumeric_integer_input(self):
        """Reject 'hello' with an error message before accepting integer 5."""
        output = io.StringIO()
        with patch("builtins.input", side_effect=["hello", "5"]) as mock_input:
            with redirect_stdout(output):
                result = read_integer("Number: ")

        self.assertEqual(result, 5)
        self.assertEqual(mock_input.call_count, 2)
        self.assertIn("Please enter a whole number.", output.getvalue())

    def test_rejects_decimal_integer_input(self):
        """Reject '3.5' rather than rounding or truncating it to an integer."""
        output = io.StringIO()
        with patch("builtins.input", side_effect=["3.5", "5"]) as mock_input:
            with redirect_stdout(output):
                result = read_integer("Number: ")

        self.assertEqual(result, 5)
        self.assertEqual(mock_input.call_count, 2)
        self.assertIn("Please enter a whole number.", output.getvalue())

    def test_rejects_blank_integer_input(self):
        """Reject empty and whitespace-only responses, then accept integer 5."""
        for entered in ["", "   "]:
            with self.subTest(entered=repr(entered)):
                output = io.StringIO()
                with patch("builtins.input", side_effect=[entered, "5"]) as mock_input:
                    with redirect_stdout(output):
                        result = read_integer("Number: ")

                self.assertEqual(result, 5)
                self.assertEqual(mock_input.call_count, 2)
                self.assertIn("Please enter a whole number.", output.getvalue())

    def test_full_launcher_sequence(self):
        """Run the manual validation scenario through the actual launcher.

        Select the example tool, reject two blank name attempts, accept Andrew,
        reject a word, a decimal, and an empty number, then accept 5. Verify the
        launcher menu, retry-message counts, and final displayed values.
        """
        tools = discover_tools()
        # Resolve the menu choice dynamically in case other tools are added.
        selection = str(tools.index(example_tool) + 1)
        entries = [selection, "", "   ", "Andrew", "hello", "3.5", "", "5"]
        output = io.StringIO()

        with patch("builtins.input", side_effect=entries) as mock_input:
            with redirect_stdout(output):
                main()

        text = output.getvalue()
        self.assertEqual(mock_input.call_count, len(entries))
        self.assertEqual(mock_input.call_args_list[0].args, ("Choose a tool: ",))
        self.assertIn("Input Validation Example", text)
        self.assertEqual(text.count("Please enter text; the input cannot be blank."), 2)
        self.assertEqual(text.count("Please enter a whole number."), 3)
        self.assertIn("Hello, Andrew!", text)
        self.assertIn("You entered: 5", text)


if __name__ == "__main__":
    unittest.main()
