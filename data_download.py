import re
# from datasets import load_dataset
#
# dataset = load_dataset("silver/personal_dialog")

# with open('famous_data/famouwords.txt','r') as word_read, open('famous_data/procced_data.txt','w') as words_write:
#
#     for i, line in enumerate(word_read):
#         line = line.replace(" ","")
#         line = line.replace("   ","")
#         line = line.replace("一一","--")
#         line = line.replace("一一一","--")
#         line = line.replace("	","")
#         line = line.replace("	","")
#
#         words_write.write(line.strip())
#         if '--' in line or '篇' in line:
#             words_write.write('\n')

# names = ['吴虹飞','于谦','郑渊洁','郭德纲','马晓春','宁财神','潘石屹','余华','贾平凹','格非','陈村','严歌苓','万方','朱文',
#          '李银河','张维迎','朱大可','陈平原','李陀','钟鸣','赵汀阳','贾樟柯','田壮壮','宁浩','张楚','何勇',
#          '沈昌文','周传基','黄永玉','吴清源','单田芳','何兆武','郑敏','赵宝熙']
# names_ = ['吴虹飞：','于谦：','郑渊洁：','郭德纲：','马晓春：','宁财神：','潘石屹：','余华：','贾平凹：','格非：','陈村：','严歌苓：','万方：','朱文：',
#           '李银河：','张维迎：','朱大可：','陈平原：','李陀：','钟鸣：','赵汀阳：','贾樟柯：','田壮壮：','宁浩：','张楚：','何勇：',
#           '沈昌文：','周传基：','黄永玉：','吴清源：','单田芳：','何兆武：','郑敏：','赵宝熙：']
# log = []
# with open('famous_data/raw/新建文本文档2.txt','r',encoding='utf-8') as word_read, open('famous_data/这个世界好些了么.txt','w',encoding='utf-8') as words_write:
#     for i, line in enumerate(word_read):
#         line = line.replace(" ","")
#         line = line.replace("   ","")
#         # if line.split('－')[0].isdigit() or line.strip() == '摄' or line.strip() == '这个世界好些了吗？':
#         #     continue
#         # if len(line.strip()) == 1:
#         #     words_write.write(line.strip())
#         #     continue
#
#         if i < 131:
#
#             for na in names_:
#                 if na in line:
#                     words_write.write('\n')
#                     log.append(line.strip())
#                     break
#                 # else:
#                 #     words_write.write(line.strip())
#                 #     continue
#             words_write.write(line.strip())
#             for na in names_:
#                 if na in line:
#                     words_write.write('\n')
#                     break
#         else:
#             if line.strip() in log:
#                 continue
#             if line.split('：')[0] in names:
#                 words_write.write('\n' + line.strip())
#             else:
#                 words_write.write(line.strip())
#             # words_write.write(line.strip() + '\n')


# names = ['杨绛','叶嘉莹','章含之','孙穗芳','靳羽西','杨澜','王小慧','林青霞','杨丽苹','张丽丽','英格丽·张','舒婷','赵玫','高岚',
#          '丁建华','王利芬','王海鸽','王丽萍','宋安娜','丛珊','郎平','蒋敏','张泉灵','许戈辉','柯兰','茹丝',
#          '史依弘','李瑛','马爱农','靳凯华','张喜静','钱向民','臧秀云','于承艳']
#
# names_ = ['杨','叶','章','孙','靳','杨','王','林','杨','张','英','舒','赵','高',
#          '丁','王','王','王','宋','丛','郎','蒋','张','许','柯','茹',
#          '史','李','马','靳','张','钱','臧','于']

# with open('famous_data/raw/张星名人访谈录爱是女人一生的梦女人篇.txt','r',encoding='utf-8') as word_read:
#     id = []
#     for i, line in enumerate(word_read):
#         if line.strip() == "访 谈 录":
#             id.append(i)
#     print(id)

