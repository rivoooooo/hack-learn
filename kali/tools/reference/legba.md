# legba

> Multiprotocol credentials bruteforcer / password sprayer and enumerator Legba is a multiprotocol credentials bruteforcer / password sprayer and enumerator built with Rust and the Tokio asynchronous runtime in order to achieve better perfor…

> **功能分类**：通用工具 ｜ **Kali 包**：`legba` ｜ **官方文档**：<https://www.kali.org/tools/legba/>

## 1. 安装

```bash
sudo apt update
sudo apt install legba
```

| 项目 | 内容 |
|------|------|
| 版本 | 1.3.0 |
| 架构 | any |
| 可执行命令 | `legba` |
| 依赖 | `libc6`、`libgcc-s1` |
| 安装体积 | 27.70 MB |
| 官网 | <https://github.com/maaaaz/webscreenshot> |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/legba> |
| 包追踪 | <https://pkg.kali.org/pkg/legba> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
legba -h          # 查看用法
man legba         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### `legba`

> 官方示例调用：`legba -h`

```text
root@kali:~# legba -h
Usage: legba [OPTIONS] [PLUGIN]
Arguments:
  [PLUGIN]  Protocol plugin to use, run with --list-plugins for a list of all available plugins
Options:
  -L, --list-plugins
          List all available protocol plugins
  -R, --recipe <RECIPE>
          Load a recipe from this YAML file
  -T, --target <TARGET>
          Single target host, url or IP address, IP range, CIDR, @filename or comma separated combination of them
      --api <API>
          Enable the REST API and bind it to the specified address:port
      --api-allowed-origin <API_ALLOWED_ORIGIN>
          Use a more restrictive CORS policy by only allowing requests from the specified origin [default: 127.0.0.1]
      --mcp <MCP>
          Enable the MCP server and bind it to the specified address:port. Use stdio to use standard input/output instead of SSE
  -U, --username <USERNAME>
          Constant, filename, glob expression as @/some/path/*.txt, permutations as #min-max:charset / #min-max or range as [min-max] / [n, n, n] [aliases: --payloads]
  -P, --password <PASSWORD>
          Constant, filename, glob expression as @/some/path/*.txt or permutations as #min-max:charset / #min-max or range as [min-max] / [n, n, n] [aliases: --key]
  -C, --combinations <COMBINATIONS>
          Load username:password combinations from this file
      --separator <SEPARATOR>
          Separator if using the --combinations/-C argument [default: :]
  -I, --iterate-by <ITERATE_BY>
          Whether to iterate by user or by password [default: user] [possible values: user, password]
  -J, --json
          Log runtime statistics and events as JSON
  -S, --session <SESSION>
          Save and restore session information to this file
  -O, --output <OUTPUT>
          Save results to this file
      --output-format <OUTPUT_FORMAT>
          Output file format [default: text] [possible values: text, csv, jsonl]
      --timeout <TIMEOUT>
          Connection timeout in milliseconds [default: 1000]
      --retries <RETRIES>
          Number of attempts if a request fails [default: 1]
      --retry-time <RETRY_TIME>
          Delay in milliseconds to wait before a retry [default: 1000]
      --report-time <REPORT_TIME>
          Report runtime statistics every N milliseconds [default: 5000]
      --single-match
          Exit after the first positive match is found
      --ulimit <ULIMIT>
          Value for ulimit (max open file descriptors) [default: 10000]
      --concurrency <CONCURRENCY>
          Number of concurrent workers [default: 6]
      --rate-limit <RATE_LIMIT>
          Limit the number of requests per second [default: 0]
  -W, --wait <WAIT>
          Wait time in milliseconds per login attempt [default: 0]
      --jitter-min <JITTER_MIN>
          Minimum number of milliseconds for random request jittering [default: 0]
      --jitter-max <JITTER_MAX>
          Maximum number of milliseconds for random request jittering [default: 0]
  -Q, --quiet
          Do not report statistics
      --generate-completions <GENERATE_COMPLETIONS>
          Generate shell completions [possible values: bash, elvish, fish, powershell, zsh]
  -h, --help
          Print help
  -V, --version
          Print version
COMMAND (CMD):
      --cmd-binary <CMD_BINARY>
          Command binary [default: ]
      --cmd-args <CMD_ARGS>
          Command arguments. {USERNAME}, {PASSWORD}, {TARGET} and {PORT} can be used as placeholders [default: ]
      --cmd-success-exit-code <CMD_SUCCESS_EXIT_CODE>
          Process exit code to be considered as a positive match [default: 0]
      --cmd-success-match <CMD_SUCCESS_MATCH>
          String to look for in the process standard output to be considered as a positive match
AMQP:
      --amqp-ssl  Enable SSL for AMQP
HTTP:
      --http-ua <HTTP_UA>
          Set a User-Agent. If none is specified, it'll be picked randomly for each request
      --http-success <HTTP_SUCCESS>
          Boolean expression to use to determine if a request is successful [default: "status == 200"]
      --http-follow-redirects
          Follow HTTP redirects
      --http-method <HTTP_METHOD>
          Request method for HTTP based plugins [default: GET]
      --http-headers <HTTP_HEADERS>...
          Request headers for HTTP based plugins
      --http-csrf-page <HTTP_CSRF_PAGE>
          For each request grab a CSRF token from this page
      --http-csrf-regexp <HTTP_CSRF_REGEXP>
          Regular expression to use to grab the CSRF token name and value [default: "<input type=\"hidden\" name=\"([^\\\"]+)\" value=\"([^\"]+)\""]
      --http-payload <HTTP_PAYLOAD>
          Request payload (query string, post body or form data) for HTTP based plugins
      --http-enum-ext <HTTP_ENUM_EXT>
          File extension for HTTP enumeration [default: php]
      --http-enum-ext-placeholder <HTTP_ENUM_EXT_PLACEHOLDER>
          File extension placeholder for HTTP enumeration wordlist [default: %EXT%]
      --http-ntlm-domain <HTTP_NTLM_DOMAIN>
          Domain for NTLM authentication over HTTP
      --http-ntlm-workstation <HTTP_NTLM_WORKSTATION>
          Workstation name for NTLM authentication over HTTP [default: CLIENT]
      --proxy <PROXY>
          Proxy URL
      --proxy-auth <PROXY_AUTH>
          Proxy authentication as username:password
DNS:
      --dns-resolvers <DNS_RESOLVERS>
          Comma separatd list of DNS resolvers to use instead of the system one
      --dns-port <DNS_PORT>
          Resolver(s) port [default: 53]
      --dns-attempts <DNS_ATTEMPTS>
          Number of retries after lookup failure before giving up [default: 1]
      --dns-ip-lookup
          Perform ip to hostname lookup
      --dns-max-positives <DNS_MAX_POSITIVES>
          If more than this amount of sequential dns resolutions point to the same ip, add that ip to an ignore list [default: 10]
      --dns-no-https
          Do not fetch HTTPS certificates for new domains
TELNET:
      --telnet-user-prompt <TELNET_USER_PROMPT>
          Telnet server username login prompt string [default: "login: "]
      --telnet-pass-prompt <TELNET_PASS_PROMPT>
          Telnet server password login prompt string [default: "Password: "]
      --telnet-prompt <TELNET_PROMPT>
          Telnet server shell prompt after successful login [default: ":~$ "]
SSH:
      --ssh-auth-mode <SSH_AUTH_MODE>
          Authentication strategy [default: password] [possible values: key, password]
      --ssh-key-passphrase <SSH_KEY_PASSPHRASE>
          Optional private key passphrase for key based authentication
SMTP:
      --smtp-mechanism <SMTP_MECHANISM>
          SMTP authentication mechanism, can be PLAIN (RFC4616), LOGIN (obsolete but needed for some providers like office365) or XOAUTH2 [default: PLAIN]
SNMP:
      --snmp-oid <SNMP_OID>  Specify a single OID to read, if not specified the entire SNMP tree is walked
      --snmp-max <SNMP_MAX>  Specify a maximum number of OIDs to walk. Set to 0 to walk the entire SNMP tree (it may take a long time) [default: 25]
SOCKS5:
      --socks5-address <SOCKS5_ADDRESS>  Remote address to test the proxying for [default: ifcfg.co]
      --socks5-port <SOCKS5_PORT>        Remote port to test the proxying for [default: 80]
POP3:
      --pop3-ssl  Enable SSL for POP3
LDAP:
      --ldap-domain <LDAP_DOMAIN>  LDAP domain
KERBEROS:
      --kerberos-realm <KERBEROS_REALM>
          Kerberos realm
      --kerberos-protocol <KERBEROS_PROTOCOL>
          Kerberos transport protocol [default: tcp] [possible values: udp, tcp]
      --kerberos-linux
          If targeting a Linux Kerberos5 implementation, pass this flag to preserve the realm string case
RDP:
      --rdp-domain <RDP_DOMAIN>  Domain name [default: ]
      --rdp-ntlm                 Use a NTLM hash instead of a password
      --rdp-admin-mode           Restricted admin mode
      --rdp-auto-logon           AutoLogon mode in case of SSL negotiation
MQTT:
      --mqtt-v5   Use v5 of the MQTT protocol
      --mqtt-ssl  Use SSL/TLS connection (mqtts://) with certificate verification disabled
REDIS:
      --redis-ssl  Enable SSL for Redis
PORT SCANNER:
      --port-scanner-ports <PORT_SCANNER_PORTS>
          Range or comma separated values of integer port numbers to scan [default: 22,80,443,79,[81-85],[19-21],[23-26],[1-4],[6-7],9,13,17,30,[32-33],[37-38],[42-43],49,53,[67-70],[88-90],[99-100],106,[109-113],[119-120],123,125,[135-139],[143-144],146,158,[161-163],177,179,192,199,207,[211-212],217,222,[254-256],259,264,280,301,306,311,340,363,366,389,402,[406-407],[416-417],425,427,434,[444-445],458,[464-465],481,497,500,502,[512-515],[517-518],520,524,539,541,[543-545],548,[554-555],559,563,587,593,[616-617],623,[625-626],631,636,639,643,646,648,657,664,[666-668],[682-689],691,700,705,711,714,720,722,726,749,[764-765],767,[772-777],[780-783],[786-787],789,[800-801],808,814,826,829,838,843,873,880,888,898,[900-903],[911-912],944,959,965,981,983,987,[989-990],[992-993],[995-1002],[1007-1014],[1019-1102],[1104-1108],[1110-1114],1117,1119,[1121-1124],1126,[1130-1132],[1137-1138],1141,1145,[1147-1149],[1151-1152],1154,[1163-1166],1169,[1174-1175],1183,[1185-1187],1192,[1198-1201],[1213-1214],[1216-1218],[1233-1234],1236,1244,[1247-1248],1259,[1271-1272],1277,1287,1296,[1300-1301],[1309-1311],1322,1328,1334,1346,1352,1417,1419,[1433-1434],1443,1455,1457,1461,[1484-1485],1494,[1500-1501],1503,1521,1524,1533,1556,1580,1583,1594,1600,1641,[1645-1646],1658,1666,[1687-1688],[1700-1701],[1717-1721],1723,1755,1761,[1782-1783],1801,[1804-1805],[1812-1813],[1839-1840],[1862-1864],1875,[1885-1886],[1900-1901],1914,1935,1947,[1971-1972],1974,1984,1993,[1998-2010],2013,[2020-2022],2030,[2033-2035],2038,[2040-2043],[2045-2049],2051,2065,2068,[2099-2100],2103,[2105-2107],2111,2119,2121,2126,2135,2144,2148,[2160-2161],2170,2179,[2190-2191],2196,2200,[2222-2223],2251,2260,2288,2301,2323,2343,2345,2362,2366,[2381-2383],[2393-2394],2399,2401,2492,2500,2522,2525,2557,[2601-2602],[2604-2605],[2607-2608],2638,[2701-2702],2710,[2717-2718],2725,2800,2809,2811,2869,2875,[2909-2910],2920,[2967-2968],2998,[3000-3001],3003,[3005-3006],3011,3017,[3030-3031],3052,3071,3077,3128,3130,3168,3211,3221,[3260-3261],[3268-3269],3283,3296,[3300-3301],3306,[3322-3325],3333,3343,3351,3367,[3369-3372],[3389-3390],3401,3404,[3456-3457],3476,3493,3517,3527,3546,3551,3580,3659,3664,[3689-3690],[3702-3703],3737,3766,3784,[3800-3801],3809,3814,[3826-3828],3851,3869,3871,3878,3880,3889,3905,3914,3918,3920,3945,3971,3986,3995,3998,[4000-4006],4008,4045,4111,[4125-4126],4129,4224,4242,4279,4321,4343,[4443-4446],4449,4500,4550,4567,4662,4666,4672,4848,[4899-4900],4998,[5000-5004],[5009-5010],5030,5033,[5050-5051],5054,[5060-5061],5080,5087,5093,[5100-5102],5120,5190,5200,5214,[5221-5222],[5225-5226],5269,5280,5298,5351,5353,5355,5357,5405,5414,[5431-5432],5440,5500,5510,5544,5550,5555,5560,5566,[5631-5633],5666,[5678-5679],5718,5730,[5800-5802],[5810-5811],5815,5822,5825,5850,5859,5862,5877,[5900-5904],[5906-5907],[5910-5911],5915,5922,5925,5950,5952,[5959-5963],[5985-5989],[5998-6007],6009,6025,6050,6059,[6100-6101],6106,6112,6123,6129,6156,[6346-6347],6389,6502,6510,6543,6547,[6565-6567],6580,6646,[6666-6669],6689,6692,6699,6779,[6788-6789],6792,6839,6881,6901,[6969-6971],[7000-7002],7004,7007,7019,7025,7070,7100,7103,7106,[7200-7201],7402,7435,7443,7496,7512,7625,7627,7676,7741,[7777-7778],7800,7911,[7920-7921],[7937-7938],[7999-8002],[8007-8011],[8021-8022],8031,8042,8045,[8080-8090],8093,[8099-8100],[8180-8181],[8192-8194],8200,8222,8254,[8290-8292],8300,8333,8383,8400,8402,8443,8500,8600,8649,[8651-8652],8654,8701,8800,8873,8888,[8899-8900],8994,[9000-9003],[9009-9011],9020,9040,9050,9071,[9080-9081],[9090-9091],[9099-9103],[9110-9111],[9199-9200],9207,9220,9290,9370,9415,9418,9485,9500,[9502-9503],9535,9575,[9593-9595],9618,9666,[9876-9878],9898,9900,9917,9929,[9943-9944],9950,9968,[9998-10004],[10009-10010],10012,[10024-10025],10080,10082,10180,10215,10243,10566,[10616-10617],10621,10626,[10628-10629],10778,[11110-11111],11487,11967,12000,12174,12265,12345,13456,13722,[13782-13783],14000,14238,[14441-14442],15000,[15002-15004],15660,15742,[16000-16001],16012,16016,16018,16080,16086,16113,16402,16420,16430,16433,16449,16498,16503,16545,16548,16573,16674,16680,16697,16700,16708,16711,16739,16766,16779,16786,16816,16829,16832,[16838-16839],16862,16896,16912,[16918-16919],[16938-16939],[16947-16948],16970,16972,16974,[16992-16993],17006,17018,17077,17091,17101,17146,[17184-17185],17205,17207,17219,[17236-17237],17282,17302,17321,[17331-17332],17338,17359,17417,[17423-17424],17455,17459,17468,17487,17490,17494,17505,17533,17549,17573,17580,17585,17592,17605,[17615-17616],17629,17638,17663,[17673-17674],17683,17726,17754,17762,17787,17814,[17823-17824],17836,17845,17877,17888,17939,17946,[17988-17989],18004,18040,18081,18101,18113,18134,18156,18228,18234,18250,18255,18258,18319,18331,18360,18373,18449,18485,18543,18582,18605,18617,18666,18669,18676,18683,18807,18818,18821,18830,18832,18835,18869,18883,18888,18958,18980,18985,[18987-18988],18991,18994,18996,19017,19022,19039,19047,19075,19096,19101,19120,19130,[19140-19141],19154,19161,19165,19181,19193,19197,19222,19227,19273,19283,19294,19315,19322,19332,19350,19374,19415,19482,19489,19500,[19503-19504],19541,19600,19605,19616,[19624-19625],19632,19639,19647,19650,19660,[19662-19663],[19682-19683],19687,19695,19707,[19717-19719],19722,19728,19780,19789,19792,19801,19842,19933,[19935-19936],19956,19995,19998,20000,[20003-20005],20019,20031,20082,20117,20120,20126,20129,20146,20154,20164,20206,20217,[20221-20222],20249,20262,20279,20288,20309,20313,20326,[20359-20360],20366,20380,20389,20409,20411,[20423-20425],20445,20449,[20464-20465],20518,20522,20525,20540,20560,20665,[20678-20679],20710,20717,20742,20752,20762,20791,20817,20828,20842,20848,20851,20865,20872,20876,20884,20919,21000,21016,21060,21083,21104,21111,21131,21167,21186,[21206-21207],21212,21247,21261,21282,21298,21303,21318,21320,21333,21344,21354,21358,21360,21364,21366,21383,21405,21454,21468,21476,21514,[21524-21525],21556,21566,21568,21571,21576,21609,21621,21625,21644,21649,21655,21663,21674,21698,21702,21710,21742,21780,21784,21800,21803,21834,21842,21847,21868,21898,21902,21923,21948,21967,22029,22043,22045,22053,22055,22105,22109,[22123-22124],22341,22692,22695,22739,22799,22846,22914,22939,22986,22996,23040,23176,23354,23502,23531,23557,23608,23679,23781,23965,23980,24007,24279,24444,24511,24594,24606,24644,24800,24854,24910,25003,25157,25240,25280,25337,25375,25462,25541,25546,25709,[25734-25735],25931,26214,26407,26415,26720,26872,26966,27000,27015,27195,[27352-27353],[27355-27356],27444,27473,27482,27707,27715,27892,27899,28122,28201,28369,28465,28493,28543,28547,28641,28840,28973,29078,29243,29256,29810,29823,29977,30000,30263,30303,30365,30544,30656,30697,30704,30718,30951,30975,31038,31059,31073,31109,31189,31195,31335,31337,31365,31625,31681,31731,31891,32345,32385,32528,[32768-32785],32798,32815,32818,32931,33030,33249,33281,[33354-33355],33459,33717,33744,33866,33872,33899,34038,34079,34125,34358,34422,34433,34555,[34570-34573],[34577-34580],34758,34796,34855,[34861-34862],34892,35438,35500,35702,35777,35794,36108,36206,36384,36458,36489,36669,36778,36893,36945,37144,37212,37393,37444,37602,37761,37783,37813,37843,38037,38063,[38292-38293],38412,38498,38615,39213,39217,39632,39683,39714,39723,39888,40019,40116,40193,40441,40539,40622,40708,40711,40724,40732,40805,40847,40866,40911,40915,41058,41081,41308,41370,41446,41511,41524,41638,41702,41774,41896,41967,41971,42056,42172,42313,42431,42434,42508,42510,42557,42577,42627,42639,43094,43195,43370,43514,43686,43824,43967,44101,44160,44176,44179,44185,44190,44253,44334,[44442-44443],44501,44508,44923,44946,44968,45100,45247,45380,45441,45685,45722,45818,45928,46093,46532,46836,47624,47765,47772,47808,47915,47981,48078,48080,48189,48255,48455,48489,48761,[49152-49163],[49165-49182],[49184-49202],[49204-49205],[49207-49216],49220,49222,49226,49259,49262,49306,49350,49360,49393,49396,49400,49503,49640,49968,[49999-50003],50006,50099,50164,50300,50389,50497,50500,50612,50636,50708,50800,50919,51103,51255,51456,51493,51554,51586,51690,51717,51905,51972,52144,52225,52503,52673,52822,52848,52869,53006,53037,53571,53589,53838,54045,54094,54114,54281,54321,54328,54711,54807,54925,55043,[55055-55056],55544,55555,55587,55600,56141,[56737-56738],57172,57294,[57409-57410],57797,57813,57843,57958,57977,58002,58075,58080,58178,58419,58631,58640,58797,59193,59207,59765,59846,60020,60172,60381,60423,60443,61024,61142,61319,61322,61370,61412,61481,61532,61550,61685,61900,61961,62078,62154,62287,62575,62677,62699,62958,63331,63420,63555,64080,64481,64513,64590,64623,64680,64727,65000,65024,65129,65389]
      --port-scanner-no-banners
          Do not attempt banner grabbing
      --port-scanner-no-udp
          Do not perform UDP scan
      --port-scanner-no-tcp
          Do not perform TCP scan
      --port-scanner-banner-timeout <PORT_SCANNER_BANNER_TIMEOUT>
          Timeout in milliseconds for banner grabbing [default: 5000]
      --port-scanner-http <PORT_SCANNER_HTTP>
          Comma separated list of ports for HTTP grabbing [default: "80, 8080, 8081, 8888"]
      --port-scanner-https <PORT_SCANNER_HTTPS>
          Comma separated list of ports for HTTPS grabbing [default: "443, 8443"]
      --port-scanner-http-headers <PORT_SCANNER_HTTP_HEADERS>
          Comma separated list lowercase header names for HTTP/HTTPS grabbing [default: "server, x-powered-by, location, content-type"]
IRC:
      --irc-tls  Use TLS for IRC
Updated on: 2026-Jun-17
 Edit this page
ldeep
linkedin2username
LIGHT
DARK
Links
Home
Download / Get Kali
Blog
OS Documentation
Tool Documentation
System Status
Archived Releases
Partnerships
Platforms
ARM (SBC)
NetHunter (Mobile)
Amazon AWS
Docker
Linode
Microsoft Azure
Microsoft Store (WSL)
Vagrant
Development
Bug Tracker
Continuous Integration
Network Mirror
Package Tracker
GitLab
Community
Discord
Support Forum
PeerTube
Follow Us
Bluesky
Facebook
Instagram
Mastodon
Substack
X
```

## 4. 实践清单

按顺序做完这五步，就能把工具从「装上」推进到「会用」：

- [ ] **1.** **装好并确认版本** —— `sudo apt install legba`，再执行 `legba --version` 2>/dev/null || `legba -V`
- [ ] **2.** **读官方帮助** —— `legba -h`，需要细节时 `man legba`
- [ ] **3.** **在自有靶场跑最小用例** —— 官方给出的调用形式是：`Usage: legba [OPTIONS] [PLUGIN]`
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/legba/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/credential-access.md`](../../tools/by-attack/credential-access.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/legba/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/legba/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
