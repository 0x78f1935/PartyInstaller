import requests
import re
from bs4 import BeautifulSoup


class WebTools(object):
    def __init__(self):
        self._url = "https://forum.eekllc.com/viewforum.php?f=8"
        self._total_pages = []

        self.all_hyperlinks = []

    def fetch_all_hyperlinks(self, htmlpage, look_for_pages: bool = False):
        """Fetches all stories and capable to look for the total pages available
        
        Note
        ----
        All pages found will be stored in the variable `self._total_pages`
        """
        soup = BeautifulSoup(htmlpage, 'html.parser')
        links = []

        for link in soup.find_all(attrs={'href': re.compile("./viewtopic")}):
            links.append((link.get('href'), link.contents))
        
        if look_for_pages:
            _ = []
            for link in soup.find_all(attrs={'href': re.compile("./viewforum")}):
                _.append(link.get('href'))
            self._total_pages = list(set([str(i).replace('./', 'https://forum.eekllc.com/') for i in _ if 'start' in str(i)]))
            
        return links

    def create_html_page_from_url(self, url):
        page = requests.get(url)
        return page.text
    
    def format_dirty_links(self, data):
        """
        This method reads the Eeck form form page.
        https://forum.eekllc.com/viewforum.php?f=8
        It will remove all pages and filters duplicates.
        """
        tmp_results = []
        results = {
            "csc": {},
            "stories" : {}
        } # Our final dict

        for i in range(len(data)):
            url = data[i][0]
            name = data[i][1][0]

            # Remove all page numbered pages
            if name != '1': # Weird somehow it fetches with the parser
                if str(url).startswith('./'):
                    url = "https://forum.eekllc.com/" + str(url)[2:]

                if 'start' not in str(url) and '#' not in str(url):
                    tmp_results.append((name, url,))

        del data
        tmp_results = list(set(tmp_results))
        # Filter out rules and installation instructions
        for item in tmp_results:
            name = item[0]
            url = item[1]
            if 'Custom Story Creator' in name:
                results['csc']['thread'] = url
                results['csc']['thread_title'] = name
                results["current_version"] = re.search(r'(csc).*(\d+\.)?(\d+\.)?(\*|\d+)', results['csc']['thread_title'].lower())
            elif 'please read - custom story showcase announcements and rules' in name.lower():
                results["rules"] = url
            else:
                results['stories'][name] = url

        return results

    def scrape_all_pages(self):
        """Scrape all available pages from data dynamically"""
        predata = self.create_html_page_from_url(self._url)
        data = [i for i in self.fetch_all_hyperlinks(predata, True)]
        for page in self._total_pages:
            [data.append(result) for result in self.fetch_all_hyperlinks(self.create_html_page_from_url(page))]
        return self.format_dirty_links(data)

    def fetch_all_li(self, htmlpage):
        soup = BeautifulSoup(htmlpage, 'html.parser')
        result = []

        for liitem in soup.find_all('dl'):
            if "viewtopic" in str(liitem):
                result.append(liitem)
        return result