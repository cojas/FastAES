在程序开发中，特别是对安全性要求较高的支付系统，数据安全已成为不可忽视的核心需求，因此数据加密是必不可少的。而 AES 作为当前最广泛使用的对称加密算法，以其卓越的安全性和性能表现，成为了业界的首选标准。

这里我基于开源的 AES 的 C 实现，封装了一个 Python 扩展，能够同时保证速度和安全性。

**安装方式如下**

~~~shell
git clone https://github.com/satori1995/FastAES.git
cd FastAES
python setup.py install
~~~

**用法如下**

~~~python
import fast_aes
import orjson

aes = fast_aes.FastAES()
aes.set_key(b"salt!!!")  # 加盐（可选）

origin_data = {"name": "Akira", "age": 18, "gender": "female"}
# 对数据进行加密，接收一个 bytes 对象
encrypted_data = aes.encrypt(orjson.dumps(origin_data))
print(encrypted_data)  # b'\x93\xf0 ~JD\xe0\xbf\xc7\xe3\xf8)...'
# 对加密后的数据进行解密
print(orjson.loads(aes.decrypt(encrypted_data)))
"""
{'name': 'Akira', 'age': 18, 'gender': 'female'}
"""
~~~

在数据传输时，发送方对数据进行 AES 加密，接收方对数据进行 AES 解密，通过这种方式便可以保证数据安全。
