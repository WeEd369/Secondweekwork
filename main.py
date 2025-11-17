import json
# 从 JSON 文件中读取数据（程序下次运行时）
try:
    with open("data.json", "r", encoding="utf-8") as f:
        volunteers = json.load(f)  # 转换为 Python 列表list
   
except FileNotFoundError:
    print("未找到数据文件，初始化空 volunteers 列表")
    volunteers = [ 
    {'id': '101', 'name': '张三', 'hours': 25},
    {'id': '102', 'name': '李四', 'hours': 40},
    {'id': '103', 'name': '王五', 'hours': 18}
    ]  # 初始化空数据结构

def list_show():
    print("欢迎使用志愿者时长管理系统")
    print("-------------------------")
    print("1. 显示所有志愿者信息")
    print("2. 查询指定志愿者时长")
    print("3. 添加新的志愿者信息")
    print("4. 统计人均志愿时长")
    print("5. 退出系统")
    print("6. 获取每日一句")
    print("-------------------------")
    print("请输入您的选择 (1-6):")

def show_all():
    print(f"\n以下是所有志愿者信息:")
    print("id\tname\thours")
    print("-------------------------")
    for volunteer in volunteers:
        print(f"{volunteer['id']}\t{volunteer['name']}\t{volunteer['hours']}")
    print("-------------------------")
    
def search():
    input_name = input("请输入您要查询志愿时长的志愿者姓名：")
    
    for volunteer in volunteers:
        if volunteer['name'] == input_name:
            print(f"{volunteer['name']}的志愿时长:{volunteer['hours']}")
            return
    print(f"查无此人！")

def correct_inputcheck(add_hours):
    try:
        value = int(add_hours)
        return True,value
    except:
        print("输入无效，请输入有效的数字")
        return False,0

def add():
    add_id = input("请输入您要添加的志愿者学号：")
    
    for volunteer in volunteers:
        if volunteer['id'] == add_id:
            print(f"\n志愿者学号：{add_id}已存在！")
            return
    add_name = (input("\n请输入您要添加的志愿者的姓名："))
    add_hours = (input("请输入志愿时长："))
    bo_l,value = correct_inputcheck(add_hours) 
    if bo_l:
        if value < 0:
            print("输入无效，请输入大于零的数字")
            return
        volunteers.append({'id':add_id,'name':add_name,'hours':value})
        loaded_data = volunteers
        print(f"\n成功添加志愿者: {add_name}")

def average_volunteers():
    sum_hour = 0
    
    for volunteer in volunteers:
        sum_hour += volunteer['hours']
    average_hour = sum_hour / len(volunteers)
    print(f"所有志愿者平均志愿时长：{average_hour:.2f}h")

def getword():
    import requests

    try:
        response = requests.get("https://v1.hitokoto.cn/?c=d&encode=text")
        if response.status_code == 200:
            print("每日一句：", response.text)
        else:
            print("获取每日一句失败，状态码：", response.status_code)
    except Exception as e:
        print("获取每日一句时发生错误：", e)

def main():
    while True:
        list_show()
        try:
            choice = input().strip()
            
            if choice == '1':
                show_all()
            elif choice == '2':
                search()
            elif choice == '3':
                add()
            elif choice == '4':
                average_volunteers()
            elif choice == '5':
                print("感谢使用！期待与您再会")
                break
            elif choice == '6':
                getword()
            else:
                print("\n选择无效,请输入1-6之间的数字")

            input("\n按Enter键继续...")
        except:
            input("\n按Enter键继续...")
main()
try:
    with open("data.json", "w", encoding="utf-8") as f:
        json.dump(volunteers, f, ensure_ascii=False, indent=4)  # 转换为 JSON 格式并写入文件
except Exception as e:
    print("保存数据时发生错误：", e)