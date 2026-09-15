# A04:2025 加密失效（Cryptographic Failures）

> 官方详情页：<https://top10.owasp.org/2025/A04_2025-Cryptographic_Failures/>
> 排名：**第 4 位**（2021 版为第 2 位，**下降 2 位**）
> CWE 数量：32 个｜平均发生率：3.80%（全榜第二高）｜相关 CVE：2,185
> 主要 CWE：CWE-327 使用已破解或危险的加密算法、CWE-331 熵不足、CWE-1241 随机数生成器使用可预测算法、CWE-338 使用弱伪随机数生成器

## 一句话理解

加密失效不是"加密被破解"，而是**该加密的地方没加密、用了弱算法、密钥管不住、随机数可预测**——结果就是敏感数据要么在传输中裸奔，要么以可逆或可爆破的形式落盘。

## 风险原理

2021 版这个类别叫"敏感数据泄露（Sensitive Data Exposure）"，2025 版坚持用**根因命名**"加密失效"。因为"数据泄露"是症状，根因是密码学用得不对。

四类根因：

1. **该保护的数据没有保护。** 明文传输、明文存储、明文写入 Cookie/日志。
2. **算法或参数太弱。** MD5/SHA-1 做完整性或口令哈希、DES/3DES/RC4、ECB 模式、RSA 无 OAEP 填充、TLS < 1.2。
3. **密钥管理失败。** 硬编码密钥、密钥入库（提交到源码仓库）、密钥复用、长期不轮换、熵不足。
4. **随机性失败。** 用非密码学随机数（如语言内置的 `random`）生成会话 ID、令牌、IV、密码重置码，导致可预测。

官方还特别强调两件"数据侧"的事：**不必要地存储敏感数据本身就是风险**（不存就不会被偷）；以及**包含敏感数据的响应必须禁用各级缓存**（CDN、Web 服务器、Redis 等）。

官方对后量子密码（Post-Quantum Cryptography，PQC）也给出了明确时间要求：高风险系统应**不晚于 2030 年底**完成迁移准备。

ASCII 数据流图：

```
                传输层                    应用层（存储/令牌）
用户 ──HTTP明文──► 攻击者嗅探 ──► 会话Cookie 被劫持
                或 TLS<1.2 / 降级攻击

口令 ──MD5(无盐)──► 数据库泄露 ──► 彩虹表/GPU 秒破
会话ID ──mt_rand()──► 可预测 → 可枚举他人会话
```

## 典型场景与真实案例模式

> 以下为"某类系统常见的模式"归纳，不指向具体厂商事件。

- **登录页未强制 HTTPS，或只在登录页加密。** 登录后的会话 Cookie 走 HTTP，被同网段攻击者嗅探后重放（会话劫持）。
- **口令存储用无盐快速哈希。** 数据库一旦泄露，未加盐的哈希可用彩虹表直接反查，加盐但用快速哈希（如单轮 SHA-256）也能被 GPU 高速爆破。
- **硬编码密钥。** 加密密钥写死在源码或配置仓库中，源码泄露或镜像被拉取即等于密钥泄露。
- **ECB 模式加密。** 相同明文块加密后产生相同密文块，攻击者通过密文模式即可推断明文结构（经典"ECB 企鹅图"）。
- **可预测的令牌。** 密码重置令牌、邀请码用时间戳或自增数生成，可被枚举。
- **缓存泄露。** 含个人信息的 API 响应缺少 `Cache-Control: no-store`，被中间缓存或浏览器磁盘缓存留存。
- **证书校验被关闭。** 移动端/服务端为"省事"设置了信任所有证书，导致中间人攻击（MITM）可行。

## 怎么测

对应 WSTG 测试项：

- [WSTG-CRYP-01](../wstg/checklist.md) 弱传输层安全（TLS）
- [WSTG-CRYP-02](../wstg/checklist.md) 填充预言（Padding Oracle）
- [WSTG-CRYP-03](../wstg/checklist.md) 通过未加密通道发送敏感信息
- [WSTG-CRYP-04](../wstg/checklist.md) 弱加密原语
- [WSTG-CONF-07](../wstg/checklist.md) HTTP 严格传输安全（HSTS）
- [WSTG-ATHN-01](../wstg/checklist.md) 凭据是否通过加密通道传输
- [WSTG-SESS-02](../wstg/checklist.md) Cookie 属性（Secure/HttpOnly/SameSite）

**手工测试步骤**

1. **检查 HTTPS 强制与 HSTS。**
   ```bash
   curl -sI http://target/ | head -1     # 应为 301/308 跳转到 https
   curl -sI https://target/ | grep -i strict-transport-security
   ```