# 张星 男人篇
# names = ['张星','傅聪','陈钢','刘诗昆','郎朗','蔡国强','韩美林','范曾','白先勇','李致','朱德庸','尔宝瑞','周龙','杜鸣心','黄宗江',
#          '徐沛东','海岩','周令钊','陈忠实','王树林','爱泼斯坦','曾宪梓','小泽征尔','朱棣文','约翰·奈斯比特','吾德','库恩',
#          '科特勒','郭少明','阿利卡诺夫','金钟七','徐勇','王志刚','吴经国','程志强','肖克凡','石康','刘明秀','姜育恒','李祥霆',
#          '司马南','李耀宇']
#
# names_2 = ['张星：','傅聪：','陈钢：','刘诗昆：','郎朗：','蔡国强：','韩美林：','范曾：','白先勇：','李致：','朱德庸：','尔宝瑞','周龙：','杜鸣心：','黄宗江：',
#          '徐沛东：','海岩：','周令钊：','陈忠实：','王树林：','爱泼斯坦：','曾宪梓：','小泽征尔：','朱棣文：','约翰·奈斯比特：','吾德：','库恩：',
#          '科特勒：','郭少明：','阿利卡诺夫：','金钟七：','徐勇：','王志刚：','吴经国：','程志强：','肖克凡：','石康：','刘明秀：','姜育恒：','李祥霆：',
#          '司马南：','李耀宇：']
#
# names_ = ['张','傅','陈','刘','郎','蔡','韩','范','白','李','朱','尔','周','杜','黄',
#           '徐','海','周','陈','王','爱','曾','小','朱','约','吾','库',
#           '科','郭','阿','金','徐','王','吴','程','肖','石','刘','姜','李',
#           '司','李']
#
# with open('famous_data/raw/张星名人访谈录男人篇.txt','r',encoding='utf-8') as word_read, open('famous_data/张星_男人篇.txt','w',encoding='utf-8') as words_write:
#     for i, line in enumerate(word_read):
#
#         if  line != '\n':
#             if line.split()[0] in names or line.split()[0] in names_ or line.split()[0] in names_2:
#                 words_write.write('\n' + line.strip())
#             else:
#                 words_write.write(line.strip())

# # 杨澜之纵横
# names = ['多明戈','梅塔','让·雷诺','尤努斯','黄永玉','马未都','赵本山','郭德纲','周立波','陈忠和','郑欣淼','蔡铭超','林毅夫','瞿墨','张黎',
#          '布什','希拉里','巩俐','张海迪','查尔斯','杨澜','卢英德','福斯特','卡特']
#
#
# names_ = ['多','梅','让','尤','黄','马','赵','郭','周','陈','郑','蔡','林','瞿','张',
#           '布','希','巩','张','查','杨','卢','福','卡']
#
# with open('famous_data/杨澜访谈之纵横.txt','r',encoding='utf-8') as word_read, open('famous_data/杨澜访谈之纵横2.txt','w',encoding='utf-8') as words_write:
#     for i, line in enumerate(word_read):
#         nPos = 0
#         for na in names:
#             if na in line.strip():
#                 nPos = line.find(na)
#         if nPos == 0:
#             words_write.write(line.strip() + '\n')
#         else:
#             words_write.write(line.strip()[:nPos] + '\n' + line.strip()[nPos:] + '\n')

# names = ['崔永元','吕克·贝松','柳云龙：','甄子丹：','曾荫权：','李连杰','杨澜','杨澜：']
#
#
#
# with open('famous_data/raw/杨澜采访.txt','r',encoding='utf-8') as word_read, open('famous_data/杨澜访谈1.txt','w',encoding='utf-8') as words_write:
#     for i, line in enumerate(word_read):
#
#         if  line != '\n':
#             if line.split()[0] in names or line.strip()[:2] in names or line.strip()[:3] in names or line.strip()[:4] in names or line.strip()[:5] in names:
#                 if line.split()[0] == '崔永元' or line.split()[0] == '李连杰' or line.split()[0] == '杨澜':
#                     words_write.write('\n' + line.strip() + ': ')
#                 else:
#                     words_write.write('\n' + line.strip())
#             else:
#                 words_write.write(line.strip())


# from docx import Document
# names = ['崔','吕','柳','甄','曾','李','杨']
# doc = Document("famous_data/raw/123.docx")
# print(doc.paragraphs)
# for paragraph in doc.paragraphs:
#     if paragraph.text != '' and paragraph.text[0] in names:
#         print(paragraph.text)


