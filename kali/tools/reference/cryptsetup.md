# cryptsetup

> Disk encryption support - startup scripts Cryptsetup provides an interface for configuring encryption on block devices (such as /home or swap partitions), using the Linux kernel device mapper target dm-crypt. It features integrated Linux U…

> **功能分类**：防护 ｜ **Kali 包**：`cryptsetup` ｜ **官方文档**：<https://www.kali.org/tools/cryptsetup/>

## 1. 安装

```bash
sudo apt update
sudo apt install cryptsetup
```

| 项目 | 内容 |
|------|------|
| 版本 | 2.8.7 |
| 架构 | linux-any |
| 可执行命令 | `cryptsetup`、`cryptdisks_start`、`cryptdisks_stop`、`luksformat`、`cryptsetup-bin`、`integritysetup`、`veritysetup`、`cryptsetup-initramfs`、`cryptsetup-ssh`、`cryptsetup-suspend`、`cryptsetup-udeb`、`libcryptsetup-dev`、`libcryptsetup12`、`libcryptsetup12-udeb` |
| 依赖 | `cryptsetup-bin` |
| 安装体积 | 465 KB |
| 官网 | <https://gitlab.com/cryptsetup/cryptsetup> |
| 源码仓库 | <https://salsa.debian.org/cryptsetup-team/cryptsetup> |
| 包追踪 | <https://pkg.kali.org/pkg/cryptsetup> |

## 2. 官方用法示例

> 官方工具页未附示例，可直接看下一节的 `-h` / man 原文自取。

