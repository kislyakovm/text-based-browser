import codecs
import os, sys, requests
from bs4 import BeautifulSoup

open_pages_list = []


def delete_text_after_dot(url):
    if 'https://' in url:
        url = url.replace('https://', '', 1)
    if '.' in url:
        dot_index = url.rfind('.')
        return url[:dot_index]


def print_text_from_file(url):
    file_address = f'{os.getcwd()}\\{folder_name}\\' + url
    with open(file_address, "r") as file:
        for line in file:
            print(line)


def parse_site(url):
    if 'https://' not in url:
        url = 'https://' + url

    user_agent = 'Mozilla/5.0'
    r = requests.get(url, headers={'User-Agent': user_agent})
    soup = BeautifulSoup(r.content, 'html.parser')

    tags_list = ['p', 'a', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'ul', 'ol', 'li']
    text = ''

    tags = soup.find_all(tags_list)
    for tag in tags:
        text = text + tag.text + '\n'

    return text


def print_site(site_text):
    print(site_text)


def main_func():
    url = input()

    if check_url(url):

        site_text = parse_site(url)
        print_site(site_text)

        file_name = delete_text_after_dot(url)

        write_file_to_folder(file_name, site_text)

    elif url == 'back':
        try:
            print_text_from_file(open_pages_list[-2])
        except IndexError:
            pass

    elif is_site_in_file(url):
        print_text_from_file(url)
    else:
        print('Incorrect URL')


def write_file_to_folder(file_name, site_text):
    with codecs.open(file_name, "w", "utf-8") as file:
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
