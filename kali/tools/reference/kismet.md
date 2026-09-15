# kismet

> Wireless network and device detector (metapackage) Kismet is a wireless network and device detector, sniffer, wardriving tool, and WIDS (wireless intrusion detection) framework. Kismet works with Wi-Fi interfaces, Bluetooth interfaces, som…

> **功能分类**：无线攻击 ｜ **Kali 包**：`kismet` ｜ **官方文档**：<https://www.kali.org/tools/kismet/>

## 1. 安装

```bash
sudo apt update
sudo apt install kismet
```

| 项目 | 内容 |
|------|------|
| 版本 | 2025.09.R1 |
| 架构 | any |
| 可执行命令 | `kismet`、`kismet-capture-antsdr-droneid`、`kismet_cap_antsdr_droneid`、`kismet-capture-bladerf-wiphy`、`kismet_cap_bladerf_wiphy`、`kismet-capture-common`、`kismet-capture-freaklabs-zigbee`、`kismet_cap_freaklabs_zigbee`、`kismet-capture-hak5-wifi-coconut`、`kismet_cap_hak5_wifi_coconut`、`kismet-capture-linux-bluetooth`、`kismet_cap_linux_bluetooth`、`kismet-capture-linux-wifi`、`kismet_cap_linux_wifi`、`kismet-capture-nrf-51822`、`kismet_cap_nrf_51822`、`kismet-capture-nrf-52840`、`kismet_cap_nrf_52840`、`kismet-capture-nrf-mousejack`、`kismet_cap_nrf_mousejack`、`kismet-capture-nxp-kw41z`、`kismet_cap_nxp_kw41z`、`kismet-capture-radiacode-usb`、`kismet_cap_radiacode_usb`、`kismet-capture-rtl433`、`kismet_cap_sdr_rtl433`、`kismet-capture-rtladsb`、`kismet_cap_sdr_rtladsb`、`kismet-capture-rz-killerbee`、`kismet_cap_rz_killerbee`、`kismet-capture-serial-radview`、`kismet_cap_serial_radview`、`kismet-capture-ti-cc-2531`、`kismet_cap_ti_cc_2531`、`kismet-capture-ti-cc-2540`、`kismet_cap_ti_cc_2540`、`kismet-capture-ubertooth-one`、`kismet_cap_ubertooth_one`、`kismet-core`、`kismet_cap_kismetdb`、`kismet_cap_pcapfile`、`kismet_server`、`kismet-logtools`、`kismetdb_clean`、`kismetdb_dump_devices`、`kismetdb_statistics`、`kismetdb_strip_packets`、`kismetdb_to_gpx`、`kismetdb_to_kml`、`kismetdb_to_pcap`、`kismetdb_to_wiglecsv`、`kismet-plugins`、`kismet_discovery`、`kismet_eventbus`、`kismet_proxytest`、`python3-kismetcapturefreaklabszigbee`、`python3-kismetcapturertl433`、`python3-kismetcapturertladsb` |
| 依赖 | `kismet-capture-antsdr-droneid`、`kismet-capture-freaklabs-zigbee`、`kismet-capture-hak5-wifi-coconut`、`kismet-capture-linux-bluetooth`、`kismet-capture-linux-wifi`、`kismet-capture-nrf-51822`、`kismet-capture-nrf-52840`、`kismet-capture-nrf-mousejack`、`kismet-capture-nxp-kw41z`、`kismet-capture-radiacode-usb`、`kismet-capture-rtl433`、`kismet-capture-rtladsb` 等 |
| 安装体积 | 23 KB |
| 官网 | <https://www.kismetwireless.net/> |
| 源码仓库 | <https://gitlab.com/kalilinux/packages/kismet> |
| 包追踪 | <https://pkg.kali.org/pkg/kismet> |

## 2. 官方用法示例

> 以下为 Kali 官方工具页给出的示例与输出原文。

```text
Usage Example
Start the Kismet server, using the wireless interface as the capture source (-c wlan0) and use the external GPSD option (–use-gpsd-gps):
```

## 3. 命令与参数（官方 help / man 原文）

