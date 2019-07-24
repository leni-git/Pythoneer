#  + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + +
# Latest 24-July-2019
# Made by Leni ♡
# + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + +

import json
from spell_checker_abstract import AbstractHanSpellChecker

class NaverSpellChecker(AbstractHanSpellChecker):
     """
     네이버 맞춤법 검사기를 크롤링하여 결과를 출력합니다.
     """

     def __init__(self):
         url = 'https://m.search.naver.com/p/csearch/ocontent/util/SpellerProxy'
         param= {
                 '_callback' : 'leni-hanspell',
                 'q' : '만나서반갑습니다',
                 'where':'nexearch',
                 'color_blindness':0
         }
         super().__init__(url=url, param=param)

     def input_checking(self):
         size = len(self.param['q'])
         if size > 500:
             print('500자 이상은 교정할 수 없습니다.')
             return False

         return True

     def formatting(self, *, response=''):
        response = response.text
        response = response.replace(self.param['_callback']+'(', '').replace(');', '')
        json_response = json.loads(response)
        # print(response)

        result = json_response['message']['result']['notag_html']
        print(' output > {}'.format(result))


if __name__ == "__main__":
    naver = NaverSpellChecker()
    naver.param['q'] = input(' input > ')
    naver.check()
