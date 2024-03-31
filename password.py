from datetime import datetime, timezone
import pytz  
  
def getStrDate():
    # 获取当前时间（假设服务器时区不是东八区）  
    now = datetime.now(timezone.utc)  # 获取UTC时间  
    
    # 设置东八区时区  
    tz_east_8 = pytz.timezone('Asia/Shanghai')  # 上海代表东八区  
    
    # 将UTC时间转换为东八区时间  
    now_east_8 = now.replace(tzinfo=pytz.utc).astimezone(tz_east_8)  

    # 提取年份、月份和日期，并格式化为两位数字  
    year = now_east_8.strftime('%Y')[-2:]  # 取年份的后两位  
    month = now_east_8.strftime('%m')      # 月份已经是两位数字  
    day = now_east_8.strftime('%d')        # 日期可能是一位或两位数字  
    
    # 如果日期是一位数字，前面补零  
    if len(day) == 1:  
        day = '0' + day  

    return  year + month + day

def getPwd():  
    result = 'HYZ' + getStrDate()  
    return result

if __name__ == "__main__":
    # 输出结果  
    print(getPwd())