#
# names = ['崔永元','吕克·贝松','柳云龙：','甄子丹：','曾荫权：','李连杰','杨澜','杨澜：',
#          '杨紫烨','洪瑛','沈冰','张悦然','王全安','王治郅','柳传志','林怀民','谭盾']
#
# names_ = ['崔','吕','柳','甄','曾','李','杨','杨',
#          '杨','洪','沈','张','王','王','柳','林','谭']
#


# with open('famous_data/raw/杨澜访谈1-2.txt','r',encoding='utf-8') as word_read, open('famous_data/杨澜访谈1-2.txt','w',encoding='utf-8') as words_write:
#     for i, line in enumerate(word_read):
#
#         if  line.strip() != '\n' and line.strip() != '':
#             print(line)
#             if line.split()[0] in names or line.split()[0] in names_:
#                 words_write.write('\n' + line.strip())
#             else:
#                 words_write.write(line.strip())


# names = []
# with open('famous_data/raw/朗读者I+II 大全集共6册.txt','r',encoding='utf-8') as word_read, open('famous_data/朗读者I+II.txt','w',encoding='utf-8') as words_write:
#     for i, line in enumerate(word_read):
#
#         if '：' in line and 1 < len(line.split('：')[0]) < 6:
#             if line.split('：')[0] not in names:
#                 names.append(line.split('：')[0])
# print(names)

# names = ['董卿', '濮存昕', '蒋励', '柳传志', '周小林', '观众', '殷洁',  '张梓琳', '许渊冲',
#          '陶艳波', '杨乃斌',  '蒋雯丽', '林兆铭', '乔榛', '唐国妹', '王千源', '秦玥飞', '谭腾蛟',
#          '周璇', '陈昱璇', '陈旖雪', '杨琪', '麦家', '徐静蕾',  '理查德', '郭小平', '李亚鹏',
#          '胡玮炜', '倪萍',  '单霁翔', '赵蕊蕊', '陈章武', '刘迅',  '女儿', '王学圻',
#          '柯洁', '许镜清', '刘震云',  '王珮瑜', '杨利伟', '陆川', '斯琴高娃', '赖敏', '丁一舟',
#          '张家敏', '张鲁新', '熊治文', '海子说', '姚晨',  '程何',  '曹文轩',   '李立群', '万鑫',
#          '司崇昶', '丁福建', '卞龙', '申海霞', '杨秋花',  '王蒙', '江一燕', '汪明荃', '罗家英',
#          '秋爸爸', '秋妈妈', '李宁', '翟墨', '樊锦诗', '王耀庆', '梁晓声',  '冉莹颖', '邹市明',
#          '邹明轩', '毕飞宇', '赵文瑄', '潘际銮', '李世豫', '张小娴', '胡忠英', '张艾嘉', '吴纯',
#          '叶锦添',  '叶嘉莹', '刘慈欣', '姚建中', '王起洪', '吴文霞',  '安文彬', '金士杰', '江疏影',
#          '王姬', '王丽珍', '郭琨', '老狼', '余秀华', '冯小刚', '张璘', '徐和谊', '郎平',
#          '张庆坤', '李忠仙', '宋世雄', '惠若琪', '魏秋月', '袁心玥', '徐云丽', '王源', '施则威',
#          '杨心怡', '单伯瑄', '薛其坤', '徐卓', '姚明', '宗庆后', '贾平凹', '许鞍华', '果妈', '果爸',
#          '果爸 果妈', '录音一', '录音二', '双雪涛', '袁泉', '崔之久', '谢又予', '胡歌', '黄泓翔',
#          '阿乙', '王石', '曾孝濂', '邓清明', '邓满琪', '刘烨', '潘建伟', '朱德庸', '靳尚谊',
#          '范迪安', '张一山', '刘仁俊', '阿来', '张毅', '杨惠姗', '程不时', '赵克良', '汤家力',
#          '陈数', '矣晓沅', '刘和平', '罗大佑', '张弥曼', '惠英红', '徐国义', '徐嘉余', '楼霞',
#          '王佩民', '李彦宏', '李韵迪', '魏世杰',  '王洛勇', '王坚', '刘亮程', '孟非', '黄永玉',
#          '马伊琍', '丘成桐', '郑智', '赖声川', '吴孟超', '宁浩', '孙雪梅', '王丽东', '俞敏洪',
#          '谭元元', '王智量', '迟福林', '唐家三少', '吉吉', '林鸣', '陈佳洱',  '白岩松', '斯那定珠',
#          '余华', '贾樟柯', '郑愁予']
#
# with open('famous_data/raw/朗读者I+II 大全集共6册.txt','r',encoding='utf-8') as word_read, open('famous_data/朗读者I+II.txt','w',encoding='utf-8') as words_write:
#     for i, line in enumerate(word_read):
#         line = line.strip()
#         try:
#             if line.split()[0] == '朗读者' and line.split()[1] in names:
#                 # print(i, line)
#                 words_write.write('\n\n' + line.split()[1])
#                 with open('famous_data/raw/朗读者I+II 大全集共6册.txt','r',encoding='utf-8') as word_read2:
#                     # print(i, line)
#                     # words_write.write('\n')
#                     for i2, line2 in enumerate(word_read2):
#
#                         line2 = line2.strip()
#                         try:
#                             if i <= i2:
#                                 # print(i, i2, line2)
#                                 if line2.strip().split('：')[0] in names:
#                                     words_write.write('\n' + line2.strip())
#                                 else:
#                                     if line2.split()[0] == '朗读者' and line2.split()[1] in names:
#                                         words_write.write('\n')
#                                     if line2.split()[0] == '朗读者读本' or line2.split()[0] == '读本':
#                                         words_write.write('\n')
#                                     words_write.write(line2.strip())
#                                 if line2.split()[0] == '朗读者读本' or line2.split()[0] == '读本' or line2.split()[0] == '导演手记':
#                                     # print('break')
#                                     break
#                         except IndexError as reason:
#                             pass
#         except IndexError as reason:
#             pass