本包提供 58 个可执行命令，下面是官方页面内嵌的帮助原文。

### `kismet_client`

官方给出的调用示例：`kismet_client -h`

```text
root@kali:~# kismet_client -h
Usage: kismet_client [OPTION]
 *** Generic Options ***
 -h, --help                   The obvious
kismet_drone
```

### `kismet_drone`

官方给出的调用示例：`kismet_drone -h`

```text
root@kali:~# kismet_drone -h
Usage: kismet_drone [OPTION]
Nearly all of these options are run-time overrides for values in the
kismet.conf configuration file.  Permanent changes should be made to
the configuration file.
 *** Generic Options ***
 -f, --config-file            Use alternate configuration file
     --no-line-wrap           Turn of linewrapping of output
                              (for grep, speed, etc)
 -s, --silent                 Turn off stdout output after setup phase
     --daemonize              Spawn detatched in the background
 *** Kismet Remote Drone Options ***
     --drone-listen           Override Kismet drone listen options
 *** Packet Capture Source Options ***
 -c, --capture-source         Specify a new packet capture source
                              (Identical syntax to the config file)
 -C, --enable-capture-sources Enable capture sources (comma-separated
                              list of names or interfaces)
kismet_server Usage Example
Start the Kismet server, using the wireless interface as the capture source (
-c wlan0
) and use the external GPSD option (
–use-gpsd-gps
):
```

### `kismet_server`

官方给出的调用示例：`kismet_server -c wlan0 --use-gpsd-gps`

```text
root@kali:~# kismet_server -c wlan0 --use-gpsd-gps
ERROR: Kismet was started as root, NOT launching external control binary.
       This is NOT the preferred method of starting Kismet as Kismet will
       continue to run as root the entire time.  Please read the README
       file section about Installation & Security and be sure this is what
       you want to do.
INFO: Reading from config file /etc/kismet/kismet.conf
INFO: No 'dronelisten' config line and no command line drone-listen
      argument given, Kismet drone server will not be enabled.
INFO: Created alert tracker...
INFO: Creating device tracker...
INFO: Registered 80211 PHY as id
```

### `kismet_cap_antsdr_droneid`

官方给出的调用示例：`kismet_cap_antsdr_droneid -h`

```text
root@kali:~# kismet_cap_antsdr_droneid -h
kismet_cap_antsdr_droneid is a capture driver for Kismet.  Typically it is started
automatically by the Kismet server.
kismet_cap_antsdr_droneid supports sending data to a remote Kismet server
usage: kismet_cap_antsdr_droneid [options]
 --connect [host]:[port]      Connect to remote Kismet server on [host] and [port]; by
                               default this now uses the new websockets interface built
                               into the Kismet webserver on port 2501; to connect using
                               the legacy remote capture protocol, specify the '--tcp'
                               option and the appropriate port, by default port 3501.
 --tcp                        Use the legacy TCP remote capture protocol, when combined
                               with the --connect option.  The modern protocol uses
                               websockets built into the Kismet server and does not
                               need this option.
 --ssl                        Use SSL to connect to a websocket-enabled Kismet server
 --ssl-certificate [certfile] Use SSL to connect to a websocket-enabled Kismet server
                               and use the provided certificate authority certificate
                               to validate the server.
 --user [username]            Kismet username for a websockets-based remote capture
                               source.  A username and password, or an API key, are
                               required for websockets mode.  A username and password
                               are ONLY used in websockets mode.
 --password [password]        Kismet password for a websockets-based remote capture source.
                               A username and password, or an API key, are required for
                               websocket mode.  A username and password are ONLY used in
                               websockets mode.
 --apikey [api key]           A Kismet API key for the 'datasource' role; this may be
                               supplied instead of a username and password for websockets
                               based remote capture.  An API key is ONLY used in websockets
                               mode.
 --endpoint [endpoint]        An alternate endpoint for the websockets connection.  By
                               default remote datasources are terminated at
                                 /datasource/remote/remotesource.ws
                               This should typically only be changed when using a HTTP proxy
                               homing the Kismet service under a directory.  Endpoints
                               should include the full path to the websocket endpoint, for
                               example:
                                 --endpoint=/kismet/proxy/datasource/remote/remotesource.ws
 --source [source def]        Specify a source to send to the remote
                              Kismet server; only used in conjunction with remote capture.
 --disable-retry              Do not attempt to reconnect to a remote server if there is an
                               error; exit immediately.  By default a remote capture will
                               attempt to reconnect indefinitely if the server is not
                               available.
 --fixed-gps [lat,lon,alt]    Set a fixed location for this capture (remote only),
                               accepts lat,lon,alt or lat,lon
 --gps-name [name]            Set an alternate GPS name for this source
 --daemonize                  Background the capture tool and enter daemon mode.
 --list                       List supported devices detected
 --autodetect [uuid:optional] Look for a Kismet server in announcement mode, optionally
                              waiting for a specific server UUID to be seen.  Requires
                              a Kismet server configured for announcement mode.
 --version                    Print version and exit.
```

