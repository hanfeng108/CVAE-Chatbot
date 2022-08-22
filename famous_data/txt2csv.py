import csv
import pandas as pd
import tqdm
# from columns_name import list_array  #list_array所在文件

def Txt2Csv(Txt_path, Csv_path):
    '''
    :param Txt_path: txt文件路径
    :param Csv_path: csv文件路径
    :return:
    '''


    out = open(Csv_path,'w',newline='')        #要转成的.csv文件，先创建一个LF1big.csv文件
    csv_writer = csv.writer(out,dialect='excel')
    csv_writer.writerow(['Celebrity', 'topic', 'persona', 'interviewer', 'interviewee'])
    # get name
    with open(Txt_path, 'r', encoding='utf-8') as fin:
        names = []
        for i, line in enumerate(fin):
            if len(line) == 0:
                continue
            if len(line.split('：')) > 1 and 1 < len(line.split('：')[0]) < 11 and line.split('：')[0] not in names:
                name = line.split('：')[0]
                names.append(line.split('：')[0])

    with open(Txt_path, 'r', encoding='utf-8') as fin:
        topic = ''
        dialog = []
        contents = []
        for i, line in enumerate(fin):
            line = line.strip()
            if len(line) == 0:
                continue
            # line_content = line
            if line.split()[0] in names:
                name = line.split()[0]
                topic = line.split()[1]
                dialog_interviewer = ''
                if len(dialog):
                    dialog = []

            if line.split('，')[0] in names:  # persona line, 将来可以在线爬取数据
                dialog.append(name)
                dialog.append(topic)
                dialog.append(line.replace(name + "，", '')) # persona

            elif line.split('：')[0] in names:  # utterance line 考虑到一个人连续说两句话
                # 去除第一句是受访者说的
                # if line.split('：')[0] != '采访者' and len(contents) == 0:
                #     continue
                if line.split('：')[0] == '采访者':
                    dialog_interviewer = line.split('：')[1]
                else:
                    if dialog_interviewer == '':
                        continue
                    dialog_response = line.split('：')[1]
                    dialog.append(dialog_interviewer)
                    dialog.append(dialog_response)
                    contents.append(dialog)
                    csv_writer.writerow(dialog)
                    dialog = dialog[:len(dialog) - 2]
                    dialog_interviewer = ''
                    dialog_response = ''

                last_name = line.split('：')[0]


    # df = pd.DataFrame(contents)
    #
    # # df.to_csv(Csv_path, header=False)           # 不添加表头
    # df.columns = ["Source", "Target", "Type", "Path"]  # 添加表头
    #
    #
    # df.to_csv(Csv_path, index=False,encoding="UTF_8_sig") #使用encoding在写入csv文件时指定编码方式，解决中文乱码问题
    print("数据写入成功")

Txt2Csv('./Celebrity_train.txt', './test.csv')
