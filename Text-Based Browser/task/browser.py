import argparse, os, shutil, sys

open_pages_list = []

nytimes_com = '''
This New Liquid Is Magnetic, and Mesmerizing

Scientists have created “soft” magnets that can flow 
and change shape, and that could be a boon to medicine 
and robotics. (Source: New York Times)


Most Wikipedia Profiles Are of Men. This Scientist Is Changing That.

Jessica Wade has added nearly 700 Wikipedia biographies for
 important female and minority scientists in less than two 
 years.

'''

bloomberg_com = '''
The Space Race: From Apollo 11 to Elon Musk

It's 50 years since the world was gripped by historic images
 of Apollo 11, and Neil Armstrong -- the first man to walk 
 on the moon. It was the height of the Cold War, and the charts
 were filled with David Bowie's Space Oddity, and Creedence's 
 Bad Moon Rising. The world is a very different place than 
 it was 5 decades ago. But how has the space race changed since
 the summer of '69? (Source: Bloomberg)


Twitter CEO Jack Dorsey Gives Talk at Apple Headquarters

Twitter and Square Chief Executive Officer Jack Dorsey 
 addressed Apple Inc. employees at the iPhone maker’s headquarters
 Tuesday, a signal of the strong ties between the Silicon Valley giants.
'''


def delete_text_after_dot(url):
    if '.' in url:
        dot_index = url.find('.')
        return url[:dot_index]


def print_text_from_file(url):
    file_address = f'{os.getcwd()}\\{folder_name}\\' + url
    with open(file_address, "r") as file:
        for line in file:
            print(line)


def print_site(url):
    if url == 'bloomberg.com':
        print(bloomberg_com)
    elif url == 'nytimes.com':
        print(nytimes_com)
    else:
        print('Error')


def main_func():
    url = input()

    if check_url(url):

        print_site(url)
        file_name = delete_text_after_dot(url)

        if url == 'bloomberg.com':
            write_file_to_folder(file_name, bloomberg_com)
        elif url == 'nytimes.com':
            write_file_to_folder(file_name, nytimes_com)

    elif url == 'back':
        try:
            print_text_from_file(open_pages_list[-2])
        except IndexError:
            pass

    elif is_site_in_file(url):
        print_text_from_file(url)
    else:
        print('Error: Incorrect URL')


def write_file_to_folder(file_name, site_text):

    with open(file_name, "w") as file:
        file.write(site_text)

    file_source = f"{os.getcwd()}\\"
    file_destination = f'{file_source}{folder_name}\\'
    os.replace(file_source + file_name, file_destination + file_name)
    open_pages_list.append(file_name)


def check_url(url):
    if url == 'exit':
        sys.exit()
    elif '.' in url:
        return True
    return False


def create_folder(folder_name):
    if not os.access(folder_name, os.F_OK):
        os.mkdir(folder_name)


def get_argument():
    args = sys.argv
    folder_name = args[1]
    return folder_name


def is_site_in_file(url):

    file_address = f'{os.getcwd()}\\{folder_name}\\' + url
    if os.path.exists(file_address):
        return True

    return False


if __name__ == '__main__':

    folder_name = get_argument()
    create_folder(folder_name)
    url = ''

    while True:
        main_func()
