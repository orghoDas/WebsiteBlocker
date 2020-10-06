import time
from datetime import datetime as dt


host_file = 'hosts'
hosts_path = r'E:\Code\Python\Python Projects\WebsiteBlocker'

redirect = '127.0.0.1'

website_list = ['www.facebook.com', 'facebook.com']

while True:
    if dt(dt.now().year, dt.now().month, dt.now().day,8) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day,16):
        print('Working Hours...')

        with open(host_file, 'r+') as file:
            content = file.read()

            for website in website_list:
                if website in content:
                    pass

                else:
                    file.write(redirect + ' ' + website + '\n')
    
    else:
        with open(host_file, 'r+') as file:
            content = file.readlines()
            file.seek()

            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)

            file.truncate()
        print('Non-Working Hours...')
    
    time.sleep(30)