from typing import Generator
import hashlib
import time

# 目标难度值
target = "0000"

# 输入字符串
# input_str = input("Enter a string: ")
input_str = "Hello world!"

# 开始计时
start_time = time.time()

def nonce_selection() -> Generator[int, None, None]:
    num = 1
    while True:
        yield num
        num += 1

def hash_alg(input_str: str, nonce: int) -> bytes:
    # 构造要计算哈希的数据
    data = input_str.encode() + nonce.to_bytes(4, byteorder="big")
    return hashlib.sha256(data).digest()[:6]

# 循环计算哈希值
for nonce in nonce_selection():
    # 计算哈希值
    hash_value = hash_alg(input_str, nonce).hex()
    print(f"0x{hash_value}")
    
    # 判断是否满足难度要求
    if str(hash_value).startswith(target):
        # 计算耗时
        end_time = time.time()
        elapsed_time = end_time - start_time
        
        # 输出结果
        print(f"Input str: {input_str}")
        print("Nonce:", nonce)
        print("Elapsed Time:", elapsed_time)
        print("Hash Value:", f"0x{hash_value}")
        break
