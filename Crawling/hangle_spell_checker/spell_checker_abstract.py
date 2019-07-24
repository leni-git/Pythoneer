#  + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + +
# Latest 24-July-2019
# Made by Leni ♡
# + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + +

from abc import *
import requests

class AbstractHanSpellChecker(metaclass=ABCMeta):

    @abstractmethod
    def __init__(self, *, url, param):
        self.utl_param_setting(url=url, param=param)

    @abstractmethod
    def formatting(self, *, response):
        pass
        # print('+ + + + request response\n{}\n'.format(response.text))
        # print('+ + + + result formatting\n')

    def input_checking(self):
        return True

    def utl_param_setting(self, *, url, param):
        # print('+ + + + set URL, param\n')
        if url[:7] == 'http://' or url[:8] == 'https://':
            self.url = url
        else:
            self.url = None
            print('please, check URL')

        if type(param) == dict:
            self.param = param
        else:
            self.param = None
            print('The value `param` type\'s have to dict')

    def check(self):
        if self.url != None and self.param != None:
            is_succeed = self.input_checking()
            if is_succeed:
                response = requests.get(self.url, params=self.param)
                # print('+ + + + request state : {}\n'.format(response))
                self.formatting(response=response)
        else:
            print('Please, check values (URL or param)')
