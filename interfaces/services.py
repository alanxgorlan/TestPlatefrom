import requests

class Services():
    def __init__(self):
        pass

    def send_request(self, data):
        """
        处理发送请求
        :param data: 前端输入的请求
        :return: 请求返回值
        """
        method = data.get('method', 'get')
        url = data.get('url')
        kwargs = {}
        if 'header' in data and data['header']:
            kwargs['header'] = data['header']
        if 'params' in data and data['params']:
            kwargs['params'] = data['params']
        #request需要三个参数，method，url和其余组成的kwargs，上面进行了判断，先简单传入header和参数
        response = requests.request(method, url, **kwargs)
        #print(response.status_code)
        return response.json()