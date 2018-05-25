import logging.config
import logging
import json

# logging.config: Internal module
# logging : Internal module
# json: Internal module

# Made by Leni ♡


# Adapter 를 사용해서 사용자가 원하는 내용을 고정적으로 넣어주도록 설정 할 수 있다.
class LoggerAdapter(logging.LoggerAdapter):
    def __init__(self, module, logger):
        super(LoggerAdapter, self).__init__(logger, {})
        self.module = module

    def process(self, msg, kwargs):
        if self.module:
            return "< %s > %s" % (self.module, msg), kwargs
        else:
            return "%s" % msg, kwargs


class Logging:
    #  HAVE TO DO
    #       1. time 을 출력할 때 "날짜, 시간, 숫자" 형태로 나오는데 저 숫자부분이 무엇을 의미하는지,
    #           없애야 하는 것인지, 어떻게 없앨 수 있는지 아직 잘 모르겠다.

    def __init__(self, name, module=False):
        # module 명을 입력하지 않았을 경우에는 출력하지 않는다.
        if module:
            self.module = module

        # 파일 위치를 매번 확인해주어야 하는 것이 매우 귀찮다.
        # 어떻게 하면 자동으로 상대 경로를 찾아서 갈 수 있을까?
        # os.path.relpath 를 써 봤지만 module_logging 디렉토리가 사라져서 사용할 수가 없었다.
        with open("module_logging/logging.json", "rt") as f:
            config = json.load(f)
        logging.config.dictConfig(config)

        self.logger = logging.getLogger(name)
        self.logger = LoggerAdapter(module, self.logger)

    def debug(self, log_message):
        self.logger.debug(log_message)


if __name__ == "__main__":
    print("""
    < python code >
    
        from module_logging.module_logging import Logging
    
        log = Logging(__name__, [__moduleName__])
        log.debug(__message__)
    
    {}
    < console print >
     
        2018-05-25 15:03:29,599 < module_logging > test .byLeni
    """.format('- '*50))


