import os, sys, subprocess
import random, time
import urllib.request
import threading
from threading import Thread
from queue import Queue

shell = "/bin/bash"

def test_subprocess():
    args = ["ping", "www.google.com", "-c", "4"]
    # subprocess.Popen(args, stdout=subprocess.PIPE)
    process = subprocess.Popen(args, stdout=subprocess.PIPE)
    # process = subprocess.Popen(args)
    # data = process.wait()
    data = process.communicate()
    for line in data:
        print(line)

def test_sys():
    print(sys.argv)
    print(sys.executable)
    print(sys.path)
    print(sys.platform)

class MyThread(Thread):
    """
    A threading example
    """

    def __init__(self, name):
        """Initialize the thread"""
        Thread.__init__(self)
        self.name = name

    def run(self):
        """Run the thread"""
        amount = random.randint(3, 15)
        time.sleep(amount)
        msg = "%s is running" % self.name
        print(msg)

def create_random_threads():
    """
    Create a group of threads
    """
    for i in range(5):
        name = "Thread #%s" % (i+1)
        my_thread = MyThread(name)
        my_thread.start()

class DownloadThread(Thread):
    """
    A threading example that can download a file
    """

    def __init__(self, url, name):
        """Initialize the thread"""
        Thread.__init__(self)
        self.name = name
        self.url = url

    def run(self):
        """Run the thread"""
        handle = urllib.request.urlopen(self.url)
        fname = os.path.basename(self.url)
        with open(fname, "wb") as f_handler:
            while True:
                chunk = handle.read(1024)
                if not chunk:
                    break
                f_handler.write(chunk)
        msg = "%s has finished downloading %s!" % (self.name,
                                                   self.url)
        print(msg)

class Downloader(threading.Thread):
    """Threaded File Downloader"""

    def __init__(self, queue):
        """Initialize the thread"""
        threading.Thread.__init__(self)
        self.queue = queue

    def run(self):
        """Run the thread"""
        while True:
            # gets the url from the queue
            url = self.queue.get()

            # download the file
            self.download_file(url)

            # send a signal to the queue that the job is done
            self.queue.task_done()

    def download_file(self, url):
        """Download the file"""
        handle = urllib.request.urlopen(url)
        fname = os.path.basename(url)
        with open(fname, "wb") as f:
            while True:
                chunk = handle.read(1024)
                if not chunk: break
                f.write(chunk)

def main(urls):
    """
    Run the program
    """
    queue = Queue()

    # create a thread pool and give them a queue
    for i in range(5):
        t = Downloader(queue)
        t.setDaemon(True)
        t.start()

    # give the queue some data
    for url in urls:
        queue.put(url)

    # wait for the queue to finish
    queue.join()

if __name__ == '__main__':

    # test_subprocess()
    # test_sys()

    # create_random_threads()
    urls = ["http://www.google.com"]
    main(urls)