```bash
cryptsetup -h          # 查看用法
man cryptsetup         # 查看手册
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 14 个可执行命令，下面是官方页面内嵌的帮助原文。

### `cryptdisks_start`

> 官方示例调用：`cryptdisks_start -h`

```text
root@kali:~# cryptdisks_start -h
Usage: /usr/sbin/cryptdisks_start [-r|--readonly] <name> [.. <name>]
reads /etc/crypttab and starts the mapping corresponding to <name>
```

### `cryptdisks_stop`

> 官方示例调用：`cryptdisks_stop -h`

```text
root@kali:~# cryptdisks_stop -h
Stopping crypto disk...-h (stopped)...done.
```

### `luksformat`

> 官方示例调用：`luksformat -h`

```text
root@kali:~# luksformat -h
luksformat - Create and format an encrypted LUKS device
Usage: luksformat [-t <file system>] <device> [ mkfs options ]
```

### `cryptsetup`

> 官方示例调用：`cryptsetup --help`

```text
root@kali:~# cryptsetup --help
cryptsetup 2.8.7 flags: UDEV BLKID KEYRING KERNEL_CAPI HW_OPAL
Usage: cryptsetup [OPTION...] <action> <action-specific>
Help options:
  -?, --help                              Show this help message
      --usage                             Display brief usage
  -V, --version                           Print package version
      --active-name=STRING                Override device autodetection of dm
                                          device to be reencrypted
      --align-payload=SECTORS             Align payload at <n> sector
                                          boundaries - for luksFormat
      --allow-discards                    Allow discards (aka TRIM) requests
                                          for device
  -q, --batch-mode                        Do not ask for confirmation
      --cancel-deferred                   Cancel a previously set deferred
                                          device removal
  -c, --cipher=STRING                     The cipher used to encrypt the disk
                                          (see /proc/crypto)
      --debug                             Show debug messages
      --debug-json                        Show debug messages including JSON
                                          metadata
      --decrypt                           Decrypt LUKS2 device (remove
                                          encryption)
      --deferred                          Device removal is deferred until the
                                          last user closes it
      --device-size=bytes                 Use only specified device size
                                          (ignore rest of device), DANGEROUS!
      --disable-blkid                     Disable blkid on-disk signature
                                          detection and wiping
      --disable-external-tokens           Disable loading of external LUKS2
                                          token plugins
      --disable-keyring                   Disable loading volume keys via
                                          kernel keyring
      --disable-locks                     Disable locking of on-disk metadata
      --disable-veracrypt                 Do not scan for VeraCrypt compatible
                                          device
      --dump-json-metadata                Dump info in JSON format (LUKS2 only)
      --dump-volume-key                   Dump volume key instead of keyslots
                                          info
      --encrypt                           Encrypt LUKS2 device (in-place
                                          encryption)
      --external-tokens-path=STRING       Path to directory with external
                                          token handlers (plugins).
      --force-password                    Disable password quality check (if
                                          enabled)
      --force-offline-reencrypt           Force offline LUKS2 reencryption and
                                          bypass active device detection
      --force-no-keyslots                 Force dangerous reencryption
                                          operation erasing all remaining
                                          keyslots
  -h, --hash=STRING                       The hash used to create the
                                          encryption key from the passphrase
      --header=STRING                     Device or file with separated LUKS
                                          header
      --header-backup-file=STRING         File with LUKS header and keyslots
                                          backup
      --hotzone-size=bytes                Maximal reencryption hotzone size
      --hw-opal                           Use HW OPAL encryption together with
                                          SW encryption
      --hw-opal-factory-reset             Wipe WHOLE OPAL disk on luksErase
      --hw-opal-only                      Use only HW OPAL encryption
      --init-only                         Initialize LUKS2 reencryption in
                                          metadata only
  -I, --integrity=STRING                  Data integrity algorithm (LUKS2 only)
      --integrity-inline                  Use inline mode (use HW integrity
                                          field)
      --integrity-key-size=BITS           The size of the data integrity key
      --integrity-legacy-padding          Use inefficient legacy padding (old
                                          kernels)
      --integrity-no-journal              Disable journal for integrity device
      --integrity-no-wipe                 Do not wipe device after format
  -i, --iter-time=msecs                   PBKDF iteration time for LUKS (in ms)
      --iv-large-sectors                  Use IV counted in sector size (not
                                          in 512 bytes)
      --json-file=STRING                  Read or write the json from or to a
                                          file
      --keep-key                          Do not change volume key
      --key-description=STRING            Keyring key description
  -d, --key-file=STRING                   Read the key from a file
  -s, --key-size=BITS                     The size of the encryption key
  -S, --key-slot=INT                      Slot number for new key (default is
                                          first free)
      --keyfile-offset=bytes              Number of bytes to skip in keyfile
  -l, --keyfile-size=bytes                Limits the read from keyfile
      --keyslot-cipher=STRING             LUKS2 keyslot: The cipher used for
                                          keyslot encryption
      --keyslot-key-size=BITS             LUKS2 keyslot: The size of the
                                          encryption key
      --label=STRING                      Set label for the LUKS2 device
      --link-vk-to-keyring=STRING         Set keyring where to link volume key
      --luks2-keyslots-size=bytes         LUKS2 header keyslots area size
      --luks2-metadata-size=bytes         LUKS2 header metadata area size
      --new-keyfile=STRING                Read the key for a new slot from a
                                          file
      --new-keyfile-offset=bytes          Number of bytes to skip in newly
                                          added keyfile
      --new-keyfile-size=bytes            Limits the read from newly added
                                          keyfile
      --new-key-description=STRING        Keyring new key description
      --new-key-size=BITS                 The size of the new encryption key
      --new-key-slot=INT                  Slot number for new key (default is
                                          first free)
      --new-token-id=INT                  Token number (default: any)
      --new-volume-key-file=STRING        Use the new volume key from file
      --new-volume-key-keyring=STRING     Use the specified keyring key as new
                                          volume key
  -o, --offset=SECTORS                    The start offset in the backend
                                          device
      --pbkdf=STRING                      PBKDF algorithm (for LUKS2):
                                          argon2i, argon2id, pbkdf2
      --pbkdf-force-iterations=LONG       PBKDF iterations cost (forced,
                                          disables benchmark)
      --pbkdf-memory=kilobytes            PBKDF memory cost limit
      --pbkdf-parallel=threads            PBKDF parallel cost
      --perf-high_priority                Set dm-crypt workqueues and the
                                          writer thread to high priority
      --perf-no_read_workqueue            Bypass dm-crypt workqueue and
                                          process read requests synchronously
      --perf-no_write_workqueue           Bypass dm-crypt workqueue and
                                          process write requests synchronously
      --perf-same_cpu_crypt               Use dm-crypt same_cpu_crypt
                                          performance compatibility option
      --perf-submit_from_crypt_cpus       Use dm-crypt submit_from_crypt_cpus
                                          performance compatibility option
      --persistent                        Set activation flags persistent for
                                          device
      --priority=STRING                   Keyslot priority: ignore, normal,
                                          prefer
      --progress-json                     Print progress data in json format
                                          (suitable for machine processing)
      --progress-frequency=secs           Progress line update (in seconds)
  -r, --readonly                          Create a readonly mapping
      --reduce-device-size=bytes          Reduce data device size (move data
                                          offset), DANGEROUS!
      --refresh                           Refresh (reactivate) device with new
                                          parameters
      --resilience=STRING                 Reencryption hotzone resilience type
                                          (checksum,journal,none)
      --resilience-hash=STRING            Reencryption hotzone checksums hash
      --resume-only                       Resume initialized LUKS2
                                          reencryption only
      --sector-size=INT                   Encryption sector size (default: 512
                                          bytes)
      --serialize-memory-hard-pbkdf       Use global lock to serialize memory
                                          hard PBKDF (OOM workaround)
      --shared                            Share device with another
                                          non-overlapping crypt segment
  -b, --size=SECTORS                      The size of the device
  -p, --skip=SECTORS                      How many sectors of the encrypted
                                          data to skip at the beginning
      --subsystem=STRING                  Set subsystem label for the LUKS2
                                          device
      --test-args                         Do not run action, just validate all
                                          command line parameters
      --test-passphrase                   Do not activate device, just check
                                          passphrase
  -t, --timeout=secs                      Timeout for interactive passphrase
                                          prompt (in seconds)
      --token-id=INT                      Token number (default: any)
      --token-only                        Do not ask for passphrase if
                                          activation by token fails
      --token-replace                     Replace the current token
      --token-type=STRING                 Restrict allowed token types used to
                                          retrieve LUKS2 key
      --tcrypt-backup                     Use backup (secondary) TCRYPT header
      --tcrypt-hidden                     Use hidden header (hidden TCRYPT
                                          device)
      --tcrypt-system                     Device is system TCRYPT drive (with
                                          bootloader)
  -T, --tries=INT                         How often the input of the
                                          passphrase can be retried
  -M, --type=STRING                       Type of device metadata: luks,
                                          luks1, luks2, plain, loopaes,
                                          tcrypt, bitlk
      --unbound                           Create or dump unbound LUKS2 keyslot
                                          (unassigned to data segment) or
                                          LUKS2 token (unassigned to keyslot)
      --use-random                        Use /dev/random for generating
                                          volume key
      --use-urandom                       Use /dev/urandom for generating
                                          volume key
      --uuid=STRING                       UUID for device to use
      --veracrypt                         Scan also for VeraCrypt compatible
                                          device
      --veracrypt-pim=INT                 Personal Iteration Multiplier for
                                          VeraCrypt compatible device
      --veracrypt-query-pim               Query Personal Iteration Multiplier
                                          for VeraCrypt compatible device
  -v, --verbose                           Shows more detailed error messages
  -y, --verify-passphrase                 Verifies the passphrase by asking
                                          for it twice
      --volume-key-file=STRING            Use the volume key from file
      --volume-key-keyring=STRING         Use the specified keyring key as a
                                          volume key
  -B, --block-size=MiB                    Reencryption block size
  -N, --new                               Create new header on not encrypted
                                          device
      --use-directio                      Use direct-io when accessing devices
      --use-fsync                         Use fsync after each block
      --write-log                         Update log file after every block
      --dump-master-key                   Alias for --dump-volume-key
      --master-key-file=STRING            Alias for --volume-key-file
