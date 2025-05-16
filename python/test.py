#!/usr/bin/env python3

def test_python_installation():
    """
    Test basic Python functionality to verify installation is working correctly.
    This function checks:
    1. Basic Python syntax and operations
    2. Standard library imports
    3. System information
    4. File I/O capabilities
    5. Exception handling
    """
    
    import sys
    import os
    import platform
    from datetime import datetime
    
    print("Starting Python installation test...")
    print("=" * 50)
    
    # Test 1: Basic operations
    try:
        print("\n1. Testing basic operations:")
        result = 2 + 2
        print(f"   Math test: 2 + 2 = {result} ✓")
        
        test_string = "Hello, Python!"
        print(f"   String test: '{test_string}' ✓")
        
        test_list = [1, 2, 3, 4, 5]
        print(f"   List test: {test_list} ✓")
    except Exception as e:
        print(f"   Basic operations failed: {e} ✗")
    
    # Test 2: System information
    try:
        print("\n2. System information:")
        print(f"   Python version: {sys.version}")
        print(f"   Platform: {platform.system()} {platform.release()}")
        print(f"   Machine: {platform.machine()}")
        print(f"   Python executable: {sys.executable}")
    except Exception as e:
        print(f"   System info failed: {e} ✗")
    
    # Test 3: Import standard libraries
    try:
        print("\n3. Testing standard library imports:")
        import json
        import urllib
        import sqlite3
        import re
        print("   Successfully imported: json, urllib, sqlite3, re ✓")
    except ImportError as e:
        print(f"   Import failed: {e} ✗")
    
    # Test 4: File operations
    try:
        print("\n4. Testing file operations:")
        test_file = "/tmp/python_test.txt"
        
        # Write to file
        with open(test_file, 'w') as f:
            f.write("Python installation test successful!")
        print(f"   File write test: Created {test_file} ✓")
        
        # Read from file
        with open(test_file, 'r') as f:
            content = f.read()
        print(f"   File read test: Read '{content}' ✓")
        
        # Clean up
        os.remove(test_file)
        print(f"   File cleanup: Removed {test_file} ✓")
    except Exception as e:
        print(f"   File operations failed: {e} ✗")
    
    # Test 5: Date and time
    try:
        print("\n5. Testing date/time operations:")
        current_time = datetime.now()
        print(f"   Current time: {current_time.strftime('%Y-%m-%d %H:%M:%S')} ✓")
    except Exception as e:
        print(f"   Date/time operations failed: {e} ✗")
    
    print("\n" + "=" * 50)
    print("Python installation test completed!")
    print("If you see mostly ✓ marks above, your Python installation is working well.")
    
if __name__ == "__main__":
    # This block runs only when the script is executed directly
    test_python_installation()
