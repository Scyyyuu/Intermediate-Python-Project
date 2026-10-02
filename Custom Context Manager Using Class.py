import time

class PerformanceTimer:
    """
    A custom context manager to measure the execution time of a code block.
    It can optionally ignore specific exceptions so your program doesn't crash.
    """
    def __init__(self, label="Code Block", ignore_errors=False):
        self.label = label
        self.ignore_errors = ignore_errors
        self.start_time = None

    def __enter__(self):
        # This runs when entering the 'with' block
        self.start_time = time.perf_counter()
        print(f"⏱️  Starting execution: [{self.label}]")
        return self  # This is what 'as timer' receives (if used)

    def __exit__(self, exc_type, exc_value, traceback):
        # This runs when exiting the 'with' block
        end_time = time.perf_counter()
        elapsed = end_time - self.start_time
        print(f"🛑 Finished: [{self.label}] took {elapsed:.6f} seconds.")

        # Check if an exception occurred inside the block
        if exc_type is not None:
            print(f"⚠️  An error occurred: {exc_type.__name__} -> {exc_value}")
            
            if self.ignore_errors:
                print("🙏 'ignore_errors' is True. Suppressing error and moving on.")
                return True  # Returning True suppresses the exception
            
            print("🚨 'ignore_errors' is False. Bubbling exception up!")
            return False  # Returning False lets Python raise the exception normally


# --- Demonstration ---

# Scenario 1: Normal execution measuring a fast loop
with PerformanceTimer("List Comprehension"):
    squares = [x**2 for x in range(1_000_000)]

print("-" * 50)

# Scenario 2: Execution that hits an error, but handles it gracefully
with PerformanceTimer("Risky Calculation", ignore_errors=True):
    print("Doing some math...")
    result = 10 / 0  # This will cause a ZeroDivisionError
    print("This line will not run.")

print("-" * 50)
print("🎉 The script successfully continued past the error!")
