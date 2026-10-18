---
id: learning.zephyr-docs.bluetooth.page-54
title: BAP广播助手Shell
kind: reference
status: maintained
domains: [zephyr, bluetooth, documentation]
source_url: https://docs.zephyrproject.org/latest/services/connectivity/bluetooth/shell/audio/bap_broadcast_assistant.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="bluetooth-basic-audio-profile-broadcast-assistant-shell"></a>

# 第54章\_蓝牙：基本音频配置文件广播助手 Shell（Bluetooth: Basic Audio Profile: Broadcast Assistant Shell）

原文：[官方页面](https://docs.zephyrproject.org/latest/services/connectivity/bluetooth/shell/audio/bap_broadcast_assistant.html)。快照读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

> 译注——操作上下文：代码块中的命令在启用了相应音频功能的目标固件 Zephyr Shell 中执行，接入与初始化见[蓝牙 Shell](P007_蓝牙Shell.md)。`uart:~$` 是提示符，后续日志是官方预期输出；不要把提示符、日志或 `<address>` 等占位符原样当作主机终端命令运行。各示例代表不同角色和操作分支，按实际连接与初始化状态选择，不连贯粘贴整章。命令缺失、初始化失败或发现未完成时，应先核对固件配置、控制器能力及当前版本帮助，再继续后续操作。

> 译注——版本与验证：原文“当前”“尚未实现”等表述均保留其快照语境。代码块完整保留原始命令、帮助和输出，本文没有执行固件构建、连接音频设备或验证互操作性。

> 译注——术语：BAP 为基本音频配置文件（Basic Audio Profile），BASS 为广播音频扫描服务（Broadcast Audio Scan Service）；接收状态（receive state）由接收设备公开，广播助手负责提供来源信息。

本文说明如何运行 BAP 广播助手（Broadcast Assistant）功能。下方示例按原文删去了部分调试行，以缩短篇幅并便于理解整体流程。

广播助手负责替资源受限的设备承担扫描工作，避免扫描消耗其电池。广播助手必须支持扫描周期性广播，也可以选择支持周期性广播同步传输（Periodic Advertising Synchronization Transfer，PAST）协议。

广播助手通常是手机或笔记本电脑，扫描周期性广播并将信息传给服务端。

要以交互方式使用广播助手，必须启用 [`CONFIG_BT_BAP_BROADCAST_ASSISTANT_LOG_LEVEL_DBG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_BAP_BROADCAST_ASSISTANT_LOG_LEVEL_DBG)。

蓝牙协议栈完成初始化（`bt init`）且已经连接设备后，可以调用 `bap_broadcast_assistant discover`，在已连接设备上发现广播音频扫描服务（Broadcast Audio Scan Service，BASS）。该命令开始发现 BASS 的 UUID，保存句柄，并订阅所有通知。

```text
uart:~$ bap_broadcast_assistant --help
bap_broadcast_assistant - Bluetooth BAP broadcast assistant client shell
                        commands
Subcommands:
discover          : Discover BASS on the server
scan_start        : Start scanning for broadcasters
scan_stop         : Stop scanning for BISs
add_src           : Add a source <address: P:XX:XX:XX:XX:XX:XX or
                     R:XX:XX:XX:XX:XX:XX> <adv_sid> <sync_pa> <broadcast_id>
                     [<sync_bis>] [<pa_interval>] [<metadata>]
add_broadcast_id  : Add a source by broadcast ID <broadcast_id> <sync_pa>
                     [<sync_bis>] [<metadata>]
add_broadcast_name: Add a source by broadcast name <broadcast_name> <sync_pa>
                     [<sync_bis>] [<metadata>]
add_pa_sync       : Add a PA sync as a source <sync_pa> <broadcast_id>
                     [bis_index [bis_index [bix_index [...]]]]>
mod_src           : Set sync <src_id> <sync_pa> [<pa_interval> | "unknown"] [<sync_bis>]
                     [<metadata>]
broadcast_code    : Send a string-based broadcast code of up to 16 bytes
                     <src_id> <broadcast code>
rem_src           : Remove a source <src_id>
read_state        : Remove a source <index>
```

<a id="example-usage"></a>

## 54.1 使用示例（Example usage）

<a id="setup"></a>

### 54.1.1 准备（Setup）

```text
uart:~$ bt init
uart:~$ bap init
uart:~$ bt connect P:xx:xx:xx:xx:xx:xx
```

<a id="when-connected"></a>

### 54.1.2 已连接时（When connected）

<a id="start-scanning-for-periodic-advertisements-for-a-server"></a>

#### 54.1.2.1 为服务端开始扫描周期性广播：

注意（Note）

原文说明：广播助手实际上不会开始扫描周期性广播，因为在原文编写时该功能尚未实现。

> 译注——版本差异：这句保留原文编写时的限制。当前读取的[官方源码](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/subsys/bluetooth/audio/shell/bap_broadcast_assistant.c)及本仓库的[相对路径对照](../../../subsys/bluetooth/audio/shell/bap_broadcast_assistant.c)中，`cmd_bap_broadcast_assistant_add_broadcast_id()` 已调用 `bt_le_scan_start()`。这只能证明该源码存在扫描调用路径，不能把原文的历史限制当作所有版本均不支持扫描，也不能据此声称目标设备已完成扫描验证。

```text
uart:~$ bap_broadcast_assistant discover
BASS discover done with 1 recv states
uart:~$ bap_broadcast_assistant scan_start true
BASS scan start successful
Found broadcaster with ID 0x05BD38 and addr R:1E:4D:0A:AA:6E:49 and sid 0x00
```

<a id="adding-a-source-to-the-receive-state-with-add-src"></a>

#### 54.1.2.2 通过 `add\_src` 向接收状态添加发送端：

```text
uart:~$ bap_broadcast_assistant add_src P:11:22:33:44:55:66 5 1 1
BASS recv state: src_id 0, addr P:11:22:33:44:55:66, sid 5, sync_state 1, encrypt_state 000000000000000000000000000000000
     [0]: BIS sync 0, metadata_len 0
```

<a id="adding-a-source-to-the-receive-state-with-add-broadcast-id-recommended"></a>

#### 54.1.2.3 通过 `add\_broadcast\_id` 向接收状态添加发送端（推荐）：

```text
uart:~$ bap_broadcast_assistant add_broadcast_id 0x05BD38 true
[DEVICE]: R:1E:4D:0A:AA:6E:49, AD evt type 5, RSSI -28 Broadcast Audio Source C:0 S:0 D:0 SR:0 E:1 Prim: LE 1M, Secn: LE 2M, Interval: 0x03c0 (1200000 us), SID: 0x0
Found BAP broadcast source with address R:1E:4D:0A:AA:6E:49 and ID 0x05BD38
BASS recv state: src_id 0, addr R:1E:4D:0A:AA:6E:49, sid 0, sync_state 0, encrypt_state 0
      [0]: BIS sync 0x0000, metadata_len 0
BASS add source successful
BASS recv state: src_id 0, addr R:1E:4D:0A:AA:6E:49, sid 0, sync_state 2, encrypt_state 0
      [0]: BIS sync 0x0000, metadata_len 0
BASS recv state: src_id 0, addr R:1E:4D:0A:AA:6E:49, sid 0, sync_state 2, encrypt_state 0
      [0]: BIS sync 0x0000, metadata_len 4
               Metadata length 2, type 2, data: 0100
```

<a id="modifying-a-receive-state"></a>

#### 54.1.2.4 修改接收状态（receive state）：

```text
uart:~$ bap_broadcast_assistant mod_src 0 true 0x03c0 0x02
BASS modify source successful
BASS recv state: src_id 0, addr R:1E:4D:0A:AA:6E:49, sid 0, sync_state 2, encrypt_state 0
      [0]: BIS sync 0x0001, metadata_len 4
               Metadata length 2, type 2, data: 0100
```

<a id="supplying-a-broadcast-code"></a>

#### 54.1.2.5 提供广播码：

```text
uart:~$ bap_broadcast_assistant broadcast_code 0 secretCode
Sending broadcast code:
00000000: 73 65 63 72 65 74 43 6f 64 65 00 00 00 00 00 00 |secretCo de....|
uart:~$ BASS broadcast code successful
```

对应官方文档源码：[doc/services/connectivity/bluetooth/shell/audio/bap_broadcast_assistant.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/doc/services/connectivity/bluetooth/shell/audio/bap_broadcast_assistant.rst)。

> 译注——源码跟踪：本仓库[对应源码](../../../doc/services/connectivity/bluetooth/shell/audio/bap_broadcast_assistant.rst)可用于对照，版本可能与网页不同。本批仅翻译和核对文档，未构建固件或连接音频设备。

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：基本音频配置文件BAP_Shell](P053_基本音频配置文件BAP_Shell.md) · [本模块主线目录](../reading/bluetooth.md) · [全部主线](../reading/README.md) · [下一篇：BAP扫描委托方Shell](P055_BAP扫描委托方Shell.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章](P053_基本音频配置文件BAP_Shell.md) · [返回大纲](大纲.md) · [下一章](P055_BAP扫描委托方Shell.md)

</details>

<!-- reading-navigation:end -->
