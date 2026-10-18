---
id: learning.zephyr-docs.bluetooth.page-53
title: 基本音频配置文件BAP_Shell
kind: reference
status: maintained
domains: [zephyr, bluetooth, documentation]
source_url: https://docs.zephyrproject.org/latest/services/connectivity/bluetooth/shell/audio/bap.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="bluetooth-basic-audio-profile-shell"></a>

<a id="bluetooth-shell-audio"></a>

# 第53章\_蓝牙：基本音频配置文件 Shell（Bluetooth: Basic Audio Profile Shell）

原文：[官方页面](https://docs.zephyrproject.org/latest/services/connectivity/bluetooth/shell/audio/bap.html)。快照读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

> 译注——操作上下文：代码块中的命令在启用了相应音频功能的目标固件 Zephyr Shell 中执行，接入与初始化见[蓝牙 Shell](P007_蓝牙Shell.md)。`uart:~$` 是提示符，后续日志是官方预期输出；不要把提示符、日志或 `<address>` 等占位符原样当作主机终端命令运行。各示例代表不同角色和操作分支，按实际连接与初始化状态选择，不连贯粘贴整章。命令缺失、初始化失败或发现未完成时，应先核对固件配置、控制器能力及当前版本帮助，再继续后续操作。

> 译注——版本与验证：原文“当前”“尚未实现”等表述均保留其快照语境。代码块完整保留原始命令、帮助和输出，本文没有执行固件构建、连接音频设备或验证互操作性。

> 译注——术语：ASE 为音频流端点（Audio Stream Endpoint）；PAC 为已发布音频能力（Published Audio Capabilities）；CIS 为连接等时流（Connected Isochronous Stream），BIS 为广播等时流（Broadcast Isochronous Stream），BIG 为广播等时组（Broadcast Isochronous Group）。单播 sink/source 的方向按远端单播服务端视角解释，参见[协议栈架构](P046_低功耗音频协议栈.md#stream-control-bap)。状态表中的 `qos-configure`／`codec-configure` 保留原文拼写，与常见的 `qos-configured`／`codec-configured` 区分。

本文说明如何运行基本音频配置文件（Basic Audio Profile，BAP）的功能，包括：

> - 能力与端点发现（Capabilities and Endpoint discovery）
>
> - 音频流端点（Audio Stream Endpoint，ASE）过程

<a id="commands"></a>

## 53.1 命令（Commands）

```text
bap --help
Subcommands:
   init                   : [ase_sink_count, ase_source_count]
   select_broadcast       : <stream>
   create_broadcast       : [preset <preset_name>] [enc <broadcast_code>]
   start_broadcast        :
   stop_broadcast         :
   delete_broadcast       :
   create_broadcast_sink  : 0x<broadcast_id>
   create_sink_by_name    : <broadcast_name>
   sync_broadcast         : 0x<bis_index> [[[0x<bis_index>] 0x<bis_index>] ...]
                           [bcode <broadcast code> || bcode_str <broadcast code
                           as string>]
   stop_broadcast_sink    : Stops broadcast sink
   term_broadcast_sink    :
   discover               : [dir: sink, source]
   config                 : <direction: sink, source> <index> [loc <loc_bits>]
                           [preset <preset_name>]
   stream_qos             : interval [framing] [latency] [pd] [sdu] [phy] [rtn]
   qos                    : Send QoS configure for Unicast Group
   enable                 : [context]
   connect                : Connect the CIS of the stream
   stop
   list
   print_ase_info         : Print ASE info for default connection
   metadata               : [context]
   start
   disable
   release
   select_unicast         : <stream>
   preset                 : <sink, source, broadcast> [preset]
                           [config
                                 [freq <frequency>]
                                 [dur <duration>]
                                 [chan_alloc <location>]
                                 [frame_len <frame length>]
                                 [frame_blks <frame blocks>]]
                           [meta
                                 [pref_ctx <context>]
                                 [stream_ctx <context>]
                                 [program_info <program info>]
                                 [lang <ISO 639-3 lang>]
                                 [ccid_list <ccids>]
                                 [parental_rating <rating>]
                                 [program_info_uri <URI>]
                                 [audio_active_state <state>]
                                 [bcast_flag]
                                 [extended <meta>]
                                 [vendor <meta>]]
   send                   : Send to Audio Stream [data]
   stats                  : Sets or gets the statistics reporting interval in # of
                           packets (set 0 to disable)
   set_location           : <direction: sink, source> <location bitmask>
   set_context            : <direction: sink, source><context bitmask> <type:
                           supported, available>
```

<a id="id1"></a>

**状态机转换（State Machine Transitions）**

| 命令（Command） | 依赖（Depends） | 允许的状态（Allowed States） | 后续状态（Next States） |
| --- | --- | --- | --- |
| `init` | 无（none） | 任意（any） | 无（none） |
| `discover` | `init` | 任意（any） | 任意（any） |
| `config` | `discover` | 空闲／编解码器已配置／QoS已配置（idle/codec-configured/qos-configured） | 编解码器已配置（codec-configured） |
| `qos` | `config` | 编解码器已配置／QoS已配置（codec-configured/qos-configured） | QoS已配置（qos-configured） |
| `enable` | `qos` | QoS已配置（qos-configured） | 启用中（enabling） |
| `connect` | `qos/enable` | QoS已配置／启用中（qos-configured/enabling） | QoS已配置／启用中（qos-configured/enabling） |
| `[start]` | `enable/connect` | 启用中（enabling） | 流传输中（streaming） |
| `disable` | `enable` | 启用中／流传输中（enabling/streaming） | 禁用中（disabling） |
| `[stop]` | `disable` | 禁用中（disabling） | QoS配置／空闲（qos-configure/idle，保留原表拼写） |
| `release` | `config` | 任意（any） | 释放中／编解码器配置／空闲（releasing/codec-configure/idle，保留原表拼写） |
| `list` | 无（none） | 任意（any） | 无（none） |
| `select_unicast` | 无（none） | 任意（any） | 无（none） |
| `send` | `enable` | 流传输中（streaming） | 无（none） |

<a id="example-central"></a>

## 53.2 中心设备示例（Example Central）

连接并建立接收端（sink）音频流：

```text
uart:~$ bt init
uart:~$ bap init
uart:~$ bt connect <address>
uart:~$ gatt exchange-mtu
uart:~$ bap discover sink
uart:~$ bap config sink 0
uart:~$ bap qos
uart:~$ bap enable
uart:~$ bap connect
```

连接并建立发送端（source）音频流：

```text
uart:~$ bt init
uart:~$ bap init
uart:~$ bt connect <address>
uart:~$ gatt exchange-mtu
uart:~$ bap discover source
uart:~$ bap config source 0
uart:~$ bap qos
uart:~$ bap enable
uart:~$ bap connect
uart:~$ bap start
```

断开并释放：

```text
uart:~$ bap disable
uart:~$ bap release
```

<a id="example-peripheral"></a>

## 53.3 外围设备示例（Example Peripheral）

监听：

```text
uart:~$ bt init
uart:~$ bap init
uart:~$ bt advertise on
```

由服务端发起禁用与释放：

```text
uart:~$ bap disable
uart:~$ bap release
```

<a id="example-broadcast-source"></a>

## 53.4 广播发送端示例（Example Broadcast Source）

创建并建立广播发送端音频流：

```text
uart:~$ bap init
uart:~$ bap create_broadcast
uart:~$ bap start_broadcast
```

停止并释放广播发送端音频流：

```text
uart:~$ bap stop_broadcast
uart:~$ bap delete_broadcast
```

<a id="example-broadcast-sink"></a>

## 53.5 广播接收端示例（Example Broadcast Sink）

扫描并建立广播接收端音频流。`bap create_broadcast_sink` 命令会使用已有的周期性广播同步（Periodic Advertising Synchronization）；如果没有可用同步，则先开始扫描，并按给定广播标识（broadcast ID）同步到周期性广播，然后再同步到广播等时组（Broadcast Isochronous Group，BIG）。

```text
uart:~$ bap init
uart:~$ bap create_broadcast_sink 0xEF6716
No PA sync available, starting scanning for broadcast_id
Found broadcaster with ID 0xEF6716 and addr R:03:47:95:75:C0:08 and sid 0x00
Attempting to PA sync to the broadcaster
PA synced to broadcast with broadcast ID 0xEF6716
Attempting to sync to the BIG
Received BASE from sink 0x20019080:
Presentation delay: 40000
Subgroup count: 1
Subgroup 0x20024182:
   Codec Format: 0x06
   Company ID  : 0x0000
   Vendor ID   : 0x0000
   codec cfg id 0x06 cid 0x0000 vid 0x0000 count 16
      Codec specific configuration:
      Sampling frequency: 16000 Hz (3)
      Frame duration: 10000 us (1)
      Channel allocation:
               Front left (0x00000001)
               Front right (0x00000002)
      Octets per codec frame: 40
      Codec specific metadata:
      Streaming audio contexts:
         Unspecified (0x0001)
      BIS index: 0x01
         codec cfg id 0x06 cid 0x0000 vid 0x0000 count 6
         Codec specific configuration:
            Channel allocation:
               Front left (0x00000001)
         Codec specific metadata:
            None
      BIS index: 0x02
         codec cfg id 0x06 cid 0x0000 vid 0x0000 count 6
         Codec specific configuration:
            Channel allocation:
               Front right (0x00000002)
         Codec specific metadata:
            None
Possible indexes: 0x01 0x02
Sink 0x20019110 is ready to sync without encryption
uart:~$ bap sync_broadcast 0x01
```

<a id="scan-for-and-establish-a-broadcast-sink-stream-by-broadcast-name"></a>

### 53.5.1 按广播名称扫描并建立广播接收端音频流（Scan for and establish a broadcast sink stream by broadcast name）

`bap create_sink_by_name` 命令会开始扫描，先按给定广播名称同步到周期性广播，再同步到 BIG。

```text
uart:~$ bap init
uart:~$ bap create_sink_by_name "Test Broadcast"
Starting scanning for broadcast_name
Found matched broadcast name 'Test Broadcast' with address R:03:47:95:75:C0:08
Found broadcaster with ID 0xEF6716 and addr R:03:47:95:75:C0:08 and sid 0x00
Attempting to PA sync to the broadcaster
PA synced to broadcast with broadcast ID 0xEF6716
Attempting to create the sink
Received BASE from sink 0x20019080:
Presentation delay: 40000
Subgroup count: 1
Subgroup 0x20024182:
   Codec Format: 0x06
   Company ID  : 0x0000
   Vendor ID   : 0x0000
   codec cfg id 0x06 cid 0x0000 vid 0x0000 count 16
      Codec specific configuration:
      Sampling frequency: 16000 Hz (3)
      Frame duration: 10000 us (1)
      Channel allocation:
               Front left (0x00000001)
               Front right (0x00000002)
      Octets per codec frame: 40
      Codec specific metadata:
      Streaming audio contexts:
         Unspecified (0x0001)
      BIS index: 0x01
         codec cfg id 0x06 cid 0x0000 vid 0x0000 count 6
         Codec specific configuration:
            Channel allocation:
               Front left (0x00000001)
         Codec specific metadata:
            None
      BIS index: 0x02
         codec cfg id 0x06 cid 0x0000 vid 0x0000 count 6
         Codec specific configuration:
            Channel allocation:
               Front right (0x00000002)
         Codec specific metadata:
            None
Possible indexes: 0x01 0x02
Sink 0x20019110 is ready to sync without encryption
uart:~$ bap sync_broadcast 0x01
```

<a id="syncing-to-encrypted-broadcast"></a>

### 53.5.2 同步到加密广播（Syncing to encrypted broadcast）

如果广播已加密，可以通过 `bap sync_broadcast` 命令输入广播码（broadcast code），如下所示：

```text
Sink 0x20019110 is ready to sync with encryption
uart:~$ bap sync_broadcast 0x01 bcode 0102030405060708090a0b0c0d0e0f
```

广播码可以包含 1—16 个值，既可以用字符串表示，也可以用十六进制值表示。

> 译注——广播码表示：原文把长度写作“values”。[官方源码](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/subsys/bluetooth/audio/shell/bap.c)及本仓库的[相对路径对照](../../../subsys/bluetooth/audio/shell/bap.c)中的 `cmd_sync_broadcast()` 使用零初始化的字节数组；`bcode` 经 `hex2bin()` 转换，`bcode_str` 按 `strlen()` 的字节数检查并复制。十六进制两个字符表示一个字节，字符串长度也按字节而非 Unicode 字符计；原例的 `0102030405060708090a0b0c0d0e0f` 为 15 个字节。原始命令与预期日志保持不变。

```text
Sink 0x20019110 is ready to sync with encryption
uart:~$ bap sync_broadcast 0x01 bcode_str thisismycode
```

停止并释放广播接收端音频流：

```text
uart:~$ bap stop_broadcast_sink
uart:~$ bap term_broadcast_sink
```

<a id="init"></a>

## 53.6 初始化（Init）

`init` 命令注册本地已发布音频能力（Published Audio Capabilities，PAC）记录。要配置音频流并正确管理所用能力，必须具备这些记录。

<a id="id2"></a>

**状态机转换（State Machine Transitions）**

| 依赖（Depends） | 允许的状态（Allowed States） | 后续状态（Next States） |
| --- | --- | --- |
| 无（none） | 任意（any） | 无（none） |

```text
uart:~$ bap init
```

<a id="discover-pac-s-and-ase-s"></a>

## 53.7 发现 PAC 与 ASE（Discover PAC(s) and ASE(s)）

建立连接后，`discover` 命令发现 PAC 记录，以及表示远端端点的 ASE 特征（characteristic）。

<a id="id3"></a>

**状态机转换（State Machine Transitions）**

| 依赖（Depends） | 允许的状态（Allowed States） | 后续状态（Next States） |
| --- | --- | --- |
| `init` | 任意（any） | 任意（any） |

注意（Note）

使用 `gatt exchange-mtu` 命令，确保最大传输单元（Maximum Transmission Unit，MTU）配置正确。

```text
uart:~$ gatt exchange-mtu
Exchange pending
Exchange successful
uart:~$ bap discover [type: sink, source]
uart:~$ bap discover sink
conn 0x8256f80: dir Sink (0x01)
codec cap id 0x06 cid 0x0000 vid 0x0000
  Codec specific capabilities:
    Supported sampling frequencies:
      8000 Hz (0x0001)
      11025 Hz (0x0002)
      16000 Hz (0x0004)
      22050 Hz (0x0008)
      24000 Hz (0x0010)
      32000 Hz (0x0020)
      44100 Hz (0x0040)
      48000 Hz (0x0080)
      88200 Hz (0x0100)
      96000 Hz (0x0200)
      176400 Hz (0x0400)
      192000 Hz (0x0800)
      384000 Hz (0x1000)
    Supported frame durations:
      7.5 ms (0x01)
      10 ms (0x02)
    Supported channel counts:
      1 channel (0x01)
      2 channels (0x02)
    Supported octets per codec frame counts:
      Min: 30
      Max: 155
    Supported max codec frames per SDU: 4
  Codec capabilities metadata:
    Preferred audio contexts:
      Unspecified        (0x0001)
      Conversational     (0x0002)
      Media              (0x0004)
conn 0x8256f80: dir Sink (0x01)
codec cap id 0x06 cid 0x0000 vid 0x0000
  Codec specific capabilities:
    Supported sampling frequencies:
      16000 Hz (0x0004)
      32000 Hz (0x0020)
      48000 Hz (0x0080)
    Supported frame durations:
      7.5 ms (0x01)
      10 ms (0x02)
    Supported channel counts:
      1 channel (0x01)
      2 channels (0x02)
    Supported octets per codec frame counts:
      Min: 30
      Max: 120
    Supported max codec frames per SDU: 4
  Codec capabilities metadata:
    Preferred audio contexts:
      Game               (0x0008)
Supported audio contexts:
  Sink:
    Unspecified        (0x0001)
    Conversational     (0x0002)
    Media              (0x0004)
    Game               (0x0008)
    Instructional      (0x0010)
    Voice assistant    (0x0020)
    Live               (0x0040)
    Sound effects      (0x0080)
  Source:
    Unspecified        (0x0001)
    Conversational     (0x0002)
    Media              (0x0004)
    Game               (0x0008)
    Instructional      (0x0010)
    Voice assistant    (0x0020)
    Live               (0x0040)
    Sound effects      (0x0080)
Sink location:
  Front left               (0x00000001)
  Front right              (0x00000002)
Available audio contexts:
  Sink:
    Unspecified        (0x0001)
    Conversational     (0x0002)
    Media              (0x0004)
    Game               (0x0008)
    Instructional      (0x0010)
    Voice assistant    (0x0020)
    Live               (0x0040)
    Sound effects      (0x0080)
  Source:
    Unspecified        (0x0001)
    Conversational     (0x0002)
    Media              (0x0004)
    Game               (0x0008)
    Instructional      (0x0010)
    Voice assistant    (0x0020)
    Live               (0x0040)
    Sound effects      (0x0080)
Conn: 0x8256f80, Sink #0: ep 0x8288e1c
Conn: 0x8256f80, Sink #1: ep 0x8289000
Discover complete: err 0
```

<a id="select-preset"></a>

## 53.8 选择预设（Select preset）

`preset` 命令可以打印默认预设配置，也可以选择其他预设；它不会更改此前已经配置的音频流。

```text
uart:~$ bap preset
preset - <sink, source, broadcast> [preset]
         [config
               [freq <frequency>]
               [dur <duration>]
               [chan_alloc <location>]
               [frame_len <frame length>]
               [frame_blks <frame blocks>]]
         [meta
               [pref_ctx <context>]
               [stream_ctx <context>]
               [program_info <program info>]
               [lang <ISO 639-3 lang>]
               [ccid_list <ccids>]
               [parental_rating <rating>]
               [program_info_uri <URI>]
               [audio_active_state <state>]
               [bcast_flag]
               [extended <meta>]
               [vendor <meta>]]
uart:~$ bap preset sink
16_2_1
codec cfg id 0x06 cid 0x0000 vid 0x0000 count 16
   Codec specific configuration:
      Sampling frequency: 16000 Hz (3)
      Frame duration: 10000 us (1)
      Channel allocation:
                  Front left (0x00000001)
                  Front right (0x00000002)
      Octets per codec frame: 40
   Codec specific metadata:
      Streaming audio contexts:
         Game (0x0008)
QoS: interval 10000 framing 0x00 phy 0x02 sdu 40 rtn 2 latency 10 pd 40000

uart:~$ bap preset sink 32_2_1
32_2_1
codec cfg id 0x06 cid 0x0000 vid 0x0000 count 16
   Codec specific configuration:
      Sampling frequency: 32000 Hz (6)
      Frame duration: 10000 us (1)
      Channel allocation:
                  Front left (0x00000001)
                  Front right (0x00000002)
      Octets per codec frame: 80
   Codec specific metadata:
      Streaming audio contexts:
         Game (0x0008)
   QoS: interval 10000 framing 0x00 phy 0x02 sdu 80 rtn 2 latency 10 pd 40000
```

<a id="configure-preset"></a>

## 53.9 配置预设（Configure preset）

`bap preset` 命令还可以配置后续命令使用的预设，可以添加、设置或重置任何值。要重置预设，直接运行该命令，不传入 `config` 或 `meta` 参数即可。参数采用蓝牙分配编号（Assigned Numbers）中定义的取值。

```text
uart:~$ bap preset sink 32_2_1
32_2_1
codec cfg id 0x06 cid 0x0000 vid 0x0000 count 16
data #0: type 0x01 value_len 1
00000000: 06                                               |.                |
data #1: type 0x02 value_len 1
00000000: 01                                               |.                |
data #2: type 0x03 value_len 4
00000000: 03 00 00 00                                      |....             |
data #3: type 0x04 value_len 2
00000000: 50 00                                            |P.               |
meta #0: type 0x02 value_len 2
00000000: 08 00                                            |..               |
QoS: interval 10000 framing 0x00 phy 0x02 sdu 80 rtn 2 latency 10 pd 40000

uart:~$ bap preset sink 32_2_1 config freq 10
32_2_1
codec cfg id 0x06 cid 0x0000 vid 0x0000 count 16
data #0: type 0x01 value_len 1
00000000: 0a                                               |.                |
data #1: type 0x02 value_len 1
00000000: 01                                               |.                |
data #2: type 0x03 value_len 4
00000000: 03 00 00 00                                      |....             |
data #3: type 0x04 value_len 2
00000000: 50 00                                            |P.               |
meta #0: type 0x02 value_len 2
00000000: 08 00                                            |..               |
QoS: interval 10000 framing 0x00 phy 0x02 sdu 80 rtn 2 latency 10 pd 40000

uart:~$ bap preset sink 32_2_1 config freq 10 meta lang "eng" stream_ctx 4
32_2_1
codec cfg id 0x06 cid 0x0000 vid 0x0000 count 16
data #0: type 0x01 value_len 1
00000000: 0a                                               |.                |
data #1: type 0x02 value_len 1
00000000: 01                                               |.                |
data #2: type 0x03 value_len 4
00000000: 03 00 00 00                                      |....             |
data #3: type 0x04 value_len 2
00000000: 50 00                                            |P.               |
meta #0: type 0x02 value_len 2
00000000: 04 00                                            |..               |
meta #1: type 0x04 value_len 3
00000000: 65 6e 67                                         |eng              |
QoS: interval 10000 framing 0x00 phy 0x02 sdu 80 rtn 2 latency 10 pd 40000
```

<a id="configure-codec"></a>

## 53.10 配置编解码器（Configure Codec）

`config` 命令尝试为给定方向的音频流配置预设编解码器参数。可以直接传入所选预设；省略时使用默认预设。

<a id="id4"></a>

**状态机转换（State Machine Transitions）**

| 依赖（Depends） | 允许的状态（Allowed States） | 后续状态（Next States） |
| --- | --- | --- |
| `discover` | 空闲／编解码器已配置／QoS已配置（idle/codec-configured/qos-configured） | 编解码器已配置（codec-configured） |

```text
uart:~$ bap config <direction: sink, source> <index> [loc <loc_bits>] [preset <preset_name>]
uart:~$ bap config sink 0
Setting location to 0x00000000
ASE config: preset 16_2_1
stream 0x2000df70 config operation rsp_code 0 reason 0
```

<a id="configure-stream-qos"></a>

## 53.11 配置音频流 QoS（Configure Stream QoS）

`stream_qos` 设置新的音频流服务质量（Quality of Service，QoS）参数。

```text
uart:~$ bap stream_qos <interval> [framing] [latency] [pd] [sdu] [phy] [rtn]
uart:~$ bap stream_qos 10
```

<a id="configure-qos"></a>

## 53.12 配置 QoS（Configure QoS）

`qos` 命令尝试按预设配置音频流的 QoS；可以通过可选参数分别设置各项 QoS 参数。

<a id="id5"></a>

**状态机转换（State Machine Transitions）**

| 依赖（Depends） | 允许的状态（Allowed States） | 后续状态（Next States） |
| --- | --- | --- |
| `config` | QoS已配置／编解码器已配置（qos-configured/codec-configured） | QoS已配置（qos-configured） |

```text
uart:~$ bap qos
```

<a id="enable"></a>

## 53.13 启用（Enable）

`enable` 命令尝试启用此前配置的音频流。

<a id="id6"></a>

**状态机转换（State Machine Transitions）**

| 依赖（Depends） | 允许的状态（Allowed States） | 后续状态（Next States） |
| --- | --- | --- |
| `qos` | QoS已配置（qos-configured） | 启用中（enabling） |

```text
uart:~$ bap enable [context]
uart:~$ bap enable Media
```

<a id="connect"></a>

## 53.14 连接（Connect）

`connect` 命令尝试连接此前配置的音频流。接收端音频流必须由单播服务端启动，发送端音频流必须由单播客户端启动。

<a id="id7"></a>

**状态机转换（State Machine Transitions）**

| 依赖（Depends） | 允许的状态（Allowed States） | 后续状态（Next States） |
| --- | --- | --- |
| `qos/enable` | QoS已配置／启用中（qos-configured/enabling） | QoS已配置／启用中（qos-configured/enabling） |

```text
uart:~$ bap connect
```

<a id="start"></a>

## 53.15 启动（Start）

仅在启动发送端音频流时需要 `start` 命令。

<a id="id8"></a>

**状态机转换（State Machine Transitions）**

| 依赖（Depends） | 允许的状态（Allowed States） | 后续状态（Next States） |
| --- | --- | --- |
| `enable/connect` | 启用中（enabling） | 流传输中（streaming） |

```text
uart:~$ bap start
```

<a id="disable"></a>

## 53.16 禁用（Disable）

`disable` 命令尝试禁用此前启用的音频流；如果远端对等设备接受请求，还会发起等时信道（ISO）断开过程。

<a id="id9"></a>

**状态机转换（State Machine Transitions）**

| 依赖（Depends） | 允许的状态（Allowed States） | 后续状态（Next States） |
| --- | --- | --- |
| `enable` | 启用中／流传输中（enabling/streaming） | 禁用中（disabling） |

```text
uart:~$ bap disable
```

<a id="stop"></a>

## 53.17 停止（Stop）

只有承担接收端角色时才需要 `stop` 命令；它向发送端表明协议栈已准备停止接收数据。

<a id="id10"></a>

**状态机转换（State Machine Transitions）**

| 依赖（Depends） | 允许的状态（Allowed States） | 后续状态（Next States） |
| --- | --- | --- |
| `disable` | 禁用中（disabling） | QoS配置／空闲（qos-configure/idle，保留原表拼写） |

```text
uart:~$ bap stop
```

<a id="release"></a>

## 53.18 释放（Release）

`release` 命令释放当前音频流及其配置。

<a id="id11"></a>

**状态机转换（State Machine Transitions）**

| 依赖（Depends） | 允许的状态（Allowed States） | 后续状态（Next States） |
| --- | --- | --- |
| `config` | 任意（any） | 释放中／编解码器配置／空闲（releasing/codec-configure/idle，保留原表拼写） |

```text
uart:~$ bap release
```

<a id="list"></a>

## 53.19 列出音频流（List）

`list` 命令列出可用音频流。

<a id="id12"></a>

**状态机转换（State Machine Transitions）**

| 依赖（Depends） | 允许的状态（Allowed States） | 后续状态（Next States） |
| --- | --- | --- |
| 无（none） | 任意（any） | 无（none） |

```text
uart:~$ bap list
*0: ase 0x01 dir 0x01 state 0x01
```

<a id="select-unicast"></a>

## 53.20 选择单播音频流（Select Unicast）

`select_unicast` 命令将指定单播音频流设为默认流。

<a id="id13"></a>

**状态机转换（State Machine Transitions）**

| 依赖（Depends） | 允许的状态（Allowed States） | 后续状态（Next States） |
| --- | --- | --- |
| 无（none） | 任意（any） | 无（none） |

```text
uart:~$ bap select <ase>
uart:~$ bap select 0x01
Default stream: 1
```

选择广播音频流：

```text
uart:~$ bap select 0x01 broadcast
Default stream: 1 (broadcast)
```

<a id="send"></a>

## 53.21 发送（Send）

`send` 命令通过 BAP 音频流发送数据。

<a id="id14"></a>

**状态机转换（State Machine Transitions）**

| 依赖（Depends） | 允许的状态（Allowed States） | 后续状态（Next States） |
| --- | --- | --- |
| `enable` | 流传输中（streaming） | 无（none） |

```text
uart:~$ bap send [count]
uart:~$ bap send
Audio sending...
```

对应官方文档源码：[doc/services/connectivity/bluetooth/shell/audio/bap.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/doc/services/connectivity/bluetooth/shell/audio/bap.rst)。

> 译注——源码跟踪：本仓库[对应源码](../../../doc/services/connectivity/bluetooth/shell/audio/bap.rst)可用于对照，版本可能与网页不同。本批仅翻译和核对文档，未构建固件或连接音频设备。

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：蓝牙音量控制](P052_蓝牙音量控制.md) · [本模块主线目录](../reading/bluetooth.md) · [全部主线](../reading/README.md) · [下一篇：BAP广播助手Shell](P054_BAP广播助手Shell.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章](P052_蓝牙音量控制.md) · [返回大纲](大纲.md) · [下一章](P054_BAP广播助手Shell.md)

</details>

<!-- reading-navigation:end -->
