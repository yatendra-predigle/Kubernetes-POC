import time

if __name__ == "__main__":
    print("Processor 2 starting...")
    for i in range(11,21):
        print(f"Processor 1 Is Printing: {i}")
    time.sleep(5)
    print("Processor 2 Completed!")
