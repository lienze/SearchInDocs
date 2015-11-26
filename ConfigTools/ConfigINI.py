__author__ = 'lienze'
# coding=utf-8
import ConfigParser


class ConfigINI:
    def __init__(self):
        # 读取配置文件ini
        self.conf = ConfigParser.ConfigParser()
        self.search_word_list = []
        self.search_dir_list = []
        if self.conf:
            res = self.conf.read("config.ini")
            if res:
                conf_exist_file = True
            else:
                conf_exist_file = False

            if not conf_exist_file:
                # 看是否存在该Section，不存在则创建
                if not self.conf.has_section("combox1"):
                    self.conf.add_section("combox1")
                    for _ in xrange(1, 6):
                        self.conf.set("combox1", "item"+str(_), "")
                if not self.conf.has_section("combox2"):
                    self.conf.add_section("combox2")
                    for _ in xrange(1, 6):
                        self.conf.set("combox2", "item"+str(_), "")
                self.conf.write(open('config.ini', "w+"))
            else:
                for num in xrange(1, 5 + 1):
                    # print num
                    # 首先读取搜索记录
                    try:
                        item_tmp1 = self.conf.get("combox1", "item" + str(num))
                        self.search_word_list.append(item_tmp1)
                    except ConfigParser.NoSectionError:
                        print 'NoSectionError'
                    except ConfigParser.NoOptionError:
                        print 'NoOptionError'
                    # print item_tmp1

                    # 接着读取搜索目录记录
                    try:
                        item_tmp2 = self.conf.get("combox2", "item" + str(num))
                        self.search_dir_list.append(item_tmp2)
                    except ConfigParser.NoSectionError:
                        print 'NoSectionError'
                    except ConfigParser.NoOptionError:
                        print 'NoOptionError'
                    # print item_tmp2


    def RecordHistoryList(self, comb1, comb2):
        # 将历史搜索记录，写入配置文件config.ini
        pass