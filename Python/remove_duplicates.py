#!/usr/bin/env python3
"""
=====================================================
PLATINUMRX DATA ANALYST ASSIGNMENT - DUPLICATE REMOVER
=====================================================

Author: Data Analyst Team
Version: 1.0
Description: Professional string manipulation utility that removes
             duplicate characters from strings using optimized algorithms.
             Includes multiple approaches for different use cases.

Features:
- Multiple removal strategies (preserve order, sorted, etc.)
- Performance optimization for large strings
- Comprehensive error handling and validation
- Batch processing capabilities
- Unit testing framework
- Performance benchmarking
- Unicode and special character support
"""

import sys
import logging
import time
import unicodedata
from typing import Union, List, Dict, Optional, Set
from collections import OrderedDict
from functools import wraps
import re

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('duplicate_remover.log'),
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
        execution_time = end_time - start_time
        logger.info(f"{func.__name__} executed in {execution_time:.6f} seconds")
        return result, execution_time
    return wrapper

class DuplicateRemoverError(Exception):
    """Custom exception for Duplicate Remover errors."""
    pass

class DuplicateRemover:
    """
    Professional duplicate character removal utility class.
    
    This class provides multiple methods to remove duplicate characters
    from strings with different strategies and optimizations.
    """
    
    def __init__(self):
        """Initialize the DuplicateRemover with default settings."""
        self.processing_count = 0
        self.total_characters_processed = 0
        self.method_performance = {}
        logger.info("DuplicateRemover initialized")
    
    def validate_input(self, input_string: Union[str, None]) -> str:
        """
        Validate and normalize input string.
        
        Args:
            input_string: Input string to validate
            
        Returns:
            str: Validated and normalized string
            
        Raises:
            DuplicateRemoverError: If input is invalid
        """
        try:
            if input_string is None:
                raise DuplicateRemoverError("Input cannot be None")
            
            if not isinstance(input_string, str):
                raise DuplicateRemoverError(f"Expected string, got {type(input_string).__name__}")
            
            # Normalize Unicode characters
            normalized = unicodedata.normalize('NFKC', input_string)
            
            # Log large inputs
            if len(normalized) > 10000:
                logger.warning(f"Processing large input: {len(normalized)} characters")
            
            return normalized
            
        except DuplicateRemoverError:
            raise
        except Exception as e:
            raise DuplicateRemoverError(f"Unexpected error during validation: {e}") from e
    
    def remove_duplicates_ordered(self, input_string: Union[str, None]) -> str:
        """
        Remove duplicate characters while preserving original order.
        Uses a set for O(1) lookup performance.
        
        Args:
            input_string: String to process
            
        Returns:
            str: String with duplicates removed
            
        Example:
            >>> remover = DuplicateRemover()
            >>> remover.remove_duplicates_ordered("programming")
            'progamin'
        """
        input_string = self.validate_input(input_string)
        
        seen = set()
        result = []
        
        for char in input_string:
            if char not in seen:
                seen.add(char)
                result.append(char)
        
        output = ''.join(result)
        self.processing_count += 1
        self.total_characters_processed += len(input_string)
        
        logger.debug(f"Ordered removal: '{input_string}' -> '{output}'")
        return output
    
    def remove_duplicates_ordered_dict(self, input_string: Union[str, None]) -> str:
        """
        Remove duplicates using OrderedDict (Python 3.7+ maintains insertion order).
        Alternative approach for comparison.
        
        Args:
            input_string: String to process
            
        Returns:
            str: String with duplicates removed
        """
        input_string = self.validate_input(input_string)
        
        # OrderedDict.fromkeys preserves order and removes duplicates
        result = ''.join(OrderedDict.fromkeys(input_string))
        
        self.processing_count += 1
        self.total_characters_processed += len(input_string)
        
        logger.debug(f"OrderedDict removal: '{input_string}' -> '{result}'")
        return result
    
    def remove_duplicates_loop(self, input_string: Union[str, None]) -> str:
        """
        Remove duplicates using traditional loop approach.
        Educational method showing basic algorithm.
        
        Args:
            input_string: String to process
            
        Returns:
            str: String with duplicates removed
        """
        input_string = self.validate_input(input_string)
        
        result = ""
        
        for char in input_string:
            if char not in result:
                result += char
        
        self.processing_count += 1
        self.total_characters_processed += len(input_string)
        
        logger.debug(f"Loop removal: '{input_string}' -> '{result}'")
        return result
    
    def remove_duplicates_sorted(self, input_string: Union[str, None]) -> str:
        """
        Remove duplicates and return sorted result.
        Useful when order doesn't matter.
        
        Args:
            input_string: String to process
            
        Returns:
            str: String with duplicates removed and sorted
        """
        input_string = self.validate_input(input_string)
        
        # Convert to set to remove duplicates, then sort and join
        result = ''.join(sorted(set(input_string)))
        
        self.processing_count += 1
        self.total_characters_processed += len(input_string)
        
        logger.debug(f"Sorted removal: '{input_string}' -> '{result}'")
        return result
    
    def remove_duplicates_regex(self, input_string: Union[str, None]) -> str:
        """
        Remove duplicates using regular expressions.
        Advanced method for specific patterns.
        
        Args:
            input_string: String to process
            
        Returns:
            str: String with consecutive duplicates removed
        """
        input_string = self.validate_input(input_string)
        
        # Remove consecutive duplicates (not all duplicates)
        result = re.sub(r'(.)\1+', r'\1', input_string)
        
        self.processing_count += 1
        self.total_characters_processed += len(input_string)
        
        logger.debug(f"Regex removal: '{input_string}' -> '{result}'")
        return result
    
    def remove_duplicates_case_insensitive(self, input_string: Union[str, None]) -> str:
        """
        Remove duplicates case-insensitively, preserving first occurrence's case.
        
        Args:
            input_string: String to process
            
        Returns:
            str: String with case-insensitive duplicates removed
        """
        input_string = self.validate_input(input_string)
        
        seen_lower = set()
        result = []
        
        for char in input_string:
            if char.lower() not in seen_lower:
                seen_lower.add(char.lower())
                result.append(char)
        
        output = ''.join(result)
        self.processing_count += 1
        self.total_characters_processed += len(input_string)
        
        logger.debug(f"Case-insensitive removal: '{input_string}' -> '{output}'")
        return output
    
    def batch_process(self, 
                     strings: List[str], 
                     method: str = 'ordered') -> List[Dict[str, Union[str, float]]]:
        """
        Process multiple strings using specified method.
        
        Args:
            strings: List of strings to process
            method: Processing method ('ordered', 'loop', 'sorted', 'dict', 'regex', 'case_insensitive')
            
        Returns:
            List of dictionaries with input, output, and processing time
        """
        methods = {
            'ordered': self.remove_duplicates_ordered,
            'loop': self.remove_duplicates_loop,
            'sorted': self.remove_duplicates_sorted,
            'dict': self.remove_duplicates_ordered_dict,
            'regex': self.remove_duplicates_regex,
            'case_insensitive': self.remove_duplicates_case_insensitive
        }
        
        if method not in methods:
            raise DuplicateRemoverError(f"Unknown method: {method}. Available: {list(methods.keys())}")
        
        process_func = methods[method]
        results = []
        
        logger.info(f"Starting batch processing of {len(strings)} items using {method} method")
        
        for i, string in enumerate(strings):
            try:
                output, exec_time = process_func(string)
                results.append({
                    'index': i,
                    'input': string,
                    'output': output,
                    'processing_time': exec_time,
                    'input_length': len(string),
                    'output_length': len(output)
                })
            except DuplicateRemoverError as e:
                logger.error(f"Error processing item {i}: {e}")
                results.append({
                    'index': i,
                    'input': string,
                    'output': f"ERROR: {e}",
                    'processing_time': 0,
                    'input_length': len(string) if string else 0,
                    'output_length': 0
                })
        
        logger.info(f"Batch processing completed")
        return results
    
    def benchmark_methods(self, test_string: str) -> Dict[str, Dict[str, float]]:
        """
        Benchmark all methods with the same input string.
        
        Args:
            test_string: String to test with all methods
            
        Returns:
            Dictionary with performance metrics for each method
        """
        methods = {
            'ordered': self.remove_duplicates_ordered,
            'loop': self.remove_duplicates_loop,
            'sorted': self.remove_duplicates_sorted,
            'dict': self.remove_duplicates_ordered_dict,
            'regex': self.remove_duplicates_regex,
            'case_insensitive': self.remove_duplicates_case_insensitive
        }
        
        results = {}
        
        logger.info(f"Benchmarking all methods with string length: {len(test_string)}")
        
        for method_name, method_func in methods.items():
            try:
                output, exec_time = method_func(test_string)
                results[method_name] = {
                    'execution_time': exec_time,
                    'output': output,
                    'output_length': len(output),
                    'compression_ratio': len(output) / len(test_string) if test_string else 0
                }
            except Exception as e:
                logger.error(f"Error in {method_name}: {e}")
                results[method_name] = {
                    'execution_time': float('inf'),
                    'output': f"ERROR: {e}",
                    'output_length': 0,
                    'compression_ratio': 0
                }
        
        # Sort by execution time
        sorted_results = dict(sorted(results.items(), key=lambda x: x[1]['execution_time']))
        
        return sorted_results
    
    def get_statistics(self) -> Dict[str, Union[int, float]]:
        """
        Get processing statistics.
        
        Returns:
            Dictionary with statistics
        """
        return {
            'total_processing_count': self.processing_count,
            'total_characters_processed': self.total_characters_processed,
            'average_string_length': self.total_characters_processed / self.processing_count if self.processing_count > 0 else 0,
            'method_performance': self.method_performance
        }
    
    def reset_statistics(self) -> None:
        """Reset processing statistics."""
        self.processing_count = 0
        self.total_characters_processed = 0
        self.method_performance = {}
        logger.info("Statistics reset")


