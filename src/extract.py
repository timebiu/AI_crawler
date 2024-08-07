
def extract_text(el):
    start_tag = '<a href="'
    end_tag = '</a>'

    # 找到<a>标签的起始位置
    start_index = el.find(start_tag)
    if start_index != -1:
        start_index += len(start_tag)
        # 找到</a>标签的结束位置
        end_index = el.find(end_tag, start_index)
        if end_index != -1:
            # 提取标题
            title = el[start_index:end_index].split('">')[-1]
    return title


def extract_url(el):
    # 使用字符串方法提取URL
    start_tag = 'href="'
    end_tag = '"'

    # 找到href属性的起始位置
    start_index = el.find(start_tag)
    if start_index != -1:
        start_index += len(start_tag)
        # 找到href属性的结束位置
        end_index = el.find(end_tag, start_index)
        if end_index != -1:
            # 提取URL
            url = el[start_index:end_index]
    return url