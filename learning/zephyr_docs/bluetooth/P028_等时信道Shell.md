---
id: learning.zephyr-docs.bluetooth.page-28
title: 等时信道Shell
kind: reference
status: maintained
domains: [zephyr, bluetooth, documentation]
source_url: https://docs.zephyrproject.org/latest/services/connectivity/bluetooth/shell/host/iso.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="bluetooth-isochronous-channels-shell"></a>

# 第28章\_等时信道Shell

原文：[官方页面](https://docs.zephyrproject.org/latest/services/connectivity/bluetooth/shell/host/iso.html)。读取日期：2026-10-14；保存的 latest 页面及 HTML 摘要见[来源记录](../SOURCES.md)。

> 译注——使用前提：以下命令在启用了对应蓝牙功能的目标固件Zephyr Shell中执行，初始化与接入方式见[蓝牙Shell](P007_蓝牙Shell.md)。代码中的 `uart:~$` 是提示符，其后输出是原文预期结果；输入命令时不复制提示符和日志。若命令不可用或初始化失败，应先检查目标配置、控制器能力及当前版本帮助，再继续连接或传输步骤。本批仅翻译与核对文档，未连接设备或执行这些命令。

等时（Isochronous，ISO）信道Shell提供单播与广播操作。连接等时组（Connected Isochronous Group，CIG）包含连接等时流（Connected Isochronous Stream，CIS）；广播等时组（Broadcast Isochronous Group，BIG）包含广播等时流（Broadcast Isochronous Stream，BIS）。下文先列原命令帮助，再按两种通信方式演示。

<a id="commands"></a>

## 28.1\_命令（Commands）

```text
iso --help
iso - Bluetooth ISO shell commands
Subcommands:
   cig_create  :[dir=tx,rx,txrx] [interval] [packing] [framing] [latency] [sdu]
               [phy] [rtn]
   cig_term    :Terminate the CIG
   connect     :Connect ISO Channel
   listen      :<dir=tx,rx,txrx> [security level]
   send        :Send to ISO Channel [count]
   disconnect  :Disconnect ISO Channel
   create-big  :Create a BIG as a broadcaster [enc <broadcast code>]
   broadcast   :Broadcast on ISO channels
   sync-big    :Synchronize to a BIG as a receiver <BIS bitfield> [mse] [timeout]
               [enc <broadcast code>]
   term-big    :Terminate a BIG
```

> 译注——命令对照：`cig_create`／`cig_term`创建／终止CIG；`connect`／`disconnect`连接／断开ISO信道；`listen`监听连接；`send`向ISO信道发送数据，count为次数。`create-big`以广播者身份创建BIG，`broadcast`发送ISO广播，`sync-big`以接收者身份同步BIG，`term-big`终止BIG。

> 译注——帮助参数：dir中的tx、rx、txrx表示发送、接收、双向；interval为间隔，packing为数据包排列方式，framing为成帧方式，latency为延迟，sdu为服务数据单元（Service Data Unit，SDU）大小，phy为物理层（Physical Layer，PHY），rtn为重传次数（Retransmission Number）。BIS bitfield是所选BIS的位域，mse为最大子事件数（Maximum Subevents），timeout为同步超时，enc后接广播码（Broadcast Code）。可用参数及单位应以所用版本帮助与接口定义为准。

<a id="unicast-examples"></a>

## 28.2\_单播示例（Unicast examples）

1. 中心设备（Central）创建CIG。前提是两台设备已经连接：

```text
uart:~$ iso cig_create
CIG created
```

2. 外设（Peripheral）监听ISO连接，方向为双向：

```text
uart:~$ iso listen txrx
```

3. 中心设备连接ISO信道：

```text
uart:~$ iso connect
ISO Connect pending...
ISO Channel 0x20000f88 connected
```

4. 发送数据：

```text
uart:~$ iso send
send: 40 bytes of data
ISO sending...
```

5. 断开ISO信道：

```text
uart:~$ iso disconnect
ISO Disconnect pending...
ISO Channel 0x20000f88 disconnected with reason 0x16
```

> 译注——单播输出：CIG created表示组已创建；Connect pending表示正在连接，connected表示已连接。示例发送40字节；Disconnect pending表示正在断开，disconnected with reason 0x16保留原文断开原因码。以上是预期日志，不是当前设备测试结果。

<a id="broadcast-examples"></a>

## 28.3\_广播示例（Broadcast examples）

<a id="setting-up-broadcaster"></a>

### 28.3.1\_设置广播者（Setting up broadcaster）

```text
uart:~$ bt init
Bluetooth initialized
uart:~$ bt adv-create nconn-nscan ext-adv
Created adv id: 0, adv: 0x200025d0
uart:~$ bt per-adv-param
uart:~$ iso create-big
BIG created
ISO Channel 0x200008c0 connected
uart:~$
uart:~$ bt adv-start
Advertiser[0] 0x200025d0 set started
uart:~$
uart:~$ bt per-adv on
Periodic advertising started
uart:~$
uart:~$ iso broadcast
send: 247 bytes of data with PSN 4350
ISO broadcasting...
```

> 译注——广播顺序：先初始化蓝牙，创建不可连接且不可扫描的扩展广播者，设置周期性广播参数，再创建BIG、启动广播及周期性广播，最后发送ISO广播数据。日志中的247字节为此次示例发送大小，PSN为包序列号（Packet Sequence Number）。

若需要加密广播，可以提供广播码，原文示例如下：

```text
uart:~$ iso create-big enc 00112233445566778899aabbccddffff
BIG created
```

> 译注——原广播码长度：示例 `00112233445566778899aabbccddffff` 是30个十六进制字符，即15字节。所读取的[官方ISO头文件](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/include/zephyr/bluetooth/iso.h)规定广播码大小为16字节，[Shell创建端实现](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/subsys/bluetooth/host/shell/iso.c)检查长度必须恰好等于该大小。因此在此实现上，原命令会被拒绝，不能把其后BIG created当作当前版本保证。使用时在两端设置同一完整16字节广播码，例如用于演示的 `00112233445566778899aabbccddeeff00`；本批未执行加密广播。

<a id="setting-up-sync-receiver"></a>

### 28.3.2\_设置同步接收者（Setting up sync receiver）

```text
uart:~$ bt init
Bluetooth initialized
uart:~$ bt scan on
[DEVICE]: R:42:0F:7A:40:AE:21, AD evt type 5, RSSI -27  C:0 S:0 D:0 SR:0 E:1 Prim: LE 1M, Secn: LE 2M, Interval: 0x0780 (2400000 us), SID: 0x0
uart:~$ bt per-adv-sync-create R:42:0F:7A:40:AE:21 0
Per adv sync pending
PER_ADV_SYNC[0]: [DEVICE]: R:42:0F:7A:40:AE:21 synced, Interval 0x0780 (2400000 us), PHY LE 2M, SD 0x0000, PAST peer not present
PER_ADV_SYNC[0]: [DEVICE]: R:42:0F:7A:40:AE:21, tx_power 127, RSSI -28, CTE 0, data length 0
BIG_INFO PER_ADV_SYNC[0]: [DEVICE]: R:42:0F:7A:40:AE:21, sid 0x00, num_bis 1, nse 0x04, interval 0x0008 (10000 us), bn 0x01, pto 0x01, irc 0x03, max_pdu 0x00f7, sdu_interval 0x2710, max_sdu 0x00f7, phy LE 2M, framing 0x00, not encrypted
uart:~$ iso sync-big 1
BIG syncing
ISO Channel 0x200008c0 connected
```

> 译注——接收顺序：初始化并扫描，根据设备地址和广播集标识（Advertising SID）创建周期性广播同步（Periodic Advertising Synchronization）。synced表示周期同步已建立，BIG_INFO报告广播等时组信息；最后 `iso sync-big 1` 选择位域的最低位，即BIS索引1，开始同步等时流。它不是把数字1当作BIG标识。设备地址、SID、间隔和信道地址均按原例保留，使用时需以实际扫描结果为准。

> 译注——组信息字段：RSSI为接收信号强度指示（Received Signal Strength Indicator），CTE为恒定音调扩展（Constant Tone Extension），PAST为周期性广播同步传输（Periodic Advertising Sync Transfer）；SD为同步传输关联的服务数据（Service Data）。num_bis为BIS数量，nse为子事件数量，bn为突发数（Burst Number），pto为预传输偏移（Pre-Transmission Offset），irc为立即重复计数（Immediate Repetition Count）；max_pdu为最大协议数据单元（Protocol Data Unit，PDU），sdu_interval／max_sdu为SDU间隔／最大SDU大小，framing为成帧方式，not encrypted表示未加密。原日志中的tx_power 127属于原始字段值，不应解释成实际127 dBm发射功率。

若需要接收加密广播，也可以提供广播码，原文示例如下：

```text
uart:~$ iso sync-big 1 enc 00112233445566778899aabbccddffff
BIG syncing
ISO Channel 0x200008c0 connected
```

> 译注——两端一致：本段沿用原文15字节示例。所读接收端实现先将广播码缓冲区清零，再解码输入；这与创建端严格要求16字节的检查不同。不要依赖这种差异使短码偶然补零，两端应显式使用相同完整16字节值，并与前一小节同步修改。


对应官方文档源码：[doc/services/connectivity/bluetooth/shell/host/iso.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/doc/services/connectivity/bluetooth/shell/host/iso.rst)。

> 译注——源码跟踪：本仓库的[对应源码](../../../doc/services/connectivity/bluetooth/shell/host/iso.rst)可用于跟踪，版本可能与网页不同；本批仅翻译和核对文档，没有执行固件构建、模拟运行或烧录。

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：L2CAP_Shell](P027_L2CAP_Shell.md) · [本模块主线目录](../reading/bluetooth.md) · [全部主线](../reading/README.md) · [下一篇：高级音频分发配置文件A2DP](P029_高级音频分发配置文件A2DP.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章](P027_L2CAP_Shell.md) · [返回大纲](大纲.md) · [下一章](P029_高级音频分发配置文件A2DP.md)

</details>

<!-- reading-navigation:end -->
