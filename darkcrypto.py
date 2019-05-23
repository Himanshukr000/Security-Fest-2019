from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes

import base64

import unittest


# Maybe this could be used to encrypt the secret messages in the board? 
# https://cryptography.io/en/latest/hazmat/primitives/asymmetric/rsa/

MESSAGE=b"Something secret"

#PEM_PASSWORD=b'Rock_You_Like_a_Hurricane'
       
PEM_PRIVATE_KEY=b"""-----BEGIN ENCRYPTED PRIVATE KEY-----
MIIFLTBXBgkqhkiG9w0BBQ0wSjApBgkqhkiG9w0BBQwwHAQIF+TK17Q9CAsCAggA
MAwGCCqGSIb3DQIJBQAwHQYJYIZIAWUDBAEqBBCebicNIgfA441g2E3t3z/oBIIE
0OAMyvjZ8MaFDLJzuzDY3RWHP0IHWiHoCBNxPJWySon/tLXoizSbsj8EKtgA0MpE
vORC4QdnKg7bqplAAXfSIRli9Hb7RcuMpKv5buW3/Oh/th8NWWM9LOQOBAO0svlR
pJhA5hZSKEgEJMd1E77mjv29gHMEzRgXvAsTOZXhgbbtPnIkQGPXZq4hXyhy0VBt
9cCevKYLgVFahIARjejN+KErNiSN0f76mc62wunum+J6uGtk/HYZ00ZsFcf/0x7B
O/8hrFsliAg+2izNLVWy/+b1oCkuaMIEZ0zXjse3iZirSmWs6F5tFGh2w5lnJB1G
hJAqTjhHdvPWpwiyTw4nCG7+FDd3v1Ih+v8Qq9evlkYg1rdwh13ymGcfko3y7p2l
SuQsJ94i5NEv4acgIE70fqXrwzbSlc+QB5RtKexMj0NxWCySe9seLQP9fbCxp6Ci
a8mHS/4hF7hBbH984QJxy7aqt+U/xLQrKkkp2Lf0KYfthmiS13e7ZEtNSzd3dxZv
eVnDNSzEh/ty/+yt5bx58AlmhNigkaPX+KrTYt1KgQBrgYyk/YNEWK8GE0Sq/4KL
uEiIa0mpbn9je7szIA9egwjIqLWasBoG1HOb5dOu/azhVoM8mheEik/FQLHhgZlo
ZoFY8Rb3jO3Mv/sod1tQE6IteAkBsfXGT8QNaJHMAjmf96aNA8y0bStpHm1ZzpzW
qX3xcr6bDAt4olonDZ1DNTZh4AnSCnKM8LM6kwwY0r8q13EHJ2Ek6L0Vh+BiIeNw
7Q/jQ1thXzrYv9e5KU5TmvZAvtXoqcUCmI2ehnOq6xmir07g4tPQIHyolbY8EHw1
r/mb3me1+8lPdvjKSCM/LqI04h3GPkfnXWwPwlBL4sd5mnKRunLHcnLDu2AVRE+R
r8DvGGIMNr+LZjxZIdjhMraR6VSSTXX028Lamz40ZY9gn3vQWeIJAi0S7g/TW+TJ
RwXGW5gmLfbzlkzgvXPRPfjk9EeBtcS4Pj7q2QIrrAdZZFCC4z5uRGmMHC/tv2/p
IYpV2kClKcnNuPvQSreJXB18GJo1VJU/o78/Hi/cr1atiERM38gP1FYk08vcwjwT
Av62VWaTXsuAsOzS/fjmSsyAlv0LN8pNJ6j3uvk+bOrbKS4V7aM0oHDhLtlJThN5
dagcklxP1VgRAXQPdGUz1oEZzoKezPxq2mJCj8QAPZFkat5mRzbUum0aAr3Yn7Vq
KLGrILx8p4sToqfiKMnayU/QCpgifgJbMun9pSvdOC40b8xUIeuN0PlIkLueA4Mu
o4pbU2inYbC+vEB3c1fHaki+Z0+jUuHyIWtEBJOD6VNYx1LU3HY6T7eV8t/8oJxi
LZCxhon+/R9kEgJO0ofp0362pFm5i1V1afzjFMAhFK4khFNdZJ6rJLrymg1ueCsx
sxSv8x8EA/ZykDJs4M/E5eSiZI9ZmrCsIrUXZ7QGjguqHXnHi7wsO3RSa2c8Bl+t
+SYlmqK5U55yHZ23rJIS/XNIaMB+mX0CHnx/+rohABcueD7Hz7Q0OHP34NuPwK3x
NAx6x4Yfrw2SiYd0Nj15N8oexI+u6/tahCL2obap9S1Y7zibfNgJs4d2yi3F3A+w
Fe+whD+k+txSfs6w50MFgI4JG2Hu6dLtdQC5FSyOAYDJ
-----END ENCRYPTED PRIVATE KEY-----"""

ENCRYPTED_MESSAGE=('rW+fOddzrtdP7ufLj9KTQa9W8T9JhEj7a2AITFA4a2UbeEAtV/ocxB/t4ikLCMsThUXXWz+UFnyXzgLgD9RM+2toOvWRiJPBM2ASjobT+bLLi31F2M3jPfqYK1L9NCSMcmpVGs+OZZhzJmTbfHLdUcDzDwdZcjKcGbwEGlL6Z7+CbHD7RvoJk7Ft3wvFZ7PWIUHPneVAsAglOalJQCyWKtkksy9oUdDfCL9yvLDV4H4HoXGfQwUbLJL4Qx4hXHh3fHDoplTqYdkhi/5E4l6HO0Qh/jmkNLuwUyhcZVnFMet1vK07ePAuu7kkMe6iZ8FNtmluFlLnrlQXrE74Z2vHbQ==')

DEFAULT_PADDING=padding.OAEP(
    mgf=padding.MGF1(algorithm=hashes.SHA256()),
    algorithm=hashes.SHA256(),
    label=None
)


class TestEncryption(unittest.TestCase):
    
    def test_encryption_decryption(self):
        private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048,
            backend=default_backend()
        )
        ciphertext = private_key.public_key().encrypt(
            MESSAGE,
            DEFAULT_PADDING
        )
        plaintext = private_key.decrypt(
            ciphertext,
            DEFAULT_PADDING
        )
        self.assertEqual(plaintext, MESSAGE)

    '''def test_generate_private_key(self):
        private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048,
            backend=default_backend()
        )

        private_pem = private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.BestAvailableEncryption(PEM_PASSWORD)
        )'''
        # print(private_pem.decode())
    
    def test_decryption(self):

        
        with open("words.txt", errors='replace') as f:
            r = f.readlines()
            p_list = [i.strip() for i in r]
        for l in p_list:


            try:

                private_key = serialization.load_pem_private_key(
                    PEM_PRIVATE_KEY,
                    password=bytes(l, 'utf-8'),   #password was falloutboy
                    backend=default_backend()
                        )
                    
                plaintext = private_key.decrypt(
                base64.b64decode(ENCRYPTED_MESSAGE.encode('utf-8')),
                DEFAULT_PADDING
                    )
                print(plaintext,' ',':pwd is','=',l)
                #self.assertEqual(MESSAGE, plaintext)
            except:
                continue

if __name__ == '__main__':
    unittest.main()
