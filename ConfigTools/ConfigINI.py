__author__ = 'lienze'
# coding=utf-8
import ConfigParser

RECORD_HISTORY_NUM = 5  # 历史记录数量

class ConfigINI:

    def __init__(self):
        # 读取配置文件ini
        conf = ConfigParser.ConfigParser()
        self.search_word_list = []
        self.search_dir_list = []
        if conf:
            res = conf.read("config.ini")
            if res:
                conf_exist_file = True
            else:
                conf_exist_file = False

            if not conf_exist_file:
                # 看是否存在该Section，不存在则创建
                if not conf.has_section("combox1"):
                    conf.add_section("combox1")
                    for _ in xrange(1, RECORD_HISTORY_NUM+1):
                        conf.set("combox1", "item"+str(_), "")
                if not conf.has_section("combox2"):
                    conf.add_section("combox2")
                    for _ in xrange(1, RECORD_HISTORY_NUM+1):
                        conf.set("combox2", "item"+str(_), "")
                conf.write(open('config.ini', "w+"))
            else:
                for num in xrange(1, RECORD_HISTORY_NUM + 1):
                    # 首先读取搜索记录
                    try:
                        item_tmp1 = conf.get("combox1", "item" + str(num))
                        if item_tmp1:
                            self.search_word_list.append(item_tmp1)
                    except ConfigParser.NoSectionError:
                        print 'NoSectionError'
                    except ConfigParser.NoOptionError:
                        print 'NoOptionError'
                    # print item_tmp1

                    # 接着读取搜索目录记录
                    try:
                        item_tmp2 = conf.get("combox2", "item" + str(num))
                        if item_tmp2:
                            self.search_dir_list.append(item_tmp2)
                    except ConfigParser.NoSectionError:
                        print 'NoSectionError'
                    except ConfigParser.NoOptionError:
                        print 'NoOptionError'
                    # print item_tmp2

    def RecordHistoryList(self):
        # 将历史搜索记录，写入配置文件config.ini
        # print 'start to record'
        conf = ConfigParser.ConfigParser()
        conf.read("config.ini")
        for _ in xrange(0, RECORD_HISTORY_NUM):
            # print _, len(self.search_word_list)
            # print _, len(self.search_dir_list)
            if _ < len(self.search_word_list):
                # 记录到配置文件中
                # print self.search_word_list[_]
                if type(self.search_word_list[_]).__name__ == 'unicode':
                    print self.search_word_list[_]
                    conf.set("combox1", "item"+str(_+1), self.search_word_list[_].encode('utf-8'))
                else:
                    conf.set("combox1", "item"+str(_+1), self.search_word_list[_])
            if _ < len(self.search_dir_list):
                print self.search_dir_list[_]
                if type(self.search_dir_list[_]).__name__ == 'unicode':
                    conf.set("combox2", "item"+str(_+1), self.search_dir_list[_].encode('utf-8'))
                else:
                    conf.set("combox2", "item"+str(_+1), self.search_dir_list[_])

        conf.write(open('config.ini', "w+"))
