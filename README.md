## GPT3.5 API 已经发布，建议直接使用官方接口，本仓库提供中转示例
#### 更改 ```server_official.py```中的API_TOKEN字段为自己的api token,然后在可以访问openai的服务器上开启服务
```bash
python3 server_official.py
```

#### 用以下方式调用服务
```bash
curl [YOUR_IP]:5001/chat_post -d '{"message": [{"role": "user", "content": "你好"}] }'  -H 'Content-Type: application/json'
```

---------分割线-----------
### 快速开始（官方服务不稳定多尝试几次，无库依赖，个人测试账户，不长期维护，仅短期有效）
```bash
python3 chat.py
```

### 依赖 Dependency
```bash
pip3 install revChatGPT --upgrade
pip3 install flask
```

### 部署服务
openai对部分地区不提供chatGPT服务，所以需要申请韩国日本等地区服务器进行中转

在申请完自己的服务器并且开放接口后，可以用此套代码进行部署，并且使用chat.py的示例代码在任意地方访问chatGPT服务

我将一个测试token放在脚本中，并不保证其长期有效，可以自行购买或申请账户后填入config.json中的email和password字段以获得稳定的服务

首先, 在你的云机器上开通端口，以5001为例

然后，拉取本代码仓库并执行 
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
python3 chat.py
```
以直接和chatGPT进行交互

注意以上的ip也是个人测试ip，不长期维护，需要更换为自己机器的ip

## Quick Start
```bash
python3 chat.py
```



## Deploy service
Openai does not provide chatGPT service in some regions, so you need to apply for servers in South Korea, Japan and other regions for transit

After applying for your own server and opening the interface, you can use this set of code to deploy, and use the sample code of chat.py to access the chatGPT service anywhere

I put a test token in the script, which does not guarantee its long-term validity. You can purchase it yourself or fill in the email and password fields in config.json after applying for an account to obtain stable services

First, open a port on your cloud machine, taking 5001 as an example

Then, pull this code warehouse and execute
```bash
python3 server.py
``` 
For service deployment

Finally, send http requests on any machine, such as
```bash
curl -XGET http://43.155.173.103:5001/chat?q=Write%20a%20python%20program%20to%20reverse%20a%20list
```
Or run on any machine
```bash
python3 server.py
```
to directly interact with chatGPT

Note that the above IP addresses are also personal test IP addresses, which do not require long-term maintenance and need to be replaced with their own machine IP addresses

