# 中阶和高阶实践。
import logging
logging.basicConfig(level=logging.INFO)

try:
    num = float(input("请输入一个数字："))
    logging.info(f"输入的数字是：{num}")
except ValueError:
    logging.error("输入的不是有效数字！")