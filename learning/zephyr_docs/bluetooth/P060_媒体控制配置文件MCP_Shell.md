---
id: learning.zephyr-docs.bluetooth.page-60
title: 媒体控制配置文件MCP_Shell
kind: reference
status: maintained
domains: [zephyr, bluetooth, documentation]
source_url: https://docs.zephyrproject.org/latest/services/connectivity/bluetooth/shell/audio/mcp.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="bluetooth-media-control-profile-shell"></a>

# 第60章\_蓝牙：媒体控制配置文件 Shell（Bluetooth: Media Control Profile Shell）

原文：[官方页面](https://docs.zephyrproject.org/latest/services/connectivity/bluetooth/shell/audio/mcp.html)。快照读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

> 译注——操作上下文：代码块中的命令在启用了相应音频功能的目标固件 Zephyr Shell 中执行，接入与初始化见[蓝牙 Shell](P007_蓝牙Shell.md)。`uart:~$` 是提示符，后续日志是官方预期输出；不要把提示符、日志或 `<address>` 等占位符原样当作主机终端命令运行。各示例代表不同角色和操作分支，按实际连接与初始化状态选择，不连贯粘贴整章。命令缺失、初始化失败或发现未完成时，应先核对固件配置、控制器能力及当前版本帮助，再继续后续操作。

> 译注——版本与验证：原文“当前”“尚未实现”等表述均保留其快照语境。代码块完整保留原始命令、帮助和输出，本文没有执行固件构建、连接音频设备或验证互操作性。

> 译注——术语：MCP 是媒体控制配置文件（Media Control Profile），MCC 是媒体控制客户端（Media Control Client）。原页的小标题将客户端写作 MCP，本译文保留该标题来源并在这里区分。ATT 是属性协议（Attribute Protocol），GATT 是通用属性配置文件（Generic Attribute Profile）。原文明确说明搜索结果与部分通知值是模拟数据，不能据示例输出认定真实媒体内容已被检索或播放。

本文说明如何通过 Shell 以客户端与服务端两种角色运行媒体控制功能。

媒体控制服务端由两部分组成：媒体播放器（media player，mpl）包含处理媒体的逻辑，媒体控制服务（media control service，mcs）为播放器提供基于 GATT 的接口。媒体控制客户端只有一个部分，即基于 GATT 的客户端 mcc。

媒体控制服务端可以包含对象传输服务（Object Transfer Service，ots），媒体控制客户端可以包含对象传输客户端（Object Transfer Client，otc）。包含这些组件后，可以使用更丰富的功能。

媒体控制服务端与客户端都只实现通用媒体控制服务（Generic Media Control Service，GMCS），不使用底层的其他媒体控制服务。

下方示例在许多情况下按原文移除了调试输出，也可能缩短较长输出，以使示例更简短清晰。

本文没有列出所有 Shell 命令，仅展示其中一部分示例。可以输入 `mcc` 或 `mpl` 后按 TAB，查看对应 Shell 的命令集合；通过 `mcc <command> help` 或 `mpl <command> help` 获取每条命令的帮助文本。

<a id="overview"></a>

## 60.1 概览（Overview）

媒体播放器具有名称与图标，便于用户识别。

播放器内容组织为曲目（track）与组（group）。一个播放器可以有多个组，一个组可以包含曲目和其他组；但在此实现中，组只能包含曲目，不能包含其他组。曲目还可以划分为分段（segment）。

活动播放器具有当前曲目；处于播放状态时，它就是正在播放的曲目。当前曲目包含标题、时长（单位为百分之一秒）和位置，即播放器在曲目中的当前位置。

还存在当前组（当前曲目所属组）、父组（当前组的父组）和下一曲目。

播放器处于播放（playing）、暂停（paused）、搜寻（seeking）或不活动（inactive）状态之一。播放时采用指定播放速度，按某个受支持的播放顺序播放曲目。曲目变化通过曲目变化特征（track changed characteristic）的通知发出。搜寻即快进或快退，曲目位置按搜寻速度移动。

支持的操作码（opcode）表示可以通过写入媒体控制点（media control point）请求哪些播放器操作。还有一个搜索控制点（search control point），允许按不同条件搜索组与曲目，并通过搜索结果返回匹配内容。

内容控制标识（Content Control ID）用于将媒体播放器与音频流关联。

<a id="media-control-client-mcp"></a>

## 60.2 媒体控制客户端（原文标题：Media Control Client，MCP）

媒体控制客户端用于控制媒体控制服务端并从中获取信息。控制通过写入两个控制点之一或其他可写特征完成；获取信息则通过读取特征，或配置服务端发送通知完成。

<a id="using-the-media-control-client"></a>

### 60.2.1 使用媒体控制客户端（Using the media control client）

使用前，必须通过 `mcc init` 初始化媒体控制客户端。

要建立到对端的连接，使用 `bt` 命令：先执行 `bt init`，再执行 `bt advertise on`；如果服务端正在广播，则执行 `bt connect`。

媒体控制客户端连接媒体控制服务端后，可以通过 `mcc discover_mcs` 发现服务端的 GMCS。该命令保存服务句柄，并可选地订阅所有通知；默认会订阅全部通知。

发现完成后，客户端可以读写特征，包括媒体控制点与搜索控制点。

<a id="example-usage"></a>

### 60.2.2 使用示例（Example usage）

<a id="setup"></a>

#### 60.2.2.1 准备（Setup）

```text
uart:~$ bt init
Bluetooth initialized

uart:~$ mcc init
MCC init complete

uart:~$ bt advertise on
Advertising started
Connected: R:F6:58:DC:27:F3:57
```

<a id="when-connected"></a>

#### 60.2.2.2 已连接时（When connected）

服务发现：GMCS 及其包含的 OTS。

```text
uart:~$ mcc discover_mcs
<dbg> bt_mcc.bt_mcc_discover_mcs: start discovery of MCS primary service
<dbg> bt_mcc.discover_primary_func: [ATTRIBUTE] handle 0x00ae
<dbg> bt_mcc.discover_primary_func: Primary discovery complete
<dbg> bt_mcc.discover_primary_func: UUID: 2800
<dbg> bt_mcc.discover_primary_func: UUID: 8fd7
<dbg> bt_mcc.discover_primary_func: Start discovery of MCS characteristics
<dbg> bt_mcc.discover_mcs_char_func: [ATTRIBUTE] handle 0x00b0
<dbg> bt_mcc.discover_mcs_char_func: Player name, UUID: 8fa0
<dbg> bt_mcc.discover_mcs_char_func: [ATTRIBUTE] handle 0x00b2
<dbg> bt_mcc.discover_mcs_char_func: Icon Object, UUID: 8fa1
<dbg> bt_mcc.discover_mcs_char_func: [ATTRIBUTE] handle 0x00b4
<dbg> bt_mcc.discover_mcs_char_func: Icon URI, UUID: 8fa2
<dbg> bt_mcc.discover_mcs_char_func: [ATTRIBUTE] handle 0x00b6
<dbg> bt_mcc.discover_mcs_char_func: Track Changed, UUID: 8fa3
<dbg> bt_mcc.discover_mcs_char_func: Subscribing - handle: 0x00b6
[...]
<dbg> bt_mcc.discover_mcs_char_func: [ATTRIBUTE] handle 0x00ea
<dbg> bt_mcc.discover_mcs_char_func: Content Control ID, UUID: 8fb5
<dbg> bt_mcc.discover_mcs_char_func: Setup complete for MCS
<dbg> bt_mcc.discover_mcs_char_func: Start discovery of included services
<dbg> bt_mcc.discover_include_func: [ATTRIBUTE] handle 0x00af
<dbg> bt_mcc.discover_include_func: Include UUID 1825
<dbg> bt_mcc.discover_include_func: Discover include complete for MCS: OTS
<dbg> bt_mcc.discover_include_func: Start discovery of OTS characteristics
<dbg> bt_mcc.discover_otc_char_func: [ATTRIBUTE] handle 0x009c
<dbg> bt_mcc.discover_otc_char_func: OTS Features
[...]
<dbg> bt_mcc.discover_otc_char_func: [ATTRIBUTE] handle 0x00ac
<dbg> bt_mcc.discover_otc_char_func: Object Size
Discovery complete
<dbg> bt_otc.bt_otc_register: 0
<dbg> bt_otc.bt_otc_register: L2CAP psm 0x  25 sec_level 1 registered
<dbg> bt_mcc.discover_otc_char_func: Setup complete for OTS 1 / 1
uart:~$
```

读取特征：以播放器名称与曲目时长为例。

```text
uart:~$ mcc read_player_name
Player name: My media player
4d 79 20 6d 65 64 69 61  20 70 6c 61 79 65 72    |My media  player

uart:~$ mcc read_track_duration
Track duration: 6300
```

某些特征的值可能过长，无法装入一个 ATT 数据包，因此会被截断；增大 ATT MTU 可能有帮助：

```text
uart:~$ mcc read_track_title
Track title: Interlude #1 (Song for

uart:~$ gatt exchange-mtu
Exchange pending
Exchange successful

uart:~$ mcc read_track_title
Track title: Interlude #1 (Song for Alison)
```

写入特征：以曲目位置为例。

曲目位置表示播放器当前位于当前曲目的何处。先读取位置，写入修改，然后再次读取确认。

```text
uart:~$ mcc read_track_position
Track Position: 0

uart:~$ mcc set_track_position 500
Track Position: 500

uart:~$ mcc read_track_position
Track Position: 500
```

通过控制点控制播放器：

写入控制点后，客户端可以请求服务端播放、暂停、快进、更换曲目、更换组等操作。有些操作，例如跳转到曲目，需要参数。原文当前使用原始操作码值作为控制点 Shell 命令的输入，并指向 `mpl.h` 头文件查找这些值。

> 译注——操作码位置：当前读取的[官方源码](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/include/zephyr/bluetooth/audio/mcs.h)及本仓库的[相对路径对照](../../../include/zephyr/bluetooth/audio/mcs.h)定义 `BT_MCS_OPC_PLAY = 0x01U`、`BT_MCS_OPC_PAUSE = 0x02U` 和 `BT_MCS_OPC_GOTO_TRACK = 0x34U`。因此原例的十进制 1、2、52 与这些定义对应；`mpl.h` 保留为原文指向的历史文件名。

依次发送播放命令（操作码“1”）、跳转到第 3 首曲目的命令（操作码“52”）以及暂停命令（操作码“2”）：

```text
uart:~$ mcc set_cp 1
Media State: 1
Operation: 1, result: 1
Operation: 1, param: 0

uart:~$ mcc set_cp 52 3
Track changed
Track title: Interlude #3 (Levanto Seventy)
Track duration: 7800
Track Position: 0
Current Track Object ID: 0x000000000104
Next Track Object ID: 0x000000000105
Operation: 52, result: 1
Operation: 52, param: 3

uart:~$ mcc set_cp 2
Media State: 2
Operation: 2, result: 1
Operation: 2, param: 0
```

<a id="using-the-included-object-transfer-client"></a>

#### 60.2.2.3 使用所包含的对象传输客户端（Using the included object transfer client）

客户端与服务端都支持对象传输时，可以使用更多特征，包括各类曲目对象与组对象的对象标识（object ID）。使用这些标识可以在服务端的对象传输服务中选择并下载对应对象。

读取当前组对象的对象标识：

```text
uart:~$ mcc read_current_group_obj_id
Current Group Object ID: 0x000000000107
```

选择具有该标识的对象：

```text
uart:~$ mcc ots_select 0x107
Selecting object succeeded
```

读取对象元数据：

```text
uart:~$ mcc ots_read_metadata
Reading object metadata succeeded
<inf> bt_mcc: Object's meta data:
<inf> bt_mcc:        Current size    :35
<inf> bt_otc: --- Displaying 1 metadata records ---
<inf> bt_otc: Object ID: 0x000000000107
<inf> bt_otc: Object name: Joe Pass - Guitar Inte
<inf> bt_otc: Object Current Size: 35
<inf> bt_otc: Object Allocate Size: 35
<inf> bt_otc: Type: Group Obj Type
<inf> bt_otc: Properties:0x4
<inf> bt_otc:  - read permitted
```

读取对象本身：

接收到的是组对象，由一系列记录组成，每条记录包含类型（曲目或组）及对象标识。

```text
uart:~$ mcc ots_read_current_group_object
<dbg> bt_mcc.on_group_content: Object type: 0, object  ID: 0x000000000102
<dbg> bt_mcc.on_group_content: Object type: 0, object  ID: 0x000000000103
<dbg> bt_mcc.on_group_content: Object type: 0, object  ID: 0x000000000104
<dbg> bt_mcc.on_group_content: Object type: 0, object  ID: 0x000000000105
<dbg> bt_mcc.on_group_content: Object type: 0, object  ID: 0x000000000106
```

<a id="search"></a>

#### 60.2.2.4 搜索（Search）

搜索控制点接受一串搜索控制项；每项包含长度、类型（例如曲目名或艺术家名）和参数（待搜索的曲目名或艺术家名）。搜索成功后，结果保存在对象传输服务的一个对象中，可以从搜索结果对象标识特征读取其标识，然后按前文下载当前组对象的方法下载搜索结果对象。执行搜索之前，搜索结果对象标识为空。

此实现具有可工作的搜索功能接口，以及服务端搜索控制点参数解析；但实际搜索是模拟的，无论搜索什么，都会返回相同结果。

搜索有两条命令：`mcc set_scp_raw` 允许以字符串输入搜索控制点参数，即搜索控制项序列；`mcc set_scp_ioptest` 执行预设互操作性（Interoperability，IOP）测试搜索，以 IOP 搜索控制点测试的轮次作为参数。

搜索之前，搜索结果对象标识为空。

```text
uart:~$ mcc read_search_results_obj_id
Search Results Object ID: 0x000000000000
<dbg> bt_mcc.mcc_read_search_results_obj_id_cb: Zero-length Search Results Object ID
```

运行与 IOP 测试第 4 轮对应的搜索：

此命令及参数生成的搜索控制点参数只有一个搜索控制项。长度字段是第一个八位字节，值为 16（0x10），不包括长度字段本身。类型字段是第二个八位字节，值为 0x04，表示按组名搜索；参数即待搜索的组名，为“TSPX_Group_Name”。

```text
uart:~$ mcc set_scp_ioptest 4
Search string:
00000000: 10 04 54 53 50 58 5f 47  72 6f 75 70 5f 4e 61 6d |..TSPX_G roup_Nam|
00000010: 65                                               |e                |
Search control point notification result code: 1
Search Results Object ID: 0x000000000107
Search Control Point set
```

搜索成功后，搜索结果对象标识具有一个值：

```text
uart:~$ mcc read_search_results_obj_id
Search Results Object ID: 0x000000000107
```

<a id="media-control-service-mcs"></a>

## 60.3 媒体控制服务（Media Control Service，MCS）

媒体控制服务 mcs 及其关联的媒体播放器 mpl，通常位于能提供媒体内容访问与服务的设备上，例如 PC 和智能手机。

如前所述，mpl 包含播放器逻辑，mcs 提供基于 GATT 的接口。将两者分离，是为了让媒体播放器也能在不使用 GATT 接口时工作。

<a id="using-the-media-control-service-and-the-media-player"></a>

### 60.3.1 使用媒体控制服务与媒体播放器（Using the media control service and the media player）

媒体控制服务与媒体播放器通常由媒体控制客户端远程控制。

使用前，原文称必须通过 `mpl init` 初始化“媒体控制客户端”。

> 译注——初始化对象：[官方源码](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/subsys/bluetooth/audio/shell/mpl.c)及本仓库的[相对路径对照](../../../subsys/bluetooth/audio/shell/mpl.c)将 `mpl init` 注册为“Initialize media player”，处理函数为 `cmd_media_proxy_pl_init()`，因此该命令初始化的是媒体播放器。前文客户端初始化命令为 `mcc init`，两者不可互换。

与客户端类似，使用 `bt` 命令建立连接：先执行 `bt init`，再执行 `bt connect <address> <address type>`；原文的另一分支是服务端广播时使用 `bt advertise on`。

<a id="id1"></a>

### 60.3.2 使用示例（Example Usage）

<a id="id2"></a>

#### 60.3.2.1 准备（Setup）

```text
uart:~$ bt init
Bluetooth initialized

uart:~$ mpl init
[Large amounts of debug output]

uart:~$ bt connect R:F9:33:3B:67:D2:A7
Connection pending
Connected: R:F9:33:3B:67:D2:A7
```

<a id="id3"></a>

#### 60.3.2.2 已连接时（When connected）

控制操作在客户端一侧完成。

服务端会输出与客户端执行的各项操作相关的调试信息。

示例：客户端发出“下一曲目”命令时，服务端的调试输出。

```text
[00:13:29.932,373] <dbg> bt_mcs.control_point_write: Opcode: 49
[00:13:29.932,403] <dbg> bt_mpl.mpl_operation_set: opcode: 49, param: 536880068
[00:13:29.932,403] <dbg> bt_mpl.paused_state_operation_handler: Operation opcode: 49
[00:13:29.932,495] <dbg> bt_mpl.do_next_track: Track ID before: 0x000000000104
[00:13:29.932,586] <dbg> bt_mpl.do_next_track: Track ID after: 0x000000000105
[00:13:29.932,617] <dbg> bt_mcs.mpl_track_changed_cb: Notifying track change
[00:13:29.932,708] <dbg> bt_mcs.mpl_track_title_cb: Notifying track title: Interlude #4 (Vesper Dreams)
[00:13:29.932,800] <dbg> bt_mcs.mpl_track_duration_cb: Notifying track duration: 13500
[00:13:29.932,861] <dbg> bt_mcs.mpl_track_position_cb: Notifying track position: 0
[00:13:29.933,044] <dbg> bt_mcs.mpl_current_track_id_cb: Notifying current track ID: 0x000000000105
[00:13:29.933,258] <dbg> bt_mcs.mpl_next_track_id_cb: Notifying next track ID: 0x000000000106
[00:13:29.933,380] <dbg> bt_mcs.mpl_operation_cb: Notifying control point - opcode: 49, result: 1
```

还提供了一些服务端命令，用来强制发送各种特征的通知，以测试客户端能否收到。由这些测试命令触发的通知值独立于媒体播放器，不对应特征的实际值，也不对应播放器的实际状态。

示例：强制发送曲目时长通知，使用模拟值。

```text
uart:~$ mpl duration_changed_cb
[00:15:17.491,058] <dbg> bt_mcs.mpl_track_duration_cb: Notifying track duration: 12000
```

对应官方文档源码：[doc/services/connectivity/bluetooth/shell/audio/mcp.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/doc/services/connectivity/bluetooth/shell/audio/mcp.rst)。

> 译注——源码跟踪：本仓库[对应源码](../../../doc/services/connectivity/bluetooth/shell/audio/mcp.rst)可用于对照，版本可能与网页不同。本批仅翻译和核对文档，未构建固件或连接音频设备。

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：游戏音频配置文件GMAP_Shell](P059_游戏音频配置文件GMAP_Shell.md) · [本模块主线目录](../reading/bluetooth.md) · [全部主线](../reading/README.md) · [下一篇：公共广播配置文件PBP_Shell](P061_公共广播配置文件PBP_Shell.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章](P059_游戏音频配置文件GMAP_Shell.md) · [返回大纲](大纲.md) · [下一章](P061_公共广播配置文件PBP_Shell.md)

</details>

<!-- reading-navigation:end -->