### `kismet_cap_bladerf_wiphy`

官方给出的调用示例：`kismet_cap_bladerf_wiphy -h`

```text
root@kali:~# kismet_cap_bladerf_wiphy -h
kismet_cap_bladerf_wiphy is a capture driver for Kismet.  Typically it is started
automatically by the Kismet server.
kismet_cap_bladerf_wiphy supports sending data to a remote Kismet server
usage: kismet_cap_bladerf_wiphy [options]
 --connect [host]:[port]      Connect to remote Kismet server on [host] and [port]; by
                               default this now uses the new websockets interface built
                               into the Kismet webserver on port 2501; to connect using
                               the legacy remote capture protocol, specify the '--tcp'
                               option and the appropriate port, by default port 3501.
 --tcp                        Use the legacy TCP remote capture protocol, when combined
                               with the --connect option.  The modern protocol uses
                               websockets built into the Kismet server and does not
                               need this option.
 --ssl                        Use SSL to connect to a websocket-enabled Kismet server
 --ssl-certificate [certfile] Use SSL to connect to a websocket-enabled Kismet server
                               and use the provided certificate authority certificate
                               to validate the server.
 --user [username]            Kismet username for a websockets-based remote capture
                               source.  A username and password, or an API key, are
                               required for websockets mode.  A username and password
                               are ONLY used in websockets mode.
 --password [password]        Kismet password for a websockets-based remote capture source.
                               A username and password, or an API key, are required for
                               websocket mode.  A username and password are ONLY used in
                               websockets mode.
 --apikey [api key]           A Kismet API key for the 'datasource' role; this may be
                               supplied instead of a username and password for websockets
                               based remote capture.  An API key is ONLY used in websockets
                               mode.
 --endpoint [endpoint]        An alternate endpoint for the websockets connection.  By
                               default remote datasources are terminated at
                                 /datasource/remote/remotesource.ws
                               This should typically only be changed when using a HTTP proxy
                               homing the Kismet service under a directory.  Endpoints
                               should include the full path to the websocket endpoint, for
                               example:
                                 --endpoint=/kismet/proxy/datasource/remote/remotesource.ws
 --source [source def]        Specify a source to send to the remote
                              Kismet server; only used in conjunction with remote capture.
 --disable-retry              Do not attempt to reconnect to a remote server if there is an
                               error; exit immediately.  By default a remote capture will
                               attempt to reconnect indefinitely if the server is not
                               available.
 --fixed-gps [lat,lon,alt]    Set a fixed location for this capture (remote only),
                               accepts lat,lon,alt or lat,lon
 --gps-name [name]            Set an alternate GPS name for this source
 --daemonize                  Background the capture tool and enter daemon mode.
 --list                       List supported devices detected
 --autodetect [uuid:optional] Look for a Kismet server in announcement mode, optionally
                              waiting for a specific server UUID to be seen.  Requires
                              a Kismet server configured for announcement mode.
 --version                    Print version and exit.
```

### `kismet_cap_freaklabs_zigbee`

官方给出的调用示例：`kismet_cap_freaklabs_zigbee -h`

