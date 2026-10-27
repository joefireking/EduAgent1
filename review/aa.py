# def _fmt(event: str, **kw) -> str:
#     """内部方法：把「事件名 + 关键字参数」格式化成一行可读字符串。
#     例：_fmt("user.login", user_id="u1") → "user.login | user_id='u1'"
#     （**kw 表示接收任意多个 key=value 形式的关键字参数，收进一个字典 kw）"""
#     if kw:  # 如果传了关键字参数（即 key=value）
#         # 把每个键值对拼成 "key=value"（{v!r} 表示用 repr 显示值，字符串会带引号），
#         # 再用空格连接，最前面加上事件名和分隔符 " | "
#         print([f"{k}={v!r}" for k, v in kw.items()])
#         return event + " | " + " ".join(f"{k}={v!r}" for k, v in kw.items())
#     return event


# print(_fmt(event="user.login", user_id="a1", user_name="张三"))


# dict1 = {"a":1, "b":2, "c":3}
#
# print(dict1.pop("a"))
# print(dict1)
from backend.config import  get_settings
settings = get_settings()                  # 读配置，拿到 log_level（如 "INFO"）
# getattr(logging, "INFO", 兜底) 把字符串级别转成 logging 模块里的常量 logging.INFO；
# .upper() 先转大写；万一配置写错找不到该常量，就用 logging.INFO 兜底
import logging
level = getattr(logging, settings.log_level.upper(), logging.INFO)
print(level)