2. **扫描 TLS 配置。**
   ```bash
   testssl.sh https://target
   # 或
   nmap --script ssl-enum-ciphers -p 443 target
   ```
   关注：是否支持 TLS 1.0/1.1、是否启用 RC4/3DES、是否支持弱曲线、是否有前向保密（FS）。
3. **检查是否混合 HTTP/HTTPS 内容。** 页面里有 `http://` 资源即为混合内容，可被降级劫持。
4. **检查 Cookie 属性。**
   ```bash
   curl -sI https://target/login | grep -i set-cookie
   # 期望看到 Secure; HttpOnly; SameSite=Lax|Strict
   ```
5. **检查缓存头。** 对返回个人数据的接口：
   ```bash
   curl -sI -H 'Cookie: session=<会话>' https://target/api/me | grep -i cache-control
   # 期望 no-store（或至少 no-cache, private）
   ```
6. **观察令牌的随机性。** 连续获取多个密码重置令牌/邀请码，比较是否包含时间戳、自增序列或重复片段。可用 Burp 的 Sequencer 做统计随机性分析。
7. **检查加密实现（如有源码）。** 搜索危险 API：
   ```bash
   grep -rEn 'MD5|SHA1|DES|RC4|ECB|Random\(\)|rand\(\)|Math\.random' --include='*.py' --include='*.java' --include='*.js' .
   ```
8. **填充预言检测。** 观察解密失败与填充错误是否返回不同响应/时间（可用于 CBC 填充预言攻击）。

## 代码示例

### 易受攻击的代码（Python）

```python
import hashlib
import random
from Crypto.Cipher import AES

SECRET_KEY = b"0123456789abcdef"          # 危险 1：硬编码 16 字节密钥

def hash_password(pw: str) -> str:
    return hashlib.md5(pw.encode()).hexdigest()   # 危险 2：MD5、无盐

def make_token() -> str:
    return str(random.randint(100000, 999999))   # 危险 3：非密码学随机数

def encrypt(data: bytes) -> bytes:
    cipher = AES.new(SECRET_KEY, AES.MODE_ECB)    # 危险 4：ECB 模式
    return cipher.encrypt(data.ljust(32, b'\0'))
```

### 修复后的代码

```python
import os
import secrets
from argon2 import PasswordHasher
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

# 修复 1：密钥来自密钥管理系统/环境，不硬编码，且不提交到仓库
SECRET_KEY = os.environ["DATA_ENCRYPTION_KEY"]   # 由 KMS/HSM 注入，定期轮换

_ph = PasswordHasher()                            # Argon2id，自适应慢哈希

def hash_password(pw: str) -> str:
    # 修复 2：自适应、加盐（自动生成盐并编码进结果）的强哈希
    return _ph.hash(pw)

def verify_password(stored: str, pw: str) -> bool:
    try:
        return _ph.verify(stored, pw)
    except Exception:
        return False

def make_token() -> str:
    # 修复 3：使用密码学安全随机数，且长度足以抵御枚举
    return secrets.token_urlsafe(32)

def encrypt(data: bytes) -> bytes:
    # 修复 4：AEAD（AES-GCM），随机 96 位 nonce，附认证标签
    nonce = os.urandom(12)
    return nonce + AESGCM(SECRET_KEY).encrypt(nonce, data, b"")
```

### 口令存储（Java / Spring Security）

```java
// 危险：快速哈希 + 无盐
String hash = DigestUtils.md5Hex(password);

// 修复：BCrypt（自适应），或更强的 Argon2id
PasswordEncoder encoder = new BCryptPasswordEncoder(12);  // work factor = 12
String hash = encoder.encode(password);                   // 自动加随机盐
boolean ok = encoder.matches(rawPassword, hash);
```

## 防御清单

- [ ] 对数据分类分级，明确哪些是敏感数据（受隐私法/PCI DSS/GDPR 约束的）。
- [ ] **不必要就不存**；能尽快删除、令牌化（tokenization）或截断的就不落库。
- [ ] 敏感数据落盘必须加密（at rest）；密钥放在 HSM 或云 KMS。
- [ ] 传输层只允许 **TLS ≥ 1.2**，启用前向保密（FS）套件，淘汰 CBC 套件，支持/规划抗量子密钥交换。
- [ ] HTTPS 强制并启用 HSTS（`max-age`、`includeSubDomains`、`preload`）。
- [ ] 对含敏感数据的响应禁用缓存（CDN/Web 服务器/应用缓存）。
- [ ] 口令用**自适应加盐哈希**：Argon2、yescrypt、scrypt 或 PBKDF2-HMAC-SHA-512；遗留 bcrypt 也要提高 work factor。
- [ ] 密钥必须密码学随机生成、以字节数组存于内存；若来自口令，必须经 KDF 派生。
- [ ] IV 按模式选择；需 nonce 的模式不必用 CSPRNG，但**同一密钥下 IV 绝不能重复**。
- [ ] 一律使用认证加密（AEAD）而非裸加密。
- [ ] 淘汰 MD5、SHA-1、CBC、PKCS#1 v1.5 等已废弃原语与填充方案。
- [ ] 不用未加密协议（FTP、STARTTLS、明文 SMTP）；不信任未校验证书的连接。
- [ ] 提供后量子迁移路线，高风险系统不晚于 2030 年底。
- [ ] 参考 [Password Storage Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html)、[Cryptographic Storage Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Cryptographic_Storage_Cheat_Sheet.html)、[Transport Layer Protection Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Transport_Layer_Protection_Cheat_Sheet.html)、[HSTS Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/HTTP_Strict_Transport_Security_Cheat_Sheet.html)。

