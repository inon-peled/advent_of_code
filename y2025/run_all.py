#!/usr/bin/env python3
"""
Run all Python files in the current directory except this script.
"""
import os
import subprocess
import sys
from pathlib import Path


def _find_python_files(script_dir, script_name):
    """Find all Python files in the directory, excluding this script."""
    py_files = sorted(script_dir.glob("*.py"))
    return [f for f in py_files if f.name != script_name]


def _run_python_file(py_file, script_dir):
    """Run a single Python file and return (filename, status)."""
    print(f"{'-'*60}")
    print(f"Running: {py_file.name}")

    try:
        result = subprocess.run(
            [sys.executable, str(py_file)],
            cwd=script_dir,
            capture_output=True,
            text=True,
            timeout=30
        )

        # Print output
        if result.stdout:
            print(result.stdout)
        if result.stderr:
            print(f"STDERR:\n{result.stderr}", file=sys.stderr)

        # Determine status
        if result.returncode == 0:
            status = "Finished running without runtime errors."
        else:
            status = f"ERROR (exit code {result.returncode})"

    except subprocess.TimeoutExpired:
        print(f"TIMEOUT: {py_file.name} took longer than 30 seconds")
        status = "TIMEOUT"
    except Exception as e:
        print(f"ERROR running {py_file.name}: {e}")
        status = f"ERROR: {e}"

    print()
    return py_file.name, status


def _print_summary(results):
    """Print summary of all results."""
    print(f"\n{'-'*60}")
    print("SUMMARY")
    for filename, status in results:
        print(f"{filename}: {status}")


def main():
    # Get the directory where this script is located
    script_dir = Path(__file__).parent
    script_name = Path(__file__).name

    # Find all Python files to run
    py_files = _find_python_files(script_dir, script_name)

    if not py_files:
        print("No Python files found to run.")
        return

    print(f"Found {len(py_files)} Python file(s) to run:\n")

    # Run all files and collect results
    results = []
    for py_file in py_files:
        result = _run_python_file(py_file, script_dir)
        results.append(result)

    # Print summary
    _print_summary(results)


if __name__ == "__main__":
    main()