```text
root@kali:~# kismet_cap_freaklabs_zigbee -h
kismet_cap_freaklabs_zigbee is a capture driver for Kismet.  Typically it is started
automatically by the Kismet server.
kismet_cap_freaklabs_zigbee supports sending data to a remote Kismet server
usage: kismet_cap_freaklabs_zigbee [options]
 --connect [host]:[port]      Connect to remote Kismet server on [host] and [port]; by
                               default this now uses the new websockets interface built
                               into the Kismet webserver on port 2501; to connect using
                               the legacy remote capture protocol, specify the '--tcp'
                               option and the appropriate port, by default port 3501.
 --tcp                        Use the legacy TCP remote capture protocol, when combined
                               with the --connect option.  The modern protocol uses
                               websockets built into the Kismet server and does not
                               need this option.
 --ssl                        Use SSL to connect to a websocket-enabled Kismet server
 --ssl-certificate [certfile] Use SSL to connect to a websocket-enabled Kismet server
                               and use the provided certificate authority certificate
                               to validate the server.
 --user [username]            Kismet username for a websockets-based remote capture
                               source.  A username and password, or an API key, are
                               required for websockets mode.  A username and password
                               are ONLY used in websockets mode.
 --password [password]        Kismet password for a websockets-based remote capture source.
                               A username and password, or an API key, are required for
                               websocket mode.  A username and password are ONLY used in
                               websockets mode.
 --apikey [api key]           A Kismet API key for the 'datasource' role; this may be
                               supplied instead of a username and password for websockets
                               based remote capture.  An API key is ONLY used in websockets
                               mode.
 --endpoint [endpoint]        An alternate endpoint for the websockets connection.  By
                               default remote datasources are terminated at
                                 /datasource/remote/remotesource.ws
                               This should typically only be changed when using a HTTP proxy
                               homing the Kismet service under a directory.  Endpoints
                               should include the full path to the websocket endpoint, for
                               example:
                                 --endpoint=/kismet/proxy/datasource/remote/remotesource.ws
 --source [source def]        Specify a source to send to the remote
                              Kismet server; only used in conjunction with remote capture.
 --disable-retry              Do not attempt to reconnect to a remote server if there is an
                               error; exit immediately.  By default a remote capture will
                               attempt to reconnect indefinitely if the server is not
                               available.
 --fixed-gps [lat,lon,alt]    Set a fixed location for this capture (remote only),
                               accepts lat,lon,alt or lat,lon
 --gps-name [name]            Set an alternate GPS name for this source
 --daemonize                  Background the capture tool and enter daemon mode.
 --list                       List supported devices detected
 --autodetect [uuid:optional] Look for a Kismet server in announcement mode, optionally
                              waiting for a specific server UUID to be seen.  Requires
                              a Kismet server configured for announcement mode.
 --version                    Print version and exit.
```

### `kismet_cap_hak5_wifi_coconut`

官方给出的调用示例：`kismet_cap_hak5_wifi_coconut -h`