<action> is one of:
	open <device> [--type <type>] [<name>] - open device as <name>
	close <name> - close device (remove mapping)
	resize <name> - resize active device
	status <name> - show device status
	benchmark [--cipher <cipher>] - benchmark cipher
	repair <device> - try to repair on-disk metadata
	reencrypt <device> - reencrypt LUKS2 device
	erase <device> - erase all keyslots (remove encryption key)
	convert <device> - convert LUKS from/to LUKS2 format
	config <device> - set permanent configuration options for LUKS2
	luksFormat <device> [<new key file>] - formats a LUKS device
	luksAddKey <device> [<new key file>] - add key to LUKS device
	luksRemoveKey <device> [<key file>] - removes supplied key or key file from LUKS device
	luksChangeKey <device> [<key file>] - changes supplied key or key file of LUKS device
	luksConvertKey <device> [<key file>] - converts a key to new pbkdf parameters
	luksKillSlot <device> <key slot> - wipes key with number <key slot> from LUKS device
	luksUUID <device> - print UUID of LUKS device
```

### `integritysetup`

> 官方示例调用：`integritysetup --help`

```text
root@kali:~# integritysetup --help
integritysetup 2.8.7 flags: UDEV BLKID KEYRING KERNEL_CAPI HW_OPAL
Usage: integritysetup [OPTION...] <action> <action-specific>
Help options:
  -?, --help                                  Show this help message
      --usage                                 Display brief usage
  -V, --version                               Print package version
      --allow-discards                        Allow discards (aka TRIM)
                                              requests for device
  -q, --batch-mode                            Do not ask for confirmation
      --buffer-sectors=SECTORS                Buffers size
      --bitmap-flush-time=ms                  Bitmap mode flush time
      --bitmap-sectors-per-bit=INT            Number of 512-byte sectors per
                                              bit (bitmap mode)
      --cancel-deferred                       Cancel a previously set deferred
                                              device removal
      --data-device=path                      Path to data device (if
                                              separated)
      --debug                                 Show debug messages
      --deferred                              Device removal is deferred until
                                              the last user closes it
      --device-size=bytes                     Use only specified device size
                                              (ignore rest of device),
                                              DANGEROUS!
      --disable-blkid                         Disable blkid on-disk signature
                                              detection and wiping
  -I, --integrity=STRING                      Data integrity algorithm
  -B, --integrity-bitmap-mode                 Use bitmap to track changes and
                                              disable journal for integrity
                                              device
      --integrity-inline                      Use inline integrity mode (HW
                                              sector tags)
      --integrity-key-file=STRING             Read the integrity key from a
                                              file
      --integrity-key-size=bytes              The size of the data integrity
                                              key
      --integrity-legacy-padding              Use inefficient legacy padding
                                              (old kernels)
      --integrity-legacy-hmac                 Do not protect superblock with
                                              HMAC (old kernels)
      --integrity-legacy-recalculate          Allow recalculating of volumes
                                              with HMAC keys (old kernels)
  -D, --integrity-no-journal                  Disable journal for integrity
                                              device
      --integrity-recalculate                 Recalculate initial tags
                                              automatically
      --integrity-recalculate-reset           Reset automatic recalculate
                                              position
  -R, --integrity-recovery-mode               Recovery mode (no journal, no
                                              tag checking)
      --interleave-sectors=SECTORS            Interleave sectors
      --journal-commit-time=ms                Journal commit time
      --journal-integrity=STRING              Journal integrity algorithm
      --journal-integrity-key-size=bytes      The size of the journal
                                              integrity key
      --journal-integrity-key-file=STRING     Read the journal integrity key
                                              from a file
      --journal-crypt=STRING                  Journal encryption algorithm
      --journal-crypt-key-file=STRING         Read the journal encryption key
                                              from a file
      --journal-crypt-key-size=bytes          The size of the journal
                                              encryption key
  -j, --journal-size=bytes                    Journal size
      --journal-watermark=percent             Journal watermark
      --no-wipe                               Do not wipe device after format
      --progress-frequency=secs               Progress line update (in seconds)
      --progress-json                         Print wipe progress data in json
                                              format (suitable for machine
                                              processing)
  -s, --sector-size=bytes                     Sector size
  -b, --size=SECTORS                          The size of the device
  -t, --tag-size=bytes                        Tag size (per-sector)
  -v, --verbose                               Shows more detailed error
                                              messages
      --wipe                                  Wipe the end of the device after
                                              resize
