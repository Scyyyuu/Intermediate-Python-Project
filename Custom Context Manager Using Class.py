import time

class PerformanceTimer:
    def __init__(self, label="Code Block", ignore_errors=False):
        self.label = label
        self.ignore_errors = ignore_errors
        self.start_time = None

    def __enter__(self):

        self.start_time = time.perf_counter()
        print(f"⏱️  Starting execution: [{self.label}]")
        return self  

    def __exit__(self, exc_type, exc_value, traceback):
        end_time = time.perf_counter()
        elapsed = end_time - self.start_time
        print(f"🛑 Finished: [{self.label}] took {elapsed:.6f} seconds.")

        if exc_type is not None:
            print(f"⚠️  An error occurred: {exc_type.__name__} -> {exc_value}")
            
            if self.ignore_errors:
                print("🙏 'ignore_errors' is True. Suppressing error and moving on.")
                return True  
            print("🚨 'ignore_errors' is False. Bubbling exception up!")
            return False  

with PerformanceTimer("List Comprehension"):
    squares = [x**2 for x in range(1_000_000)]

print("-" * 50)


with PerformanceTimer("Risky Calculation", ignore_errors=True):
    print("Doing some math...")
    result = 10 / 0  
    print("This line will not run.")

print("-" * 50)
print("🎉 The script successfully continued past the error!")
