---
id: learning.zephyr-docs.bluetooth.page-59
title: 游戏音频配置文件GMAP_Shell
kind: reference
status: maintained
domains: [zephyr, bluetooth, documentation]
source_url: https://docs.zephyrproject.org/latest/services/connectivity/bluetooth/shell/audio/gmap.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="bluetooth-gaming-audio-profile-shell"></a>

# 第59章\_蓝牙：游戏音频配置文件 Shell（Bluetooth: Gaming Audio Profile Shell）

原文：[官方页面](https://docs.zephyrproject.org/latest/services/connectivity/bluetooth/shell/audio/gmap.html)。快照读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

> 译注——操作上下文：代码块中的命令在启用了相应音频功能的目标固件 Zephyr Shell 中执行，接入与初始化见[蓝牙 Shell](P007_蓝牙Shell.md)。`uart:~$` 是提示符，后续日志是官方预期输出；不要把提示符、日志或 `<address>` 等占位符原样当作主机终端命令运行。各示例代表不同角色和操作分支，按实际连接与初始化状态选择，不连贯粘贴整章。命令缺失、初始化失败或发现未完成时，应先核对固件配置、控制器能力及当前版本帮助，再继续后续操作。

> 译注——版本与验证：原文“当前”“尚未实现”等表述均保留其快照语境。代码块完整保留原始命令、帮助和输出，本文没有执行固件构建、连接音频设备或验证互操作性。

> 译注——术语：UGG 为单播游戏网关（Unicast Game Gateway），UGT 为单播游戏终端（Unicast Game Terminal）；BGS／BGR 分别为广播游戏发送方／接收方（Broadcast Game Sender/Receiver）。日志中的 `ugg_feat`、`ugt_feat`、`bgs_feat`、`bgr_feat` 是不同角色的功能位，不等同于当前连接的 GAP 角色。

本文说明如何运行游戏音频配置文件（Gaming Audio Profile，GMAP）的 Shell 功能。与大多数较低层配置文件不同，GMAP 在所有参与设备上都存在，并具有游戏音频服务（Gaming Audio Service，GMAS）。因此，发起方与接受方，或中心设备与外围设备，都应发现远端设备的 GMAS，确定其支持的 GMAP 角色与功能。

<a id="using-the-gmap-shell"></a>

## 59.1 使用 GMAP Shell（Using the GMAP Shell）

蓝牙协议栈完成初始化（`bt init`）后，可以调用 `gmap init` 注册 GMAS；原文也强烈建议通过 `bap init` 启用 BAP。

```text
uart:~$ gmap --help
gmap - Bluetooth GMAP shell commands
Subcommands:
  init      : [none]
  set_role  : [ugt | ugg | bgr | bgs]
  discover  : [none]
  ac_1      : Unicast audio configuration 1
  ac_2      : Unicast audio configuration 2
  ac_3      : Unicast audio configuration 3
  ac_4      : Unicast audio configuration 4
  ac_5      : Unicast audio configuration 5
  ac_6_i    : Unicast audio configuration 6(i)
  ac_6_ii   : Unicast audio configuration 6(ii)
  ac_7_ii   : Unicast audio configuration 7(ii)
  ac_8_i    : Unicast audio configuration 8(i)
  ac_8_ii   : Unicast audio configuration 8(ii)
  ac_11_i   : Unicast audio configuration 11(i)
  ac_11_ii  : Unicast audio configuration 11(ii)
  ac_12     : Broadcast audio configuration 12
  ac_13     : Broadcast audio configuration 13
  ac_14     : Broadcast audio configuration 14
```

在设备支持相应角色的前提下，可以通过 `set_role` 命令在运行时更改角色；GMAP 角色依赖某些 BAP 配置。

<a id="example-central-with-gmap-ugt-role"></a>

## 59.2 具有 GMAP UGT 角色的中心设备示例（Example Central with GMAP UGT role）

使用音频配置（Audio Configuration，AC）3 连接并建立游戏音频流；为便于阅读，原文省略了部分日志：

```text
uart:~$ bt init
uart:~$ bap init
uart:~$ gmap init
uart:~$ bt connect <address>
uart:~$ gatt exchange-mtu
uart:~$ bap discover
Discover complete: err 0
uart:~$ cap_initiator discover
discovery completed with CSIS
uart:~$ gmap discover
gmap discovered for conn 0x2001c7d8:
     role 0x0f
     ugg_feat 0x07
     ugt_feat 0x6f
     bgs_feat 0x01
     bgr_feat 0x03
uart:~$ bap preset sink 32_2_gr
uart:~$ bap preset source 32_2_gs
uart:~$ gmap ac_3
Starting 2 streams for AC_3
stream 0x20020060 config operation rsp_code 0 reason 0
stream 0x200204d0 config operation rsp_code 0 reason 0
stream 0x200204d0 qos operation rsp_code 0 reason 0
stream 0x20020060 qos operation rsp_code 0 reason 0
Stream 0x20020060 enabled
stream 0x200204d0 enable operation rsp_code 0 reason 0
Stream 0x200204d0 enabled
stream 0x20020060 enable operation rsp_code 0 reason 0
Stream 0x20020060 started
stream 0x200204d0 start operation rsp_code 0 reason 0
Stream 0x200204d0 started
Unicast start completed
uart:~$ bap start_sine
Started transmitting on default_stream 0x20020060
[0]: stream 0x20020060 : TX LC3: 80 (seq_num 24800)
```

对应官方文档源码：[doc/services/connectivity/bluetooth/shell/audio/gmap.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/doc/services/connectivity/bluetooth/shell/audio/gmap.rst)。

> 译注——源码跟踪：本仓库[对应源码](../../../doc/services/connectivity/bluetooth/shell/audio/gmap.rst)可用于对照，版本可能与网页不同。本批仅翻译和核对文档，未构建固件或连接音频设备。

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：协调集标识配置文件CSIP_Shell](P058_协调集标识配置文件CSIP_Shell.md) · [本模块主线目录](../reading/bluetooth.md) · [全部主线](../reading/README.md) · [下一篇：媒体控制配置文件MCP_Shell](P060_媒体控制配置文件MCP_Shell.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章](P058_协调集标识配置文件CSIP_Shell.md) · [返回大纲](大纲.md) · [下一章](P060_媒体控制配置文件MCP_Shell.md)

</details>

<!-- reading-navigation:end -->