<action> is one of:
	format <integrity_device> - format device
	open <integrity_device> <name> - open device as <name>
	close <name> - close device (remove mapping)
	status <name> - show active device status
	dump <integrity_device> - show on-disk information
	resize <name> - resize active device
<name> is the device to create under /dev/mapper
<integrity_device> is the device containing data with integrity tags
Default compiled-in dm-integrity parameters:
	Checksum algorithm: crc32c
	Maximum keyfile size: 4kB
```

### `veritysetup`

> 官方示例调用：`veritysetup --help`

```text
root@kali:~# veritysetup --help
veritysetup 2.8.7 flags: UDEV BLKID KEYRING KERNEL_CAPI HW_OPAL
Usage: veritysetup [OPTION...] <action> <action-specific>
Help options:
  -?, --help                           Show this help message
      --usage                          Display brief usage
  -V, --version                        Print package version
      --cancel-deferred                Cancel a previously set deferred device
                                       removal
      --check-at-most-once             Verify data block only the first time
                                       it is read
      --data-block-size=bytes          Block size on the data device
      --data-blocks=blocks             The number of blocks in the data file
      --debug                          Show debug messages
      --deferred                       Device removal is deferred until the
                                       last user closes it
      --error-as-corruption            Handle IO error as corruption.
      --fec-device=path                Path to device with error correction
                                       data
      --fec-offset=bytes               Starting offset on the FEC device
      --fec-roots=bytes                FEC parity bytes
      --format=number                  Format type (1 - normal, 0 - original
                                       Chrome OS)
  -h, --hash=string                    Hash algorithm
      --hash-block-size=bytes          Block size on the hash device
      --hash-offset=bytes              Starting offset on the hash device
      --ignore-corruption              Ignore corruption, log it only
      --ignore-zero-blocks             Do not verify zeroed blocks
      --no-superblock                  Do not use verity superblock
      --panic-on-corruption            Panic kernel if corruption is detected
      --restart-on-corruption          Restart kernel if corruption is detected
      --root-hash-file=STRING          Path to root hash file
      --root-hash-signature=STRING     Path to root hash signature file
  -s, --salt=hex string                Salt
      --shared                         Share data device with another verity
                                       segment
      --use-tasklets                   Use kernel tasklets for performance
      --uuid=STRING                    UUID for device to use
  -v, --verbose                        Shows more detailed error messages
