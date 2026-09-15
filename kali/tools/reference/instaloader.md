# instaloader

> Instagram automatic photo downloader Instaloader downloads photos from Instagram, including public and private profiles, hashtags, user stories, feeds and saved media. How as well as comments, geotags and captions for each post. It automat…

> **功能分类**：通用工具 ｜ **Kali 包**：`instaloader` ｜ **官方文档**：<https://www.kali.org/tools/instaloader/>

## 1. 安装

```bash
sudo apt update
sudo apt install instaloader
```

| 项目 | 内容 |
|------|------|
| 版本 | 4.15.1 |
| 架构 | all |
| 可执行命令 | `instaloader` |
| 依赖 | `python3`、`python3-requests` |
| 安装体积 | 319 KB |
| 官网 | <https://github.com/instaloader/instaloader> |
| 源码仓库 | <https://salsa.debian.org/debian/instaloader> |
| 包追踪 | <https://pkg.kali.org/pkg/instaloader> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
instaloader -h          # 查看用法
man instaloader         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 1 个可执行命令，下面是官方页面内嵌的帮助原文。

### `instaloader`

> 官方示例调用：`instaloader -h`

```text
root@kali:~# instaloader -h
usage:
instaloader [--comments] [--geotags]
            [--stories] [--highlights] [--tagged] [--reels] [--igtv]
            [--login YOUR-USERNAME] [--fast-update]
            profile | "#hashtag" | %location_id | :stories | :feed | :saved
instaloader --help
Download pictures (or videos) along with their captions and other metadata
from Instagram.
What to Download:
  Specify a list of targets. For each of these, Instaloader creates a folder
  and downloads all posts. The following targets are supported:
  profile               Download profile. If an already-downloaded profile has
                        been renamed, Instaloader automatically finds it by
                        its unique ID and renames the folder likewise.
  @profile              Download all followees of profile. Requires login.
                        Consider using :feed rather than @yourself.
  "#hashtag"            Download #hashtag.
  %location_id          Download %location_id. Requires login.
  :feed                 Download pictures from your feed. Requires login.
  :stories              Download the stories of your followees. Requires
                        login.
  :saved                Download the posts that you marked as saved. Requires
                        login.
  -- -shortcode         Download the post with the given shortcode
  filename.json[.xz]    Re-Download the given object.
  +args.txt             Read targets (and options) from given textfile.
What to Download of each Post:
  --slide SLIDE         Set what image/interval of a sidecar you want to
                        download.
  --no-pictures         Do not download post pictures. Cannot be used together
                        with --fast-update. Implies --no-video-thumbnails,
                        does not imply --no-videos.
  -V, --no-videos       Do not download videos.
  --no-video-thumbnails
                        Do not download thumbnails of videos.
  -G, --geotags         Download geotags when available. Geotags are stored as
                        a text file with the location's name and a Google Maps
                        link. This requires an additional request to the
                        Instagram server for each picture. Requires login.
  -C, --comments        Download and update comments for each post. This
                        requires an additional request to the Instagram server
                        for each post, which is why it is disabled by default.
                        Requires login.
  --no-captions         Do not create txt files.
  --post-metadata-txt POST_METADATA_TXT
                        Template to write in txt file for each Post.
  --storyitem-metadata-txt STORYITEM_METADATA_TXT
                        Template to write in txt file for each StoryItem.
  --no-metadata-json    Do not create a JSON file containing the metadata of
                        each post.
  --no-compress-json    Do not xz compress JSON files, rather create pretty
                        formatted JSONs.
What to Download of each Profile:
  --no-posts            Do not download regular posts.
  --no-profile-pic      Do not download profile picture.
  -s, --stories         Also download stories of each profile that is
                        downloaded. Requires login.
  --highlights          Also download highlights of each profile that is
                        downloaded. Requires login.
  --tagged              Also download posts where each profile is tagged.
  --reels               Also download Reels videos.
  --igtv                Also download IGTV videos.
Which Posts to Download:
  -F, --fast-update     For each target, stop when encountering the first
                        already-downloaded picture. This flag is recommended
                        when you use Instaloader to update your personal
                        Instagram archive.
  --latest-stamps [STAMPSFILE]
                        Store the timestamps of latest media scraped for each
                        profile. This allows updating your personal Instagram
                        archive even if you delete the destination
                        directories. If STAMPSFILE is not provided, defaults
                        to /root/.config/instaloader/latest-stamps.ini
  --post-filter, --only-if filter
                        Expression that, if given, must evaluate to True for
                        each post to be downloaded. Must be a syntactically
                        valid python expression. Variables are evaluated to
                        instaloader.Post attributes. Example: --post-
                        filter=viewer_has_liked.
  --storyitem-filter filter
                        Expression that, if given, must evaluate to True for
                        each storyitem to be downloaded. Must be a
                        syntactically valid python expression. Variables are
                        evaluated to instaloader.StoryItem attributes.
  -c, --count COUNT     Do not attempt to download more than COUNT posts.
                        Applies to #hashtag, %location_id, :feed, and :saved.
Login (Download Private Profiles):
  Instaloader can login to Instagram. This allows downloading private
  profiles. To login, pass the --login option. Your session cookie (not your
  password!) will be saved to a local file to be reused next time you want
  Instaloader to login. Instead of --login, the --load-cookies option can be
  used to import a session from a browser.
  -l, --login YOUR-USERNAME
                        Login name (profile name) for your Instagram account.
  -b, --load-cookies BROWSER-NAME
                        Browser name to load cookies from Instagram
  -B, --cookiefile COOKIE-FILE
                        Cookie file of a profile to load cookies
  -f, --sessionfile SESSIONFILE
                        Path for loading and storing session key file.
                        Defaults to
                        /root/.config/instaloader/session-<login_name>
  -p, --password YOUR-PASSWORD
                        Password for your Instagram account. Without this
                        option, you'll be prompted for your password
                        interactively if there is not yet a valid session
                        file.
How to Download:
  --dirname-pattern DIRNAME_PATTERN
                        Name of directory where to store posts. {profile} is
                        replaced by the profile name, {target} is replaced by
                        the target you specified, i.e. either :feed, #hashtag
                        or the profile name. Defaults to '{target}'.
  --filename-pattern FILENAME_PATTERN
                        Prefix of filenames for posts and stories, relative to
                        the directory given with --dirname-pattern. {profile}
                        is replaced by the profile name,{target} is replaced
                        by the target you specified, i.e. either :feed#hashtag
                        or the profile name. Defaults to '{date_utc}_UTC'
  --title-pattern TITLE_PATTERN
                        Prefix of filenames for profile pics, hashtag profile
                        pics, and highlight covers. Defaults to
                        '{date_utc}_UTC_{typename}' if --dirname-pattern
                        contains '{target}' or '{dirname}', or if --dirname-
                        pattern is not specified. Otherwise defaults to
                        '{target}_{date_utc}_UTC_{typename}'.
  --resume-prefix PREFIX
                        Prefix for filenames that are used to save the
                        information to resume an interrupted download.
  --sanitize-paths      Sanitize paths so that the resulting file and
                        directory names are valid on both Windows and Unix.
  --no-resume           Do not resume a previously-aborted download iteration,
                        and do not save such information when interrupted.
  --user-agent USER_AGENT
                        User Agent to use for HTTP requests. Defaults to
                        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36
                        (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36'.
  --max-connection-attempts N
                        Maximum number of connection attempts until a request
                        is aborted. Defaults to 3. If a connection fails, it
                        can be manually skipped by hitting CTRL+C. Set this to
                        0 to retry infinitely.
  --request-timeout N   Seconds to wait before timing out a connection
                        request. Defaults to 300.
  --abort-on STATUS_CODES
                        Comma-separated list of HTTP status codes that cause
                        Instaloader to abort, bypassing all retry logic.
  --no-iphone           Do not attempt to download iPhone version of images
                        and videos.
Miscellaneous Options:
  -q, --quiet           Disable user interaction, i.e. do not print messages
                        (except errors) and fail if login credentials are
                        needed but not given. This makes Instaloader suitable
                        as a cron job.
  -h, --help            Show this help message and exit.
  --version             Show version number and exit.
The complete documentation can be found at https://instaloader.github.io/.
Updated on: 2026-May-25
 Edit this page
hoaxshell
iodine
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
Newsletter
RSS
Policies
Cookie Policy
Privacy Policy
Trademark Policy
© OffSec Services Limited 2026. All rights reserved.
Kali Linux is part of OffSec's Community Projects
Learn more about OffSec's free, open-source penetration testing tools for cybersecurity professionals
```

## 4. 实践清单

按顺序做完这五步，就能把工具从「装上」推进到「会用」：

- [ ] **1.** **装好并确认版本** —— `sudo apt install instaloader`，再执行 `instaloader --version` 2>/dev/null || `instaloader -V`
- [ ] **2.** **读官方帮助** —— `instaloader -h`，需要细节时 `man instaloader`
- [ ] **3.** **在自有靶场跑最小用例** —— 用 `instaloader -h` 里最简单的那个子命令试一次
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/instaloader/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/reconnaissance.md`](../../tools/by-attack/reconnaissance.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/instaloader/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/instaloader/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
