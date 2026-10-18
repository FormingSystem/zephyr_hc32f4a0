---
id: learning.zephyr-docs.bluetooth.page-42
title: 消息访问配置文件MAP_Shell
kind: reference
status: maintained
domains: [zephyr, bluetooth, documentation]
source_url: https://docs.zephyrproject.org/latest/services/connectivity/bluetooth/shell/classic/map.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="bluetooth-map-shell"></a>

# 第42章\_消息访问配置文件MAP\_Shell

原文：[官方页面](https://docs.zephyrproject.org/latest/services/connectivity/bluetooth/shell/classic/map.html)。读取日期：2026-10-14；保存的 latest 页面及 HTML 摘要见[来源记录](../SOURCES.md)。

> 译注——使用前提：以下命令在启用了对应蓝牙功能的目标固件Zephyr Shell中执行，初始化与接入方式见[蓝牙Shell](P007_蓝牙Shell.md)。代码中的 `uart:~$` 是提示符，其后输出是原文预期结果；输入命令时不复制提示符和日志。若命令不可用或初始化失败，应先检查目标配置、控制器能力及当前版本帮助，再继续连接或传输步骤。本批仅翻译与核对文档，未连接设备或执行这些命令。

> 译注——角色与术语：MCE 是消息客户端设备（Message Client Equipment），MSE 是消息服务端设备（Message Server Equipment）；MAS 是消息访问服务端（Message Access Server），MNS 是消息通知服务端（Message Notification Server）。消息访问由 MCE 向 MSE 发起；通知方向相反，由 MSE 向 MCE 的 MNS 发起。下面每组日志标出设备角色，不能仅凭设备名称推断其在每条连接中的客户端／服务端角色。SDP 为服务发现协议（Service Discovery Protocol），ACL 为异步面向连接链路，L2CAP 为逻辑链路控制与适配协议，RFCOMM 为串口仿真协议。SRM 是单响应模式（Single Response Mode），SRMP 是单响应模式参数（Single Response Mode Parameter）。`/`、`telecom` 等是协议中的对象目录，不是读者机器上的仓库路径。

本文说明如何运行经典蓝牙（Bluetooth Classic）的消息访问配置文件（Message Access Profile，MAP）Shell 功能。`map` 命令提供经典蓝牙 MAP Shell 命令。

<a id="commands"></a>

## 42.1 命令（Commands）

<a id="main-commands"></a>

### 42.1.1 主命令（Main Commands）

`map` 命令如下：

```text
uart:~$ map
map - Bluetooth MAP shell commands
Subcommands:
  add_header  : Adding header sets
  mce         : MCE commands
  mse         : MSE commands
```

<a id="mce-commands"></a>

### 42.1.2 MCE 命令（MCE Commands）

`map mce` 命令如下：

```text
uart:~$ map mce
mce - MCE commands
Subcommands:
  mas  : MCE MAS commands
  mns  : MCE MNS commands
```

<a id="mce-mas-commands"></a>

#### 42.1.2.1 MCE 的 MAS 命令（MCE MAS Commands）

`map mce mas` 命令如下：

```text
uart:~$ map mce mas
mas - MCE MAS commands
Subcommands:
  discover            : [none]
  select              : <instance_id>
  rfcomm_connect      : <channel> <instance_id> [supported_features]
  rfcomm_disconnect   : [none]
  l2cap_connect       : <psm> <instance_id> [supported_features]
  l2cap_disconnect    : [none]
  connect             : [none]
  disconnect          : [none]
  abort               : [none]
  set_folder          : <path: "/" | ".." | "../folder" | "folder">
  set_ntf_reg         : [none]
  get_folder_listing  : [srmp]
  get_msg_listing     : [name <folder_name>] [srmp]
  get_msg             : <msg_handle> [srmp]
  set_msg_status      : <msg_handle>
  push_msg            : [folder_name]
  update_inbox        : [none]
  get_mas_inst_info   : [srmp]
  set_owner_status    : [none]
  get_owner_status    : [srmp]
  get_convo_listing   : [srmp]
  set_ntf_filter      : [none]
```

<a id="mce-mns-commands"></a>

#### 42.1.2.2 MCE 的 MNS 命令（MCE MNS Commands）

`map mce mns` 命令如下：

```text
uart:~$ map mce mns
mns - MCE MNS commands
Subcommands:
  register           : [none]
  rfcomm_register    : [none]
  rfcomm_disconnect  : [none]
  l2cap_register     : [none]
  l2cap_disconnect   : [none]
  connect            : <rsp: success, error> [rsp_code]
  disconnect         : <rsp: success, error> [rsp_code]
  abort              : <rsp: success, error> [rsp_code]
  send_event         : <rsp: noerror, error> [rsp_code] [srmp]
```

<a id="mse-commands"></a>

### 42.1.3 MSE 命令（MSE Commands）

`map mse` 命令如下：

```text
uart:~$ map mse
mse - MSE commands
Subcommands:
  mas  : MSE MAS commands
  mns  : MSE MNS commands
```

<a id="mse-mas-commands"></a>

#### 42.1.3.1 MSE 的 MAS 命令（MSE MAS Commands）

`map mse mas` 命令如下：

```text
uart:~$ map mse mas
mas - MSE MAS commands
Subcommands:
  select              : <instance_id>
  register            : [none]
  rfcomm_register     : [none]
  rfcomm_disconnect   : [none]
  l2cap_register      : [none]
  l2cap_disconnect    : [none]
  connect             : <rsp: success, error> [rsp_code]
  disconnect          : <rsp: success, error> [rsp_code]
  abort               : <rsp: success, error> [rsp_code]
  set_folder          : <rsp: success, error> [rsp_code]
  set_ntf_reg         : <rsp: noerror, error> [rsp_code]
  get_folder_listing  : <rsp: noerror, error> [rsp_code] [srmp]
  get_msg_listing     : <rsp: noerror, error> [rsp_code] [srmp]
  get_msg             : <rsp: noerror, error> [rsp_code] [srmp]
  set_msg_status      : <rsp: noerror, error> [rsp_code]
  push_msg            : <rsp: noerror, error> [rsp_code] [srmp]
  update_inbox        : <rsp: noerror, error> [rsp_code]
  get_mas_inst_info   : <rsp: noerror, error> [rsp_code] [srmp]
  set_owner_status    : <rsp: noerror, error> [rsp_code]
  get_owner_status    : <rsp: noerror, error> [rsp_code] [srmp]
  get_convo_listing   : <rsp: noerror, error> [rsp_code] [srmp]
  set_ntf_filter      : <rsp: noerror, error> [rsp_code]
```

<a id="mse-mns-commands"></a>

#### 42.1.3.2 MSE 的 MNS 命令（MSE MNS Commands）

`map mse mns` 命令如下：

```text
uart:~$ map mse mns
mns - MSE MNS commands
Subcommands:
  discover            : [none]
  rfcomm_connect      : <channel> [supported_features]
  rfcomm_disconnect   : [none]
  l2cap_connect       : <psm> [supported_features]
  l2cap_disconnect    : [none]
  connect             : [none]
  disconnect          : [none]
  abort               : [none]
  send_event          : [none]
```

<a id="application-parameter-commands"></a>

### 42.1.4 应用参数命令（Application Parameter Commands）

`map add_header app_param` 命令如下：

```text
uart:~$ map add_header app_param
app_param - Application parameter commands
Subcommands:
  list                          : List all added application parameters
  clear                         : Clear all application parameters
  max_list_count                : <count: 0-65535>
  list_start_offset             : <offset: 0-65535>
  filter_msg_type               : <type_mask: hex>
  filter_period_begin           : <time: YYYYMMDDTHHMMSS[+/-HHMM]>
  filter_period_end             : <time: YYYYMMDDTHHMMSS[+/-HHMM]>
  filter_read_status            : <no_filter/unread/read>
  filter_recipient              : <recipient_address>
  filter_originator             : <originator_address>
  filter_priority               : <no_filter/high/non_high>
  attachment                    : <on/off>
  transparent                   : <on/off>
  retry                         : <on/off>
  new_message                   : <on/off>
  notification_status           : <on/off>
  mas_instance_id               : <id: 0-255>
  parameter_mask                : <mask: hex>
  folder_listing_size           : <size: 0-65535>
  listing_size                  : <size: 0-65535>
  subject_length                : <length: 0-255>
  charset                       : <native/utf8>
  fraction_request              : <first/next>
  fraction_deliver              : <more/last>
  status_indicator              : <read/deleted/extended>
  status_value                  : <yes/no>
  mse_time                      : <time: YYYYMMDDTHHMMSS[+/-HHMM]>
  database_id                   : <id_string: max 32 chars>
  convo_listing_ver             : <version_string: max 32 chars>
  presence_availability         : <unknown/offline/online/away/dnd/busy/meeting>
  presence_text                 : <text>
  last_activity                 : <time: YYYYMMDDTHHMMSS[+/-HHMM]>
  filter_last_activity_begin    : <time: YYYYMMDDTHHMMSS[+/-HHMM]>
  filter_last_activity_end      : <time: YYYYMMDDTHHMMSS[+/-HHMM]>
  chat_state                    : <unknown/inactive/active/composing/paused/gone>
  conversation_id               : <id_string: max 32 chars>
  folder_ver                    : <version_string: max 32 chars>
  filter_msg_handle             : <handle_string: max 16 chars>
  notification_filter_mask      : <mask: hex>
  convo_parameter_mask          : <mask: hex>
  owner_uci                     : <uci_string>
  extended_data                 : <data_string>
  map_supported_features        : [none]
  message_handle                : <handle_string: max 16 chars>
  modify_text                   : <prepend/replace>
```

<a id="usage-examples"></a>

## 42.2 使用示例（Usage Examples）

<a id="sdp-discovery"></a>

### 42.2.1 SDP 服务发现（SDP Discovery）

<a id="mce-discover-mse"></a>

#### 42.2.1.1 MCE 发现 MSE（MCE Discover MSE）

MCE 可以发现远端设备上的 MSE 服务：

```text
uart:~$ map mce mas discover
Found RFCOMM channel 0x06
Found GOEP L2CAP PSM 0x1003
Found MAP profile version 0x0104
Found MAP features 0x007fffff
Found service name: MAP MAS 0
Found MAP instance ID 0
Found MAP MSG type 0x1f
uart:~$
```

<a id="mse-discover-mce"></a>

#### 42.2.1.2 MSE 发现 MCE（MSE Discover MCE）

MSE 可以发现远端设备上的 MCE 服务：

```text
uart:~$ map mse mns discover
Found RFCOMM channel 0x06
Found GOEP L2CAP PSM 0x1003
Found MAP profile version 0x0104
Found MAP features 0x0077ffff
Found service name: MAP MNS
uart:~$
```

<a id="connect-map-transport"></a>

### 42.2.2 连接 MAP 传输层（Connect MAP Transport）

创建 MAP 传输连接前，应先建立 ACL 连接。

<a id="mas-transport-connection"></a>

#### 42.2.2.1 MAS 传输连接（MAS Transport Connection）

<a id="rfcomm-transport"></a>

##### 42.2.2.1.1 RFCOMM 传输（RFCOMM Transport）

**消息客户端设备 MCE（MCE）**

<a id="tab-0-TUNF"></a>
<a id="panel-0-TUNF"></a>

```text
uart:~$ map mce mas rfcomm_connect 6 0 7fffff
Security changed: XX:XX:XX:XX:XX:XX level 2
MCE MAS RFCOMM connected: 0x20005a00, addr: XX:XX:XX:XX:XX:XX, instance_id: 0
Selected MCE MAS instance_id 0 as default
uart:~$
```

**消息服务端设备 MSE（MSE）**

<a id="tab-0-TVNF"></a>
<a id="panel-0-TVNF"></a>

```text
uart:~$ map mse mas register
MSE MAS server(s) registered
uart:~$ map mse mas rfcomm_register
RFCOMM server (channel 06, mas_instance_id 0, map_supported_features 007fffff) is registered
MSE MAS SDP record 0 registered
RFCOMM server (channel 07, mas_instance_id 1, map_supported_features 007fffff) is registered
MSE MAS SDP record 1 registered
Security changed: XX:XX:XX:XX:XX:XX level 2
MSE MAS RFCOMM connected: 0x20005c00, addr: XX:XX:XX:XX:XX:XX, instance_id: 0
Selected MSE MAS instance_id 0 as default
uart:~$
```

<a id="l2cap-transport"></a>

##### 42.2.2.1.2 L2CAP 传输（L2CAP Transport）

**消息客户端设备 MCE（MCE）**

<a id="tab-1-TUNF"></a>
<a id="panel-1-TUNF"></a>

```text
uart:~$ map mce mas l2cap_connect 1003 0 7fffff
Security changed: XX:XX:XX:XX:XX:XX level 2
MCE MAS L2CAP connected: 0x20005a00, addr: XX:XX:XX:XX:XX:XX, instance_id: 0
Selected MCE MAS instance_id 0 as default
uart:~$
```

**消息服务端设备 MSE（MSE）**

<a id="tab-1-TVNF"></a>
<a id="panel-1-TVNF"></a>

```text
uart:~$ map mse mas register
MSE MAS server(s) registered
uart:~$ map mse mas l2cap_register
L2CAP server (psm 1003, mas_instance_id 0, map_supported_features 007fffff) is registered
MSE MAS SDP record 0 registered
L2CAP server (psm 1005, mas_instance_id 1, map_supported_features 007fffff) is registered
MSE MAS SDP record 1 registered
Security changed: XX:XX:XX:XX:XX:XX level 2
MSE MAS L2CAP connected: 0x20005c00, addr: XX:XX:XX:XX:XX:XX, instance_id: 0
Selected MSE MAS instance_id 0 as default
uart:~$
```

<a id="mns-transport-connection"></a>

#### 42.2.2.2 MNS 传输连接（MNS Transport Connection）

<a id="id1"></a>

##### 42.2.2.2.1 RFCOMM 传输（RFCOMM Transport）

**消息客户端设备 MCE（MCE）**

<a id="tab-2-TUNF"></a>
<a id="panel-2-TUNF"></a>

```text
uart:~$ map mce mns register
MCE MNS server(s) registered
uart:~$ map mce mns rfcomm_register
RFCOMM server (channel 06, map_supported_features 0077ffff) is registered
MCE MNS SDP record registered
MCE MNS RFCOMM connected: 0x20005b00, addr: XX:XX:XX:XX:XX:XX
uart:~$
```

**消息服务端设备 MSE（MSE）**

<a id="tab-2-TVNF"></a>
<a id="panel-2-TVNF"></a>

```text
uart:~$ map mse mns rfcomm_connect 6 77ffff
MSE MNS RFCOMM connected: 0x20005d00, addr: XX:XX:XX:XX:XX:XX
uart:~$
```

<a id="id2"></a>

##### 42.2.2.2.2 L2CAP 传输（L2CAP Transport）

**消息客户端设备 MCE（MCE）**

<a id="tab-3-TUNF"></a>
<a id="panel-3-TUNF"></a>

```text
uart:~$ map mce mns register
MCE MNS server(s) registered
uart:~$ map mce mns l2cap_register
L2CAP server (psm 1003, map_supported_features 0077ffff) is registered
MCE MNS SDP record registered
MCE MNS L2CAP connected: 0x20005b00, addr: XX:XX:XX:XX:XX:XX
uart:~$
```

**消息服务端设备 MSE（MSE）**

<a id="tab-3-TVNF"></a>
<a id="panel-3-TVNF"></a>

```text
uart:~$ map mse mns l2cap_connect 1003 77ffff
MSE MNS L2CAP connected: 0x20005d00, addr: XX:XX:XX:XX:XX:XX
uart:~$
```

<a id="disconnect-map-transport"></a>

### 42.2.3 断开 MAP 传输层（Disconnect MAP Transport）

<a id="mas-transport-disconnection"></a>

#### 42.2.3.1 断开 MAS 传输连接（MAS Transport Disconnection）

<a id="rfcomm-transport-mce-initiates"></a>

##### 42.2.3.1.1 RFCOMM 传输：MCE 发起（RFCOMM Transport (MCE initiates)）

**消息客户端设备 MCE（MCE）**

<a id="tab-4-TUNF"></a>
<a id="panel-4-TUNF"></a>

```text
uart:~$ map mce mas rfcomm_disconnect
MCE MAS RFCOMM disconnected: 0x20005a00
No connected MCE MAS instance available for conn XX:XX:XX:XX:XX:XX
uart:~$
```

**消息服务端设备 MSE（MSE）**

<a id="tab-4-TVNF"></a>
<a id="panel-4-TVNF"></a>

```text
MSE MAS RFCOMM disconnected: 0x20005c00
No connected MSE MAS instance available for conn XX:XX:XX:XX:XX:XX
uart:~$
```

<a id="rfcomm-transport-mse-initiates"></a>

##### 42.2.3.1.2 RFCOMM 传输：MSE 发起（RFCOMM Transport (MSE initiates)）

**消息客户端设备 MCE（MCE）**

<a id="tab-5-TUNF"></a>
<a id="panel-5-TUNF"></a>

```text
MCE MAS RFCOMM disconnected: 0x20005a00
No connected MCE MAS instance available for conn XX:XX:XX:XX:XX:XX
uart:~$
```

**消息服务端设备 MSE（MSE）**

<a id="tab-5-TVNF"></a>
<a id="panel-5-TVNF"></a>

```text
uart:~$ map mse mas rfcomm_disconnect
MSE MAS RFCOMM disconnected: 0x20005c00
No connected MSE MAS instance available for conn XX:XX:XX:XX:XX:XX
uart:~$
```

<a id="l2cap-transport-mce-initiates"></a>

##### 42.2.3.1.3 L2CAP 传输：MCE 发起（L2CAP Transport (MCE initiates)）

**消息客户端设备 MCE（MCE）**

<a id="tab-6-TUNF"></a>
<a id="panel-6-TUNF"></a>

```text
uart:~$ map mce mas l2cap_disconnect
MCE MAS L2CAP disconnected: 0x20005a00
No connected MCE MAS instance available for conn XX:XX:XX:XX:XX:XX
uart:~$
```

**消息服务端设备 MSE（MSE）**

<a id="tab-6-TVNF"></a>
<a id="panel-6-TVNF"></a>

```text
MSE MAS L2CAP disconnected: 0x20005c00
No connected MSE MAS instance available for conn XX:XX:XX:XX:XX:XX
uart:~$
```

<a id="l2cap-transport-mse-initiates"></a>

##### 42.2.3.1.4 L2CAP 传输：MSE 发起（L2CAP Transport (MSE initiates)）

**消息客户端设备 MCE（MCE）**

<a id="tab-7-TUNF"></a>
<a id="panel-7-TUNF"></a>

```text
MCE MAS L2CAP disconnected: 0x20005a00
No connected MCE MAS instance available for conn XX:XX:XX:XX:XX:XX
uart:~$
```

**消息服务端设备 MSE（MSE）**

<a id="tab-7-TVNF"></a>
<a id="panel-7-TVNF"></a>

```text
uart:~$ map mse mas l2cap_disconnect
MSE MAS L2CAP disconnected: 0x20005c00
No connected MSE MAS instance available for conn XX:XX:XX:XX:XX:XX
uart:~$
```

<a id="mns-transport-disconnection"></a>

#### 42.2.3.2 断开 MNS 传输连接（MNS Transport Disconnection）

<a id="id3"></a>

##### 42.2.3.2.1 RFCOMM 传输：MSE 发起（RFCOMM Transport (MSE initiates)）

**消息客户端设备 MCE（MCE）**

<a id="tab-8-TUNF"></a>
<a id="panel-8-TUNF"></a>

```text
MCE MNS RFCOMM disconnected: 0x20005b00
uart:~$
```

**消息服务端设备 MSE（MSE）**

<a id="tab-8-TVNF"></a>
<a id="panel-8-TVNF"></a>

```text
uart:~$ map mse mns rfcomm_disconnect
MSE MNS RFCOMM disconnected: 0x20005d00
uart:~$
```

<a id="id4"></a>

##### 42.2.3.2.2 RFCOMM 传输：MCE 发起（RFCOMM Transport (MCE initiates)）

**消息客户端设备 MCE（MCE）**

<a id="tab-9-TUNF"></a>
<a id="panel-9-TUNF"></a>

```text
uart:~$ map mce mns rfcomm_disconnect
MCE MNS RFCOMM disconnected: 0x20005b00
uart:~$
```

**消息服务端设备 MSE（MSE）**

<a id="tab-9-TVNF"></a>
<a id="panel-9-TVNF"></a>

```text
MSE MNS RFCOMM disconnected: 0x20005d00
uart:~$
```

<a id="id5"></a>

##### 42.2.3.2.3 L2CAP 传输：MSE 发起（L2CAP Transport (MSE initiates)）

**消息客户端设备 MCE（MCE）**

<a id="tab-10-TUNF"></a>
<a id="panel-10-TUNF"></a>

```text
MCE MNS L2CAP disconnected: 0x20005b00
uart:~$
```

**消息服务端设备 MSE（MSE）**

<a id="tab-10-TVNF"></a>
<a id="panel-10-TVNF"></a>

```text
uart:~$ map mse mns l2cap_disconnect
MSE MNS L2CAP disconnected: 0x20005d00
uart:~$
```

<a id="id6"></a>

##### 42.2.3.2.4 L2CAP 传输：MCE 发起（L2CAP Transport (MCE initiates)）

**消息客户端设备 MCE（MCE）**

<a id="tab-11-TUNF"></a>
<a id="panel-11-TUNF"></a>

```text
uart:~$ map mce mns l2cap_disconnect
MCE MNS L2CAP disconnected: 0x20005b00
uart:~$
```

**消息服务端设备 MSE（MSE）**

<a id="tab-11-TVNF"></a>
<a id="panel-11-TVNF"></a>

```text
MSE MNS L2CAP disconnected: 0x20005d00
uart:~$
```

<a id="connect-to-map-server"></a>

### 42.2.4 连接 MAP 服务端（Connect to MAP Server）

<a id="mce-mas-connect-to-mse-mas"></a>

#### 42.2.4.1 MCE MAS 连接 MSE MAS（MCE MAS Connect to MSE MAS）

**消息客户端设备 MCE（MCE）**

<a id="tab-12-TUNF"></a>
<a id="panel-12-TUNF"></a>

```text
uart:~$ map mce mas connect
MCE MAS 0x20005a00 conn rsp, rsp_code Success, version 10, mopl 0fff
HI 4a Len 16
00000000: bb 58 2b 40 42 0c 11 db  b0 de 08 00 20 0c 9a 66 |.X+@B... .... ..f|
HI cb Len 4
Conn ID: 00000001
uart:~$
```

**消息服务端设备 MSE（MSE）**

<a id="tab-12-TVNF"></a>
<a id="panel-12-TVNF"></a>

```text
MSE MAS 0x20005c00 conn req, version 10, mopl 0fff
HI 46 Len 16
00000000: bb 58 2b 40 42 0c 11 db  b0 de 08 00 20 0c 9a 66 |.X+@B... .... ..f|
HI 4c Len 6
T 29 L 4
00000000: 00 77 ff ff                                      |.w..             |
uart:~$ map mse mas connect success
uart:~$
```

<a id="mse-mns-connect-to-mce-mns"></a>

#### 42.2.4.2 MSE MNS 连接 MCE MNS（MSE MNS Connect to MCE MNS）

**消息服务端设备 MSE（MSE）**

<a id="tab-13-TVNF"></a>
<a id="panel-13-TVNF"></a>

```text
uart:~$ map mse mns connect
MSE MNS 0x20005d00 conn rsp, rsp_code Success, version 10, mopl 0fff
HI 4a Len 16
00000000: bb 58 2b 41 42 0c 11 db  b0 de 08 00 20 0c 9a 66 |.X+AB... .... ..f|
HI cb Len 4
Conn ID: 00000001
uart:~$
```

**消息客户端设备 MCE（MCE）**

<a id="tab-13-TUNF"></a>
<a id="panel-13-TUNF"></a>

```text
MCE MNS 0x20005b00 conn req, version 10, mopl 0fff
HI 46 Len 16
00000000: bb 58 2b 41 42 0c 11 db  b0 de 08 00  20 0c 9a 66 |.X+AB... .... ..f|
uart:~$ map mce mns connect success
uart:~$
```

<a id="disconnect-from-map-server"></a>

### 42.2.5 断开与 MAP 服务端的连接（Disconnect from MAP Server）

<a id="mce-mas-disconnect-from-mse-mas"></a>

#### 42.2.5.1 MCE MAS 断开与 MSE MAS 的连接（MCE MAS Disconnect from MSE MAS）

**消息客户端设备 MCE（MCE）**

<a id="tab-14-TUNF"></a>
<a id="panel-14-TUNF"></a>

```text
uart:~$ map mce mas disconnect
MCE MAS 0x20005a00 disconn rsp, rsp_code Success
uart:~$
```

**消息服务端设备 MSE（MSE）**

<a id="tab-14-TVNF"></a>
<a id="panel-14-TVNF"></a>

```text
MSE MAS 0x20005c00 disconn req
HI c0 Len 4
Conn ID: 00000001
uart:~$ map mse mas disconnect success
uart:~$
```

<a id="mse-mns-disconnect-from-mce-mns"></a>

#### 42.2.5.2 MSE MNS 断开与 MCE MNS 的连接（MSE MNS Disconnect from MCE MNS）

**消息服务端设备 MSE（MSE）**

<a id="tab-15-TVNF"></a>
<a id="panel-15-TVNF"></a>

```text
uart:~$ map mse mns disconnect
MSE MNS 0x20005d00 disconn rsp, rsp_code Success
uart:~$
```

**消息客户端设备 MCE（MCE）**

<a id="tab-15-TUNF"></a>
<a id="panel-15-TUNF"></a>

```text
MCE MNS 0x20005b00 disconn req
HI c0 Len 4
Conn ID: 00000001
uart:~$ map mce mns disconnect success
uart:~$
```

<a id="map-operations"></a>

### 42.2.6 MAP 操作（MAP Operations）

<a id="set-notification-registration"></a>

#### 42.2.6.1 设置通知注册（Set Notification Registration）

**消息客户端设备 MCE（MCE）**

<a id="tab-16-TUNF"></a>
<a id="panel-16-TUNF"></a>

```text
uart:~$ map mce mas set_ntf_reg
Adding default application parameters:
  Notification status: 0x01
MCE MAS 0x20005a00 set_ntf_reg rsp, rsp_code Success
uart:~$
```

**消息服务端设备 MSE（MSE）**

<a id="tab-16-TVNF"></a>
<a id="panel-16-TVNF"></a>

```text
MSE MAS 0x20005c00 set_ntf_reg req, final true, data len 52
HI cb Len 4
Conn ID: 00000001
HI 42 Len 34
00000000: 78 2d 62 74 2f 4d 41 50  2d 4e 6f 74 69 66 69 63 |x-bt/MAP -Notific|
00000010: 61 74 69 6f 6e 52 65 67  69 73 74 72 61 74 69 6f |ationReg istratio|
00000020: 6e 00                                            |n.               |
HI 4c Len 3
T 0e L 1
00000000: 01                                               |.                |
HI 49 Len 1
00000000: 30                                               |0                |
uart:~$ map mse mas set_ntf_reg noerror
uart:~$
```

<a id="set-folder"></a>

#### 42.2.6.2 设置文件夹（Set Folder）

**消息客户端设备 MCE（MCE）**

<a id="tab-17-TUNF"></a>
<a id="panel-17-TUNF"></a>

```text
uart:~$ map mce mas set_folder /
MCE MAS 0x20005a00 set_folder rsp, rsp_code Success
uart:~$ map mce mas set_folder telecom
MCE MAS 0x20005a00 set_folder rsp, rsp_code Success
uart:~$ map mce mas set_folder ..
MCE MAS 0x20005a00 set_folder rsp, rsp_code Success
uart:~$
```

**消息服务端设备 MSE（MSE）**

<a id="tab-17-TVNF"></a>
<a id="panel-17-TVNF"></a>

```text
MSE MAS 0x20005c00 set_folder req, flags 2, data len 8
HI cb Len 4
Conn ID: 00000001
HI 01 Len 0
uart:~$ map mse mas set_folder success
MSE MAS 0x20005c00 set_folder req, flags 2, data len 24
HI cb Len 4
Conn ID: 00000001
HI 01 Len 16
00000000: 00 74 00 65 00 6c 00 65  00 63 00 6f 00 6d 00 00 |.t.e.l.e .c.o.m..|
uart:~$ map mse mas set_folder success
MSE MAS 0x20005c00 set_folder req, flags 3, data len 8
HI cb Len 4
Conn ID: 00000001
HI 01 Len 0
uart:~$ map mse mas set_folder success
uart:~$
```

<a id="get-folder-listing"></a>

#### 42.2.6.3 获取文件夹列表（Get Folder Listing）

<a id="id7"></a>

##### 42.2.6.3.1 RFCOMM 传输（RFCOMM Transport）

使用 RFCOMM 传输时，可以多次调用同一 Shell 命令，直到完整消息传输结束。

**消息客户端设备 MCE（MCE）**

<a id="tab-18-TUNF"></a>
<a id="panel-18-TUNF"></a>

```text
uart:~$ map mce mas get_folder_listing
MCE MAS 0x20005a00 get_folder_listing rsp, rsp_code Continue, data len 252
HI 48 Len 249
00000000: 3c 3f 78 6d 6c 20 76 65  72 73 69 6f 6e 3d 27 31 |<?xml ve rsion='1|
00000010: 2e 30 27 20 65 6e 63 6f  64 69 6e 67 3d 27 75 74 |.0' enco ding='ut|
...
uart:~$ map mce mas get_folder_listing
MCE MAS 0x20005a00 get_folder_listing rsp, rsp_code Success, data len 4
HI 49 Len 1
00000000: 00                                               |.                |
uart:~$
```

**消息服务端设备 MSE（MSE）**

<a id="tab-18-TVNF"></a>
<a id="panel-18-TVNF"></a>

```text
MSE MAS 0x20005c00 get_folder_listing req, final true, data len 30
HI cb Len 4
Conn ID: 00000001
HI 42 Len 22
00000000: 78 2d 6f 62 65 78 2f 66  6f 6c 64 65 72 2d 6c 69 |x-obex/f older-li|
00000010: 73 74 69 6e 67 00                                |sting.           |
uart:~$ map mse mas get_folder_listing noerror
MSE MAS 0x20005c00 get_folder_listing req, final true, data len 0
uart:~$ map mse mas get_folder_listing noerror
uart:~$
```

<a id="l2cap-transport-with-srm"></a>

##### 42.2.6.3.2 启用 SRM 的 L2CAP 传输（L2CAP Transport with SRM）

使用默认启用 SRM 的 L2CAP 传输时，无需再次发送 GET 请求。

**消息客户端设备 MCE（MCE）**

<a id="tab-19-TUNF"></a>
<a id="panel-19-TUNF"></a>

```text
uart:~$ map mce mas get_folder_listing
MCE MAS 0x20005c98 get_folder_listing rsp, rsp_code Continue, data len 252
HI 97 Len 1
OBEX SRM: 01
HI 48 Len 247
00000000: 3c 3f 78 6d 6c 20 76 65  72 73 69 6f 6e 3d 27 31 |<?xml ve rsion='1|
00000010: 2e 30 27 20 65 6e 63 6f  64 69 6e 67 3d 27 75 74 |.0' enco ding='ut|
...
MCE MAS 0x20005a00 get_folder_listing rsp, rsp_code Success, data len 6
HI 49 Len 3
00000000: 67 3e 00                                         |g>.              |
...
uart:~$
```

**消息服务端设备 MSE（MSE）**

<a id="tab-19-TVNF"></a>
<a id="panel-19-TVNF"></a>

```text
MSE MAS 0x20005c00 get_folder_listing req, final true, data len 32
HI cb Len 4
Conn ID: 00000001
HI 97 Len 1
OBEX SRM: 01
HI 42 Len 22
00000000: 78 2d 6f 62 65 78 2f 66  6f 6c 64 65 72 2d 6c 69 |x-obex/f older-li|
00000010: 73 74 69 6e 67 00                                |sting.           |
...
uart:~$ map mse mas get_folder_listing noerror
uart:~$ map mse mas get_folder_listing noerror
uart:~$
```

<a id="l2cap-transport-with-srm-and-srmp"></a>

##### 42.2.6.3.3 启用 SRM 和 SRMP 的 L2CAP 传输（L2CAP Transport with SRM and SRMP）

使用同时启用 SRM 和 SRMP 的 L2CAP 传输时，需要继续发送 GET 请求，直到 SRMP 被禁用。

**消息客户端设备 MCE（MCE）**

<a id="tab-20-TUNF"></a>
<a id="panel-20-TUNF"></a>

```text
uart:~$ map mce mas get_folder_listing srmp
MCE MAS 0x20005a00 get_folder_listing rsp, rsp_code Continue, data len 252
HI 97 Len 1
OBEX SRM: 01
HI 48 Len 247
00000000: 3c 3f 78 6d 6c 20 76 65  72 73 69 6f 6e 3d 27 31 |<?xml ve rsion='1|
00000010: 2e 30 27 20 65 6e 63 6f  64 69 6e 67 3d 27 75 74 |.0' enco ding='ut|
...
MCE MAS 0x20005a00 get_folder_listing rsp, rsp_code Success, data len 6
HI 49 Len 3
00000000: 67 3e 00                                         |g>.              |
...
uart:~$
```

**消息服务端设备 MSE（MSE）**

<a id="tab-20-TVNF"></a>
<a id="panel-20-TVNF"></a>

```text
MSE MAS 0x20005c00 get_folder_listing req, final true, data len 34
HI cb Len 4
Conn ID: 00000001
HI 97 Len 1
OBEX SRM: 01
HI 98 Len 1
OBEX SRMP: 01
HI 42 Len 22
00000000: 78 2d 6f 62 65 78 2f 66  6f 6c 64 65 72 2d 6c 69 |x-obex/f older-li|
00000010: 73 74 69 6e 67 00                                |sting.           |
uart:~$ map mse mas get_folder_listing noerror
MSE MAS 0x20005c00 get_folder_listing req, final true, data len 0
uart:~$ map mse mas get_folder_listing noerror
uart:~$
```

<a id="get-message-listing"></a>

#### 42.2.6.4 获取消息列表（Get Message Listing）

<a id="id8"></a>

##### 42.2.6.4.1 RFCOMM 传输（RFCOMM Transport）

**消息客户端设备 MCE（MCE）**

<a id="tab-21-TUNF"></a>
<a id="panel-21-TUNF"></a>

```text
uart:~$ map mce mas get_msg_listing
MCE MAS 0x20005a00 get_msg_listing rsp, rsp_code Continue, data len 252
HI 4c Len 29
T 0d L 1
00000000: 00                                               |.                |
T 19 L 20
00000000: 32 30 32 35 30 31 30 31  54 31 32 30 30 30 30 2b |20250101 T120000+|
00000010: 30 30 30 30                                      |0000             |
T 12 L 2
00000000: 00 02                                            |..               |
HI 48 Len 217
00000000: 3c 3f 78 6d 6c 20 76 65  72 73 69 6f 6e 3d 27 31 |<?xml ve rsion='1|
00000010: 2e 30 27 20 65 6e 63 6f  64 69 6e 67 3d 27 75 74 |.0' enco ding='ut|
...
uart:~$ map mce mas get_msg_listing
MCE MAS 0x20005a00 get_msg_listing rsp, rsp_code Success, data len 52
HI 49 Len 49
00000000: 22 20 73 65 6e 74 3d 22  6e 6f 22 20 70 72 6f 74 |" sent=" no" prot|
...
uart:~$
```

**消息服务端设备 MSE（MSE）**

<a id="tab-21-TVNF"></a>
<a id="panel-21-TVNF"></a>

```text
MSE MAS 0x20005c00 get_msg_listing req, final true, data len 32
HI cb Len 4
Conn ID: 00000001
HI 42 Len 21
00000000: 78 2d 62 74 2f 4d 41 50  2d 6d 73 67 2d 6c 69 73 |x-bt/MAP -msg-lis|
00000010: 74 69 6e 67 00                                   |ting.            |
HI 01 Len 0
uart:~$ map mse mas get_msg_listing noerror
Adding default application parameters:
  New message: 0
  MSE time: 20250101T120000+0000
  Listing size: 2
MSE MAS 0x20005c00 get_msg_listing req, final true, data len 0
uart:~$ map mse mas get_msg_listing noerror
uart:~$
```

<a id="id9"></a>

##### 42.2.6.4.2 启用 SRM 的 L2CAP 传输（L2CAP Transport with SRM）

**消息客户端设备 MCE（MCE）**

<a id="tab-22-TUNF"></a>
<a id="panel-22-TUNF"></a>

```text
uart:~$ map mce mas get_msg_listing
MCE MAS 0x20005a00 get_msg_listing rsp, rsp_code Continue, data len 252
HI 97 Len 1
OBEX SRM: 01
HI 4c Len 29
T 0d L 1
00000000: 00                                               |.                |
T 19 L 20
00000000: 32 30 32 35 30 31 30 31  54 31 32 30 30 30 30 2b |20250101 T120000+|
00000010: 30 30 30 30                                      |0000             |
T 12 L 2
00000000: 00 02                                            |..               |
HI 48 Len 215
00000000: 3c 3f 78 6d 6c 20 76 65  72 73 69 6f 6e 3d 27 31 |<?xml ve rsion='1|
...
MCE MAS 0x20005a00 get_msg_listing rsp, rsp_code Continue, data len 252
HI 48 Len 249
00000000: 2e 63 6f 6d 22 20 72 65  63 69 70 69 65 6e 74 5f |.com" re cipient_|
...
MCE MAS 0x20005c98 get_msg_listing rsp, rsp_code Success, data len 54
HI 49 Len 51
00000000: 65 73 22 20 73 65 6e 74  3d 22 6e 6f 22 20 70 72 |es" sent ="no" pr|
00000010: 6f 74 65 63 74 65 64 3d  22 6e 6f 22 2f 3e 0d 0a |otected= "no"/>..|
...
uart:~$
```

**消息服务端设备 MSE（MSE）**

<a id="tab-22-TVNF"></a>
<a id="panel-22-TVNF"></a>

```text
MSE MAS 0x20005c00 get_msg_listing req, final true, data len 34
HI cb Len 4
Conn ID: 00000001
HI 97 Len 1
OBEX SRM: 01
HI 42 Len 21
00000000: 78 2d 62 74 2f 4d 41 50  2d 6d 73 67 2d 6c 69 73 |x-bt/MAP -msg-lis|
00000010: 74 69 6e 67 00                                   |ting.            |
uart:~$ map mse mas get_msg_listing noerror
Adding default application parameters:
  New message: 0
  MSE time: 20250101T120000+0000
  Listing size: 2
uart:~$ map mse mas get_msg_listing noerror
uart:~$ map mse mas get_msg_listing noerror
uart:~$
```

<a id="id10"></a>

##### 42.2.6.4.3 启用 SRM 和 SRMP 的 L2CAP 传输（L2CAP Transport with SRM and SRMP）

**消息客户端设备 MCE（MCE）**

<a id="tab-23-TUNF"></a>
<a id="panel-23-TUNF"></a>

```text
uart:~$ map mce mas get_msg_listing srmp
MCE MAS 0x20005a00 get_msg_listing rsp, rsp_code Continue, data len 252
HI 97 Len 1
OBEX SRM: 01
HI 4c Len 29
T 0d L 1
00000000: 00                                               |.                |
T 19 L 20
00000000: 32 30 32 35 30 31 30 31  54 31 32 30 30 30 30 2b |20250101 T120000+|
00000010: 30 30 30 30                                      |0000             |
T 12 L 2
00000000: 00 02                                            |..               |
HI 48 Len 215
00000000: 3c 3f 78 6d 6c 20 76 65  72 73 69 6f 6e 3d 27 31 |<?xml ve rsion='1|
...
uart:~$ map mce mas get_msg_listing
MCE MAS 0x20005a00 get_msg_listing rsp, rsp_code Continue, data len 252
HI 48 Len 249
00000000: 2e 63 6f 6d 22 20 72 65  63 69 70 69 65 6e 74 5f |.com" re cipient_|
00000010: 6e 61 6d 65 3d 22 42 6f  62 22 20 72 65 63 69 70 |name="Bo b" recip|
...
MCE MAS 0x20005a00 get_msg_listing rsp, rsp_code Success, data len 54
HI 49 Len 51
00000000: 65 73 22 20 73 65 6e 74  3d 22 6e 6f 22 20 70 72 |es" sent ="no" pr|
00000010: 6f 74 65 63 74 65 64 3d  22 6e 6f 22 2f 3e 0d 0a |otected= "no"/>..|
...
uart:~$
```

**消息服务端设备 MSE（MSE）**

<a id="tab-23-TVNF"></a>
<a id="panel-23-TVNF"></a>

```text
MSE MAS 0x20005c00 get_msg_listing req, final true, data len 36
HI cb Len 4
Conn ID: 00000001
HI 97 Len 1
OBEX SRM: 01
HI 98 Len 1
OBEX SRMP: 01
HI 42 Len 21
00000000: 78 2d 62 74 2f 4d 41 50  2d 6d 73 67 2d 6c 69 73 |x-bt/MAP -msg-lis|
00000010: 74 69 6e 67 00                                   |ting.            |
HI 01 Len 0
uart:~$ map mse mas get_msg_listing noerror
Adding default application parameters:
  New message: 0
  MSE time: 20250101T120000+0000
  Listing size: 2
MSE MAS 0x20005c00 get_msg_listing req, final true, data len 0
uart:~$ map mse mas get_msg_listing noerror
uart:~$ map mse mas get_msg_listing noerror
uart:~$
```

<a id="get-message"></a>

#### 42.2.6.5 获取消息（Get Message）

<a id="id11"></a>

##### 42.2.6.5.1 RFCOMM 传输（RFCOMM Transport）

**消息客户端设备 MCE（MCE）**

<a id="tab-24-TUNF"></a>
<a id="panel-24-TUNF"></a>

```text
uart:~$ map mce mas get_msg 0000000000000001
Adding default application parameters:
  Attachment: OFF (0x00)
  Charset: UTF-8 (0x01)
MCE MAS 0x20005a00 get_msg rsp, rsp_code Continue, data len 252
HI 48 Len 249
00000000: 42 45 47 49 4e 3a 42 4d  53 47 0d 0a 56 45 52 53 |BEGIN:BM SG..VERS|
00000010: 49 4f 4e 3a 31 2e 30 0d  0a 53 54 41 54 55 53 3a |ION:1.0. .STATUS:|
...
uart:~$ map mce mas get_msg 0000000000000001
MCE MAS 0x20005a00 get_msg rsp, rsp_code Success, data len 87
HI 49 Len 84
00000000: 3c 3e 3f 2f 0a 2d 20 4e  75 6d 62 65 72 73 3a 20 |<>?/.- N umbers: |
00000010: 30 31 32 33 34 35 36 37  38 39 0a 0a 45 6e 64 20 |01234567 89..End |
...
uart:~$
```

**消息服务端设备 MSE（MSE）**

<a id="tab-24-TVNF"></a>
<a id="panel-24-TVNF"></a>

```text
MSE MAS 0x20005c00 get_msg req, final true, data len 67
HI cb Len 4
Conn ID: 00000001
HI 42 Len 13
00000000: 78 2d 62 74 2f 6d 65 73  73 61 67 65 00          |x-bt/mes sage.   |
HI 01 Len 34
00000000: 00 30 00 30 00 30 00 30  00 30 00 30 00 30 00 30 |.0.0.0.0 .0.0.0.0|
00000010: 00 30 00 30 00 30 00 30  00 30 00 30 00 30 00 31 |.0.0.0.0 .0.0.0.1|
00000020: 00 00                                            |..               |
HI 4c Len 6
T 0a L 1
00000000: 00                                               |.                |
T 14 L 1
00000000: 01                                               |.                |
uart:~$ map mse mas get_msg noerror
MSE MAS 0x20005c00 get_msg req, final true, data len 0
uart:~$ map mse mas get_msg noerror
uart:~$
```

<a id="id12"></a>

##### 42.2.6.5.2 启用 SRM 的 L2CAP 传输（L2CAP Transport with SRM）

**消息客户端设备 MCE（MCE）**

<a id="tab-25-TUNF"></a>
<a id="panel-25-TUNF"></a>

```text
uart:~$ map mce mas get_msg 0000000000000001
Adding default application parameters:
  Attachment: OFF (0x00)
  Charset: UTF-8 (0x01)
MCE MAS 0x20005a00 get_msg rsp, rsp_code Continue, data len 252
HI 97 Len 1
OBEX SRM: 01
HI 48 Len 247
00000000: 42 45 47 49 4e 3a 42 4d  53 47 0d 0a 56 45 52 53 |BEGIN:BM SG..VERS|
00000010: 49 4f 4e 3a 31 2e 30 0d  0a 53 54 41 54 55 53 3a |ION:1.0. .STATUS:|
...
MCE MAS 0x20005a00 get_msg rsp, rsp_code Success, data len 89
HI 49 Len 86
00000000: 2c 2e 3c 3e 3f 2f 0a 2d  20 4e 75 6d 62 65 72 73 |,.<>?/.-  Numbers|
uart:~$
```

**消息服务端设备 MSE（MSE）**

<a id="tab-25-TVNF"></a>
<a id="panel-25-TVNF"></a>

```text
MSE MAS 0x20005c00 get_msg req, final true, data len 69
HI cb Len 4
Conn ID: 00000001
HI 97 Len 1
OBEX SRM: 01
HI 42 Len 13
00000000: 78 2d 62 74 2f 6d 65 73  73 61 67 65 00          |x-bt/mes sage.   |
HI 01 Len 34
00000000: 00 30 00 30 00 30 00 30  00 30 00 30 00 30 00 30 |.0.0.0.0 .0.0.0.0|
00000010: 00 30 00 30 00 30 00 30  00 30 00 30 00 30 00 31 |.0.0.0.0 .0.0.0.1|
00000020: 00 00                                            |..               |
HI 4c Len 6
T 0a L 1
00000000: 00                                               |.                |
T 14 L 1
00000000: 01                                               |.                |
uart:~$ map mse mas get_msg noerror
uart:~$ map mse mas get_msg noerror
uart:~$
```

<a id="id13"></a>

##### 42.2.6.5.3 启用 SRM 和 SRMP 的 L2CAP 传输（L2CAP Transport with SRM and SRMP）

**消息客户端设备 MCE（MCE）**

<a id="tab-26-TUNF"></a>
<a id="panel-26-TUNF"></a>

```text
uart:~$ map mce mas get_msg 0000000000000001 srmp
Adding default application parameters:
  Attachment: OFF (0x00)
  Charset: UTF-8 (0x01)
MCE MAS 0x20005a00 get_msg rsp, rsp_code Continue, data len 252
HI 97 Len 1
OBEX SRM: 01
HI 48 Len 247
00000000: 42 45 47 49 4e 3a 42 4d  53 47 0d 0a 56 45 52 53 |BEGIN:BM SG..VERS|
...
uart:~$ map mce mas get_msg 0000000000000001
MCE MAS 0x20005a00 get_msg rsp, rsp_code Continue, data len 252
HI 48 Len 249
00000000: 37 38 39 0d 0a 45 4e 44  3a 56 43 41 52 44 0d 0a |789..END :VCARD..|
00000010: 42 45 47 49 4e 3a 42 42  4f 44 59 0d 0a 43 48 41 |BEGIN:BB ODY..CHA|
...
MCE MAS 0x20005a00 get_msg rsp, rsp_code Success, data len 89
HI 49 Len 86
00000000: 2c 2e 3c 3e 3f 2f 0a 2d  20 4e 75 6d 62 65 72 73 |,.<>?/.-  Numbers|
...
uart:~$
```

**消息服务端设备 MSE（MSE）**

<a id="tab-26-TVNF"></a>
<a id="panel-26-TVNF"></a>

```text
MSE MAS 0x20005c00 get_msg req, final true, data len 71
HI cb Len 4
Conn ID: 00000001
HI 97 Len 1
OBEX SRM: 01
HI 98 Len 1
OBEX SRMP: 01
HI 42 Len 13
00000000: 78 2d 62 74 2f 6d 65 73  73 61 67 65 00          |x-bt/mes sage.   |
HI 01 Len 34
00000000: 00 30 00 30 00 30 00 30  00 30 00 30 00 30 00 30 |.0.0.0.0 .0.0.0.0|
00000010: 00 30 00 30 00 30 00 30  00 30 00 30 00 30 00 31 |.0.0.0.0 .0.0.0.1|
00000020: 00 00                                            |..               |
HI 4c Len 6
T 0a L 1
00000000: 00                                               |.                |
T 14 L 1
00000000: 01                                               |.                |
uart:~$ map mse mas get_msg noerror
MSE MAS 0x20005c00 get_msg req, final true, data len 0
uart:~$ map mse mas get_msg noerror
uart:~$ map mse mas get_msg noerror
uart:~$
```

<a id="set-message-status"></a>

#### 42.2.6.6 设置消息状态（Set Message Status）

**消息客户端设备 MCE（MCE）**

<a id="tab-27-TUNF"></a>
<a id="panel-27-TUNF"></a>

```text
uart:~$ map mce mas set_msg_status 0000000000000001
Adding default application parameters:
  Status indicator: 0x00
  Status value: 0x00
MCE MAS 0x20005a00 set_msg_status rsp, rsp_code Success
uart:~$
```

**消息服务端设备 MSE（MSE）**

<a id="tab-27-TVNF"></a>
<a id="panel-27-TVNF"></a>

```text
MSE MAS 0x20005c00 set_msg_status req, final true, data len 77
HI cb Len 4
Conn ID: 00000001
HI 01 Len 34
00000000: 00 30 00 30 00 30 00 30  00 30 00 30 00 30 00 30 |.0.0.0.0 .0.0.0.0|
00000010: 00 30 00 30 00 30 00 30  00 30 00 30 00 30 00 31 |.0.0.0.0 .0.0.0.1|
00000020: 00 00                                            |..               |
HI 42 Len 19
00000000: 78 2d 62 74 2f 6d 65 73  73 61 67 65 53 74 61 74 |x-bt/mes sageStat|
00000010: 75 73 00                                         |us.              |
HI 4c Len 6
T 17 L 1
00000000: 00                                               |.                |
T 18 L 1
00000000: 00                                               |.                |
HI 49 Len 1
00000000: 30                                               |0                |
uart:~$ map mse mas set_msg_status noerror
uart:~$
```

<a id="push-message"></a>

#### 42.2.6.7 推送消息（Push Message）

<a id="id14"></a>

##### 42.2.6.7.1 RFCOMM 传输（RFCOMM Transport）

**消息客户端设备 MCE（MCE）**

<a id="tab-28-TUNF"></a>
<a id="panel-28-TUNF"></a>

```text
uart:~$ map mce mas push_msg
Adding default application parameters:
  Charset: UTF-8 (0x01)
MCE MAS 0x20005a00 push_msg rsp, rsp_code Continue, data len 0
...
uart:~$ map mce mas push_msg
MCE MAS 0x20005a00 push_msg rsp, rsp_code Success, data len 37
HI 01 Len 34
00000000: 00 30 00 30 00 30 00 30  00 30 00 30 00 30 00 30 |.0.0.0.0 .0.0.0.0|
00000010: 00 30 00 30 00 30 00 30  00 30 00 30 00 30 00 31 |.0.0.0.0 .0.0.0.1|
00000020: 00 00                                            |..               |
...
uart:~$
```

**消息服务端设备 MSE（MSE）**

<a id="tab-28-TVNF"></a>
<a id="panel-28-TVNF"></a>

```text
MSE MAS 0x20005c00 push_msg req, final false, data len 252
HI cb Len 4
Conn ID: 00000001
HI 42 Len 13
00000000: 78 2d 62 74 2f 6d 65 73  73 61 67 65 00          |x-bt/mes sage.   |
HI 01 Len 0
HI 4c Len 3
T 14 L 1
00000000: 01                                               |.                |
HI 48 Len 219
00000000: 42 45 47 49 4e 3a 42 4d  53 47 0d 0a 56 45 52 53 |BEGIN:BM SG..VERS|
00000010: 49 4f 4e 3a 31 2e 30 0d  0a 53 54 41 54 55 53 3a |ION:1.0. .STATUS:|
...
uart:~$ map mse mas push_msg noerror
MSE MAS 0x20005c00 push_msg req, final true, data len 117
HI 49 Len 114
00000000: 61 63 74 65 72 73 3a 20  40 23 24 25 26 2a 28 29 |acters:  @#$%&*()|
...
uart:~$ map mse mas push_msg noerror
uart:~$
```

<a id="id15"></a>

##### 42.2.6.7.2 启用 SRM 的 L2CAP 传输（L2CAP Transport with SRM）

**消息客户端设备 MCE（MCE）**

<a id="tab-29-TUNF"></a>
<a id="panel-29-TUNF"></a>

```text
uart:~$ map mce mas push_msg
Adding default application parameters:
  Charset: UTF-8 (0x01)
MCE MAS 0x20005a00 push_msg rsp, rsp_code Continue, data len 2
HI 97 Len 1
OBEX SRM: 01
...
uart:~$ map mce mas push_msg
uart:~$ map mce mas push_msg
MCE MAS 0x20005a00 push_msg rsp, rsp_code Success, data len 37
HI 01 Len 34
00000000: 00 30 00 30 00 30 00 30  00 30 00 30 00 30 00 30 |.0.0.0.0 .0.0.0.0|
00000010: 00 30 00 30 00 30 00 30  00 30 00 30 00 30 00 31 |.0.0.0.0 .0.0.0.1|
00000020: 00 00                                            |..               |
...
uart:~$
```

**消息服务端设备 MSE（MSE）**

<a id="tab-29-TVNF"></a>
<a id="panel-29-TVNF"></a>

```text
MSE MAS 0x20005c00 push_msg req, final false, data len 252
HI cb Len 4
Conn ID: 00000001
HI 97 Len 1
OBEX SRM: 01
HI 42 Len 13
00000000: 78 2d 62 74 2f 6d 65 73  73 61 67 65 00          |x-bt/mes sage.   |
HI 01 Len 0
HI 4c Len 3
T 14 L 1
00000000: 01                                               |.                |
HI 48 Len 217
00000000: 42 45 47 49 4e 3a 42 4d  53 47 0d 0a 56 45 52 53 |BEGIN:BM SG..VERS|
00000010: 49 4f 4e 3a 31 2e 30 0d  0a 53 54 41 54 55 53 3a |ION:1.0. .STATUS:|
...
uart:~$ map mse mas push_msg noerror
MSE MAS 0x20005c00 push_msg req, final false, data len 252
HI 48 Len 249
00000000: 54 46 2d 38 3a 2b 30 31  32 33 34 35 36 37 38 39 |TF-8:+01 23456789|
...
MSE MAS 0x20005c00 push_msg req, final true, data len 119
HI 49 Len 116
00000000: 61 72 61 63 74 65 72 73  3a 20 40 23 24 25 26 2a |aracters : @#$%&*|
...
uart:~$ map mse mas push_msg noerror
uart:~$
```

<a id="id16"></a>

##### 42.2.6.7.3 启用 SRM 和 SRMP 的 L2CAP 传输（L2CAP Transport with SRM and SRMP）

**消息客户端设备 MCE（MCE）**

<a id="tab-30-TUNF"></a>
<a id="panel-30-TUNF"></a>

```text
uart:~$ map mce mas push_msg
Adding default application parameters:
  Charset: UTF-8 (0x01)
MCE MAS 0x20005a00 push_msg rsp, rsp_code Continue, data len 4
HI 97 Len 1
OBEX SRM: 01
HI 98 Len 1
OBEX SRMP: 01
...
uart:~$ map mce mas push_msg
MCE MAS 0x20005c98 push_msg rsp, rsp_code Continue, data len 0
uart:~$ map mce mas push_msg
MCE MAS 0x20005a00 push_msg rsp, rsp_code Success, data len 37
HI 01 Len 34
00000000: 00 30 00 30 00 30 00 30  00 30 00 30 00 30 00 30 |.0.0.0.0 .0.0.0.0|
00000010: 00 30 00 30 00 30 00 30  00 30 00 30 00 30 00 31 |.0.0.0.0 .0.0.0.1|
00000020: 00 00                                            |..               |
...
uart:~$
```

**消息服务端设备 MSE（MSE）**

<a id="tab-30-TVNF"></a>
<a id="panel-30-TVNF"></a>

```text
MSE MAS 0x20005c00 push_msg req, final false, data len 252
HI cb Len 4
Conn ID: 00000001
HI 97 Len 1
OBEX SRM: 01
HI 42 Len 13
00000000: 78 2d 62 74 2f 6d 65 73  73 61 67 65 00          |x-bt/mes sage.   |
HI 01 Len 0
HI 4c Len 3
T 14 L 1
00000000: 01                                               |.                |
HI 48 Len 217
00000000: 42 45 47 49 4e 3a 42 4d  53 47 0d 0a 56 45 52 53 |BEGIN:BM SG..VERS|
00000010: 49 4f 4e 3a 31 2e 30 0d  0a 53 54 41 54 55 53 3a |ION:1.0. .STATUS:|
...
uart:~$ map mse mas push_msg noerror srmp
MSE MAS 0x20005c00 push_msg req, final false, data len 252
HI 48 Len 249
00000000: 54 46 2d 38 3a 2b 30 31  32 33 34 35 36 37 38 39 |TF-8:+01 23456789|
...
uart:~$ map mse mas push_msg noerror
MSE MAS 0x20005c00 push_msg req, final true, data len 119
HI 49 Len 116
00000000: 61 72 61 63 74 65 72 73  3a 20 40 23 24 25 26 2a |aracters : @#$%&*|
...
uart:~$ map mse mas push_msg noerror
uart:~$
```

<a id="update-inbox"></a>

#### 42.2.6.8 更新收件箱（Update Inbox）

**消息客户端设备 MCE（MCE）**

<a id="tab-31-TUNF"></a>
<a id="panel-31-TUNF"></a>

```text
uart:~$ map mce mas update_inbox
MCE MAS 0x20005a00 update_inbox rsp, rsp_code Success
uart:~$
```

**消息服务端设备 MSE（MSE）**

<a id="tab-31-TVNF"></a>
<a id="panel-31-TVNF"></a>

```text
MSE MAS 0x20005c00 update_inbox req, final true, data len 35
HI cb Len 4
Conn ID: 00000001
HI 42 Len 23
00000000: 78 2d 62 74 2f 4d 41 50  2d 6d 65 73 73 61 67 65 |x-bt/MAP -message|
00000010: 55 70 64 61 74 65 00                             |Update.          |
HI 49 Len 1
00000000: 30                                               |0                |
uart:~$ map mse mas update_inbox noerror
uart:~$
```

<a id="get-mas-instance-information"></a>

#### 42.2.6.9 获取 MAS 实例信息（Get MAS Instance Information）

<a id="id17"></a>

##### 42.2.6.9.1 RFCOMM 传输（RFCOMM Transport）

**消息客户端设备 MCE（MCE）**

<a id="tab-32-TUNF"></a>
<a id="panel-32-TUNF"></a>

```text
uart:~$ map mce mas get_mas_inst_info
Adding default application parameters:
  Instance ID: 0
MCE MAS 0x20005a00 get_mas_inst_info rsp, rsp_code Success, data len 21
HI 49 Len 18
00000000: 4d 41 53 20 49 6e 73 74  61 6e 63 65 20 49 6e 66 |MAS Inst ance Inf|
00000010: 6f 00                                            |o.               |
uart:~$
```

**消息服务端设备 MSE（MSE）**

<a id="tab-32-TVNF"></a>
<a id="panel-32-TVNF"></a>

```text
MSE MAS 0x20005c00 get_mas_inst_info req, final true, data len 42
HI cb Len 4
Conn ID: 00000001
HI 42 Len 28
00000000: 78 2d 62 74 2f 4d 41 53  49 6e 73 74 61 6e 63 65 |x-bt/MAS Instance|
00000010: 49 6e 66 6f 72 6d 61 74  69 6f 6e 00             |Informat ion.    |
HI 4c Len 3
T 0f L 1
00000000: 00                                               |.                |
uart:~$ map mse mas get_mas_inst_info noerror
uart:~$
```

<a id="id18"></a>

##### 42.2.6.9.2 启用 SRM 的 L2CAP 传输（L2CAP Transport with SRM）

**消息客户端设备 MCE（MCE）**

<a id="tab-33-TUNF"></a>
<a id="panel-33-TUNF"></a>

```text
uart:~$ map mce mas get_mas_inst_info
Adding default application parameters:
  Instance ID: 0
MCE MAS 0x20005a00 get_mas_inst_info rsp, rsp_code Success, data len 23
HI 97 Len 1
OBEX SRM: 01
HI 49 Len 18
00000000: 4d 41 53 20 49 6e 73 74  61 6e 63 65 20 49 6e 66 |MAS Inst ance Inf|
00000010: 6f 00                                            |o.               |
uart:~$
```

**消息服务端设备 MSE（MSE）**

<a id="tab-33-TVNF"></a>
<a id="panel-33-TVNF"></a>

```text
MSE MAS 0x20005c00 get_mas_inst_info req, final true, data len 44
HI cb Len 4
Conn ID: 00000001
HI 97 Len 1
OBEX SRM: 01
HI 42 Len 28
00000000: 78 2d 62 74 2f 4d 41 53  49 6e 73 74 61 6e 63 65 |x-bt/MAS Instance|
00000010: 49 6e 66 6f 72 6d 61 74  69 6f 6e 00             |Informat ion.    |
HI 4c Len 3
T 0f L 1
00000000: 00                                               |.                |
uart:~$ map mse mas get_mas_inst_info noerror
uart:~$
```

<a id="id19"></a>

##### 42.2.6.9.3 启用 SRM 和 SRMP 的 L2CAP 传输（L2CAP Transport with SRM and SRMP）

**消息客户端设备 MCE（MCE）**

<a id="tab-34-TUNF"></a>
<a id="panel-34-TUNF"></a>

```text
uart:~$ map mce mas get_mas_inst_info srmp
Adding default application parameters:
  Instance ID: 0
MCE MAS 0x20005a00 get_mas_inst_info rsp, rsp_code Success, data len 23
HI 97 Len 1
OBEX SRM: 01
HI 49 Len 18
00000000: 4d 41 53 20 49 6e 73 74  61 6e 63 65 20 49 6e 66 |MAS Inst ance Inf|
00000010: 6f 00                                            |o.               |
uart:~$
```

**消息服务端设备 MSE（MSE）**

<a id="tab-34-TVNF"></a>
<a id="panel-34-TVNF"></a>

```text
MSE MAS 0x20005c00 get_mas_inst_info req, final true, data len 46
HI cb Len 4
Conn ID: 00000001
HI 97 Len 1
OBEX SRM: 01
HI 98 Len 1
OBEX SRMP: 01
HI 42 Len 28
00000000: 78 2d 62 74 2f 4d 41 53  49 6e 73 74 61 6e 63 65 |x-bt/MAS Instance|
00000010: 49 6e 66 6f 72 6d 61 74  69 6f 6e 00             |Informat ion.    |
HI 4c Len 3
T 0f L 1
00000000: 00                                               |.                |
uart:~$ map mse mas get_mas_inst_info noerror
uart:~$
```

<a id="set-owner-status"></a>

#### 42.2.6.10 设置所有者状态（Set Owner Status）

**消息客户端设备 MCE（MCE）**

<a id="tab-35-TUNF"></a>
<a id="panel-35-TUNF"></a>

```text
uart:~$ map mce mas set_owner_status
Adding default application parameters:
  Chat state: 0x00
MCE MAS 0x20005a00 set_owner_status rsp, rsp_code Success
uart:~$
```

**消息服务端设备 MSE（MSE）**

<a id="tab-35-TVNF"></a>
<a id="panel-35-TVNF"></a>

```text
MSE MAS 0x20005c00 set_owner_status req, final true, data len 35
HI cb Len 4
Conn ID: 00000001
HI 42 Len 17
00000000: 78 2d 62 74 2f 6f 77 6e  65 72 53 74 61 74 75 73 |x-bt/own erStatus|
00000010: 00                                               |.                |
HI 4c Len 3
T 21 L 1
00000000: 00                                               |.                |
HI 49 Len 1
00000000: 30                                               |0                |
uart:~$ map mse mas set_owner_status noerror
uart:~$
```

<a id="get-owner-status"></a>

#### 42.2.6.11 获取所有者状态（Get Owner Status）

<a id="id20"></a>

##### 42.2.6.11.1 RFCOMM 传输（RFCOMM Transport）

**消息客户端设备 MCE（MCE）**

<a id="tab-36-TUNF"></a>
<a id="panel-36-TUNF"></a>

```text
uart:~$ map mce mas get_owner_status
MCE MAS 0x20005a00 get_owner_status rsp, rsp_code Success, data len 18
HI 4c Len 12
T 1c L 1
00000000: 00                                               |.                |
T 1d L 7
00000000: 55 6e 6b 6e 6f 77 6e                             |Unknown          |
uart:~$
```

**消息服务端设备 MSE（MSE）**

<a id="tab-36-TVNF"></a>
<a id="panel-36-TVNF"></a>

```text
MSE MAS 0x20005c00 get_owner_status req, final true, data len 25
HI cb Len 4
Conn ID: 00000001
HI 42 Len 17
00000000: 78 2d 62 74 2f 6f 77 6e  65 72 53 74 61 74 75 73 |x-bt/own erStatus|
00000010: 00                                               |.                |
uart:~$ map mse mas get_owner_status noerror
Adding default application parameters:
  Presence:  0x00
  Presence text: Unknown
uart:~$
```

<a id="id21"></a>

##### 42.2.6.11.2 启用 SRM 的 L2CAP 传输（L2CAP Transport with SRM）

**消息客户端设备 MCE（MCE）**

<a id="tab-37-TUNF"></a>
<a id="panel-37-TUNF"></a>

```text
uart:~$ map mce mas get_owner_status
MCE MAS 0x20005a00 get_owner_status rsp, rsp_code Success, data len 20
HI 97 Len 1
OBEX SRM: 01
HI 4c Len 12
T 1c L 1
00000000: 00                                               |.                |
T 1d L 7
00000000: 55 6e 6b 6e 6f 77 6e                             |Unknown          |
HI 49 Len 0
uart:~$
```

**消息服务端设备 MSE（MSE）**

<a id="tab-37-TVNF"></a>
<a id="panel-37-TVNF"></a>

```text
MSE MAS 0x20005c00 get_owner_status req, final true, data len 27
HI cb Len 4
Conn ID: 00000001
HI 97 Len 1
OBEX SRM: 01
HI 42 Len 17
00000000: 78 2d 62 74 2f 6f 77 6e  65 72 53 74 61 74 75 73 |x-bt/own erStatus|
00000010: 00                                               |.                |
uart:~$ map mse mas get_owner_status noerror
Adding default application parameters:
  Presence:  0x00
  Presence text: Unknown
uart:~$
```

<a id="id22"></a>

##### 42.2.6.11.3 启用 SRM 和 SRMP 的 L2CAP 传输（L2CAP Transport with SRM and SRMP）

**消息客户端设备 MCE（MCE）**

<a id="tab-38-TUNF"></a>
<a id="panel-38-TUNF"></a>

```text
uart:~$ map mce mas get_owner_status srmp
MCE MAS 0x20005a00 get_owner_status rsp, rsp_code Success, data len 20
HI 97 Len 1
OBEX SRM: 01
HI 4c Len 12
T 1c L 1
00000000: 00                                               |.                |
T 1d L 7
00000000: 55 6e 6b 6e 6f 77 6e                             |Unknown          |
HI 49 Len 0
uart:~$
```

**消息服务端设备 MSE（MSE）**

<a id="tab-38-TVNF"></a>
<a id="panel-38-TVNF"></a>

```text
MSE MAS 0x20005c00 get_owner_status req, final true, data len 29
HI cb Len 4
Conn ID: 00000001
HI 97 Len 1
OBEX SRM: 01
HI 98 Len 1
OBEX SRMP: 01
HI 42 Len 17
00000000: 78 2d 62 74 2f 6f 77 6e  65 72 53 74 61 74 75 73 |x-bt/own erStatus|
00000010: 00                                               |.                |
uart:~$ map mse mas get_owner_status noerror
Adding default application parameters:
  Presence:  0x00
  Presence text: Unknown
uart:~$
```

<a id="get-conversation-listing"></a>

#### 42.2.6.12 获取会话列表（Get Conversation Listing）

<a id="id23"></a>

##### 42.2.6.12.1 RFCOMM 传输（RFCOMM Transport）

**消息客户端设备 MCE（MCE）**

<a id="tab-39-TUNF"></a>
<a id="panel-39-TUNF"></a>

```text
uart:~$ map mce mas get_convo_listing
MCE MAS 0x20005a00 get_convo_listing rsp, rsp_code Continue, data len 252
HI 4c Len 72
T 12 L 2
00000000: 00 02                                            |..               |
T 1a L 32
00000000: 30 30 30 30 30 30 30 30  30 30 30 30 30 30 30 31 |00000000 00000001|
00000010: 30 30 30 30 30 30 30 30  30 30 30 30 30 30 30 31 |00000000 00000001|
T 1b L 32
00000000: 30 30 30 30 30 30 30 30  30 30 30 30 30 30 30 31 |00000000 00000001|
00000010: 30 30 30 30 30 30 30 30  30 30 30 30 30 30 30 31 |00000000 00000001|
HI 48 Len 174
00000000: 3c 3f 78 6d 6c 20 76 65  72 73 69 6f 6e 3d 27 31 |<?xml ve rsion='1|
00000010: 2e 30 27 20 65 6e 63 6f  64 69 6e 67 3d 27 75 74 |.0' enco ding='ut|
...
uart:~$ map mce mas get_convo_listing
MCE MAS 0x20005a00 get_convo_listing rsp, rsp_code Success, data len 117
HI 49 Len 114
00000000: 22 20 6e 61 6d 65 3d 22  42 6f 62 22 20 70 72 65 |" name=" Bob" pre|
...
uart:~$
```

**消息服务端设备 MSE（MSE）**

<a id="tab-39-TVNF"></a>
<a id="panel-39-TVNF"></a>

```text
MSE MAS 0x20005c00 get_convo_listing req, final true, data len 31
HI cb Len 4
Conn ID: 00000001
HI 42 Len 23
00000000: 78 2d 62 74 2f 4d 41 50  2d 63 6f 6e 76 6f 2d 6c |x-bt/MAP -convo-l|
00000010: 69 73 74 69 6e 67 00                             |isting.          |
uart:~$ map mse mas get_convo_listing noerror
Adding default application parameters:
  Listing size: 2
  Database ID: 00000000000000010000000000000001
  Conversation version counter: 00000000000000010000000000000001
MSE MAS 0x20005c00 get_convo_listing req, final true, data len 0
uart:~$ map mse mas get_convo_listing noerror
uart:~$
```

<a id="id24"></a>

##### 42.2.6.12.2 启用 SRM 的 L2CAP 传输（L2CAP Transport with SRM）

**消息客户端设备 MCE（MCE）**

<a id="tab-40-TUNF"></a>
<a id="panel-40-TUNF"></a>

```text
uart:~$ map mce mas get_convo_listing
MCE MAS 0x20005a00 get_convo_listing rsp, rsp_code Continue, data len 252
HI 97 Len 1
OBEX SRM: 01
HI 4c Len 72
T 12 L 2
00000000: 00 02                                            |..               |
T 1a L 32
00000000: 30 30 30 30 30 30 30 30  30 30 30 30 30 30 30 31 |00000000 00000001|
00000010: 30 30 30 30 30 30 30 30  30 30 30 30 30 30 30 31 |00000000 00000001|
T 1b L 32
00000000: 30 30 30 30 30 30 30 30  30 30 30 30 30 30 30 31 |00000000 00000001|
00000010: 30 30 30 30 30 30 30 30  30 30 30 30 30 30 30 31 |00000000 00000001|
HI 48 Len 172
00000000: 3c 3f 78 6d 6c 20 76 65  72 73 69 6f 6e 3d 27 31 |<?xml ve rsion='1|
00000010: 2e 30 27 20 65 6e 63 6f  64 69 6e 67 3d 27 75 74 |.0' enco ding='ut|
...
MCE MAS 0x20005a00 get_convo_listing rsp, rsp_code Success, data len 119
HI 49 Len 116
00000000: 32 31 22 20 6e 61 6d 65  3d 22 42 6f 62 22 20 70 |21" name ="Bob" p|
...
uart:~$
```

**消息服务端设备 MSE（MSE）**

<a id="tab-40-TVNF"></a>
<a id="panel-40-TVNF"></a>

```text
MSE MAS 0x20005c00 get_convo_listing req, final true, data len 33
HI cb Len 4
Conn ID: 00000001
HI 97 Len 1
OBEX SRM: 01
HI 42 Len 23
00000000: 78 2d 62 74 2f 4d 41 50  2d 63 6f 6e 76 6f 2d 6c |x-bt/MAP -convo-l|
00000010: 69 73 74 69 6e 67 00                             |isting.          |
uart:~$ map mse mas get_convo_listing noerror
Adding default application parameters:
  Listing size: 2
  Database ID: 00000000000000010000000000000001
  Conversation version counter: 00000000000000010000000000000001
uart:~$ map mse mas get_convo_listing noerror
uart:~$
```

<a id="id25"></a>

##### 42.2.6.12.3 启用 SRM 和 SRMP 的 L2CAP 传输（L2CAP Transport with SRM and SRMP）

**消息客户端设备 MCE（MCE）**

<a id="tab-41-TUNF"></a>
<a id="panel-41-TUNF"></a>

```text
uart:~$ map mce mas get_convo_listing srmp
MCE MAS 0x20005a00 get_convo_listing rsp, rsp_code Continue, data len 252
HI 97 Len 1
OBEX SRM: 01
HI 4c Len 72
T 12 L 2
00000000: 00 02                                            |..               |
T 1a L 32
00000000: 30 30 30 30 30 30 30 30  30 30 30 30 30 30 30 31 |00000000 00000001|
00000010: 30 30 30 30 30 30 30 30  30 30 30 30 30 30 30 31 |00000000 00000001|
T 1b L 32
00000000: 30 30 30 30 30 30 30 30  30 30 30 30 30 30 30 31 |00000000 00000001|
00000010: 30 30 30 30 30 30 30 30  30 30 30 30 30 30 30 31 |00000000 00000001|
HI 48 Len 172
00000000: 3c 3f 78 6d 6c 20 76 65  72 73 69 6f 6e 3d 27 31 |<?xml ve rsion='1|
00000010: 2e 30 27 20 65 6e 63 6f  64 69 6e 67 3d 27 75 74 |.0' enco ding='ut|
...
uart:~$ map mce mas get_convo_listing
MCE MAS 0x20005a00 get_convo_listing rsp, rsp_code Continue, data len 252
HI 48 Len 249
00000000: 79 65 73 22 20 76 65 72  73 69 6f 6e 5f 63 6f 75 |yes" ver sion_cou|
...
MCE MAS 0x20005a00 get_convo_listing rsp, rsp_code Success, data len 119
HI 49 Len 116
00000000: 32 31 22 20 6e 61 6d 65  3d 22 42 6f 62 22 20 70 |21" name ="Bob" p|
...
uart:~$
```

**消息服务端设备 MSE（MSE）**

<a id="tab-41-TVNF"></a>
<a id="panel-41-TVNF"></a>

```text
MSE MAS 0x20005c00 get_convo_listing req, final true, data len 35
HI cb Len 4
Conn ID: 00000001
HI 97 Len 1
OBEX SRM: 01
HI 98 Len 1
OBEX SRMP: 01
HI 42 Len 23
00000000: 78 2d 62 74 2f 4d 41 50  2d 63 6f 6e 76 6f 2d 6c |x-bt/MAP -convo-l|
00000010: 69 73 74 69 6e 67 00                             |isting.          |
uart:~$ map mse mas get_convo_listing noerror
Adding default application parameters:
  Listing size: 2
  Database ID: 00000000000000010000000000000001
  Conversation version counter: 00000000000000010000000000000001
MSE MAS 0x20005c00 get_convo_listing req, final true, data len 0
uart:~$ map mse mas get_convo_listing noerror
uart:~$ map mse mas get_convo_listing noerror
uart:~$
```

<a id="set-notification-filter"></a>

#### 42.2.6.13 设置通知过滤器（Set Notification Filter）

**消息客户端设备 MCE（MCE）**

<a id="tab-42-TUNF"></a>
<a id="panel-42-TUNF"></a>

```text
uart:~$ map mce mas set_ntf_filter
Adding default application parameters:
  Notification filter mask: 0x00007fff
MCE MAS 0x20005a00 set_ntf_filter rsp, rsp_code Success
uart:~$
```

**消息服务端设备 MSE（MSE）**

<a id="tab-42-TVNF"></a>
<a id="panel-42-TVNF"></a>

```text
MSE MAS 0x20005c00 set_ntf_filter req, final true, data len 50
HI cb Len 4
Conn ID: 00000001
HI 42 Len 29
00000000: 78 2d 62 74 2f 4d 41 50  2d 6e 6f 74 69 66 69 63 |x-bt/MAP -notific|
00000010: 61 74 69 6f 6e 2d 66 69  6c 74 65 72 00          |ation-fi lter.   |
HI 4c Len 6
T 25 L 4
00000000: 00 00 7f ff                                      |....             |
HI 49 Len 1
00000000: 30                                               |0                |
uart:~$ map mse mas set_ntf_filter noerror
uart:~$
```

<a id="send-event"></a>

#### 42.2.6.14 发送事件（Send Event）

<a id="id26"></a>

##### 42.2.6.14.1 RFCOMM 传输（RFCOMM Transport）

**消息服务端设备 MSE（MSE）**

<a id="tab-43-TVNF"></a>
<a id="panel-43-TVNF"></a>

```text
uart:~$ map mse mns send_event
Adding default application parameters:
  Instance ID: 0
MSE MNS 0x20005d00 send_event rsp, rsp_code Continue, data len 0
uart:~$ map mse mns send_event
MSE MNS 0x20005d00 send_event rsp, rsp_code Success, data len 0
uart:~$
```

**消息客户端设备 MCE（MCE）**

<a id="tab-43-TUNF"></a>
<a id="panel-43-TUNF"></a>

```text
MCE MNS 0x20005b00 send_event req, final false, data len 252
HI cb Len 4
Conn ID: 00000001
HI 42 Len 22
00000000: 78 2d 62 74 2f 4d 41 50  2d 65 76 65 6e 74 2d 72 |x-bt/MAP -event-r|
00000010: 65 70 6f 72 74 00                                |eport.           |
HI 4c Len 3
T 0f L 1
00000000: 00                                               |.                |
HI 48 Len 213
00000000: 3c 3f 78 6d 6c 20 76 65  72 73 69 6f 6e 3d 27 31 |<?xml ve rsion='1|
00000010: 2e 30 27 20 65 6e 63 6f  64 69 6e 67 3d 27 75 74 |.0' enco ding='ut|
...
uart:~$ map mce mns send_event noerror
MCE MNS 0x20005b00 send_event req, final true, data len 8
HI 49 Len 5
00000000: 6f 72 74 3e 00                                   |ort>.            |
uart:~$ map mce mns send_event noerror
uart:~$
```

<a id="id27"></a>

##### 42.2.6.14.2 启用 SRM 的 L2CAP 传输（L2CAP Transport with SRM）

**消息服务端设备 MSE（MSE）**

<a id="tab-44-TVNF"></a>
<a id="panel-44-TVNF"></a>

```text
uart:~$ map mse mns send_event
Adding default application parameters:
  Instance ID: 0
MSE MNS 0x20005d00 send_event rsp, rsp_code Continue, data len 2
HI 97 Len 1
OBEX SRM: 01
uart:~$ map mse mns send_event
MSE MNS 0x20005d00 send_event rsp, rsp_code Success, data len 0
uart:~$
```

**消息客户端设备 MCE（MCE）**

<a id="tab-44-TUNF"></a>
<a id="panel-44-TUNF"></a>

```text
MCE MNS 0x20005b00 send_event req, final false, data len 252
HI cb Len 4
Conn ID: 00000001
HI 97 Len 1
OBEX SRM: 01
HI 42 Len 22
00000000: 78 2d 62 74 2f 4d 41 50  2d 65 76 65 6e 74 2d 72 |x-bt/MAP -event-r|
00000010: 65 70 6f 72 74 00                                |eport.           |
HI 4c Len 3
T 0f L 1
00000000: 00                                               |.                |
HI 48 Len 211
00000000: 3c 3f 78 6d 6c 20 76 65  72 73 69 6f 6e 3d 27 31 |<?xml ve rsion='1|
00000010: 2e 30 27 20 65 6e 63 6f  64 69 6e 67 3d 27 75 74 |.0' enco ding='ut|
...
uart:~$ map mce mns send_event noerror
MCE MNS 0x20005b00 send_event req, final true, data len 10
HI 49 Len 7
00000000: 65 70 6f 72 74 3e 00                             |eport>.          |
uart:~$ map mce mns send_event noerror
uart:~$
```

<a id="id28"></a>

##### 42.2.6.14.3 启用 SRM 和 SRMP 的 L2CAP 传输（L2CAP Transport with SRM and SRMP）

**消息服务端设备 MSE（MSE）**

<a id="tab-45-TVNF"></a>
<a id="panel-45-TVNF"></a>

```text
uart:~$ map mse mns send_event
Adding default application parameters:
  Instance ID: 0
MSE MNS 0x20005d00 send_event rsp, rsp_code Continue, data len 4
HI 97 Len 1
OBEX SRM: 01
HI 98 Len 1
OBEX SRMP: 01
uart:~$ map mse mns send_event
MSE MNS 0x20005d00 send_event rsp, rsp_code Success, data len 0
uart:~$
```

**消息客户端设备 MCE（MCE）**

<a id="tab-45-TUNF"></a>
<a id="panel-45-TUNF"></a>

```text
MCE MNS 0x20005b00 send_event req, final false, data len 252
HI cb Len 4
Conn ID: 00000001
HI 97 Len 1
OBEX SRM: 01
HI 42 Len 22
00000000: 78 2d 62 74 2f 4d 41 50  2d 65 76 65 6e 74 2d 72 |x-bt/MAP -event-r|
00000010: 65 70 6f 72 74 00                                |eport.           |
HI 4c Len 3
T 0f L 1
00000000: 00                                               |.                |
HI 48 Len 211
00000000: 3c 3f 78 6d 6c 20 76 65  72 73 69 6f 6e 3d 27 31 |<?xml ve rsion='1|
00000010: 2e 30 27 20 65 6e 63 6f  64 69 6e 67 3d 27 75 74 |.0' enco ding='ut|
...
uart:~$ map mce mns send_event noerror srmp
MCE MNS 0x20005b00 send_event req, final true, data len 10
HI 49 Len 7
00000000: 65 70 6f 72 74 3e 00                             |eport>.          |
uart:~$ map mce mns send_event noerror
uart:~$
```

<a id="application-parameters"></a>

### 42.2.7 应用参数（Application Parameters）

MAP Shell 提供向请求添加应用参数（application parameters）的命令。必须在发送对应操作命令之前添加这些参数。

<a id="adding-application-parameters"></a>

#### 42.2.7.1 添加应用参数（Adding Application Parameters）

可以使用 `map add_header app_param` 命令添加应用参数：

```text
uart:~$ map add_header app_param max_list_count 10
Added MaxListCount: 10
uart:~$ map add_header app_param list_start_offset 0
Added ListStartOffset: 0
uart:~$ map add_header app_param charset utf8
Added Charset: utf8 (1)
uart:~$
```

<a id="listing-application-parameters"></a>

#### 42.2.7.2 列出应用参数（Listing Application Parameters）

查看全部已添加的应用参数：

```text
uart:~$ map add_header app_param list
Added application parameters (3):
  [0] Tag=0x01, Len=2
00000000: 00 0a                                            |..               |
  [1] Tag=0x02, Len=2
00000000: 00 00                                            |..               |
  [2] Tag=0x14, Len=1
00000000: 01                                               |.                |
uart:~$
```

<a id="clearing-application-parameters"></a>

#### 42.2.7.3 清除应用参数（Clearing Application Parameters）

清除全部已添加的应用参数：

```text
uart:~$ map add_header app_param clear
Cleared all application parameters
uart:~$
```

<a id="example-get-message-listing-with-filters"></a>

#### 42.2.7.4 示例：带过滤条件获取消息列表（Example: Get Message Listing with Filters）

```text
uart:~$ map add_header app_param max_list_count 10
Added MaxListCount: 10
uart:~$ map add_header app_param filter_msg_type 1f
Added FilterMessageType: 0x1f
  EMAIL=Y, SMS_GSM=Y, SMS_CDMA=Y, MMS=Y, IM=Y
uart:~$ map add_header app_param filter_read_status unread
Added FilterReadStatus: unread (1)
uart:~$ map mce mas get_msg_listing
MCE MAS 0x20005a00 get_msg_listing rsp, rsp_code Continue, data len 252
...
uart:~$ map add_header app_param clear
Cleared all application parameters
uart:~$
```

> 译注——日志完整性：本页代码框中的 `...` 来自官方示例本身。不同模式下的两端日志分别保留，不补造中间请求或响应。应用参数应在发起请求前添加；本例收到 `Continue` 后仍需依据所用传输模式完成后续交互，不能把这一行当作完整消息已经接收。

<a id="additional-information"></a>

## 42.3 补充信息（Additional Information）

<a id="rfcomm-vs-l2cap-transport"></a>

### 42.3.1 RFCOMM 与 L2CAP 传输比较（RFCOMM vs L2CAP Transport）

<a id="id29"></a>

#### 42.3.1.1 RFCOMM 传输（RFCOMM Transport）

执行 GET 或 PUT 操作时，必须多次调用同一 Shell 命令，直到完整消息传输结束。

<a id="id30"></a>

#### 42.3.1.2 启用 SRM 的 L2CAP 传输（L2CAP Transport with SRM）

启用单响应模式（Single Response Mode，SRM）时，无需重复 GET 请求，服务端会发送所有响应数据包。对于 PUT 操作，客户端发送所有请求数据包而不等待中间响应；服务端收到最终 PUT 请求后发送一个响应。

<a id="id31"></a>

#### 42.3.1.3 启用 SRM 和 SRMP 的 L2CAP 传输（L2CAP Transport with SRM and SRMP）

同时启用 SRM 和单响应模式参数（Single Response Mode Parameter，SRMP）时，需要继续发送 GET 请求和 PUT 响应，直到 SRMP 被禁用。

<a id="srm-single-response-mode"></a>

### 42.3.2 单响应模式（SRM (Single Response Mode)）

L2CAP 传输（GOEP v2.0）会自动启用 SRM。

<a id="get-operations"></a>

#### 42.3.2.1 GET 操作（GET Operations）

GET 操作启用 SRM 时：

客户端只发送一个 GET 请求。

服务端连续发送多个响应数据包，无需等待额外请求。

可以使用 `srmp` 参数控制流量，使传输等待下一次请求。

<a id="put-operations"></a>

#### 42.3.2.2 PUT 操作（PUT Operations）

PUT 操作启用 SRM 时：

客户端连续发送多个 PUT 请求，无需等待额外响应。

服务端收到最终 PUT 请求时，发送一个 PUT 响应。

可以使用 `srmp` 参数控制流量，使传输等待下一次响应。

<a id="multiple-instance-support"></a>

### 42.3.3 多实例支持（Multiple Instance Support）

MAP Shell 支持多个 MAS 实例（instance）：

MCE 可以同时连接多个 MSE MAS 实例。

MSE 可以注册多个具有不同实例 ID 的 MAS 实例。

使用 `select` 命令在实例之间切换。

```text
uart:~$ map mce mas select 0
Selected MCE MAS instance_id 0 as default
uart:~$
```


对应官方文档源码：[doc/services/connectivity/bluetooth/shell/classic/map.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/doc/services/connectivity/bluetooth/shell/classic/map.rst)。

> 译注——源码跟踪：本仓库的[对应源码](../../../doc/services/connectivity/bluetooth/shell/classic/map.rst)可用于跟踪，版本可能与网页不同；本批仅翻译和核对文档，没有执行固件构建、模拟运行或烧录。

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：经典蓝牙L2CAP_Shell](P041_经典蓝牙L2CAP_Shell.md) · [本模块主线目录](../reading/bluetooth.md) · [全部主线](../reading/README.md) · [下一篇：电话簿访问配置文件PBAP_Shell](P043_电话簿访问配置文件PBAP_Shell.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章](P041_经典蓝牙L2CAP_Shell.md) · [返回大纲](大纲.md) · [下一章](P043_电话簿访问配置文件PBAP_Shell.md)

</details>

<!-- reading-navigation:end -->
