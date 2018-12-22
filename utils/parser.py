import requests
from bs4 import BeautifulSoup


class Parser(object):
    def parse_data(self, url, selectors):
        response = dict()
        soup = self.get_soup(url)
        for selector in selectors.get('items'):
            response[selector.get('name')] = []
            if(selector.get('has_children', False)):
                keys = selectors.get('keys').get(selector.get('name'))
                if(selector.get('type') == 'selector'):
                    things = self.get_children_from_selector(soup, selector.get('value'), selector.get('child_selector'))
                    data_list = []
                    for thing in things:
                        data = dict()
                        for key, value in keys.items():
                            data[key] = self.get_attr_from_soup(thing, value)
                        data_list.append(data)
                response[selector.get('name')] = data_list
            else:
                response[selector.get('name')] = self.get_attr_from_soup(soup, selector)
        if len(response) == 1:
            response = response.values()[0]
        return response

    def get_soup(self, url):
        return BeautifulSoup(requests.get(url).text, 'html.parser')

    def get_children_from_selector(self, soup, selector, child_selector):
        things = soup.select_one(selector)
        if things:
            return things.findChildren(child_selector.get('value'), recursive=False)
        else:
            return []

    def get_element_from_selector(self, soup, selector):
        thing = soup.select_one(selector)
        if thing:
            return thing
        else:
            return None

    def get_element_from_finder(self, soup, selector):
        thing = soup.find(selector.get('tag'), selector.get('extra'))
        if thing:
            return thing
        else:
            return None
    
    def get_attr_from_soup(self, soup, key):
        attr = None
        if key.get('type') == 'selector':
            attr = self.get_element_from_selector(soup, key.get('selector'))
        elif key.get('type') == 'finder':
            attr = self.get_element_from_finder(soup, key.get('selector'))
        if attr:
            if key.get('attr') == 'text':
                return key.get('prefix', '') + attr.text.encode('utf-8').strip() + key.get('postfix', '')
            else:
                return key.get('prefix', '') + attr.get(key.get('attr')) + key.get('postfix', '')
        return ""