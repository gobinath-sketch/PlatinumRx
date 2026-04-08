#!/usr/bin/env python3
"""
=====================================================
PLATINUMRX DATA ANALYST ASSIGNMENT - TIME CONVERTER
=====================================================

Author: Data Analyst Team
Version: 1.0
Description: Professional time conversion utility that converts
             integer minutes into human-readable "X hrs Y mins" format.
             Includes comprehensive error handling and validation.

Features:
- Input validation and error handling
- Support for negative values
- Batch processing capabilities
- Unit testing framework
- Performance optimization
- Logging and debugging support
"""

import sys
import logging
from typing import Union, List, Tuple, Optional
import time
from functools import wraps

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('time_converter.log'),
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger(__name__)

def performance_monitor(func):
    """Decorator to monitor function performance."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        logger.info(f"{func.__name__} executed in {end_time - start_time:.4f} seconds")
        return result
    return wrapper

class TimeConverterError(Exception):
    """Custom exception for Time Converter errors."""
    pass

class TimeConverter:
    """
    Professional time conversion utility class.
    
    This class provides methods to convert integer minutes into
    human-readable time format with comprehensive error handling.
    """
    
    def __init__(self):
        """Initialize the TimeConverter with default settings."""
        self.conversion_count = 0
        logger.info("TimeConverter initialized")
    
    def validate_input(self, minutes: Union[int, str]) -> int:
        """
        Validate and convert input to integer.
        
        Args:
            minutes: Input value (int or string representing int)
            
        Returns:
            int: Validated integer value
            
        Raises:
            TimeConverterError: If input is invalid
        """
        try:
            # Handle string inputs
            if isinstance(minutes, str):
                minutes = minutes.strip()
                if not minutes:
                    raise TimeConverterError("Empty string input")
                minutes = int(minutes)
            
            # Check if it's an integer
            if not isinstance(minutes, int):
                raise TimeConverterError(f"Expected integer, got {type(minutes).__name__}")
            
            # Check for reasonable bounds (optional)
            if abs(minutes) > 525600:  # More than a year in minutes
                logger.warning(f"Large input value: {minutes} minutes")
            
            return minutes
            
        except ValueError as e:
            raise TimeConverterError(f"Invalid numeric input: {minutes}") from e
        except Exception as e:
            raise TimeConverterError(f"Unexpected error during validation: {e}") from e
    
    @performance_monitor
    def convert_minutes(self, minutes: Union[int, str]) -> str:
        """
        Convert minutes to "X hrs Y mins" format.
        
        Args:
            minutes: Number of minutes to convert
            
        Returns:
            str: Formatted time string
            
        Examples:
            >>> converter = TimeConverter()
            >>> converter.convert_minutes(130)
            '2 hrs 10 mins'
            >>> converter.convert_minutes(45)
            '0 hrs 45 mins'
            >>> converter.convert_minutes(-30)
            '-0 hrs 30 mins'
        """
        try:
            # Validate input
            minutes = self.validate_input(minutes)
            
            # Handle zero case
            if minutes == 0:
                result = "0 hrs 0 mins"
                self.conversion_count += 1
                logger.debug(f"Converted {minutes} to '{result}'")
                return result
            
            # Calculate hours and minutes
            abs_minutes = abs(minutes)
            hours = abs_minutes // 60
            remaining_minutes = abs_minutes % 60
            
            # Handle negative values
            sign = '-' if minutes < 0 else ''
            
            # Format the result
            result = f"{sign}{hours} hrs {remaining_minutes} mins"
            
            self.conversion_count += 1
            logger.debug(f"Converted {minutes} to '{result}'")
            
            return result
            
        except TimeConverterError:
            raise
        except Exception as e:
            raise TimeConverterError(f"Error during conversion: {e}") from e
    
    @performance_monitor
    def batch_convert(self, minutes_list: List[Union[int, str]]) -> List[Tuple[Union[int, str], str]]:
        """
        Convert a list of minute values to formatted strings.
        
        Args:
            minutes_list: List of minute values to convert
            
        Returns:
            List[Tuple]: List of (input, output) tuples
            
        Example:
            >>> converter = TimeConverter()
            >>> converter.batch_convert([130, 45, 120])
            [(130, '2 hrs 10 mins'), (45, '0 hrs 45 mins'), (120, '2 hrs 0 mins')]
        """
        results = []
        errors = []
        
        logger.info(f"Starting batch conversion of {len(minutes_list)} items")
        
        for i, minutes in enumerate(minutes_list):
            try:
                result = self.convert_minutes(minutes)
                results.append((minutes, result))
            except TimeConverterError as e:
                error_msg = f"Error converting item {i} ({minutes}): {e}"
                errors.append(error_msg)
                logger.error(error_msg)
                results.append((minutes, f"ERROR: {e}"))
        
        if errors:
            logger.warning(f"Batch conversion completed with {len(errors)} errors")
        else:
            logger.info(f"Batch conversion completed successfully")
        
        return results
    
    def get_conversion_stats(self) -> dict:
        """
        Get conversion statistics.
        
        Returns:
            dict: Statistics about conversions performed
        """
        return {
            'total_conversions': self.conversion_count,
            'class_name': self.__class__.__name__
        }
    
    def reset_stats(self) -> None:
        """Reset conversion statistics."""
        self.conversion_count = 0
        logger.info("Conversion statistics reset")

def interactive_mode():
    """
    Interactive mode for command-line usage.
    """
    print("=" * 60)
    print("PLATINUMRX TIME CONVERTER - INTERACTIVE MODE")
    print("=" * 60)
    print("Enter minutes to convert (or 'quit' to exit)")
    print("Commands:")
    print("  'batch' - Enter multiple values")
    print("  'stats' - Show conversion statistics")
    print("  'reset' - Reset statistics")
    print("  'quit'  - Exit the program")
    print("-" * 60)
    
    converter = TimeConverter()
    
    while True:
        try:
            user_input = input("\nEnter minutes (or command): ").strip()
            
            if user_input.lower() == 'quit':
                print("Goodbye!")
                break
            
            elif user_input.lower() == 'stats':
                stats = converter.get_conversion_stats()
                print(f"\nStatistics: {stats}")
            
            elif user_input.lower() == 'reset':
                converter.reset_stats()
                print("Statistics reset!")
            
            elif user_input.lower() == 'batch':
                print("Enter minutes separated by commas:")
                batch_input = input("> ").strip()
                minutes_list = [item.strip() for item in batch_input.split(',')]
                results = converter.batch_convert(minutes_list)
                
                print("\nBatch Results:")
                print("-" * 40)
                for input_val, output in results:
                    print(f"{input_val:>10} -> {output}")
            
            else:
                # Single conversion
                result = converter.convert_minutes(user_input)
                print(f"Result: {result}")
        
        except KeyboardInterrupt:
            print("\n\nProgram interrupted. Goodbye!")
            break
        except TimeConverterError as e:
            print(f"Error: {e}")
        except Exception as e:
            logger.error(f"Unexpected error: {e}")
            print(f"Unexpected error occurred. Check logs for details.")


def run_tests():
    """
    Run comprehensive unit tests for the TimeConverter class.
    """
    print("=" * 60)
    print("RUNNING TIME CONVERTER TESTS")
    print("=" * 60)
    
    converter = TimeConverter()
    test_cases = [
        # (input, expected_output, description)
        (0, "0 hrs 0 mins", "Zero minutes"),
        (60, "1 hrs 0 mins", "Exactly one hour"),
        (130, "2 hrs 10 mins", "Standard case"),
        (45, "0 hrs 45 mins", "Less than one hour"),
        (120, "2 hrs 0 mins", "Exactly two hours"),
        (59, "0 hrs 59 mins", "One minute before hour"),
        (61, "1 hrs 1 mins", "One minute after hour"),
        (-30, "-0 hrs 30 mins", "Negative value"),
        (-90, "-1 hrs 30 mins", "Negative value > 1 hour"),
        ("120", "2 hrs 0 mins", "String input"),
        ("  45  ", "0 hrs 45 mins", "String with whitespace"),
    ]
    
    passed = 0
    failed = 0
    
    for input_val, expected, description in test_cases:
        try:
            result = converter.convert_minutes(input_val)
            if result == expected:
                print(f"✓ PASS: {description} - {input_val} -> {result}")
                passed += 1
            else:
                print(f"✗ FAIL: {description} - {input_val} -> {result} (expected {expected})")
                failed += 1
        except Exception as e:
            print(f"✗ ERROR: {description} - {input_val} -> Exception: {e}")
            failed += 1
    
    # Test batch conversion
    print("\nTesting batch conversion...")
    try:
        batch_results = converter.batch_convert([130, 45, -30, "120"])
        expected_batch = [(130, '2 hrs 10 mins'), (45, '0 hrs 45 mins'), (-30, '-0 hrs 30 mins'), ("120", '2 hrs 0 mins')]
        
        if batch_results == expected_batch:
            print("✓ PASS: Batch conversion")
            passed += 1
        else:
            print(f"✗ FAIL: Batch conversion - {batch_results}")
            failed += 1
    except Exception as e:
        print(f"✗ ERROR: Batch conversion - {e}")
        failed += 1
    
    # Test error handling
    print("\nTesting error handling...")
    error_cases = ["", "abc", None, "12.5"]
    for error_case in error_cases:
        try:
            converter.convert_minutes(error_case)
            print(f"✗ FAIL: Should have raised error for {error_case}")
            failed += 1
        except TimeConverterError:
            print(f"✓ PASS: Correctly handled error for {error_case}")
            passed += 1
        except Exception as e:
            print(f"✗ ERROR: Unexpected exception for {error_case}: {e}")
            failed += 1
    
    print("\n" + "=" * 60)
    print(f"TEST RESULTS: {passed} passed, {failed} failed")
    print("=" * 60)
    
    return failed == 0


def main():
    """
    Main function with command-line argument handling.
    """
    if len(sys.argv) > 1:
        command = sys.argv[1].lower()
        
        if command == 'test':
            success = run_tests()
            sys.exit(0 if success else 1)
        
        elif command == 'interactive':
            interactive_mode()
        
        elif command == 'convert':
            if len(sys.argv) != 3:
                print("Usage: python 01_Time_Converter.py convert <minutes>")
                sys.exit(1)
            
            try:
                converter = TimeConverter()
                result = converter.convert_minutes(sys.argv[2])
                print(result)
            except TimeConverterError as e:
                print(f"Error: {e}", file=sys.stderr)
                sys.exit(1)
        
        else:
            print("Unknown command. Available commands: test, interactive, convert")
            sys.exit(1)
    
    else:
        # Default: show usage
        print("PLATINUMRX TIME CONVERTER")
        print("=" * 40)
        print("Usage:")
        print("  python 01_Time_Converter.py test         - Run tests")
        print("  python 01_Time_Converter.py interactive  - Interactive mode")
        print("  python 01_Time_Converter.py convert <n>  - Convert single value")
        print()
        print("Example:")
        print("  python 01_Time_Converter.py convert 130")
        print("  Output: 2 hrs 10 mins")


if __name__ == "__main__":
    main()