```text
root@kali:~# kismet_cap_hak5_wifi_coconut -h
kismet_cap_hak5_wifi_coconut is a capture driver for Kismet.  Typically it is started
automatically by the Kismet server.
kismet_cap_hak5_wifi_coconut supports sending data to a remote Kismet server
usage: kismet_cap_hak5_wifi_coconut [options]
 --connect [host]:[port]      Connect to remote Kismet server on [host] and [port]; by
                               default this now uses the new websockets interface built
                               into the Kismet webserver on port 2501; to connect using
                               the legacy remote capture protocol, specify the '--tcp'
                               option and the appropriate port, by default port 3501.
 --tcp                        Use the legacy TCP remote capture protocol, when combined
                               with the --connect option.  The modern protocol uses
                               websockets built into the Kismet server and does not
                               need this option.
 --ssl                        Use SSL to connect to a websocket-enabled Kismet server
 --ssl-certificate [certfile] Use SSL to connect to a websocket-enabled Kismet server
                               and use the provided certificate authority certificate
                               to validate the server.
 --user [username]            Kismet username for a websockets-based remote capture
                               source.  A username and password, or an API key, are
                               required for websockets mode.  A username and password
                               are ONLY used in websockets mode.
 --password [password]        Kismet password for a websockets-based remote capture source.
                               A username and password, or an API key, are required for
                               websocket mode.  A username and password are ONLY used in
                               websockets mode.
 --apikey [api key]           A Kismet API key for the 'datasource' role; this may be
                               supplied instead of a username and password for websockets
                               based remote capture.  An API key is ONLY used in websockets
                               mode.
 --endpoint [endpoint]        An alternate endpoint for the websockets connection.  By
                               default remote datasources are terminated at
                                 /datasource/remote/remotesource.ws
                               This should typically only be changed when using a HTTP proxy
                               homing the Kismet service under a directory.  Endpoints
                               should include the full path to the websocket endpoint, for
                               example:
                                 --endpoint=/kismet/proxy/datasource/remote/remotesource.ws
 --source [source def]        Specify a source to send to the remote
                              Kismet server; only used in conjunction with remote capture.
 --disable-retry              Do not attempt to reconnect to a remote server if there is an
                               error; exit immediately.  By default a remote capture will
                               attempt to reconnect indefinitely if the server is not
                               available.
 --fixed-gps [lat,lon,alt]    Set a fixed location for this capture (remote only),
                               accepts lat,lon,alt or lat,lon
 --gps-name [name]            Set an alternate GPS name for this source
 --daemonize                  Background the capture tool and enter daemon mode.
 --list                       List supported devices detected
 --autodetect [uuid:optional] Look for a Kismet server in announcement mode, optionally
                              waiting for a specific server UUID to be seen.  Requires
                              a Kismet server configured for announcement mode.
 --version                    Print version and exit.
```

### `kismet_cap_linux_bluetooth`

官方给出的调用示例：`kismet_cap_linux_bluetooth -h`

```text
root@kali:~# kismet_cap_linux_bluetooth -h
kismet_cap_linux_bluetooth is a capture driver for Kismet.  Typically it is started
automatically by the Kismet server.
kismet_cap_linux_bluetooth supports sending data to a remote Kismet server
usage: kismet_cap_linux_bluetooth [options]
 --connect [host]:[port]      Connect to remote Kismet server on [host] and [port]; by
                               default this now uses the new websockets interface built
                               into the Kismet webserver on port 2501; to connect using
                               the legacy remote capture protocol, specify the '--tcp'
                               option and the appropriate port, by default port 3501.
 --tcp                        Use the legacy TCP remote capture protocol, when combined
                               with the --connect option.  The modern protocol uses
                               websockets built into the Kismet server and does not
                               need this option.
 --ssl                        Use SSL to connect to a websocket-enabled Kismet server
 --ssl-certificate [certfile] Use SSL to connect to a websocket-enabled Kismet server
                               and use the provided certificate authority certificate
                               to validate the server.
 --user [username]            Kismet username for a websockets-based remote capture
                               source.  A username and password, or an API key, are
                               required for websockets mode.  A username and password
                               are ONLY used in websockets mode.
 --password [password]        Kismet password for a websockets-based remote capture source.
                               A username and password, or an API key, are required for
                               websocket mode.  A username and password are ONLY used in
                               websockets mode.
 --apikey [api key]           A Kismet API key for the 'datasource' role; this may be
                               supplied instead of a username and password for websockets
                               based remote capture.  An API key is ONLY used in websockets
                               mode.
 --endpoint [endpoint]        An alternate endpoint for the websockets connection.  By
                               default remote datasources are terminated at
                                 /datasource/remote/remotesource.ws
                               This should typically only be changed when using a HTTP proxy
                               homing the Kismet service under a directory.  Endpoints
                               should include the full path to the websocket endpoint, for
                               example:
                                 --endpoint=/kismet/proxy/datasource/remote/remotesource.ws
 --source [source def]        Specify a source to send to the remote
                              Kismet server; only used in conjunction with remote capture.
 --disable-retry              Do not attempt to reconnect to a remote server if there is an
                               error; exit immediately.  By default a remote capture will
                               attempt to reconnect indefinitely if the server is not
                               available.
 --fixed-gps [lat,lon,alt]    Set a fixed location for this capture (remote only),
                               accepts lat,lon,alt or lat,lon
 --gps-name [name]            Set an alternate GPS name for this source
 --daemonize                  Background the capture tool and enter daemon mode.
 --list                       List supported devices detected
 --autodetect [uuid:optional] Look for a Kismet server in announcement mode, optionally
                              waiting for a specific server UUID to be seen.  Requires
                              a Kismet server configured for announcement mode.
 --version                    Print version and exit.
```

