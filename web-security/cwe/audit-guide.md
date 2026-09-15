# CWE 代码审计检查点指南

本页从 [2025 CWE Top 25](./README.md#3-2025-年-cwe-top-25-最危险软件弱点) 中选取 **12 个重点弱点**，每个给出四样东西：

1. **弱点本质**（为什么这是个弱点）
2. **易出现的代码模式**（看到什么要警觉）
3. **grep / 检索思路**（怎么快速定位可疑点）
4. **误报排除**（什么情况下看着像但不是）

编号与名称来自 <https://cwe.mitre.org/top25/archive/2025/2025_cwe_top25.html>。

> **使用前提**：静态检索（grep）只能定位**候选点**，最终判定必须人读代码 + 数据流分析 + 动态验证。**grep 命中不等于漏洞存在，grep 未命中也不等于安全。** 这与 [PTES 漏洞分析阶段](../ptes/README.md#6-阶段四漏洞分析vulnerability-analysis) 对"扫描器只提供线索"的纪律是一致的。

---

## 索引

| # | CWE | 名称 | 主要风险类型 |
| --- | --- | --- | --- |
| 1 | CWE-79 | 跨站脚本（XSS） | 客户侧代码注入 |
| 2 | CWE-89 | SQL 注入 | 服务端解释器注入 |
| 3 | CWE-78 | OS 命令注入 | 服务端解释器注入 |
| 4 | CWE-94 | 代码注入 / 动态求值 | 服务端代码执行 |
| 5 | CWE-22 | 路径穿越 | 文件系统越界访问 |
| 6 | CWE-434 | 危险类型文件上传 | 任意文件落地 |
| 7 | CWE-502 | 反序列化不可信数据 | 直接 RCE |
| 8 | CWE-862 | 缺失授权 | 访问控制缺失 |
| 9 | CWE-639 | 通过用户可控键绕过授权（IDOR） | 访问控制缺失 |
| 10 | CWE-352 | 跨站请求伪造（CSRF） | 会话与请求完整性 |
| 11 | CWE-306 | 关键功能缺失认证 | 认证缺失 |
| 12 | CWE-918 | 服务端请求伪造（SSRF） | 边界绕过与内网探测 |

---

## 1. CWE-79 跨站脚本（XSS）

**弱点本质**：把不可信输入直接放进 HTML/JS/CSS/URL 的**输出上下文**中，浏览器会把它当代码执行。根因不是"没过滤输入"，而是**输出时没有按上下文做编码**。

### 易出现的代码模式

**服务端模板（Jinja2 / Thymeleaf / JSP / ERB / Twig）**

```jinja
{# 危险：显式关闭转义 #}
<p>{{ user_comment | safe }}</p>
```

```jsp
<%-- 危险：直接把请求参数拼进 HTML --%>
<div><%= request.getParameter("nickname") %></div>
```

```html
<!-- Thymeleaf：utext 不转义，th:text 才转义 -->
<div th:utext="${comment}"></div>
```

**前端 DOM（这是最容易被漏掉的一类）**

```javascript
// 危险：直接把不可信数据写入 HTML 解析上下文
document.getElementById('out').innerHTML = location.hash.slice(1);
element.outerHTML = userInput;
document.write(userInput);
$('#out').html(userInput);          // jQuery .html()
element.insertAdjacentHTML('beforeend', userInput);
ReactDOM.render(<div dangerouslySetInnerHTML={{__html: userInput}} />, el);

// 危险：把不可信数据当 URL / 脚本源
script.src = userInput;
location.href = userInput;           // 若允许 javascript: 前缀
setTimeout(userInput, 0);            // 字符串形式，等价于 eval
new Function(userInput);
eval(userInput);                     // 若数据来自服务端拼接
```

**JSON 注入到 script 块**

```html
<script>
  var config = <?= json_encode($data) ?>;  // 若未加 HTML 编码，</script> 可逃逸
</script>
```

### grep / 检索思路

```bash
# 服务端模板里的"关闭转义"标记
rg -n --glob '*.{jsp,jspx,ftl,vm,html,hbs,ejs,erb,php}' \
   'safe|raw|utext|escapeXml\s*=\s*"false"|<%=' 

# 前端 DOM 危险汇（Sink）
rg -n --glob '*.{js,jsx,ts,tsx,vue}' \
   'innerHTML|outerHTML|insertAdjacentHTML|document\.write|dangerouslySetInnerHTML'

rg -n --glob '*.{js,jsx,ts,tsx}' '\.html\('

# 动态求值
rg -n --glob '*.{js,jsx,ts,tsx,vue}' 'eval\(|new Function\(|setTimeout\(\s*[A-Za-z_$]'

# 模板引擎的"不转义"配置
rg -n -i 'autoescape|auto_escape|escapeOutput|htmlEscape' 
```

**审计顺序建议**：先查"输出点（Sink）"，再反查每个 Sink 的数据来源（Source），看中间有没有编码。

### 误报排除

| 看着像 XSS | 为什么可能不是 |
| --- | --- |
| `.innerHTML =` 赋值给**由常量文字拼接**的字符串（无外部输入） | 无不可信数据流入 |
| `.innerHTML =` 赋值给经过 `DOMPurify.sanitize()` 或等价净化库的值 | 已净化，但要确认配置未放宽（例如 `ALLOW_UNKNOWN_PROTOCOLS: true`） |
| 前端框架的 `{{ }}` 插值 | Vue/Angular/React 默认转义；只有 `v-html`、`dangerouslySetInnerHTML` 才是危险汇 |
| `innerHTML` 赋值后**立即**用数字索引遍历其 `childNodes` 做统计 | 仍是危险汇，但如果值来源可信则为误报 |
| 服务端 `escapeHtml()` 之后再拼接 | 若编码**在正确上下文**下完成，则安全；但注意"HTML 编码"用在 JS 字符串上下文或 URL 上下文里是**不够的**——这是最常见的假阴性原因 |
| `textContent =` / `innerText =` | 这两个是安全的文本上下文赋值，不是危险汇 |

**关键判据：上下文匹配。** 同一段数据在 HTML 正文、HTML 属性、JS 字符串、URL 中需要的编码方式不同。用 HTML 编码去应付 JS 字符串上下文，仍会被绕过。

---

## 2. CWE-89 SQL 注入

**弱点本质**：把不可信输入**拼接**进 SQL 语句结构，导致数据被解释为语句。

### 易出现的代码模式

```java
// 危险：字符串拼接
String q = "SELECT * FROM users WHERE name='" + name + "'";
stmt.executeQuery(q);

// 危险：MyBatis ${} 是字符串替换，不是参数绑定；#{} 才是绑定
@Select("SELECT * FROM users WHERE id = ${id}")
User findById(String id);

// 危险：存储过程内部再拼接（预编译也救不了）
// CREATE PROCEDURE p(@n NVARCHAR(50)) AS
//   EXEC('SELECT * FROM users WHERE name=''' + @n + '''')
```

```python
# 危险
cursor.execute("SELECT * FROM t WHERE id = %s" % user_id)
cursor.execute(f"SELECT * FROM t WHERE id = {user_id}")
cursor.execute("SELECT * FROM t WHERE id = " + user_id)
cursor.execute("SELECT * FROM t WHERE id = '%s'" % user_id)

# 相对安全：参数化
cursor.execute("SELECT * FROM t WHERE id = %s", (user_id,))
```

```javascript
// 危险
db.query(`SELECT * FROM t WHERE id = ${id}`);
connection.query("SELECT * FROM t WHERE id = " + id);

// 表名/列名无法参数化——这是"无法用绑定解决"的典型场景
db.query(`SELECT * FROM ${tableName} WHERE id = ?`, [id]);
```

```php
// 危险
$sql = "SELECT * FROM t WHERE id = " . $_GET['id'];
$sql = "SELECT * FROM t WHERE id = '{$_GET['id']}'";
```

**排序、分页、表名这类"结构位置"的注入最容易被漏掉**，因为它们无法用占位符参数化，开发者常直接拼接。

```python
# 危险：ORDER BY 位置拼接
sql = f"SELECT * FROM t ORDER BY {sort_field} {direction}"
```

### grep / 检索思路

```bash
# 直接用语言层的字符串插值/拼接去构造 SQL 关键字
rg -n -i --glob '*.{py,java,js,ts,php,go,rb,cs}' \
   '(select|insert|update|delete|from|where|order by|group by)\b[^;]*(%s|\+\s*[A-Za-z_]|\.format\(|f"|f'"'"'|\$\{)'

# MyBatis 的 ${}
rg -n '\$\{' --glob '*.xml' --glob '*.java'

# 动态 SQL API
rg -n -i 'createQuery\(|createNativeQuery\(|executeQuery\(|rawQuery\(|query\(|execQuery\('

# ORM 的原始 SQL 逃生舱
rg -n -i 'raw\(|extra\(|RawSQL|RawQuery|sequelize\.query|knex\.raw|EntityManager\.createNativeQuery'
```

**数据流检索法（比 grep 有效得多）**：从 Controller / Handler 入口参数出发，逐层跟踪到 DAO 层，看中间有没有出现字符串拼接。这才是真正的审计方式。

### 误报排除

| 看着像注入 | 为什么可能不是 |
| --- | --- |
| `f"SELECT ... WHERE id = {int(user_id)}"` | `int()` 强制转换后不可能携带语法字符（但要注意 `int()` 抛异常的处理，以及负数/极大值带来的逻辑问题——那属于另一个 CWE） |
| 拼接的值来自服务端枚举白名单（如 `if sort not in ('asc','desc'): raise`） | 已做白名单约束 |
| 使用 `%s` 但参数在 execute 的第二个参数里 | 这是参数化，安全 |
| MyBatis `#{}` | 是预编译占位符，安全；只有 `${}` 危险 |
| 表名拼接但表名来自服务端硬编码常量 | 无外部输入 |

**最需要警惕的假阴性**：

- **第二道注入**（Second-order SQL Injection）：输入先存进数据库（安全地存），后续另一个功能把它**取出来再拼接**到 SQL 里。grep 很难发现，必须跨功能追踪数据生命周期。
- **预编译也挡不住的场景**：`ORDER BY` / 表名 / 列名 / `LIMIT` 参数在某些驱动里不支持绑定，开发者就会退回拼接。
- **ORM 的 `raw` / `extra` / `whereRaw`**：框架给了"逃生舱"，用了就等于放弃参数化。

---

## 3. CWE-78 OS 命令注入

**弱点本质**：把不可信输入传给会**启动系统命令或进程**的 API，且使用了 shell 解析。

### 易出现的代码模式

```python
# 危险：shell=True，输入被 shell 解析
subprocess.run("ping -c 1 " + host, shell=True)
os.system(f"convert {filename} out.png")
os.popen("nslookup " + domain)
subprocess.call(f"tar -czf backup.tar.gz {path}", shell=True)
```

```java
// 危险：Runtime.exec / ProcessBuilder 传 shell
Runtime.getRuntime().exec("/bin/sh -c 'ping " + host + "'");
new ProcessBuilder("sh", "-c", "convert " + filename).start();
```

```php
system("ping -c 1 " . $host);
exec("convert {$file} out.png");
shell_exec("ls " . $dir);
passthru($cmd);
```

```javascript
// 危险：exec 走 shell，execFile 不走
child_process.exec(`ping -c 1 ${host}`);
child_process.execSync("convert " + file);
```

```go
// 危险
exec.Command("sh", "-c", "ping -c 1 "+host)
// 相对安全：不经 shell
exec.Command("ping", "-c", "1", host)
```

**要点**：区别在**是否经由 shell 解释**。`shell=True` / `sh -c` / `child_process.exec` 都会走 shell，`;` `|` `&&` `$()` 反引号都会生效。

### grep / 检索思路

```bash
# 危险 API
rg -n -i 'os\.system|os\.popen|subprocess\.(run|call|check_output|Popen)[^)]*shell\s*=\s*True'
rg -n -i 'Runtime\.getRuntime\(\)\.exec|new ProcessBuilder'
rg -n -i '\b(system|exec|shell_exec|passthru|popen|proc_open)\s*\(' --glob '*.php'
rg -n -i 'child_process\.(exec|execSync)\(' --glob '*.{js,ts}'
rg -n 'exec\.Command\(\s*"(sh|bash|cmd|powershell)' --glob '*.go'

# 危险拼接模式（命令 + 用户变量）
rg -n '(system|exec|popen|subprocess|child_process)[^;\n]*(\+|\$\{|%s|\.format)'
```

### 误报排除

| 看着像命令注入 | 为什么可能不是 |
| --- | --- |
| `exec.Command("ping", "-c", "1", host)`（Go，参数数组，无 shell） | 不经 shell，参数不会被拆分；但若 `host` 以 `-` 开头仍可能被当作选项（**参数注入 CWE-88**，是另一个问题，不能因"不是命令注入"就放过） |
| `child_process.execFile(...)` | 不走 shell |
| `subprocess.run([...], shell=False)` 且参数是列表 | 不经 shell |
| 命令字符串完全由服务端常量构成 | 无外部输入 |
| 输入先经过严格白名单（如 `^[a-zA-Z0-9\.-]+$`）校验 | 已约束字符集（但仍需确认校验在拼接**之前**，且没有编码绕过） |

**注意区分**：CWE-78 是**命令注入**（能执行额外命令），CWE-88 是**参数注入**（不能执行新命令但能改变参数语义，如 `--output=/etc/passwd`）。两者常同时存在，报告里可以分开写。

---

## 4. CWE-94 代码注入 / 动态求值

**弱点本质**：把不可信输入交给能**执行代码**的机制（eval、模板、反射、动态导入）。

### 易出现的代码模式

```python
# 危险
eval(user_input)
exec(user_input)
getattr(obj, user_attr)()                  # 若 user_attr 可控
__import__(user_module)                    # 动态导入
pickle.loads(...)                          # 也可归 CWE-502
jinja2.Template(user_template).render()    # 服务端模板注入 SSTI
yaml.load(data)                            # 默认 Loader 可构造对象，应用 safe_load
```

```javascript
// 危险
eval(code);
new Function(code)();
setTimeout(code, 0);                       // 字符串形式
vm.runInNewContext(code);                  // 若 code 不可信
require(userPath);                         // 动态 require
```

```php
// 危险
eval($code);
assert($code);                             // 老版本 PHP 的 assert 会执行字符串
call_user_func($cb, ...);
include($_GET['page']);                    // 可归 CWE-98 远程/本地文件包含
preg_replace('/x/e', $code, $s);           // /e 修饰符（已废弃但老代码有）
```

```java
// 危险
ScriptEngineManager().getEngineByName("js").eval(userScript);
Class.forName(userClassName).newInstance();   // 反射
```

### grep / 检索思路

```bash
rg -n '\beval\s*\(' 
rg -n '\bexec\s*\('
rg -n 'new Function\s*\(' --glob '*.{js,ts}'
rg -n -i 'fromCharCode|atob\s*\(|Buffer\.from\([^,)]*,\s*[\x27"]base64'   # 常见混淆前置
rg -n 'ScriptEngine|Nashorn|getEngineByName' --glob '*.java'
rg -n 'Class\.forName|newInstance\(' --glob '*.java'
rg -n -i 'Template\(|from_string\(|compile\(.*\)\.render' --glob '*.py'
rg -n 'yaml\.load\(|pickle\.loads\(|marshal\.loads\(|cPickle' --glob '*.py'
```

### 误报排除

| 看着像代码注入 | 为什么可能不是 |
| --- | --- |
| `eval` 的参数是**服务端生成的常量表达式**（如配置解析器内部） | 无外部输入 |
| `eval` 用于反序列化**自己加密签名的**数据且已验证签名 | 完整性有保证（但需确认签名算法与密钥管理无弱点） |
| `yaml.safe_load` | 只构造基础类型，不是危险汇 |
| `json.loads` | JSON 不是可执行结构，安全（除非后续把它喂给别的求值汇） |
| `pickle.loads` 但数据来自**本地可信文件**（如自己的缓存） | 需评估该文件能否被外部写入；能写就是真漏洞 |
| `Class.forName` 的参数来自服务端枚举 | 无外部输入 |

**最容易漏的**：**服务端模板注入（SSTI）**。开发者以为模板引擎只是"渲染字符串"，但只要**模板内容本身**由用户控制，就能通过模板语法访问宿主语言的运行时（如 Jinja2 的 `{{ ''.__class__.__mro__ }}`）。判断标准是：**用户控制的是"模板的变量"还是"模板的文本"？** 前者安全，后者危险。

---

## 5. CWE-22 路径穿越

**弱点本质**：用不可信输入构造文件路径，且没有把它限制在预期目录内，导致 `../` 逃逸。

### 易出现的代码模式

```python
# 危险
f = open(os.path.join(UPLOAD_DIR, filename))        # filename = "../../etc/passwd"
path = "/var/www/files/" + request.args['f']
send_file(path)
zipfile.ZipFile(...).extractall(dest)               # zip slip
tar.extractall(dest)                                # tar slip
```

```java
// 危险
new File(baseDir, userPath);
Files.readAllBytes(Paths.get(baseDir + userPath));
```

```php
readfile($_GET['file']);
include($_GET['page']);                             // 同时也是 LFI
```

```javascript
fs.readFileSync(path.join(baseDir, req.query.file));
res.sendFile(path.resolve(baseDir, req.query.file));
```

### grep / 检索思路

```bash
# 文件 API + 用户输入
rg -n -i '(open|readfile|readFile|readFileSync|createReadStream|writeFile|send_file|sendFile|Paths\.get|new File|FileInputStream)\([^)]*(\$_|request\.|req\.params|req\.query|req\.body|params\[|args\[)' 

# 解压相关的 slip
rg -n -i 'extractall|extract\(|untar|unzip|ZipInputStream|TarArchiveInputStream'

# 已有的防护（用于排除）
rg -n -i 'realpath|canonical|normalize|isWithin|resolve\(\)|startsWith\(.*base|toAbsolutePath'
```

### 误报排除

| 看着像路径穿越 | 为什么可能不是 |
| --- | --- |
| 路径经过 `realpath()` / `os.path.realpath()` 并确认前缀在基线目录内 | 已规范化并校验（注意：**校验必须在规范化之后**，且要用路径分隔符比较，避免 `/var/www/` 被 `/var/www-evil/` 前缀匹配） |
| 输入经严格白名单（如仅允许 `[a-zA-Z0-9._-]+` 且显式拒绝 `..`） | 已约束 |
| 基线目录本身由服务端常量决定，且输入只用于文件名部分并被 `basename()` 处理 | `basename` 去掉了目录部分（但要确认各语言 `basename` 行为，例如 Windows 反斜杠） |
| 输入是数字 ID，实际路径由服务端映射表得出 | 无路径拼接 |
| 只读且目录内无可读敏感文件 | 仍是弱点，但影响被降级——**不要因此不报，要在影响里说明** |

**两个常见假阴性**：

- **只在字符串层检查 `../`**，但攻击者可以用 URL 编码（`%2e%2e%2f`）、双重编码、反斜杠（Windows）、Unicode 归一化绕过。
- **`os.path.join(base, user)` 的行为陷阱**：如果 `user` 是**绝对路径**，Python 的 `join` 会直接丢弃 `base`。所以"用了 join 就安全"是错的。

---

## 6. CWE-434 危险类型文件上传

**弱点本质**：允许上传可被服务器/浏览器解释执行的文件类型，且上传后能被访问或执行。

### 易出现的代码模式

```python
# 危险：只信客户端提供的文件名/类型
filename = request.files['f'].filename
ext = filename.rsplit('.', 1)[1]
if ext in ['jpg','png']:                 # 绕过方式：烧瓶双扩展名 a.php.jpg / a.jpg.php / 大小写 / .phtml .php5
    save(os.path.join(UPLOAD, filename)) # 直接用原文件名
```

```php
// 危险：用 $_FILES['type']（客户端可控）
if ($_FILES['f']['type'] == 'image/png') { move_uploaded_file(...); }
```

```java
// 危险
new File(uploadDir, file.getOriginalFilename());   // 路径穿越 + 类型不受控
```

### grep / 检索思路

```bash
# 上传相关 API
rg -n -i 'multipart|MultipartFile|FormData|move_uploaded_file|getOriginalFilename|save\(.*upload|multer|busboy'

# 是否只依赖客户端提供的类型/文件名
rg -n -i "\\\$_FILES|\.filename|originalname|getOriginalFilename|\.contentType|Content-Type"

# 上传目录是否落在 Web 根目录下（这是致命的放大器）
rg -n -i 'upload.*(webroot|www|static|public|htdocs)'
```

### 误报排除

| 看着像不安全上传 | 为什么可能不是 |
| --- | --- |
| 上传目录在 Web 根之外，且由应用以数据流方式读取返回 | 无法直接执行；但要注意"文件名被用于响应头"导致的 header 注入 |
| 服务端用**文件内容魔数（magic bytes）**校验类型而非扩展名，且重命名文件、剥离扩展名 | 显著降低风险（仍需注意多态文件 / 解析器漏洞） |
| 类型白名单 + 服务端生成随机文件名 + 存储到对象存储且不设 Content-Type 为可执行 | 组合防护到位 |
| 上传的是纯数据文件（CSV/JSON）且后续只做解析 | 不是 CWE-434 的主场景，但需检查解析器本身的弱点（如 CSV 公式注入、XML XXE） |

**判据链条**：**能不能上传 → 能不能访问到 → 能不能被解释执行 → 能不能拿到权限。** 四步中任何一步断掉，风险大降。审计时要**沿这条链走完**，而不是只看第一步。

---

## 7. CWE-502 反序列化不可信数据

**弱点本质**：把不可信字节流交给反序列化器，而反序列化过程本身能**构造对象并触发代码**（魔术方法、`readObject`、`__reduce__` 等）。

### 易出现的代码模式

```java
// 危险：原生 Java 反序列化
ObjectInputStream ois = new ObjectInputStream(new ByteArrayInputStream(bytes));
Object o = ois.readObject();

// 危险：XMLDecoder / SnakeYAML（默认构造器）/ XStream / Hessian / 各类 RMI-JMX 入口
new XMLDecoder(input).readObject();
new Yaml().load(untrusted);                 // SnakeYAML 默认 load 可实例化任意类
// 识别特征：HTTP body 以 base64 的 "rO0AB" 开头（Java 序列化魔数 AC ED 00 05）
```

```python
# 危险
pickle.loads(data)
yaml.load(data)                # 应使用 yaml.safe_load
dill.loads(data)
jsonpickle.decode(data)
```

```php
// 危险
unserialize($_COOKIE['x']);
```

```javascript
// 危险
node-serialize / funcster 之类的库的 unserialize()
```

### grep / 检索思路

```bash
rg -n 'readObject\(|ObjectInputStream|XMLDecoder|XStream|Hessian|Burlap|Kryo|SnakeYAML|new Yaml\(\)'
rg -n 'pickle\.loads?|cPickle|dill\.loads?|yaml\.load\(' --glob '*.py'
rg -n 'unserialize\s*\(' --glob '*.php'
rg -n -i 'deserialize|unserialize|fromObject|readResolve|readObject'
```

流量侧特征：抓包看 HTTP body / Cookie / 隐藏字段是否以 **`rO0AB`** 开头（Base64 后的 Java 序列化魔数 `AC ED 00 05`）或以 **`gASV`** / `gAJ` 开头（Python pickle 的协议标记）。

### 误报排除

| 看着像反序列化风险 | 为什么可能不是 |
| --- | --- |
| 反序列化的数据来自**本进程**写入的本地缓存，且该缓存路径不可被外部写入 | 数据源可信（但需确认路径权限与文件权限） |
| 使用 `yaml.safe_load`、`json.loads`、`XMLDecoder` 之外的**显式白名单**对象工厂（如 Jackson 的 `activateDefaultTyping` 已移除 + 白名单） | 已限制可构造的类 |
| 反序列化前**先验签**（如带 HMAC 的会话 Cookie）且密钥未泄露 | 完整性有保证 |
| 用 `__reduce__` 白名单、`pickle.Unpickler.find_class` 重写做限制 | 已加固（需读实现确认白名单真的生效） |
| 关闭了 Java 反序列化的危险 gadget 链（如新版 JDK 的序列化过滤器） | 有纵深防御，但**不应作为唯一防线** |

**判断标准是"不可信 + 能构造对象"，二者缺一不可。** 所以审计时必须回答两个问题：(1) 字节流能否被非可信方控制？(2) 序列化器是否允许实例化任意类？

---

## 8. CWE-862 缺失授权

**弱点本质**：**根本没有**做授权检查（不是检查错了，是没检查）。

### 易出现的代码模式

```java
// 危险：只有认证（@Authenticated），没有授权
@GetMapping("/api/users/{id}/profile")        // 任何登录用户都能读任何人的资料
public Profile getProfile(@PathVariable Long id) {
    return userService.find(id);
}
```

```python
# 危险：接口只校验"已登录"，不校验"是不是管理员"
@app.route("/admin/settings", methods=["POST"])
@login_required
def update_settings():
    ...
```

```javascript
// 危险：前端隐藏按钮当作访问控制
// 前端: {isAdmin && <button onClick={deleteUser}/>}
router.delete('/api/users/:id', requireLogin, (req, res) => {
  User.destroy({ where: { id: req.params.id } });   // 后端没检查 req.user.isAdmin
});
```

**三个高频场景**

1. **只在前端做权限**：菜单/按钮按角色隐藏，接口裸奔。
2. **只检查了"登录态"，没检查"资源归属/角色"**：这是 CWE-862 与 CWE-639 的边界。
3. **新增接口忘记加中间件**：批量新增接口时，只复制了业务逻辑，没复制注解/装饰器。

### grep / 检索思路

**反向检索法（最有效）**：先列出所有路由/控制器，再逐个核对是否有授权注解。

```bash
# 1) 列出所有路由（以 Spring 为例）
rg -n '@(Get|Post|Put|Delete|Patch|Request)Mapping' --glob '*.java' -A 3

# 2) 列出所有授权相关注解/中间件
rg -n -i '@PreAuthorize|@Secured|@RolesAllowed|hasRole|hasAuthority|checkPermission|authorize\(|requireRole|@admin_required|can\('

# 3) 差集比对：有路由但没有授权注解的，就是候选
```

```bash
# 前端隐藏 vs 后端校验 的对比
rg -n -i 'v-if\s*=.*(isAdmin|hasRole|can)|isAdmin\s*&&|role\s*===?\s*["\x27]admin' --glob '*.{vue,jsx,tsx,js,ts}'
```

### 误报排除

| 看着像缺失授权 | 为什么可能不是 |
| --- | --- |
| 授权在**过滤器 / 拦截器 / 网关**统一做了（如 Spring Security 的 `http.authorizeHttpRequests`、Kong/Envoy 的鉴权插件） | 已集中管控——**这是默认的误报源，必须先读全局安全配置** |
| 方法上有 `@PreAuthorize` 在**类级别**声明 | 继承生效，需看类注解 |
| 接口返回的数据本身不含敏感信息且是公开内容 | 无需授权 |
| 在 Service 层做了归属校验（`if (record.ownerId != currentUser.id) throw`） | 已有校验，只是位置不在 Controller |
| 通过数据库视图/行级安全（RLS）做了约束 | 在数据层管控 |

**结论：审计 CWE-862 的第一动作不是读接口，而是先读全局的认证授权配置。** 否则会产生巨量误报。

---

## 9. CWE-639 通过用户可控键绕过授权（IDOR）

**弱点本质**：授权**做了**，但判断依据是**用户可控的键**（如路径/参数里的 ID），而没校验"当前主体是否有权访问该键对应的资源"。

### 易出现的代码模式

```java
// 危险：直接用请求里的 id 查询，未验证归属
@GetMapping("/orders/{orderId}")
public Order get(@PathVariable Long orderId) {
    return orderRepo.findById(orderId).orElseThrow();   // 没有 order.userId == currentUser.id 的条件
}
```

```python
# 危险：从前端传来的 tenant_id / user_id
@app.get("/api/invoices")
def list_invoices():
    tenant_id = request.args.get('tenant_id')     # 客户端可控 → 跨租户读取
    return query(tenant_id)

# 相对安全：从会话/令牌推导
    tenant_id = current_user.tenant_id
```

```javascript
// 危险：改 user_id 即可查他人
app.get('/api/messages', (req, res) => {
  Message.findAll({ where: { userId: req.query.userId } });
});
```

**变体**

- 路径参数（`/users/1002`）→ 最常见的 IDOR。
- 查询参数（`?tenant_id=7`）→ 多租户越权。
- 请求体字段（`{"userId": 1002}`）→ 容易被忽略。
- **JWT 中自带的可控字段**：如 `tenantId` 若来自客户端可改的 claim（需与签名校验一起看）。
- **GraphQL 的 node ID**：base64 编码的 `Type:ID`，改 ID 即可越权。

### grep / 检索思路

```bash
# 1) 找出所有"把请求参数直接当查询条件"的地方
rg -n -i '(findById|findOne|findByPk|get\(|filter\(|where\()\s*\(?\s*(req\.(params|query|body)|request\.(args|form|json)|\$_GET|\$_POST|params\[|id)' 

# 2) 找出"从会话推导主体"的模式（这些是安全范例）
rg -n -i 'current_user|currentUser|req\.user|SecurityContext|getPrincipal|session\[.user' 

# 3) 前端有没有把后端返回的内部 ID 直接用于后续请求
rg -n -i 'href=.*\$\{.*\.id\}|axios\.(get|delete)\(.*\+.*id|fetch\(.*\+.*id'
```

### 误报排除

| 看着像 IDOR | 为什么可能不是 |
| --- | --- |
| 查询条件里带了主体约束，如 `where userId = currentUser.id AND id = :id` | 已做归属校验 |
| 有统一的资源授权中间件（如 Spring Security 的 `@PostAuthorize` + `returnObject.owner == authentication.name`） | 已集中校验，需读实现确认 |
| ID 是**不可猜测的随机 UUID**，且无枚举接口 | 降低可发现性，但**不改变漏洞性质**——仍应报，只是优先级下调；UUID 泄露后照样越权 |
| 资源本身是公开信息（如公开文章） | 无需授权 |
| 使用的 ORM 有**多租户插件**自动注入 tenant 条件 | 已自动约束，需确认插件真的启用且无 `ignoreTenant` 逃生舱 |

**与 CWE-862 的区别**：CWE-862 是**没有**授权检查，CWE-639 是**有**检查但检查逻辑可被用户可控键绕过。写报告时按实际代码判断，不要混用。

---

## 10. CWE-352 跨站请求伪造（CSRF）

**弱点本质**：浏览器会自动携带 Cookie，攻击者用第三方页面构造请求，让受害者在**已登录状态**下执行非预期操作。

### 易出现的代码模式

```java
// 危险：全局关闭 CSRF 保护
http.csrf().disable();
```

```python
# Django：视图上加 csrf_exempt
@csrf_exempt
def transfer(request): ...

# Flask-WTF 未启用 CSRFProtect
```

```javascript
// 危险：用 Query String / Header 里的 token 做认证，而不是 Cookie
// 更危险的组合：Cookie 认证 + 无 SameSite + 无 CSRF token + 允许跨站表单提交
```

```html
<!-- 危险：Cookie 没有 SameSite 属性，浏览器默认行为随版本变化 -->
Set-Cookie: session=abc; Path=/
```

**关键配置上下文**

- Cookie 的 `SameSite`：`Strict` 最强，`Lax` 可挡大部分跨站 POST，`None` 必须搭配 `Secure` 且等于放弃这条防线。
- 状态变更接口是否只接受 `POST/PUT/DELETE`（`GET` 做写操作是 CSRF 的放大器）。
- 是否有自定义请求头校验（如 `X-Requested-With`）——这是**弱防护**，能挡简单表单但不能挡所有场景，不能单独作为防线。

### grep / 检索思路

```bash
rg -n -i 'csrf\.disable|csrf_exempt|csrfProtect|CSRFProtect|csrfToken|_csrf|X-CSRF'
rg -n -i 'SameSite|set_cookie|add_cookie|Set-Cookie'
rg -n -i '@(Get|RequestMapping)Mapping.*(delete|remove|update|transfer|pay|reset)'   # GET 做写操作
```

### 误报排除

| 看着像 CSRF | 为什么可能不是 |
| --- | --- |
| 接口用 **Bearer Token（Authorization 头）** 认证而非 Cookie | 浏览器不会自动附加，天然免疫 CSRF（前提是没有回退到 Cookie） |
| 全局启用了框架的 CSRF 中间件，且已确认对所有写方法生效 | 已防护 |
| Cookie 设置 `SameSite=Strict` 且业务不接受跨站发起 | 基本可挡 |
| 接口是纯读取（幂等） | CSRF 需要"状态变更"才有意义 |
| 有严格的自定义头校验 + CORS 限制，且**不存在**允许 `null`/通配 Origin 的配置 | 有效防护（但要确认 CORS 配置真的收紧） |
| 接口要求二次验证（密码/OTP/图形码） | 攻击者无法提供，实际不可利用 |

**最容易错判的两种情形**

1. **"我们用了 JWT，所以没有 CSRF"** —— 如果 JWT 存在 Cookie 里而不是 `Authorization` 头，同样有 CSRF。
2. **"我们关了 CORS，所以没有 CSRF"** —— CORS 限制的是**读取响应**，不限制**发送请求**。CSRF 只需要请求发出去，不需要读响应。

---

## 11. CWE-306 关键功能缺失认证

**弱点本质**：敏感功能（改配置、执行任务、导出数据、重置密码）**完全没有认证**，匿名即可调用。

### 易出现的代码模式

```python
# 危险：管理/运维接口裸奔
@app.route("/admin/export_all")            # 无 @login_required
def export_all(): ...

@app.route("/internal/health/db")          # 暴露内部信息
def db_health(): ...
```

```java
// 危险：actuator / 内部端点未加鉴权
// application.yml
// management.endpoints.web.exposure.include: "*"   且未配置安全约束
```

```nginx
# 危险：把内部接口直接暴露在公网
location /internal/ { proxy_pass http://internal-svc/; }
```

**高频场景**

- 调试 / 健康检查 / 指标端点（`/actuator/*`、`/debug`、`/metrics`、`/_profiler`）。
- 内部服务间接口（设计时假设"只在 VPC 内可达"，但被网关或反向代理暴露）。
- 定时任务的手动触发接口（`/job/run?name=...`）。
- 密码重置 / 邮箱验证的"服务端接口"。
- 老版本残留的测试接口。

### grep / 检索思路

```bash
# 1) 搜索明显的敏感路径名
rg -n -i '/(admin|internal|debug|test|dev|ops|manage|console|actuator|metrics|health|swagger|api-docs)'

# 2) 搜框架的"默认全开"配置
rg -n -i 'exposure\.include|endpoints\.enabled|swagger.*enabled|debug\s*=\s*true'

# 3) 反向：列出所有路由，标注哪些有鉴权装饰器，差集即候选
rg -n '@(app|bp)\.route|@(Get|Post|Put|Delete)Mapping|router\.(get|post|put|delete)'
```

### 误报排除

| 看着像缺失认证 | 为什么可能不是 |
| --- | --- |
| 认证由**网关/反向代理**统一前置（如 API Gateway 的 JWT 验证、mTLS） | 已在外层管控——**审计第一动作是先读网关配置** |
| 端点确实只在**不可路由的内网**且网络策略严格（需实际验证，不能只看文档） | 风险降低，但仍建议加应用层认证（纵深防御） |
| `/health` 只返回 `{"status":"ok"}`，无任何内部信息 | 影响可忽略，可作为信息类低危 |
| 有 mTLS 客户端证书校验 | 是认证，只是形式不同 |
| 端点是 OAuth2 的公开端点（`/oauth/token`、`/.well-known/*`） | 设计上就该公开 |

**关键动作**：**用匿名会话实际请求一遍**。这是唯一可靠的判定方式，也是 [PTES 漏洞分析阶段](../ptes/README.md#6-阶段四漏洞分析vulnerability-analysis) 要求"必须人工验证"的典型场景。

---

## 12. CWE-918 服务端请求伪造（SSRF）

**弱点本质**：服务端根据不可信输入发起网络请求，导致攻击者能让服务器去访问**它自己本来不该访问的地址**。

### 易出现的代码模式

```python
# 危险
url = request.args['url']
resp = requests.get(url)                       # 可请求 http://169.254.169.254/...
content = urllib.request.urlopen(user_url).read()
```

```java
// 危险
new URL(userInput).openStream();
HttpClient.newHttpClient().send(HttpRequest.newBuilder(URI.create(userInput)).build(), ...);
ImageIO.read(new URL(userInput));              // 图片处理也常是 SSRF
```

```php
file_get_contents($_GET['url']);
curl_exec(curl_init($_GET['url']));
```

```javascript
axios.get(req.body.url);
fetch(userInput);
// 危险：无头浏览器
await page.goto(userInput);
```

**高频出现位置**（不止"URL 参数"这一种）

- 头像 / 图片 / 文件"从 URL 导入"功能。
- Webhook 配置与回调地址。
- PDF / 截图 / 网页预览生成（无头浏览器最容易 SSRF）。
- XML 解析器（XXE 也是 SSRF 的一种形态）。
- 支持 URL 的富文本 / Markdown 渲染器（图片自动抓取）。
- SSE / 推送订阅地址。

### grep / 检索思路

```bash
rg -n -i '(requests\.(get|post|put|head)|urlopen|urllib|http\.client|HttpClient|OkHttp|RestTemplate|WebClient|axios|fetch\(|got\(|superagent|file_get_contents|curl_init|page\.goto|ImageIO\.read)'

# 是否已有 SSRF 防护
rg -n -i '169\.254\.169\.254|metadata\.google|allowed_hosts|allowlist|urlparse|InetAddress|isInternalIp|deny.*private'
```

### 误报排除

| 看着像 SSRF | 为什么可能不是 |
| --- | --- |
| URL 来自服务端配置（管理员在后台配置时已认证且做了校验） | 数据源可信程度不同——但仍要问"管理员账号被拿了呢"，通常降级而非完全排除 |
| 目标主机经**解析后 IP** 白名单校验，且校验在**每次重定向后重新执行** | 有效防护（只校验第一跳是常见缺陷） |
| 使用了 DNS 固定 / 网络层出站策略，把服务端能访问的范围限死在必要域名 | 体系性防护，最可靠 |
| 请求的目标是固定的第三方 API 地址，用户输入只影响查询参数值 | 不可控主机 |
| 请求在**客户端发起**（浏览器直接请求用户给的 URL） | 那是 CWE-601 开放重定向或客户端问题，不是 SSRF |

**四个必查的绕过点**（决定"有防护"是真防护还是假防护）

1. **重定向**：只校验了第一个 URL，服务端跟随 302 跳到内网地址。
2. **解析差异（DNS Rebinding / TOCTOU）**：校验时解析为公网 IP，实际请求时 DNS 重新解析为内网 IP。
3. **编码与地址表示**：`http://0x7f000001/`、`http://2130706433/`、`http://[::1]/`、`http://127.0.0.1.nip.io/`、带用户名 `http://expected.com@169.254.169.254/`。
4. **协议**：只禁了 `http/https` 却没禁 `file://`、`gopher://`、`dict://`、`ftp://`。

**结论：看到"有 SSRF 防护"不要直接判为误报，必须读防护实现，逐一验证上述四类绕过是否被覆盖。**

---

## 审计工作流建议

把本页的检查点落成可执行的流程：

```
第 0 步｜先读全局
  读认证授权配置、网关配置、过滤器链、CORS 配置。
  → 目的：避免后面产生巨量误报（尤其 CWE-862 / 306 / 352 / 918）

第 1 步｜确定范围与优先级
  按技术栈从 Top 25 中筛出相关弱点，排序成清单。
  → 纯 Web 应用：优先 79 / 89 / 862 / 639 / 352 / 306 / 918 / 434 / 502
  → 含 C/C++ 组件：追加 787 / 416 / 125 / 120 / 121 / 122

第 2 步｜机械检索
  用本页的 grep 命令扫出候选清单。
  → 产出：候选点列表（此时全是"疑似"）

第 3 步｜数据流分析
  对每个候选点，从输入源（Source）追到危险汇（Sink），确认不可信数据真的流到了。
  → 这一步淘汰大部分误报

第 4 步｜动态验证
  在授权环境构造最小 PoC 证明可利用。
  → 产出：可复现证据（对应 PTES 漏洞分析阶段的证据要求）

第 5 步｜归类与合并
  每个确认项归到一个 CWE，同类合并成一条修复项。
  → 产出：按 CWE 组织的发现清单，可直接对接开发排期

第 6 步｜回写规则
  把本次的高频 CWE 写入项目安全需求与设计评审检查表。
  → 目的：从"修漏洞"走向"防弱点"
```

---

## 与流程的衔接

| 本页内容 | 用在 [PTES](../ptes/README.md) 的哪一步 | 产出物 |
| --- | --- | --- |
| 第 1～2 节的检查点与 grep | 阶段四 漏洞分析（候选点发现） | 候选弱点清单 |
| 第 3～4 节的数据流与验证 | 阶段四 漏洞分析（真实可利用性验证） | 已验证漏洞清单 + 证据 |
| 第 5 节的归类合并 | 阶段七 报告 | 按 CWE 组织的发现与修复建议 |
| 第 6 节的规则回写 | 项目管理侧 | 安全需求基线、设计评审检查表 |
| 引用的漏洞类型编号 | 阶段七 报告的"弱点分类"字段 | 见 [报告模板](../ptes/templates.md#51-表结构) |

## 来源 URL

- 2025 CWE Top 25（本页 12 个弱点的编号、名称、排名、分值的来源）：<https://cwe.mitre.org/top25/archive/2025/2025_cwe_top25.html>
- CWE Top 25 门户：<https://cwe.mitre.org/top25/>
- CWE 条目定义（`Potential Mitigations` 段落是官方修复方向索引）：`https://cwe.mitre.org/data/definitions/<数字>.html`
  - 例：CWE-89 <https://cwe.mitre.org/data/definitions/89.html>｜CWE-79 <https://cwe.mitre.org/data/definitions/79.html>｜CWE-918 <https://cwe.mitre.org/data/definitions/918.html>
- CWE 数据索引（层级与视角）：<https://cwe.mitre.org/data/index.html>
- CWE 官网：<https://cwe.mitre.org/>
- OWASP Top 10:2025 分类页（用于确认本页弱点的 OWASP 归属）：
  - A01 Broken Access Control：<https://owasp.org/Top10/2025/A01_2025-Broken_Access_Control/>
  - A05 Injection：<https://owasp.org/Top10/2025/A05_2025-Injection/>
  - A06 Insecure Design：<https://owasp.org/Top10/2025/A06_2025-Insecure_Design/>
  - A07 Authentication Failures：<https://owasp.org/Top10/2025/A07_2025-Authentication_Failures/>
  - A08 Software or Data Integrity Failures：<https://owasp.org/Top10/2025/A08_2025-Software_or_Data_Integrity_Failures/>
  - A10 Mishandling of Exceptional Conditions：<https://owasp.org/Top10/2025/A10_2025-Mishandling_of_Exceptional_Conditions/>

> ⚠️ **说明与待核实项**
>
> 1. 本页的 **CWE 编号、名称、排名来自 2025 CWE Top 25 官方列表**，已核实。
> 2. 本页的 **代码示例是为说明弱点模式而编写的教学示例**，不是从任何真实项目复制。示例中的 API 名称取自各语言的标准库与主流框架，**具体参数签名与默认行为请以对应版本的官方文档为准**（例如 Python `subprocess` 的默认 `shell` 取值、各框架 CSRF 中间件的默认启用状态都会随版本变化）。
> 3. 本页的 **grep 命令是思路示范，不是可直接全量套用的脚本**。不同项目的目录结构与命名差异很大，请按实际情况调整 glob 与正则；`rg` 指 ripgrep，用 `grep -rEn` 亦可。
> 4. 各弱点的 **"误报排除"表格是方法论性质的经验总结**，不是官方定义。最终判定必须回到 CWE 官方条目的定义与 `Potential Mitigations` 段落，并结合实际代码与动态验证。
