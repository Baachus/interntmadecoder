"""This removes all instances of chrome driver when running a lot of Selenium Tests"""
import subprocess

def kill_chromedriver():
    """Removes all instances of chrome driver running in the background"""
    try:
        subprocess.run(['taskkill', '/IM', 'chromedriver.exe', '/F'], check=True)
        print('All instances of chromedriver have been closed')
    except subprocess.CalledProcessError:
        print('No instances of chromedriver were found')

kill_chromedriver()