### `kismet_cap_linux_wifi`

官方给出的调用示例：`kismet_cap_linux_wifi -h`

```text
root@kali:~# kismet_cap_linux_wifi -h
kismet_cap_linux_wifi is a capture driver for Kismet.  Typically it is started
automatically by the Kismet server.
kismet_cap_linux_wifi supports sending data to a remote Kismet server
usage: kismet_cap_linux_wifi [options]
 --connect [host]:[port]      Connect to remote Kismet server on [host] and [port]; by
                               default this now uses the new websockets interface built
                               into the Kismet webserver on port 2501; to connect using
                               the legacy remote capture protocol, specify the '--tcp'
                               option and the appropriate port, by default port 3501.
 --tcp                        Use the legacy TCP remote capture protocol, when combined
                               with the --connect option.  The modern protocol uses
                               websockets built into the Kismet server and does not
                               need this option.
 --ssl                        Use SSL to connect to a websocket-enabled Kismet server
 --ssl-certificate [certfile] Use SSL to connect to a websocket-enabled Kismet server
                               and use the provided certificate authority certificate
                               to validate the server.
 --user [username]            Kismet username for a websockets-based remote capture
                               source.  A username and password, or an API key, are
                               required for websockets mode.  A username and password
                               are ONLY used in websockets mode.
 --password [password]        Kismet password for a websockets-based remote capture source.
                               A username and password, or an API key, are required for
                               websocket mode.  A username and password are ONLY used in
                               websockets mode.
 --apikey [api key]           A Kismet API key for the 'datasource' role; this may be
                               supplied instead of a username and password for websockets
                               based remote capture.  An API key is ONLY used in websockets
                               mode.
 --endpoint [endpoint]        An alternate endpoint for the websockets connection.  By
                               default remote datasources are terminated at
                                 /datasource/remote/remotesource.ws
                               This should typically only be changed when using a HTTP proxy
                               homing the Kismet service under a directory.  Endpoints
                               should include the full path to the websocket endpoint, for
                               example:
                                 --endpoint=/kismet/proxy/datasource/remote/remotesource.ws
 --source [source def]        Specify a source to send to the remote
                              Kismet server; only used in conjunction with remote capture.
 --disable-retry              Do not attempt to reconnect to a remote server if there is an
                               error; exit immediately.  By default a remote capture will
                               attempt to reconnect indefinitely if the server is not
                               available.
 --fixed-gps [lat,lon,alt]    Set a fixed location for this capture (remote only),
                               accepts lat,lon,alt or lat,lon
 --gps-name [name]            Set an alternate GPS name for this source
 --daemonize                  Background the capture tool and enter daemon mode.
 --list                       List supported devices detected
 --autodetect [uuid:optional] Look for a Kismet server in announcement mode, optionally
                              waiting for a specific server UUID to be seen.  Requires
                              a Kismet server configured for announcement mode.
 --version                    Print version and exit.
```

### `kismet_cap_nrf_51822`

官方给出的调用示例：`kismet_cap_nrf_51822 -h`