# name = ['杜鲁门·卡波蒂','欧内斯特·海明威','亨利·米勒','弗拉基米尔·纳博科夫','杰克·凯鲁亚克',
#         '约翰·厄普代克','加夫列尔·加西亚·马尔克斯','雷蒙德·卡佛','米兰·昆德拉','阿兰·罗伯格里耶',
#         '君特·格拉斯','保罗·奥斯特','村上春树','奥尔罕·帕慕克','斯蒂芬·金','翁贝托·埃科']
#
# name_ = ['卡波蒂','海明威','米勒','纳博科夫','凯鲁亚克',
#         '厄普代克','马尔克斯','卡佛','昆德拉','罗伯格里耶',
#         '格拉斯','奥斯特','村上春树','帕慕克','金','埃科']
#
#
#
# names2 = [ '拉尔夫·艾里森', '《巴黎评论》', '艾里森', '罗伯特·弗罗斯特','弗罗斯特', '伊利亚·爱伦堡', '爱伦堡',
#         '塞利纳', '阿瑟·米勒', '米勒', '约翰·多斯·帕索斯','多斯·帕索斯', '海因里希·伯尔', '伯尔', '哈罗德·布鲁姆',
#            '布鲁姆', '布鲁姆夫人', '钦努阿·阿契贝', '阿契贝', '约翰·勒卡雷', '勒卡雷', 'A.S.拜厄特',
#            '拜厄特', '乔纳森·弗兰岑', '弗兰岑', '埃马纽艾尔·卡雷尔', '卡雷尔', '凯尔泰斯','路易—费迪南·塞利纳',
#            '费迪南·塞利纳','塞利纳','罗伯特·戈特利布','戈特利布','凯尔泰斯·伊姆莱','伊姆莱']



# with open('famous_data/raw/巴黎评论·作家访谈6.txt','r',encoding='utf-8') as word_read, open('famous_data/巴黎评论·作家访谈6.txt','w',encoding='utf-8') as words_write:
#     for i, line in enumerate(word_read):
#
#         if '：' in line and 1 < len(line.split('：')[0]) < 8:
#             if line.split('：')[0] not in names2:
#                 names2.append(line.split('：')[0])
# print(names2)