def interactive_mode():
    """
    Interactive mode for command-line usage.
    """
    print("=" * 70)
    print("PLATINUMRX DUPLICATE REMOVER - INTERACTIVE MODE")
    print("=" * 70)
    print("Available methods:")
    print("  1. ordered       - Remove duplicates preserving order (recommended)")
    print("  2. loop          - Traditional loop method")
    print("  3. sorted        - Remove duplicates and sort result")
    print("  4. dict          - Using OrderedDict method")
    print("  5. regex         - Remove consecutive duplicates")
    print("  6. case_insensitive - Remove duplicates ignoring case")
    print("\nCommands:")
    print("  'batch'         - Process multiple strings")
    print("  'benchmark'     - Compare all methods")
    print("  'stats'         - Show processing statistics")
    print("  'reset'         - Reset statistics")
    print("  'quit'          - Exit program")
    print("-" * 70)
    
    remover = DuplicateRemover()
    
    while True:
        try:
            user_input = input("\nEnter string (or command): ").strip()
            
            if user_input.lower() == 'quit':
                print("Goodbye!")
                break
            
            elif user_input.lower() == 'stats':
                stats = remover.get_statistics()
                print(f"\nStatistics: {stats}")
            
            elif user_input.lower() == 'reset':
                remover.reset_statistics()
                print("Statistics reset!")
            
            elif user_input.lower() == 'batch':
                print("Enter strings separated by commas:")
                batch_input = input("> ").strip()
                strings = [s.strip() for s in batch_input.split(',')]
                
                print("\nSelect method (1-6):")
                method_choice = input("> ").strip()
                method_map = {
                    '1': 'ordered', '2': 'loop', '3': 'sorted',
                    '4': 'dict', '5': 'regex', '6': 'case_insensitive'
                }
                
                method = method_map.get(method_choice, 'ordered')
                results = remover.batch_process(strings, method)
                
                print(f"\nBatch Results ({method} method):")
                print("-" * 50)
                for result in results:
                    print(f"Input:  {result['input']}")
                    print(f"Output: {result['output']}")
                    print(f"Time:   {result['processing_time']:.6f}s")
                    print("-" * 50)
            
            elif user_input.lower() == 'benchmark':
                test_string = input("Enter test string for benchmarking: ").strip()
                results = remover.benchmark_methods(test_string)
                
                print(f"\nBenchmark Results:")
                print("-" * 70)
                print(f"{'Method':<20} {'Time (s)':<12} {'Output':<20} {'Compression':<12}")
                print("-" * 70)
                
                for method, metrics in results.items():
                    time_str = f"{metrics['execution_time']:.6f}"
                    output_str = metrics['output'][:20] + "..." if len(metrics['output']) > 20 else metrics['output']
                    comp_str = f"{metrics['compression_ratio']:.2%}"
                    print(f"{method:<20} {time_str:<12} {output_str:<20} {comp_str:<12}")
            
            else:
                # Single string processing
                print("\nSelect method (1-6, default=1):")
                method_choice = input("> ").strip() or '1'
                method_map = {
                    '1': 'ordered', '2': 'loop', '3': 'sorted',
                    '4': 'dict', '5': 'regex', '6': 'case_insensitive'
                }
                
                method = method_map.get(method_choice, 'ordered')
                
                if method == 'ordered':
                    result = remover.remove_duplicates_ordered(user_input)
                elif method == 'loop':
                    result = remover.remove_duplicates_loop(user_input)
                elif method == 'sorted':
                    result = remover.remove_duplicates_sorted(user_input)
                elif method == 'dict':
                    result = remover.remove_duplicates_ordered_dict(user_input)
                elif method == 'regex':
                    result = remover.remove_duplicates_regex(user_input)
                elif method == 'case_insensitive':
                    result = remover.remove_duplicates_case_insensitive(user_input)
                
                print(f"Result ({method}): {result}")
        
        except KeyboardInterrupt:
            print("\n\nProgram interrupted. Goodbye!")
            break
        except DuplicateRemoverError as e:
            print(f"Error: {e}")
        except Exception as e:
            logger.error(f"Unexpected error: {e}")
            print(f"Unexpected error occurred. Check logs for details.")


