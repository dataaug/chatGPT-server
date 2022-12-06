### 依赖
```bash
pip3 install revChatGPT --upgrade
pip3 install flask
```

### 具体使用
openai对部分地区不提供chatGPT服务，所以需要申请韩国日本等地区服务器进行中转
在申请完自己的服务器并且开放接口后，可以用此套代码进行部署，并且使用chatGPT.py的示例代码在任意地方访问chatGPT服务
我将一个测试token放在脚本中，并不保证其长期有效，可以自行购买或申请账户后填入chat2gpt.py中的email和password字段以获得稳定的服务
首先, 在你的云机器上开通端口，以5001为例
然后，并执行 
```bash
python3 server.py
``` 
以进行服务部署

最后，在任意机器上发http请求，如
```bash
curl -XGET http://43.155.173.103:5001/chat?q=Write%20a%20python%20program%20to%20reverse%20a%20list
```
或者在任意机器上运行
```bash
python3 server.py
```
以直接和chatGPT进行交互
