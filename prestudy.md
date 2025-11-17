本地开发环境 (工欲善其事)

知道如何在自己的电脑上安装 Python 和 VS Code。✔
学会打开 VS Code 内置的终端 (Terminal)✔，并能使用 cd, ls (或 dir) 等基本命令切换目录。
<!-- VS Code 终端默认会继承系统的终端类型：Windows：通常是 Command Prompt（CMD）或 PowerShell（VS终端使用的） -->
# cd　　全称：Change Directory切换目录　
　　　　　　　　　<!-- 在计算机中，目录是用于组织和存储文件的容器（即文件夹）日常操作时
 “新建文件夹”等行为本质上都是在操作目录。 -->
D:         <!-- 在Windows里需要先切换到对应盘 -->
cd D:/name <!-- 用绝对路径切换 tip:输入路径时，可按 Tab 键自动补全 若路径包含空格需用引号包裹-->

cd name    <!-- 若已在对应目录，用相对路径即可 -->

cd ..      <!-- 从当前目录回到上一级.在winPowerShell是cd ~，CMD是cd %userprofile% -->
# ls   全称：List Segment（列出片段）或 List Directory Contents（列出目录内容）
ls         <!-- 列出当前目录内容（简洁版） -->
ls -l      <!-- long详细列表（显示权限、大小、修改时间等） -->
ls -a      <!-- all显示所有文件（包括隐藏文件，以.开头的文件） -->
# dir  全称：Directory目录 显示当前目录下的文件和文件夹 用于CMD
dir        <!-- 列出目录内容 -->
项目管理的基石：虚拟环境 (venv)
#　虚拟环境是一个独立隔离的程序运行环境
理解为什么需要虚拟环境（为每个项目创建独立的“工具箱”）。
# 避免冲突，减少内存与资源占用，便于合作
掌握创建 (python -m venv venv) 和激活虚拟环境的命令。
# 用venv创建虚拟环境：打开终端，执行以下命令
　　　 python -m venv 环境名　　<!-- 目录下会生成一个同名文件夹，包含虚拟环境的所有文件（解释器、pip、依赖库等） -->
   　　myenv\Scripts\activate.bat（CMD中）或.\myenv\Scripts\Activate.ps1（pshell中）<!-- 激活虚拟环境activate -->
学会在激活虚拟环境后，使用 pip install requests 来安装第三方库。
#      pip install requests==2.20.0       <!-- 安装依赖（仅在当前虚拟环境生效） -->
       pip list                           <!-- 查看当前环境安装的库 -->
知道如何使用 pip freeze > requirements.txt 生成项目依赖文件。
#      pip freeze > requirements.txt      <!-- 导出当前虚拟环境的依赖为.txt，供他人或部署时使用 -->
            用pip install -r requirements.txt 在新的虚拟环境中执行
退出用 deactivate  回到系统
Python 包管理器 （pip）
# 即Package Installer for Python，是用于安装、卸载、管理第三方库（包）的工具


# 创建文件夹：Windows：md 文件夹名 或 mkdir 文件夹名
文件操作与 JSON
#　.json 是 JSON 格式的文件，用于数据交换和存储，语法简洁、跨语言兼容
<!-- API 数据交互：前后端分离开发中，后端常返回 JSON 格式数据，前端解析后展示（例如接　
　口 https://api.example.com/user 返回用户信息 JSON）
通过 json.dump() 和 json.load()，可以轻松实现程序运行中数据的存储和复用
JSON 适合存储中小型数据，若数据量极大（如百万级条目），可能影响读写效率，可考虑数据库SQL（如 SQLite、MySQL）。 -->
掌握 Python 的 with open(...) 语句来安全地读写文件。
学会使用 json 模块的 json.load() (从文件读取 JSON) 和 json.dump() (将 Python 字典/列表写入 JSON 文件)。
# 读取已有数据
import json
# 从 JSON 文件中读取数据（程序下次运行时）
try:
    with open("user_data.json", "r", encoding="utf-8") as f:
        loaded_data = json.load(f)  <!-- 转换为什么类型取决于后文给变量loaded_data的定义 -->

   # 复用读取到的数据
    print(f"加载的用户信息：{loaded_data['name']}，年龄 {loaded_data['age']}")
    print(f"偏好设置：{loaded_data['settings']['theme']} 主题")

except FileNotFoundError:
    print("未找到数据文件，使用默认数据")
   # 可选：如果文件不存在，初始化默认数据
    loaded_data = {"name": "Guest", "age": 0, "hobbies": [], "settings": {}}
#　存储运行时产生的数据：
import json

# 程序运行中产生的数据（例如用户信息、配置参数等）
# 例如：
user_data = {
    "name": "Alice",
    "age": 20,
    "hobbies": ["reading", "coding"],
    "settings": {"theme": "dark", "notifications": True}
}

# 将数据写入 JSON 文件（存储到磁盘）
with open("user_data.json", "w", encoding="utf-8") as f:
    ensure_ascii=False：<!-- 保留中文等非 ASCII 字符的原始样子 -->
    indent=2：<!-- 格式化输出，便于人类阅读 -->
    json.dump(user_data, f, ensure_ascii=False, indent=2)

print("数据已保存到 user_data.json")


HTTP 网络请求 (初探)

初步理解客户端 (Client) 和服务器 (Server) 的概念。
学会使用 requests 库的 requests.get() 方法来从一个 URL 获取数据。
推荐教程：B站视频：HTTP是什么？<https://www.bilibili.com/video/BV1zb4y127JU/ >
# 协议·是为了实现数据传输、功能控制而约定的 “通用规则集合
<!-- 比如USB 协议（通用串行总线协议）,蓝牙协议（BLE),WiFi 协议；物联网场景低功耗、远距离通信的LoRa 协议例：自动驾驶场景车载数据传输低延迟、高可靠性的以太网 AVB 协议，51 单片机常用的 UART 串口协议,HTTP,HTTPS也是协议 -->
# 两个对象：服务端与客户端，服务端持续等待客户端发起请求并作出回复
一次交流由客户端向服务端通过网络发起请求报文开始，到服务端向客户端返回响应报文结束，默认的持久连接直到客户端发送Connection：close首部结束
<!--                         请求报文                           响应报文
起始行                 |<方法> <请求URL（地址）> <版本>    |<版本> <状态码> <原因短语>
<首部> -资源的属性和条件|<请求首部>                        |<响应首部>
                                                         |<主体> -->
<!-- 状态码：2xx 成功 3xx 重定向  4xx 客户端错误   5xx 服务端错误 -->
# TCP/IP网络通信层级划分：应用层（HTTP所属层）  传输层（TCP✔和UDP所属层）  网际层   网络接口层
<!-- cookie是一种节省服务端资源实现保存客户端信息的方式，在首部加上cookie信息即可 -->