```text
root@kali:~# kismet_cap_nrf_51822 -h
kismet_cap_nrf_51822 is a capture driver for Kismet.  Typically it is started
automatically by the Kismet server.
kismet_cap_nrf_51822 supports sending data to a remote Kismet server
usage: kismet_cap_nrf_51822 [options]
 --connect [host]:[port]      Connect to remote Kismet server on [host] and [port]; by
                               default this now uses the new websockets interface built
                               into the Kismet webserver on port 2501; to connect using
                               the legacy remote capture protocol, specify the '--tcp'
                               option and the appropriate port, by default port 3501.
 --tcp                        Use the legacy TCP remote capture protocol, when combined
                               with the --connect option.  The modern protocol uses
                               websockets built into the Kismet server and does not
                               need this option.
 --ssl                        Use SSL to connect to a websocket-enabled Kismet server
 --ssl-certificate [certfile] Use SSL to connect to a websocket-enabled Kismet server
                               and use the provided certificate authority certificate
                               to validate the server.
 --user [username]            Kismet username for a websockets-based remote capture
                               source.  A username and password, or an API key, are
                               required for websockets mode.  A username and password
                               are ONLY used in websockets mode.
 --password [password]        Kismet password for a websockets-based remote capture source.
                               A username and password, or an API key, are required for
                               websocket mode.  A username and password are ONLY used in
                               websockets mode.
 --apikey [api key]           A Kismet API key for the 'datasource' role; this may be
                               supplied instead of a username and password for websockets
                               based remote capture.  An API key is ONLY used in websockets
                               mode.
 --endpoint [endpoint]        An alternate endpoint for the websockets connection.  By
                               default remote datasources are terminated at
                                 /datasource/remote/remotesource.ws
                               This should typically only be changed when using a HTTP proxy
                               homing the Kismet service under a directory.  Endpoints
                               should include the full path to the websocket endpoint, for
                               example:
                                 --endpoint=/kismet/proxy/datasource/remote/remotesource.ws
 --source [source def]        Specify a source to send to the remote
                              Kismet server; only used in conjunction with remote capture.
 --disable-retry              Do not attempt to reconnect to a remote server if there is an
                               error; exit immediately.  By default a remote capture will
                               attempt to reconnect indefinitely if the server is not
                               available.
 --fixed-gps [lat,lon,alt]    Set a fixed location for this capture (remote only),
                               accepts lat,lon,alt or lat,lon
 --gps-name [name]            Set an alternate GPS name for this source
 --daemonize                  Background the capture tool and enter daemon mode.
 --list                       List supported devices detected
 --autodetect [uuid:optional] Look for a Kismet server in announcement mode, optionally
                              waiting for a specific server UUID to be seen.  Requires
                              a Kismet server configured for announcement mode.
 --version                    Print version and exit.
```

## 4. 实践清单

按顺序做完这五步，就能把工具从「装上」推进到「会用」：

- [ ] **1.** **装好并确认版本** —— `sudo apt install kismet`，再执行 `kismet --version` 2>/dev/null || `kismet -V`
- [ ] **2.** **读官方帮助** —— `kismet -h`，需要细节时 `man kismet`
- [ ] **3.** **在自有靶场跑最小用例** —— 官方给出的调用形式是：`Usage: kismet_client [OPTION]`
- [ ] **4.** **对照官方文档确认参数语义** —— <https://www.kali.org/tools/kismet/>，重点核对上一步用到的每个参数
- [ ] **5.** **记录输出并解读** —— 把关键字段抄进笔记，写清「它说明什么」「下一步该做什么」

> ⚠️ 只在**自己的设备**或**获得书面授权**的目标上使用。未授权扫描/入侵在多数司法辖区构成违法。
> 靶场搭建见 [`../../labs/README.md`](../../labs/README.md)。

## 5. 相关

- **精讲教程**（含原理、参数详解、靶场实操与输出解读）：[kismet](../../tools/tutorials/05-无线攻击/kismet.md)
- 按攻击阶段浏览同类工具：[`../../tools/by-attack/reconnaissance.md`](../../tools/by-attack/reconnaissance.md)
- 按包速查：[`../catalog/`](../catalog/) ｜ 全量清单：[`../catalog/all-tools.md`](../catalog/all-tools.md)
- Kali 官方工具页：<https://www.kali.org/tools/kismet/>

---

## 来源

- 工具元数据与用法示例、help 原文均抓取自 <https://www.kali.org/tools/kismet/>（同步日期：2026-09-15）
- 抓取与生成脚本：`scripts/fetch_kali_tools.py` · `scripts/fetch_kali_usage.py` · `scripts/gen_kali_reference.py`