<action> is one of:
	format <data_device> <hash_device> - format device
	verify <data_device> <hash_device> [<root_hash>] - verify device
	open <data_device> <name> <hash_device> [<root_hash>] - open device as <name>
	close <name> - close device (remove mapping)
	status <name> - show active device status
	dump <hash_device> - show on-disk information
<name> is the device to create under /dev/mapper
<data_device> is the data device
<hash_device> is the device containing verification data
<root_hash> hash of the root node on <hash_device>
Default compiled-in dm-verity parameters:
	Hash: sha256, Data block (bytes): 4096, Hash block (bytes): 4096, Salt size: 32, Hash format: 1
```

### `cryptsetup-ssh`

> 官方示例调用：`cryptsetup-ssh --help`

```text
root@kali:~# cryptsetup-ssh --help
Usage: cryptsetup-ssh [OPTION...] <action> <device>
Experimental cryptsetup plugin for unlocking LUKS2 devices with token connected
to an SSH server
 Options for the 'add' action:
      --external-tokens-path=STRING
                             Path to directory containinig libcryptsetup
                             external tokens
      --key-slot=NUM         Keyslot to assign the token to. If not specified,
                             token will be assigned to the first keyslot
                             matching provided passphrase.
      --ssh-keypath=STRING   Path to the SSH key for connecting to the remote
                             server
      --ssh-path=STRING      Path to the key file on the remote server
      --ssh-server=STRING    IP address/URL of the remote server for this token
      --ssh-user=STRING      Username used for the remote server
 Generic options:
      --debug                Show debug messages
      --debug-json           Show debug messages including JSON metadata
  -v, --verbose              Shows more detailed error messages
  -?, --help                 Give this help list
      --usage                Give a short usage message
  -V, --version              Print program version
This plugin currently allows only adding a token to an existing key slot.
Specified SSH server must contain a key file on the specified path with a
passphrase for an existing key slot on the device.
Provided credentials will be used by cryptsetup to get the password when
opening the device using the token.
Note: The information provided when adding the token (SSH server address, user
and paths) will be stored in the LUKS2 header in plaintext.
```

## 4. 实践清单

按顺序做完这五步，就能把工具从「装上」推进到「会用」：

- [ ] **1.** **装好并确认版本** —— `sudo apt install cryptsetup`，再执行 `cryptsetup --version` 2>/dev/null || `cryptsetup -V`
- [ ] **2.** **读官方帮助** —— `cryptsetup -h`，需要细节时 `man cryptsetup`
- [ ] **3.** **在自有靶场跑最小用例** —— 官方给出的调用形式是：`Usage: /usr/sbin/cryptdisks_start [-r|--readonly] <name> [.. <name>]`
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/cryptsetup/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- 精讲教程：本工具暂无专篇，可在 [`../../tools/tutorials/`](../../tools/tutorials/) 中按分类查阅同类工具
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/cryptsetup/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/cryptsetup/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
