import unittest
from unittest.mock import patch, MagicMock
from pkgutil import ModuleInfo

import main

class TestToolDiscovery(unittest.TestCase):

    # Patch import_module and iter_modules directly in the 'main' namespace
    @patch('main.import_module')
    @patch('main.iter_modules')
    def test_discover_example_tool_and_ignore_private(self, mock_iter_modules, mock_import_module):
        
        # Simulate pkgutil finding an example tool and a private tool
        mock_iter_modules.return_value = [
            ModuleInfo(None, 'example', False),
            ModuleInfo(None, '_private_tool', False)
        ]
        
        # Prevent the import function from actually trying to load files
        mock_import_module.return_value = MagicMock()

        # Call the launcher's discovery function
        main.discover_tools()

        # Assert the example tool WAS discovered and passed to import_module
        mock_import_module.assert_any_call('tools.example')

        # Assert private modules starting with '_' were IGNORED
        for call_obj in mock_import_module.call_args_list:
            module_name = call_obj[0][0] 
            self.assertNotIn('_private_tool', module_name, "Launcher incorrectly tried to import a private module.")

if __name__ == '__main__':
    unittest.main()