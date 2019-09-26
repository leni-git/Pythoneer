# Made by Leni ♡

from logging import LoggerAdapter

class LoggerAdapter(LoggerAdapter):
    # Adapter 를 사용해서 사용자가 원하는 내용을 고정적으로 넣어주도록 설정 할 수 있다.
    def __init__(self, module, logger):
        super(LoggerAdapter, self).__init__(logger, {})
        self.module = module

    def process(self, msg, kwargs):
        if self.module:
            return "< %s > %s" % (self.module, msg), kwargs
        else:
            return "%s" % msg, kwargs
