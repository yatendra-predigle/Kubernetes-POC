import time

if __name__ == "__main__":
    print("Processor 1 starting...")
    for i in range(10):
        print(f"Processor 1 Is Printing: {i}")
    time.sleep(5)
    print("Processor 1 Completed!")