## 常见坑

- **坑 1：用 SHA-256 存口令。** SHA-256 是"快哈希"，设计目标就是快，正好方便攻击者暴力枚举。口令必须用慢哈希（Argon2/scrypt/bcrypt/PBKDF2）。
- **坑 2：自己发明加密方案。** 自制的"异或 + Base64"或自定义混淆不是加密。永远使用经过验证的库与标准 API。
- **坑 3：CBC 模式配静态 IV。** 静态或可预测 IV 会泄露明文结构，且 CBC 无完整性保护，易受填充预言攻击。默认选 AEAD（GCM/ChaCha20-Poly1305）。
- **坑 4：密钥轮换缺失。** "密钥永久有效"意味着一旦泄露就永远可解密。需要轮换机制与密钥版本管理。
- **坑 5：只加密传输忘了落盘（或反之）。** 传输加密不能替代存储加密；两者是独立的威胁模型。
- **坑 6：把口令当密钥直接用。** 口令熵低，必须经 KDF（如 PBKDF2/Argon2）派生为密钥。
- **坑 7：`Math.random()` / `random` 生成安全令牌。** 这些是非密码学随机数，可被预测。必须用 `secrets`、`SecureRandom`、`crypto.randomBytes`。
- **坑 8：全局关闭证书校验。** 为了应对自签证书而设置"信任所有证书"，等于自我制造 MITM 通道。

## 自测题

**1. 为什么 MD5 加盐仍不足以安全存储口令？**

<details><summary>答案</summary>

加盐只能阻止彩虹表与相同口令的批量比对，但 MD5 是快速哈希，GPU 每秒可计算数十亿次。攻击者仍可对单个目标高速暴力枚举。正确做法是使用带工作因子的自适应哈希（Argon2id、scrypt、bcrypt、PBKDF2），使单次计算成本足够高。
</details>

**2. 应用用 AES-ECB 加密用户身份证号。攻击者拿到密文能推断出什么？为什么？**

<details><summary>答案</summary>

ECB 对相同明文块产生相同密文块，且不隐藏明文的模式。攻击者可识别"哪些记录的字段相同"、猜出字段结构（如日期、地区码的规律），甚至通过对照已知明文进行块替换。应改用 AEAD 模式（如 AES-GCM）并配随机 nonce。
</details>

**3. 会话 ID 用 Python 的 `random.randint` 生成，风险是什么？**

<details><summary>答案</summary>

`random` 是梅森旋转伪随机数生成器（Mersenne Twister），不是密码学安全的。攻击者观察足够多的输出即可预测后续值，从而枚举或伪造他人会话。修复：使用 `secrets` 模块（底层是操作系统 CSPRNG）。
</details>

**4. 一个返回个人资料的 API 响应包含 `Cache-Control: public, max-age=3600`，有什么问题？**

<details><summary>答案</summary>

`public` 允许共享缓存（CDN、代理）存储该响应，可能导致 A 用户的个人资料被缓存后返回给 B 用户，造成跨用户数据泄露。含敏感数据的响应应使用 `Cache-Control: no-store`。
</details>

**5. 为什么官方要求"提前准备后量子密码（PQC）"？**

<details><summary>答案</summary>

因为存在"先收集、后解密（harvest now, decrypt later）"的威胁：攻击者现在就截获并保存加密流量，等量子计算机成熟后再解密。对于长期保密要求高的数据，加密算法必须提前迁移，官方建议高风险系统不晚于 2030 年底完成。
</details>

## 来源

- <https://top10.owasp.org/2025/A04_2025-Cryptographic_Failures/>
- <https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/09-Weak_Cryptography/README>
- <https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html>
- <https://cheatsheetseries.owasp.org/cheatsheets/Transport_Layer_Protection_Cheat_Sheet.html>