def run_tests():
    """
    Run comprehensive unit tests for the DuplicateRemover class.
    """
    print("=" * 70)
    print("RUNNING DUPLICATE REMOVER TESTS")
    print("=" * 70)
    
    remover = DuplicateRemover()
    test_cases = [
        # (input, expected_output, description)
        ("programming", "progamin", "Standard case"),
        ("hello world", "helo wrd", "With spaces"),
        ("aaaaabbbbccccc", "abc", "Repeated characters"),
        ("", "", "Empty string"),
        ("a", "a", "Single character"),
        ("abca", "abc", "Character at start and end"),
        ("Python3.8!", "Python3.8!", "With special characters"),
        ("AaBbCc", "AaBbCc", "Case sensitive"),
        ("123123123", "123", "Numbers"),
        ("!@#!!@#@", "!@#", "Special characters"),
        ("   ", " ", "Multiple spaces"),
        ("abcd", "abcd", "No duplicates"),
    ]
    
    passed = 0
    failed = 0
    
    print("Testing ordered removal method...")
    for input_val, expected, description in test_cases:
        try:
            result = remover.remove_duplicates_ordered(input_val)
            if result == expected:
                print(f"✓ PASS: {description} - '{input_val}' -> '{result}'")
                passed += 1
            else:
                print(f"✗ FAIL: {description} - '{input_val}' -> '{result}' (expected '{expected}')")
                failed += 1
        except Exception as e:
            print(f"✗ ERROR: {description} - '{input_val}' -> Exception: {e}")
            failed += 1
    
    # Test case insensitive
    print("\nTesting case insensitive method...")
    case_test_cases = [
        ("HelloHELLO", "Helo"),
        ("AaBbAaBb", "AB"),
        ("PythonPYTHON", "Python"),
    ]
    
    for input_val, expected in case_test_cases:
        try:
            result = remover.remove_duplicates_case_insensitive(input_val)
            if result == expected:
                print(f"✓ PASS: Case insensitive - '{input_val}' -> '{result}'")
                passed += 1
            else:
                print(f"✗ FAIL: Case insensitive - '{input_val}' -> '{result}' (expected '{expected}')")
                failed += 1
        except Exception as e:
            print(f"✗ ERROR: Case insensitive - '{input_val}' -> Exception: {e}")
            failed += 1
    
    # Test sorted method
    print("\nTesting sorted method...")
    sorted_test_cases = [
        ("programming", "agimnopr"),
        ("hello", "ehlo"),
        ("python", "hnopty"),
    ]
    
    for input_val, expected in sorted_test_cases:
        try:
            result = remover.remove_duplicates_sorted(input_val)
            if result == expected:
                print(f"✓ PASS: Sorted - '{input_val}' -> '{result}'")
                passed += 1
            else:
                print(f"✗ FAIL: Sorted - '{input_val}' -> '{result}' (expected '{expected}')")
                failed += 1
        except Exception as e:
            print(f"✗ ERROR: Sorted - '{input_val}' -> Exception: {e}")
            failed += 1
    
    # Test error handling
    print("\nTesting error handling...")
    error_cases = [None, 123, [], {}]
    for error_case in error_cases:
        try:
            remover.remove_duplicates_ordered(error_case)
            print(f"✗ FAIL: Should have raised error for {error_case}")
            failed += 1
        except DuplicateRemoverError:
            print(f"✓ PASS: Correctly handled error for {error_case}")
            passed += 1
        except Exception as e:
            print(f"✗ ERROR: Unexpected exception for {error_case}: {e}")
            failed += 1
    
    print("\n" + "=" * 70)
    print(f"TEST RESULTS: {passed} passed, {failed} failed")
    print("=" * 70)
    
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
        
        elif command == 'remove':
            if len(sys.argv) < 3:
                print("Usage: python 02_Remove_Duplicates.py remove <string> [method]")
                print("Methods: ordered, loop, sorted, dict, regex, case_insensitive")
                sys.exit(1)
            
            try:
                remover = DuplicateRemover()
                method = sys.argv[3].lower() if len(sys.argv) > 3 else 'ordered'
                
                if method == 'ordered':
                    result = remover.remove_duplicates_ordered(sys.argv[2])
                elif method == 'loop':
                    result = remover.remove_duplicates_loop(sys.argv[2])
                elif method == 'sorted':
                    result = remover.remove_duplicates_sorted(sys.argv[2])
                elif method == 'dict':
                    result = remover.remove_duplicates_ordered_dict(sys.argv[2])
                elif method == 'regex':
                    result = remover.remove_duplicates_regex(sys.argv[2])
                elif method == 'case_insensitive':
                    result = remover.remove_duplicates_case_insensitive(sys.argv[2])
                else:
                    print(f"Unknown method: {method}")
                    sys.exit(1)
                
                print(result)
            except DuplicateRemoverError as e:
                print(f"Error: {e}", file=sys.stderr)
                sys.exit(1)
        
        else:
            print("Unknown command. Available commands: test, interactive, remove")
            sys.exit(1)
    
    else:
        # Default: show usage
        print("PLATINUMRX DUPLICATE REMOVER")
        print("=" * 50)
        print("Usage:")
        print("  python 02_Remove_Duplicates.py test                    - Run tests")
        print("  python 02_Remove_Duplicates.py interactive             - Interactive mode")
        print("  python 02_Remove_Duplicates.py remove <string> [method] - Remove duplicates")
        print()
        print("Example:")
        print("  python 02_Remove_Duplicates.py remove programming")
        print("  Output: progamin")
        print()
        print("  python 02_Remove_Duplicates.py remove 'HelloHELLO' case_insensitive")
        print("  Output: Hello")


if __name__ == "__main__":
    main()
