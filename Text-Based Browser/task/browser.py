import argparse, os, shutil, sys

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
    elif is_site_in_file():
        pass
    else:
        print('Error: Incorrect URL')


# def write_to_file():
#     with open(f'') as file:
#         pass
#
#
# def arguments():
#     parser = argparse.ArgumentParser()
#
#     parser.add_argument('')


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


def is_site_in_file():
    pass


if __name__ == '__main__':

    folder_name = get_argument()
    create_folder(folder_name)
    url = ''

    while True:
        main_func()
