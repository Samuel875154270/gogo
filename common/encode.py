import hashlib
import base64
import time


def encode_password(password):
    """
    密码加密
    :param password:
    :return:
    """
    timestamp = str(int(time.time()))
    sha1_encode = sha1_password(password)
    new_encode = "{}{}{}".format(timestamp[-5:], sha1_encode, timestamp[:5])
    base64_encode = base64.b64encode(new_encode.encode())
    base64_encode = base64_encode.decode().replace("=", "]P[")
    base64_encode = base64_encode[::-1]

    return base64_encode


def decode_password(en_password):
    """
    密码解密
    :param en_password:
    :return:
    """
    base64_decode = en_password[::-1]
    base64_decode = base64_decode.replace("]P[", "=").encode()
    base64_decode = base64.b64decode(base64_decode)
    sha_decode = base64_decode.decode()[5:-5]

    return sha_decode


def sha1_password(password):
    """
    sha1加密
    :param password:
    :return:
    """
    sha1_encode = hashlib.sha1(password.encode()).hexdigest()
    return sha1_encode
