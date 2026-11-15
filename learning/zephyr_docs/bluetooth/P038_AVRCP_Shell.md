---
id: learning.zephyr-docs.bluetooth.page-38
title: AVRCP_Shell
kind: reference
status: maintained
domains: [zephyr, bluetooth, documentation]
source_url: https://docs.zephyrproject.org/latest/services/connectivity/bluetooth/shell/classic/avrcp.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="bluetooth-classic-avrcp-shell"></a>

# 第38章\_AVRCP\_Shell

原文：[官方页面](https://docs.zephyrproject.org/latest/services/connectivity/bluetooth/shell/classic/avrcp.html)。读取日期：2026-10-14；保存的 latest 页面及 HTML 摘要见[来源记录](../SOURCES.md)。

> 译注——使用前提：以下命令在启用了对应蓝牙功能的目标固件Zephyr Shell中执行，初始化与接入方式见[蓝牙Shell](P007_蓝牙Shell.md)。代码中的 `uart:~$` 是提示符，其后输出是原文预期结果；输入命令时不复制提示符和日志。若命令不可用或初始化失败，应先检查目标配置、控制器能力及当前版本帮助，再继续连接或传输步骤。本批仅翻译与核对文档，未连接设备或执行这些命令。

> 译注——角色：控制方（CT）和目标方（TG）指 AVRCP 的角色，不能与蓝牙协议栈中的控制器（Controller）硬件概念混同。下面帮助中的命令拼写和输出保留英文，以便与固件对照。

本文说明如何通过 Shell 命令使用经典蓝牙（Bluetooth Classic）的音视频远程控制配置文件（Audio/Video Remote Control Profile，AVRCP）功能。`avrcp` 命令同时提供控制方（Controller，CT）和目标方（Target，TG）角色，用于操作 AVRCP 的控制与浏览功能。

有两个子命令：`avrcp ct` 和 `avrcp tg`。前者提供控制方（CT）功能，后者提供目标方（TG）功能。

<a id="prerequisites"></a>

## 38.1 前提条件（Prerequisites）

运行 `avrcp` Shell 前，确保构建配置已启用经典蓝牙和 Shell。必须先建立与对端设备的 BR/EDR ACL 连接（通常使用通用 `bt` Shell 命令），然后才能创建 AVRCP 控制连接或浏览连接。

<a id="commands"></a>

### 38.1.1 命令（Commands）

除了 `avrcp ct register_cb` 和 `avrcp tg register_cb`，其余命令都只能在建立 ACL 连接后使用。

`avrcp` 命令如下：

```text
uart:~$ avrcp
avrcp - Bluetooth AVRCP shell commands
Subcommands:
  connect                : connect AVRCP
  disconnect             : disconnect AVRCP
  browsing_connect       : connect browsing AVRCP
  browsing_disconnect    : disconnect browsing AVRCP
  ct                     : AVRCP CT shell commands
  tg                     : AVRCP TG shell commands
```

`avrcp ct` 命令如下：

```text
uart:~$ avrcp ct
ct - AVRCP CT shell commands
Subcommands:
  register_cb                 : register avrcp ct callbacks
  get_unit                    : get unit info
  get_subunit                 : get subunit info
  get_caps                    : get capabilities <cap_id: company or events>
  play                        : request a play at the remote player
  pause                       : request a pause at the remote player
  register_notification       : register notify <event_id> [playback_interval]
  set_browsed_player          : set browsed player <player_id>
  get_folder_items            : [none]
  change_path                 : [none]
  get_item_attrs              : get item attrs [scope]
  get_total_number_of_items   : get total number of items [scope]
  search                      : search [search_string]
  list_app_attrs              : [none]
  list_app_vals               : List App vals <attr_id>
  get_app_curr                : Get curr player app setting val [attr1] [attr2] ...
  set_app_val                 : Set app setting Val <attr1> <val1> [<attr2> <val2>] ...
  get_app_attr_text           : Get app setting attrs text <attr1> [attr2] ...
  get_app_val_text            : Get setting vals Text <attr_id> <val1> [val2] ...
  inform_displayable_char     : Inform Displayable Character Set <charset_id1> [charset_id2] ...
  inform_batt                 : Inform Battery Status Of CT <Battery status>
  set_absolute_volume         : set absolute volume <volume>
  get_element_attrs           : get element attrs [identifier] [attr1] [attr2] ...
  get_play_status             : [none]
  set_addressed_player        : set addressed player <player_id>
  play_item                   : PlayItem <scope> <uid_hex> <uid_counter>
  add_to_now_playing          : AddToNowPlaying <scope> <uid_hex> <uid_counter>
```

`avrcp tg` 命令如下：

```text
uart:~$ avrcp tg
tg - AVRCP TG shell commands
Subcommands:
  register_cb                                : register avrcp tg callbacks
  send_unit_rsp                              : send unit info response
  send_subunit_rsp                           : [none]
  send_get_caps_rsp                          : send get capabilities response [status]
  send_notification_rsp                      : send notify rsp <event_id> <type> [value...]
  send_browsed_player_rsp                    : Send SetBrowsedPlayer response
  send_get_folder_items_rsp                  : send get folder items [status]
  send_change_path_rsp                       : send change path [status]
  send_get_item_attrs_rsp                    : send get item attrs [status]
  send_get_total_number_of_items_rsp         : send get total number of items [status]
  send_search_rsp                            : search [status]
  send_browsing_general_reject               : send browsing general reject [reason]
  send_passthrough_rsp                       : send_passthrough_rsp <op/opvu> <opid> <state>
  send_list_player_app_setting_attrs_rsp     : send attrs rsp <num> [attr_id...]
  send_list_player_app_setting_vals_rsp      : send vals rsp <num> [val_id...]
  send_get_curr_player_app_setting_val_rsp   : send current vals rsp <num_pairs> [attr val]...
  send_set_player_app_setting_val_rsp        : set app setting val rsp [status]
  send_get_player_app_setting_attr_text_rsp  : send get player app setting attr text rsp [status]
  send_get_player_app_setting_val_text_rsp   : send get player app setting val text rsp [status]
  send_inform_displayable_char_rsp           : send displayable char rsp [status]
  send_inform_batt_status_of_ct_rsp          : send inform batt rsp [status]
  send_get_element_attrs_rsp                 : send get element attrs response<large: 1>
  send_absolute_volume_rsp                   : send absolute volume rsp <volume>
  send_get_play_status_rsp                   : send get play status [status]
  send_set_addressed_player_rsp              : send set addressed player rsp [status]
  send_play_item_rsp                         : send play item rsp [status]
  send_add_to_now_playing_rsp                : send add to now playing rsp [status]
```

<a id="basic-avrcp-operations"></a>
<a id="avrcp-basic-operations"></a>

### 38.1.2 AVRCP 基本操作（Basic AVRCP Operations）

双方分别使用 `avrcp ct register_cb` 和 `avrcp tg register_cb` 注册 AVRCP 回调。

使用 `avrcp connect` 创建 AVRCP 连接。

CT 使用 `avrcp ct get_caps events` 获取 TG 的能力（capabilities）。

CT 使用 `avrcp ct register_notification 0x01` 注册通知（notification）。

CT 使用 `avrcp ct play` 请求播放控制。

CT 使用 `avrcp ct get_play_status` 获取当前播放状态。

CT 使用 `avrcp ct get_element_attrs` 获取元素属性（element attributes），也就是元数据（metadata）。

CT 使用 `avrcp ct set_absolute_volume 50` 设置音量。

CT 使用 `avrcp ct pause` 暂停播放。

**注意（Note）**

CT（控制方）发送命令，TG（目标方）作出响应。对于支持通知的事件，TG 通常在注册后立即发送临时响应（INTERIM），报告当前值；实际值发生变化后，再发送变化响应（CHANGED）。

**设备 A：控制方 CT（Device A (CT - Controller)）**

<a id="tab-0-RGV2aWNlIEEgKENUIC0gQ29udHJvbGxlcik="></a>
<a id="panel-0-RGV2aWNlIEEgKENUIC0gQ29udHJvbGxlcik="></a>

```text
uart:~$ avrcp ct register_cb
AVRCP CT callbacks registered
uart:~$ avrcp connect
AVRCP CT connected
uart:~$ avrcp ct get_caps events
GetCapabilities : status=0x04
Remote supported EventID = 0x01
Remote supported EventID = 0x02
Remote supported EventID = 0x0d
uart:~$ avrcp ct register_notification 0x01
Get capabilities command sent successfully: cap_id=events
Sent register notification event_id=0x01
AVRCP notification rsp: tid=0x01, status=0x04, event_id=0x01
 Notification type: INTERIM
 PLAYBACK_STATUS_CHANGED: status=0x00
uart:~$ avrcp ct play
Passthrough PRESSED command sent successfully: opid=0x44
Passthrough RELEASED command sent successfully: opid=0x44
<input `avrcp tg send_passthrough_rsp op play pressed` in TG side>
AVRCP passthrough command accepted, operation id = 0x44, state = 0
<input `avrcp tg send_passthrough_rsp op play released` in TG side>
AVRCP passthrough command accepted, operation id = 0x44, state = 1
<input `avrcp tg send_notification_rsp 0x01 changed 1` in TG side>
AVRCP notification rsp: tid=0x01, status=0x04, event_id=0x01
 Notification type: CHANGED
 PLAYBACK_STATUS_CHANGED: status=0x01
uart:~$ avrcp ct get_play_status
AVRCP GetPlayStatus
getplaystatus : status=0x04
GetPlayStatus: len=180000 ms, pos=30000 ms, status=0x01
 status: PLAYING
uart:~$ avrcp ct get_element_attrs
Requesting element attributes: identifier=0x0000000000000000, num_attrs=0
AVRCP CT get element attrs command sent
GetElementAttributes : status=0x04
AVRCP GetElementAttributes response received, tid=0x05, num_attrs=7
 Attr[0]: ID=0x00000001 (TITLE), charset=0x006a, len=11
   Value: "Test Title"
 Attr[1]: ID=0x00000002 (ARTIST), charset=0x006a, len=11
   Value: "Test Artist"
uart:~$ avrcp ct set_absolute_volume 50
set absolute volume absolute_volume=0x32
AVRCP set absolute volume rsp: tid=0x02, status=0x04, volume=0x32
uart:~$ avrcp ct pause
Passthrough PRESSED command sent successfully: opid=0x46
Passthrough RELEASED command sent successfully: opid=0x46
<input `avrcp tg send_passthrough_rsp op pause pressed` in TG side>
AVRCP passthrough command accepted, operation id = 0x46, state = 0
<input `avrcp tg send_passthrough_rsp op pause released` in TG side>
AVRCP passthrough command accepted, operation id = 0x46, state = 1
```

**设备 B：目标方 TG（Device B (TG - Target)）**

<a id="tab-0-RGV2aWNlIEIgKFRHIC0gVGFyZ2V0KQ=="></a>
<a id="panel-0-RGV2aWNlIEIgKFRHIC0gVGFyZ2V0KQ=="></a>

```text
uart:~$ avrcp tg register_cb
AVRCP TG callbacks registered
<input `avrcp connect` in CT side>
AVRCP TG connected
<input `avrcp ct get_caps events` in CT side>
AVRCP get capabilities command received: cap_id 0x03 (EVENTS_SUPPORTED)
uart:~$ avrcp tg send_get_caps_rsp
Get capabilities response sent successfully
<input `avrcp ct register_notification 0x01` in CT side>
receive register notification request event_id=0x01
uart:~$ avrcp tg send_notification_rsp 0x01 interim 0
Sent notification rsp event_id=0x01 type=interim
<input `avrcp ct play` in CT side>
receive passthrough command: op_id=0x44 (PLAY)
uart:~$ avrcp tg send_passthrough_rsp op play pressed
Passthrough opid=0x44 (STANDARD), state=pressed sent successfully
uart:~$ avrcp tg send_passthrough_rsp op play released
Passthrough opid=0x44 (STANDARD), state=released sent successfully
uart:~$ avrcp tg send_notification_rsp 0x01 changed 1
Sent notification rsp event_id=0x01 type=changed
<input `avrcp ct get_play_status` in CT side>
receive get play status request
uart:~$ avrcp tg send_get_play_status_rsp
GetPlayStatus rsp sent
<input `avrcp ct get_element_attrs` in CT side>
AVRCP GetElementAttributes command received
uart:~$ avrcp tg send_get_element_attrs_rsp 0
Sending standard GetElementAttributes response (7 attrs)
GetElementAttributes response sent successfully
<input `avrcp ct set_absolute_volume 50` in CT side>
AVRCP set_absolute_volume_req: tid=0x06, absolute_volume=0x32
uart:~$ avrcp tg send_absolute_volume_rsp 50
Set absolute volume response sent successfully
<input `avrcp ct pause` in CT side>
AVRCP passthrough command received: opid = 0x46
uart:~$ avrcp tg send_passthrough_rsp op pause pressed
send passthrough response
uart:~$ avrcp tg send_passthrough_rsp op pause released
send passthrough response
```

<a id="avrcp-connection"></a>

### 38.1.3 AVRCP 连接（AVRCP Connection）

AVRCP 配置文件（profile）同时支持控制连接和浏览连接。控制连接用于基本远程控制，浏览连接用于浏览媒体内容。

<a id="control-connection"></a>

#### 38.1.3.1 控制连接（Control Connection）

建立 AVRCP 控制连接：

在 CT 端注册回调：

```text
uart:~$ avrcp ct register_cb
AVRCP CT callbacks registered
```

在 TG 端注册回调：

```text
uart:~$ avrcp tg register_cb
AVRCP TG callbacks registered
```

连接 AVRCP：

```text
uart:~$ avrcp connect
AVRCP CT connected
AVRCP TG connected
```

断开 AVRCP：

```text
uart:~$ avrcp disconnect
AVRCP CT disconnected
AVRCP TG disconnected
```

<a id="browsing-connection"></a>

#### 38.1.3.2 浏览连接（Browsing Connection）

控制连接建立后，可以发起浏览连接：

连接浏览通道：

```text
uart:~$ avrcp browsing_connect
AVRCP browsing connect request sent
AVRCP CT browsing connected
AVRCP TG browsing connected
```

断开浏览通道：

```text
uart:~$ avrcp browsing_disconnect
AVRCP browsing disconnect request sent
AVRCP CT browsing disconnected
AVRCP TG browsing disconnected
```

<a id="basic-playback-control"></a>

### 38.1.4 基本播放控制（Basic Playback Control）

从 CT 端控制播放：

**播放命令（Play Command）**

<a id="tab-1-UGxheSBDb21tYW5k"></a>
<a id="panel-1-UGxheSBDb21tYW5k"></a>

```text
uart:~$ avrcp ct play
Passthrough PRESSED command sent successfully: opid=0x44
Passthrough RELEASED command sent successfully: opid=0x44
```

**暂停命令（Pause Command）**

<a id="tab-1-UGF1c2UgQ29tbWFuZA=="></a>
<a id="panel-1-UGF1c2UgQ29tbWFuZA=="></a>

```text
uart:~$ avrcp ct pause
Passthrough PRESSED command sent successfully: opid=0x46
Passthrough RELEASED command sent successfully: opid=0x46
```

<a id="get-capabilities"></a>

### 38.1.5 获取能力（Get Capabilities）

查询支持的能力：

**公司标识符（Company ID）**

<a id="tab-2-Q29tcGFueSBJRA=="></a>
<a id="panel-2-Q29tcGFueSBJRA=="></a>

```text
uart:~$ avrcp ct get_caps company
Get capabilities command sent successfully: cap_id=company
GetCapabilities : status=0x04
Remote CompanyID = 0x001958
```

**支持的事件（Events Supported）**

<a id="tab-2-RXZlbnRzIFN1cHBvcnRlZA=="></a>
<a id="panel-2-RXZlbnRzIFN1cHBvcnRlZA=="></a>

```text
uart:~$ avrcp ct get_caps events
Get capabilities command sent successfully: cap_id=events
GetCapabilities : status=0x04
Remote supported EventID = 0x01
Remote supported EventID = 0x02
Remote supported EventID = 0x03
Remote supported EventID = 0x04
Remote supported EventID = 0x0d
```

**TG 响应（TG Response）**

<a id="tab-2-VEcgUmVzcG9uc2U="></a>
<a id="panel-2-VEcgUmVzcG9uc2U="></a>

```text
uart:~$ avrcp tg send_get_caps_rsp
Sending company ID capability rsp: 0x001958
```

<a id="media-metadata-operations"></a>

### 38.1.6 媒体元数据操作（Media Metadata Operations）

<a id="get-element-attributes"></a>

#### 38.1.6.1 获取元素属性（Get Element Attributes）

获取当前播放媒体的元数据：

**CT 请求（CT Request）**

<a id="tab-3-Q1QgUmVxdWVzdA=="></a>
<a id="panel-3-Q1QgUmVxdWVzdA=="></a>

```text
uart:~$ avrcp ct get_element_attrs
Requesting element attributes: identifier=0x0000000000000000, num_attrs=0
AVRCP CT get element attrs command sent
GetElementAttributes : status=0x04
AVRCP GetElementAttributes response received, tid=0x00, num_attrs=7
 Attr[0]: ID=0x00000001 (TITLE), charset=0x006a, len=11
   Value: "Test Title"
 Attr[1]: ID=0x00000002 (ARTIST), charset=0x006a, len=11
   Value: "Test Artist"
 Attr[2]: ID=0x00000003 (ALBUM), charset=0x006a, len=10
   Value: "Test Album"
 Attr[3]: ID=0x00000004 (TRACK_NUMBER), charset=0x006a, len=1
   Value: "1"
 Attr[4]: ID=0x00000005 (TOTAL_TRACKS), charset=0x006a, len=2
   Value: "10"
 Attr[5]: ID=0x00000006 (GENRE), charset=0x006a, len=4
   Value: "Rock"
 Attr[6]: ID=0x00000007 (PLAYING_TIME), charset=0x006a, len=6
   Value: "240000"
```

**TG 响应（TG Response）**

<a id="tab-3-VEcgUmVzcG9uc2U="></a>
<a id="panel-3-VEcgUmVzcG9uc2U="></a>

```text
uart:~$ avrcp tg send_get_element_attrs_rsp 0
Sending standard GetElementAttributes response (7 attrs)
GetElementAttributes response sent successfully
```

<a id="play-status"></a>

#### 38.1.6.2 播放状态（Play Status）

获取当前播放状态：

**CT 请求（CT Request）**

<a id="tab-4-Q1QgUmVxdWVzdA=="></a>
<a id="panel-4-Q1QgUmVxdWVzdA=="></a>

```text
uart:~$ avrcp ct get_play_status
AVRCP GetPlayStatus
getplaystatus : status=0x04
GetPlayStatus: len=180000 ms, pos=30000 ms, status=0x01
 status: PLAYING
```

**TG 响应（TG Response）**

<a id="tab-4-VEcgUmVzcG9uc2U="></a>
<a id="panel-4-VEcgUmVzcG9uc2U="></a>

```text
uart:~$ avrcp tg send_get_play_status_rsp
GetPlayStatus rsp sent
```

<a id="volume-control"></a>

### 38.1.7 音量控制（Volume Control）

设置绝对音量（absolute volume）：

**CT 设置音量（CT Set Volume）**

<a id="tab-5-Q1QgU2V0IFZvbHVtZQ=="></a>
<a id="panel-5-Q1QgU2V0IFZvbHVtZQ=="></a>

```text
uart:~$ avrcp ct set_absolute_volume 50
set absolute volume absolute_volume=0x32
AVRCP set absolute volume rsp: tid=0x01, status=0x04, volume=0x32
```

**TG 响应（TG Response）**

<a id="tab-5-VEcgUmVzcG9uc2U="></a>
<a id="panel-5-VEcgUmVzcG9uc2U="></a>

```text
uart:~$ avrcp tg send_absolute_volume_rsp 50
Set absolute volume response sent successfully
```

<a id="event-notifications"></a>

### 38.1.8 事件通知（Event Notifications）

注册通知并处理事件：

<a id="register-for-volume-change-notification"></a>

#### 38.1.8.1 注册音量变化通知（Register for Volume Change Notification）

**CT 注册（CT Register）**

<a id="tab-6-Q1QgUmVnaXN0ZXI="></a>
<a id="panel-6-Q1QgUmVnaXN0ZXI="></a>

```text
uart:~$ avrcp ct register_notification 0x0d
Sent register notification event_id=0x0d
AVRCP notification rsp: tid=0x02, status=0x04, event_id=0x0d
 Notification type: INTERIM
 VOLUME_CHANGED: absolute_volume=0x0a
AVRCP notify_changed_cb received: event_id=0x0d
 Notification type: CHANGED
 VOLUME_CHANGED: absolute_volume=0x14
```

**TG 发送通知（TG Send Notification）**

<a id="tab-6-VEcgU2VuZCBOb3RpZmljYXRpb24="></a>
<a id="panel-6-VEcgU2VuZCBOb3RpZmljYXRpb24="></a>

```text
uart:~$ avrcp tg send_notification_rsp 0x0d interim 10
Sent notification rsp event_id=0x0d type=interim

uart:~$ avrcp tg send_notification_rsp 0x0d changed 20
Sent notification rsp event_id=0x0d type=changed
```

<a id="browsing-operations"></a>

### 38.1.9 浏览操作（Browsing Operations）

<a id="set-browsed-player"></a>

#### 38.1.9.1 设置被浏览的播放器（Set Browsed Player）

**CT 请求（CT Request）**

<a id="tab-7-Q1QgUmVxdWVzdA=="></a>
<a id="panel-7-Q1QgUmVxdWVzdA=="></a>

```text
uart:~$ avrcp ct set_browsed_player 1
AVRCP send set browsed player req
AVRCP set browsed player success, tid = 0
  UID Counter: 1
  Number of Items: 100
  Charset ID: 0x006A
  Folder Depth: 1
  charset_id  : 0x006A
  Get folder Name (hex)  :
00000000: 4d 75 73 69 63                                   |Music            |
```

**TG 响应（TG Response）**

<a id="tab-7-VEcgUmVzcG9uc2U="></a>
<a id="panel-7-VEcgUmVzcG9uc2U="></a>

```text
uart:~$ avrcp tg send_browsed_player_rsp
Send set browsed player response, status = 0x04
```

<a id="get-folder-items"></a>

#### 38.1.9.2 获取文件夹条目（Get Folder Items）

**CT 请求（CT Request）**

<a id="tab-8-Q1QgUmVxdWVzdA=="></a>
<a id="panel-8-Q1QgUmVxdWVzdA=="></a>

```text
uart:~$ avrcp ct get_folder_items
Sent GetFolderItems command
AVRCP get folder items success, tid = 1
  UID Counter: 1
  Number of Items: 1
Media Player Item:
  item_len   : 28
  player_id   : 1
  major_type  : 0x01
  sub_type    : 0x00000000
  play_status : 0x00
  charset_id  : 0x006A
  name_len    : 4
  charset_id  : 0x006A
  Name (hex)  :
00000000: 44:65:6d:6f                                      |Demo
```

**TG 响应（TG Response）**

<a id="tab-8-VEcgUmVzcG9uc2U="></a>
<a id="panel-8-VEcgUmVzcG9uc2U="></a>

```text
uart:~$ avrcp tg send_get_folder_items_rsp
TG: Sent GetFolderItems response
```

<a id="player-application-settings"></a>

### 38.1.10 播放器应用设置（Player Application Settings）

列出并获取播放器应用设置：

<a id="list-available-settings"></a>

#### 38.1.10.1 列出可用设置（List Available Settings）

**CT 请求（CT Request）**

<a id="tab-9-Q1QgUmVxdWVzdA=="></a>
<a id="panel-9-Q1QgUmVxdWVzdA=="></a>

```text
uart:~$ avrcp ct list_app_attrs
Sent list player app setting attrs
list player app setting attrs : status=0x04
attr =0x01 (EQUALIZER)
attr =0x02 (REPEAT_MODE)
```

**TG 响应（TG Response）**

<a id="tab-9-VEcgUmVzcG9uc2U="></a>
<a id="panel-9-VEcgUmVzcG9uc2U="></a>

```text
uart:~$ avrcp tg send_list_player_app_setting_attrs_rsp 2 0x01 0x02
TG: Sent list player app setting attrs response
```

<a id="get-current-settings"></a>

#### 38.1.10.2 获取当前设置（Get Current Settings）

**CT 请求（CT Request）**

<a id="tab-10-Q1QgUmVxdWVzdA=="></a>
<a id="panel-10-Q1QgUmVxdWVzdA=="></a>

```text
uart:~$ avrcp ct get_app_curr 1 2
Sent get_curr_player_app_setting_val num=2
get curr player app setting val : status=0x04
attr_id :1 val 1
attr_id :2 val 1
```

**TG 响应（TG Response）**

<a id="tab-10-VEcgUmVzcG9uc2U="></a>
<a id="panel-10-VEcgUmVzcG9uc2U="></a>

```text
uart:~$ avrcp tg send_get_curr_player_app_setting_val_rsp 2 0x01 0x01 0x02 0x02
TG: Send get curr player app setting val rsp (num=2)
```

> 译注——原日志差异：本节 CT 日志中的当前设置值为 1、1，而 TG 响应命令设置的是 1、2。两段原文均完整保留；它们不能作为同一次请求和响应完全一致的验证记录。


对应官方文档源码：[doc/services/connectivity/bluetooth/shell/classic/avrcp.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/doc/services/connectivity/bluetooth/shell/classic/avrcp.rst)。

> 译注——源码跟踪：本仓库的[对应源码](../../../doc/services/connectivity/bluetooth/shell/classic/avrcp.rst)可用于跟踪，版本可能与网页不同；本批仅翻译和核对文档，没有执行固件构建、模拟运行或烧录。

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：A2DP_Shell](P037_A2DP_Shell.md) · [本模块主线目录](../reading/bluetooth.md) · [全部主线](../reading/README.md) · [下一篇：GOEP_Shell](P039_GOEP_Shell.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章](P037_A2DP_Shell.md) · [返回大纲](大纲.md) · [下一章](P039_GOEP_Shell.md)

</details>

<!-- reading-navigation:end -->
