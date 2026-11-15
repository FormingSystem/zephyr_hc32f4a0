---
id: learning.zephyr-docs.bluetooth.page-56
title: 通用音频配置文件CAP_Shell
kind: reference
status: maintained
domains: [zephyr, bluetooth, documentation]
source_url: https://docs.zephyrproject.org/latest/services/connectivity/bluetooth/shell/audio/cap.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="bluetooth-common-audio-profile-shell"></a>

# 第56章\_蓝牙：通用音频配置文件 Shell（Bluetooth: Common Audio Profile Shell）

原文：[官方页面](https://docs.zephyrproject.org/latest/services/connectivity/bluetooth/shell/audio/cap.html)。快照读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

> 译注——操作上下文：代码块中的命令在启用了相应音频功能的目标固件 Zephyr Shell 中执行，接入与初始化见[蓝牙 Shell](P007_蓝牙Shell.md)。`uart:~$` 是提示符，后续日志是官方预期输出；不要把提示符、日志或 `<address>` 等占位符原样当作主机终端命令运行。各示例代表不同角色和操作分支，按实际连接与初始化状态选择，不连贯粘贴整章。命令缺失、初始化失败或发现未完成时，应先核对固件配置、控制器能力及当前版本帮助，再继续后续操作。

> 译注——版本与验证：原文“当前”“尚未实现”等表述均保留其快照语境。代码块完整保留原始命令、帮助和输出，本文没有执行固件构建、连接音频设备或验证互操作性。

> 译注——术语：ASE 为音频流端点（Audio Stream Endpoint），PAC 为已发布音频能力（Published Audio Capabilities）；BASE 为基本音频公告（Basic Audio Announcement）。CAP 的三个角色分别为发起方（Initiator）、接受方（Acceptor）和命令方（Commander）。

本文说明如何运行通用音频配置文件（Common Audio Profile，CAP）功能。

<a id="cap-acceptor"></a>

## 56.1 CAP 接受方（CAP Acceptor）

接受方通常是资源受限的设备，例如头戴式耳机、耳塞或助听器。如果它与一个或多个其他 CAP 接受方配成一组，可以初始化一个协调集标识服务（Coordinated Set Identification Service，CSIS）实例。

<a id="using-the-cap-acceptor"></a>

### 56.1.1 使用 CAP 接受方（Using the CAP Acceptor）

蓝牙协议栈完成初始化（`bt init`）后，可以调用 `cap_acceptor init` 注册接受方；这会注册通用音频服务（Common Audio Service，CAS）、CSIS 服务及回调函数。

```text
cap_acceptor --help
cap_acceptor - Bluetooth CAP acceptor shell commands
Subcommands:
  init          :Initialize the service and register callbacks [size <int>]
                 [rank <int>] [not-lockable] [sirk <data>]
  lock          :Lock the set
  release       :Release the set [force]
  sirk          :Set the currently used SIRK <sirk>
  get_info      :Get CSIS info
  sirk_rsp      :Set the response used in SIRK requests <accept, accept_enc,
                 reject, oob>
```

除了初始化 CAS 和 CSIS，还提供了锁定、释放 CSIS 实例，以及打印 SIRK 和修改 SIRK 访问权限的命令。

<a id="setting-a-new-sirk"></a>

#### 56.1.1.1 设置新的 SIRK（Setting a new SIRK）

该命令可以修改当前使用的集合标识解析密钥（Set Identity Resolving Key，SIRK）。要在无线广播中使用新的可解析集合标识符（Resolvable Set Identifier，RSI），必须再次调用 `bt adv-data` 或 `bt advertise`，设置新的广播数据。如果启用了 `CONFIG_BT_CSIP_SET_MEMBER_SIRK_NOTIFIABLE`，也会通知已连接客户端。

```text
uart:~$ cap_acceptor sirk 00112233445566778899aabbccddeeff
SIRK updated
```

<a id="getting-the-current-sirk"></a>

#### 56.1.1.2 获取当前 SIRK（Getting the current SIRK）

该命令可以获取当前使用的 SIRK。

```text
uart:~$ cap_acceptor get_info
Info for 0x2003b0c8
        SIRK
00000000: 20 37 0a 00 95 c4 04 20  00 00 00 00 f1 79 09 00 | 7.....  .....y..|
        Set size: 2
        Rank: 1
        Lockable: true
        Locked: false
```

<a id="cap-initiator"></a>

## 56.2 CAP 发起方（CAP Initiator）

发起方通常是资源较充足的设备，例如手机或 PC。它可以发现 CAP 接受方的 CAS 以及可选的 CSIS 服务，通过读取 CSIS 获取同一协调集（Coordinated Set）中其他 CAP 接受方的信息。发起方可以对临时组合（ad-hoc）或协调集中的一组设备执行流控制过程，从而方便地一次为多台设备建立多个音频流。

<a id="using-the-cap-initiator"></a>

### 56.2.1 使用 CAP 发起方（Using the CAP Initiator）

蓝牙协议栈完成初始化（`bt init`）后，发起方可以调用 `cap_initiator discover`，发现 CAS 及其中可选包含的 CSIS 实例。CAP 发起方也支持作为广播音频发送端。

```text
uart:~$ cap_initiator --help
cap_initiator - Bluetooth CAP initiator shell commands
Subcommands:
  discover          : Discover CAS
  unicast_start     : Unicast Start [csip] [sinks <cnt> (default 1)] [sources
                     <cnt> (default 1)] [conns (<cnt> | all) (default 1)]
  unicast_list      : Unicast list streams
  unicast_update    : Unicast Update <all | stream [stream [stream...]]>
  unicast_stop      : Unicast stop streams [stream [stream [stream...]]] (all by default)
  unicast_cancel    : Unicast cancel current procedure
  ac_1              : Unicast audio configuration 1
  ac_2              : Unicast audio configuration 2
  ac_3              : Unicast audio configuration 3
  ac_4              : Unicast audio configuration 4
  ac_5              : Unicast audio configuration 5
  ac_6_i            : Unicast audio configuration 6(i)
  ac_6_ii           : Unicast audio configuration 6(ii)
  ac_7_i            : Unicast audio configuration 7(i)
  ac_7_ii           : Unicast audio configuration 7(ii)
  ac_8_i            : Unicast audio configuration 8(i)
  ac_8_ii           : Unicast audio configuration 8(ii)
  ac_9_i            : Unicast audio configuration 9(i)
  ac_9_ii           : Unicast audio configuration 9(ii)
  ac_10             : Unicast audio configuration 10
  ac_11_i           : Unicast audio configuration 11(i)
  ac_11_ii          : Unicast audio configuration 11(ii)
  broadcast_start   :
  broadcast_update  : <meta>
  broadcast_stop    :
  broadcast_delete  :
  ac_12             : Broadcast audio configuration 12
  ac_13             : Broadcast audio configuration 13
  ac_14             : Broadcast audio configuration 14
```

在执行任何音频流操作之前，设备还必须执行 `bap discover`，发现 ASE 和 PAC 记录；也需要调用 `bap init`。

<a id="when-connected"></a>

#### 56.2.1.1 已连接时（When connected）

发现设备上的 CAS 与 CSIS：

```text
uart:~$ cap_initiator discover
discovery completed with CSIS
```

发现设备上的 ASE 与 PAC 记录：

```text
uart:~$ bap discover
conn 0x81cc260: #0: codec 0x81d5b28 dir 0x01
codec 0x06 cid 0x0000 vid 0x0000 count 5
data #0: type 0x01 len 2
00000000: f5                                               |.                |
data #1: type 0x02 len 1
data #2: type 0x03 len 1
data #3: type 0x04 len 4
00000000: 1e 00 f0                                         |...              |
data #4: type 0x05 len 1
meta #0: type 0x01 len 2
00000000: 06                                               |.                |
dir 1 loc 1
snk ctx 6 src ctx 6
Conn: 0x81cc260, Sink #0: ep 0x81e4248
Conn: 0x81cc260, Sink #1: ep 0x81e46a8
conn 0x81cc260: #0: codec 0x81d5f00 dir 0x02
codec 0x06 cid 0x0000 vid 0x0000 count 5
data #0: type 0x01 len 2
00000000: f5                                               |.                |
data #1: type 0x02 len 1
data #2: type 0x03 len 1
data #3: type 0x04 len 4
00000000: 1e 00 f0                                         |...              |
data #4: type 0x05 len 1
meta #0: type 0x01 len 2
00000000: 06                                               |.                |
dir 2 loc 1
snk ctx 6 src ctx 6
Conn: 0x81cc260, Source #0: ep 0x81e5c88
Conn: 0x81cc260, Source #1: ep 0x81e60e8
Discover complete: err 0
```

对于希望加入集合使用的每台设备，都应执行上述两类发现命令。要使用多台设备，继续连接其他设备，然后用 `bt select` 选中将要执行命令的设备。

所有设备连接完成且执行了相应发现命令后，可以使用 `cap_initiator unicast_start`，使一个或多个音频流进入流传输状态（streaming）。

```text
uart:~$ cap_initiator unicast_start sinks 1 sources 0 conns all
Setting up 1 sinks and 0 sources on each (2) conn
Starting 1 streams
Unicast start completed
```

要停止所有已启动的音频流，可以使用 `cap_initiator unicast_stop`。

```text
uart:~$ cap_initiator unicast_stop all
Unicast stop completed
```

<a id="when-doing-broadcast"></a>

#### 56.2.1.2 广播操作（When doing broadcast）

作为 CAP 发起方启动广播，需要完成以下几个步骤：

- 创建并配置带有周期性广播的扩展广播集（extended advertising set）。

- 创建并配置广播发送端。

- 设置扩展广播数据和周期性广播数据。

下列命令使用 BAP 定义的 `16_2_1` 预设，建立 CAP 广播发送端：

```text
bt init
bap init
bt adv-create nconn-nscan ext-adv
bt per-adv-param
bap preset broadcast 16_2_1
cap_initiator ac_12
bt adv-data dev-name discov
bt per-adv-data
cap_initiator broadcast_start
bt adv-start
bt per-adv on
```

`cap_initiator ac_12`、`cap_initiator ac_13` 和 `cap_initiator ac_14` 命令创建广播发送端，并按 BAP 定义的相应音频配置进行设置。之后可以用 `cap_initiator broadcast_stop` 停止它，或用 `cap_initiator broadcast_delete` 删除它。

广播发送端的元数据（metadata）可以随时更新，即使已经开始流传输也可以。使用 `cap_initiator broadcast_update` 更新元数据；该命令接受一个数据数组，除了数据本身有效之外，唯一要求是必须设置流上下文（streaming context）。例如，将流上下文设为媒体，可以按下例执行：

```text
cap_initiator broadcast_update 03020400
CAP Broadcast source updated with new metadata. Update the advertised base via `bt per-adv-data`
bt per-adv-data
```

之后应使用 `bt per-adv-data` 命令，更新广播中的基本音频公告（BASE）数据。数据必须采用小端序（little-endian）：上例元数据 `03020400` 中，`03` 是长度，`02` 是类型（流上下文），`0400` 是 `BT_AUDIO_CONTEXT_TYPE_MEDIA` 的值。原文在此将其数值写为不完整的 `0x`。

> 译注——元数据数值：[官方源码](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/include/zephyr/bluetooth/assigned_numbers.h)及本仓库的[相对路径对照](../../../include/zephyr/bluetooth/assigned_numbers.h)定义 `BT_AUDIO_CONTEXT_TYPE_MEDIA = BIT(2)`，即 `0x0004`。按小端序编码为 `04 00`，因此原例 `03 02 04 00` 的长度、类型和值彼此一致；不完整的 `0x` 是原文缺漏，命令数据无需因此修改。

<a id="cap-commander"></a>

## 56.3 CAP 命令方（CAP Commander）

命令方通常与 CAP 发起方位于同一设备，也可以位于资源较充足的独立移动设备，例如手机或智能手表。它可以发现 CAP 接受方的 CAS 及可选的 CSIS 服务，通过读取 CSIS 获取同一协调集中其他 CAP 接受方的信息。命令方可以向 CAP 接受方提供广播发送端信息，或协调静音、音量等采集与呈现信息。

<a id="using-the-cap-commander"></a>

### 56.3.1 使用 CAP 命令方（Using the CAP Commander）

蓝牙协议栈完成初始化（`bt init`）后，命令方可以调用 `cap_commander discover`，发现 CAS 及其中可选包含的 CSIS 实例。

```text
cap_commander --help
cap_commander - Bluetooth CAP commander shell commands
Subcommands:
  discover                  :Discover CAS
  cancel                    :CAP commander cancel current procedure
  change_volume             :Change volume on all connections <volume>
  change_volume_mute        :Change volume mute state on all connections <mute>
  change_volume_offset      :Change volume offset per connection <volume_offset
                             [volume_offset [...]]>
  change_microphone_mute    :Change microphone mute state on all connections <mute>
  change_microphone_gain    :Change microphone gain per connection <gain
                             [gain [...]]>
  broadcast_reception_start : Start broadcast reception with source
                              <address: P:XX:XX:XX:XX:XX:XX or R:XX:XX:XX:XX:XX:XX>
                              <adv_sid> <broadcast_id>
                              [<pa_interval>] [<sync_bis>] [<metadata>]
  broadcast_reception_stop  : Stop broadcast reception <src_id [...]>
  distribute_broadcast_code : Distribute broadcast code <src_id [...]> <broadcast_code>
```

在执行任何音频流操作之前，设备还必须执行 `bap discover`，发现 ASE 和 PAC 记录；也需要调用 `bap init`。

<a id="id1"></a>

#### 56.3.1.1 已连接时（When connected）

<a id="discovering-cas-and-csis-on-a-device"></a>

##### 56.3.1.1.1 发现设备上的 CAS 与 CSIS

```text
uart:~$ cap_commander discover
discovery completed with CSIS
```

<a id="setting-the-volume-on-all-connected-devices"></a>

##### 56.3.1.1.2 设置所有已连接设备的音量

```text
uart:~$ vcp_vol_ctlr discover
VCP discover done with 1 VOCS and 1 AICS
uart:~$ cap_commander change_volume 15
uart:~$ cap_commander change_volume 15
Setting volume to 15 on 2 connections
VCP volume 15, mute 0
VCP vol_set done
VCP volume 15, mute 0
VCP flags 0x01
VCP vol_set done
Volume change completed
```

<a id="setting-the-volume-offset-on-one-or-more-devices"></a>

##### 56.3.1.1.3 设置一台或多台设备的音量偏移（volume offset）

偏移值按连接索引分配：连接索引 0 使用第一个偏移值，索引 1 使用第二个偏移值，以此类推：

```text
uart:~$ bt connect <device A>
Connected: <device A>
uart:~$ cap_commander discover
discovery completed with CSIS
uart:~$ vcp_vol_ctlr discover
VCP discover done with 1 VOCS and 1 AICS
uart:~$
uart:~$ bt connect <device B>
Connected: <device B>
uart:~$ cap_commander discover
discovery completed with CSIS
uart:~$ vcp_vol_ctlr discover
VCP discover done with 1 VOCS and 1 AICS
uart:~$
uart:~$ cap_commander change_volume_offset 10
Setting volume offset on 1 connections
VOCS inst 0x200140a4 offset 10
Offset set for inst 0x200140a4
Volume offset change completed
uart:~$
uart:~$ cap_commander change_volume_offset 10 15
Setting volume offset on 2 connections
Offset set for inst 0x200140a4
VOCS inst 0x20014188 offset 15
Offset set for inst 0x20014188
Volume offset change completed
```

<a id="setting-the-volume-mute-on-all-connected-devices"></a>

##### 56.3.1.1.4 设置所有已连接设备的音量静音状态

```text
uart:~$ bt connect <device A>
Connected: <device A>
uart:~$ cap_commander discover
discovery completed with CSIS
uart:~$ vcp_vol_ctlr discover
VCP discover done with 1 VOCS and 1 AICS
uart:~$
uart:~$ bt connect <device B>
Connected: <device B>
uart:~$ cap_commander discover
discovery completed with CSIS
uart:~$ vcp_vol_ctlr discover
VCP discover done with 1 VOCS and 1 AICS
uart:~$
uart:~$ cap_commander change_volume_mute 1
Setting volume mute to 1 on 2 connections
VCP volume 100, mute 1
VCP mute done
VCP volume 100, mute 1
VCP mute done
Volume mute change completed
uart:~$ cap_commander change_volume_mute 0
Setting volume mute to 0 on 2 connections
VCP volume 100, mute 0
VCP unmute done
VCP volume 100, mute 0
VCP unmute done
Volume mute change completed
```

<a id="setting-the-microphone-mute-on-all-connected-devices"></a>

##### 56.3.1.1.5 设置所有已连接设备的麦克风静音状态

```text
uart:~$ bt connect <device A>
Connected: <device A>
uart:~$ cap_commander discover
discovery completed with CSIS
uart:~$ micp_mic_ctlr discover
MICP discover done with 1 VOCS and 1 AICS
uart:~$
uart:~$ bt connect <device B>
Connected: <device B>
uart:~$ cap_commander discover
discovery completed with CSIS
uart:~$ micp_mic_ctlr discover
MICP discover done with 1 VOCS and 1 AICS
uart:~$
uart:~$ cap_commander change_microphone_mute 1
Setting microphone mute to 1 on 2 connections
MICP microphone 100, mute 1
MICP mute done
MICP microphone 100, mute 1
MICP mute done
Microphone mute change completed
uart:~$ cap_commander change_microphone_mute 0
Setting microphone mute to 0 on 2 connections
MICP microphone 100, mute 0
MICP unmute done
MICP microphone 100, mute 0
MICP unmute done
Microphone mute change completed
```

<a id="setting-the-microphone-gain-on-one-or-more-devices"></a>

##### 56.3.1.1.6 设置一台或多台设备的麦克风增益（gain）

增益按连接索引分配：连接索引 0 使用第一个值，索引 1 使用第二个值，以此类推。原文在此将这些增益值称为“offset”：

```text
uart:~$ bt connect <device A>
Connected: <device A>
uart:~$ cap_commander discover
discovery completed with CSIS
uart:~$ micp_mic_ctlr discover
MICP discover done with 1 AICS
uart:~$
uart:~$ bt connect <device B>
Connected: <device B>
uart:~$ cap_commander discover
discovery completed with CSIS
uart:~$ micp_mic_ctlr discover
MICP discover done with 1 AICS
uart:~$
uart:~$ cap_commander change_microphone_gain 10
Setting microphone gain on 1 connections
AICS inst 0x200140a4 state gain 10, mute 0, mode 0
Gain set for inst 0x200140a4
Microphone gain change completed
uart:~$
uart:~$ cap_commander change_microphone_gain 10 15
Setting microphone gain on 2 connections
Gain set for inst 0x200140a4
AICS inst 0x20014188 state gain 15, mute 0, mode 0
Gain set for inst 0x20014188
Microphone gain change completed
```

<a id="starting-and-stopping-broadcast-reception"></a>

##### 56.3.1.1.7 启动与停止广播接收

```text
uart:~$ bt connect <device A>
Connected: <device A>
uart:~$ bap_init
uart:~$ cap_commander discover
discovery completed with CSIS
uart:~$ bap_broadcast_assistant discover
BASS discover done with 1 recv states
uart:~$ cap_commander broadcast_reception_start <device B> 0 4
Starting broadcast reception on 1 connection(s)
Broadcast reception start completed
uart:~$ cap_commander broadcast_reception_stop 0
Stopping broadcast reception on 1 connection(s)
Broadcast reception stop completed
```

<a id="distributing-the-broadcast-code"></a>

##### 56.3.1.1.8 分发广播码

```text
uart:~$ bt connect <device A>
Connected: <device A>
uart:~$ bap_init
uart:~$ cap_commander discover
discovery completed with CSIS
uart:~$ bap_broadcast_assistant discover
BASS discover done with 1 recv states
uart:~$ cap_commander broadcast_reception_start <device B> 0 4
Starting broadcast reception on 1 connection(s)
Broadcast reception start completed
uart:~$ cap_commander distribute_broadcast_code 0 "BroadcastCode"
Distribute broadcast code completed
```

<a id="cap-handover"></a>

## 56.4 CAP 切换（CAP Handover）

切换过程允许在单播音频流与广播音频流之间切换。由于广播音频流始终为单向，这些过程只适用于音频从发起方流向接受方的流，即接收端音频流（sink stream）。

<a id="using-the-cap-handover-procedures"></a>

### 56.4.1 使用 CAP 切换过程（Using the CAP Handover procedures）

蓝牙协议栈完成初始化（`bt init`）、连接一个或多个远端 CAP 接受方设备并建立音频流后，即可用切换过程在单播与广播之间切换。执行任一切换过程前，必须已经发出并完成 `bap discover`、`cap_initiator discover` 和 `bap_broadcast_assistant discover` 命令。

```text
cap_handover --help
cap_handover - Bluetooth CAP handover shell commands
Subcommands:
  unicast_to_broadcast  : Handover current unicast group to broadcast (unicast
                        group will be deleted) [enc <broadcast_code>] [preset <preset_name>]
  broadcast_to_unicast  : Handover current broadcast source to unicast
                        (broadcast source will be deleted)
                        [conns <count>|all] [preset <preset_name>]
```

<a id="handover-unicast-to-broadcast"></a>

#### 56.4.1.1 从单播切换到广播（Handover unicast to broadcast）

该命令将一个或多个单播音频流切换为广播。

```text
uart:~$ bt init
uart:~$ bap init
uart:~$ bt connect <addr>

# Discover necessary services
uart:~$ bap discover
uart:~$ cap_initiator discover
uart:~$ bap_broadcast_assistant discover

# Setup unicast audio e.g. using the ac_1
uart:~$ cap_initiator ac_1

# Create a non-connectable and non-scannable extended advertising set for broadcast
uart:~$ bt adv-create nconn-nscan ext-adv
uart:~$ bt per-adv-param

# Perform the handover and update the advertising data to contain the broadcast ID
uart:~$ cap_handover unicast_to_broadcast
uart:~$ bt adv-data dev-name discov
uart:~$ bt per-adv-data

# Enable periodic advertising (extended advertising is enabled as part of handover)
uart:~$ bt per-adv on
```

<a id="handover-broadcast-to-unicast"></a>

#### 56.4.1.2 从广播切换到单播（Handover broadcast to unicast）

该命令把一个或多个音频流从广播切换到单播；原文在这一句中也将待切换对象称为“unicast streams”。

```text
uart:~$ bt init
uart:~$ bap init
uart:~$ bt connect <addr>

# Discover necessary services
uart:~$ bap discover
uart:~$ cap_initiator discover
uart:~$ bap_broadcast_assistant discover

# Create a non-connectable and non-scannable extended advertising set for broadcast
uart:~$ bt adv-create nconn-nscan ext-adv
uart:~$ bt per-adv-param

# Setup broadcast audio e.g. using the ac_12
uart:~$ cap_initiator ac_12
uart:~$ cap_initiator broadcast_start

# Set advertising data and enable advertising
uart:~$ bt adv-data dev-name discov
uart:~$ bt per-adv-data
uart:~$ bt per-adv on
uart:~$ bt adv-start

# Wait for broadcast sink to self-scan, or use broadcast reception to instruct sink to sync

# Perform the handover
uart:~$ cap_handover broadcast_to_unicast

# Terminate the advertiser (optional)
uart:~$ bt adv-stop
uart:~$ bt per-adv off
uart:~$ bt adv-delete
```

对应官方文档源码：[doc/services/connectivity/bluetooth/shell/audio/cap.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/doc/services/connectivity/bluetooth/shell/audio/cap.rst)。

> 译注——源码跟踪：本仓库[对应源码](../../../doc/services/connectivity/bluetooth/shell/audio/cap.rst)可用于对照，版本可能与网页不同。本批仅翻译和核对文档，未构建固件或连接音频设备。

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：BAP扫描委托方Shell](P055_BAP扫描委托方Shell.md) · [本模块主线目录](../reading/bluetooth.md) · [全部主线](../reading/README.md) · [下一篇：通话控制配置文件CCP_Shell](P057_通话控制配置文件CCP_Shell.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章](P055_BAP扫描委托方Shell.md) · [返回大纲](大纲.md) · [下一章](P057_通话控制配置文件CCP_Shell.md)

</details>

<!-- reading-navigation:end -->