# with open('famous_data/raw/巴黎评论·作家访谈6.txt','r',encoding='utf-8') as word_read, open('famous_data/巴黎评论·作家访谈6.txt','w',encoding='utf-8') as words_write:
#     for i, line in enumerate(word_read):
#         # print(line)
#         if  line.strip().startswith('◎')  or line.strip().startswith('（原载') or line.strip().startswith('[') :
#             continue
#         try:
#             # if  line.strip().split('：')[0] in names2 or line.strip().split('：')[0] in name or line.strip().split('：')[0] in name_:
#             if  line.strip().split('：')[0] in names2:
#                 words_write.write('\n' + line.strip())
#             else:
#                 words_write.write(line.strip())
#
#
#         except AttributeError as reason:
#              print('error')

# names2 = [ '加西亚·马尔克斯', '马尔克斯', '埃内斯托·贡萨莱斯·贝梅霍', '贝梅霍',
#            '丽塔·吉伯特', '吉伯特']
#
#
# with open('famous_data/加西亚·马尔克斯访谈录.txt','r',encoding='utf-8') as word_read, open('famous_data/加西亚·马尔克斯访谈录2.txt','w',encoding='utf-8') as words_write:
#     for i, line in enumerate(word_read):
#
#         try:
#             # if  line.strip().split('：')[0] in names2 or line.strip().split('：')[0] in name or line.strip().split('：')[0] in name_:
#             if  line.strip().split('：')[0] in names2:
#                 words_write.write('\n' + line.strip())
#             else:
#                 words_write.write(line.strip())
#
#
#         except AttributeError as reason:
#             print('error')

# names2 = [ '拉尔夫·艾里森', '《巴黎评论》', '艾里森', '罗伯特·弗罗斯特','弗罗斯特', '伊利亚·爱伦堡', '爱伦堡',
#         '塞利纳', '阿瑟·米勒', '米勒', '约翰·多斯·帕索斯','多斯·帕索斯', '海因里希·伯尔', '伯尔', '哈罗德·布鲁姆',
#            '布鲁姆', '布鲁姆夫人', '钦努阿·阿契贝', '阿契贝', '约翰·勒卡雷', '勒卡雷', 'A.S.拜厄特',
#            '拜厄特', '乔纳森·弗兰岑', '弗兰岑', '埃马纽艾尔·卡雷尔', '卡雷尔', '凯尔泰斯','路易—费迪南·塞利纳',
#            '费迪南·塞利纳','塞利纳','罗伯特·戈特利布','戈特利布','凯尔泰斯·伊姆莱','伊姆莱']


# names1= ['托马斯·米德尔霍夫', '黄奇帆', '林怀民', '邵忠', '蒋昌健', '托马斯', '杨润', '王海兵', '王全安', '王荣轩', '王石', '武韬', '王小慧', '王侠军', '徐永光', '杨紫烨', '郑佳明', '周梁淑怡']
names2= ['托马斯·米德尔霍夫','杨澜', '黄奇帆', '林怀民', '邵忠', '蒋昌健', '托马斯', '杨润', '王海兵', '王全安', '王荣轩', '王石', '武韬', '王小慧', '王侠军', '徐永光', '杨紫烨', '郑佳明', '周梁淑怡']


# with open('famous_data/raw/让未来记住今天下杨澜访谈录6周年特辑.txt','r',encoding='utf-8') as word_read, open('famous_data/让未来记住今天下杨澜访谈录6周年特辑.txt','w',encoding='utf-8') as words_write:
#     for i, line in enumerate(word_read):
#
#         if '：' in line and len(line.split('：')[0]) < 8:
#             if line.split('：')[0] not in names2:
#                 names2.append(line.split('：')[0])
#         # if line.split()[0] not in names2:
#         #     names2.append(line.split()[0])
# print(names2)

