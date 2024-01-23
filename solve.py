import requests
from bs4 import BeautifulSoup
import os  
import sys

main_code = '''#include <stdio.h>
int main()
{

}
'''

def get_codewars_title(url):
    response = requests.get(url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        
        page_title_element = soup.find('h4', class_='ml-2 mb-3')
        
        if page_title_element:
            page_title = page_title_element.text.strip().replace(' ','_')
            return page_title
        else:
            return False
    else:
        return False

def problem_website(url):
    if 'codewars' in url:
        return 'codewars'
    
def dir(website:str , problem_name:str):
    if not os.path.isdir(website):
        os.mkdir(website)
    os.mkdir(website+'/'+problem_name)
    return website + '/' + problem_name + '/'

def create_files (url , path):
    open_browser = f'''import webbrowser
webbrowser.open('{url}')
'''

    with open(path + "main.c", "w") as main_c:
        main_c.write(main_code)

    with open(path + "open.py", "w") as open_py:
        open_py.write(open_browser)
    

    
def main(argv):
    if('.com' in argv[1] and len(sys.argv) == 2 ) :
        websit = problem_website(argv[1])
        title  = get_codewars_title(argv[1])
        path   = dir(websit ,title)
        print(path + 'main.c')
        create_files(argv[1],path)
    else :
        print('invalid usage \npython solve <url>')

if __name__ == "__main__":
    main(sys.argv)
   
        

    


#url = 'https://www.codewars.com/kata/5263c6999e0f40dee200059d/train/c'