# with open('famous_data/让未来记住今天下杨澜访谈录6周年特辑.txt','r',encoding='utf-8') as word_read, open('famous_data/让未来记住今天下杨澜访谈录6周年特辑2.txt','w',encoding='utf-8') as words_write:
#     for i, line in enumerate(word_read):
#         # print(line)
#         if  line.strip().startswith('◎')  or line.strip().startswith('（原载') or line.strip().startswith('[') :
#             continue
#         try:
#             # if  line.strip().split('：')[0] in names_:
#             #     name = line.strip().split('：')[0]
#             #     print(name)
#
#             nPos = line.find('杨澜',3)
#             for name in names1:
#
#                 nPos2 = line.find(name,3)
#
#             if  line.strip().split('：')[0] in names2 or line.strip().split()[0] in names2 :
#                 if nPos != -1 and nPos2 == -1:
#
#                     words_write.write('\n' + line[:nPos] + '\n' + line[nPos:])
#                 elif nPos == -1 and nPos2 != -1:
#                     words_write.write('\n' + line[:nPos2] + '\n' + line[nPos2:])
#                 elif nPos != -1 and nPos2 != -1:
#                     words_write.write('\n' + line[:nPos] + '\n' + line[nPos:nPos2] +
#                                       '\n' + line[nPos:nPos2] + '\n' + line[nPos2:])
#                 else:
#                     words_write.write('\n' + line.strip())
#             else:
#                 words_write.write(line.strip())
#
#
#         except IndexError as reason:
#              print('error')

names2= ['鲁豫', '查良镛', '朱德庸', '朱重威', '韩寒', '舒乙', '沈昌文', '陈冠中', '雷颐', '魏明伦',
         '阿来', '海岩', '况浩文', '周梅森', '邓贤', '郭敬明', '李彦宏', '张朝阳', '郑明明',
         '刘晓庆', '张兰', '江南春', '李想', '高燃', '戴志康', '茅侃侃', '裘秋帆', '董铭',
         '冯炜炜', '田野', '杨怀定', '王晨', '刘磊', '帅学军', '范冰冰', '李玉', '李宇春',
         '文章', '马伊琍', '周觅', '刘易阳', '童佳倩', '胡歌', 'Karen', '景天',  '郑渊洁',
         '郑亚旗', '郑小琼', '高晓攀', '尤宪超', '李林', '赵臣', '刘伟', '伊能静', '高晓松',
         '周立波', '白浪', '赵举山', '白天德', '山娃', '杨阳', '记者', '雷文新', '王刚',
         '张悦', '李灵', '高翔', '周云洁', '高展', '云洁爸', '云洁',   '李庆文', '董栋',
         '秦汉', '孙国豪', '刘德华',  '黄秋生', '张学友', '李宗盛', '崔健',  '曾志伟', '罗大佑',
         '任贤齐', '钟镇涛', '梁家辉','梁',  '孙一',  '黑玫瑰',  '成龙', '吴若甫', '罗家英',
         '濮存昕', '苏民', '苏宁', '陈宝国',  '刘佩琦', '刘威',  '张铁林', '唐国强', '冯远征',
         '梁丹妮']



# with open('famous_data/raw/鲁豫有约说出你的故事5册.txt','r',encoding='utf-8') as word_read, open('famous_data/鲁豫有约说出你的故事5册.txt','w',encoding='utf-8') as words_write:
#     for i, line in enumerate(word_read):
#
#         if '：' in line and len(line.split('：')[0]) < 8:
#             if line.split('：')[0] not in names2:
#                 names2.append(line.split('：')[0])
#         # if line.split()[0] not in names2:
#         #     names2.append(line.split()[0])
# print(names2)

with open('famous_data/raw/鲁豫有约说出你的故事5册.txt','r',encoding='utf-8') as word_read, open('famous_data/鲁豫有约说出你的故事5册.txt','w',encoding='utf-8') as words_write:
    for i, line in enumerate(word_read):
        line = line.strip()
        try:
            if line.split()[0] == '人物小传' or line.split()[0] == '人物小传：':
                # print(i, line)
                # words_write.write('\n\n')
                with open('famous_data/raw/鲁豫有约说出你的故事5册.txt','r',encoding='utf-8') as word_read2:
                    # print(i, line)
                    # words_write.write('\n')
                    for i2, line2 in enumerate(word_read2):
                        line2 = line2.strip()
                        try:
                            if i <= i2:
                                # print(i, i2, line2)
                                if line2.strip().split('：')[0] in names2:
                                    words_write.write('\n')
                                    break
                                else:
                                    words_write.write(line2.strip())
                        except IndexError as reason:
                            pass
            if line.split()[0] in names2 or line.split('——')[0] in names2 or line.split('：')[1] in names2 :
                words_write.write('\n\n\n' + line + '\n')
            if line.split('：')[0] in names2:
                words_write.write(line + '\n')
        except IndexError as reason:
            pass



