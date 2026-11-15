---
id: learning.zephyr-docs.bluetooth.page-55
title: BAP扫描委托方Shell
kind: reference
status: maintained
domains: [zephyr, bluetooth, documentation]
source_url: https://docs.zephyrproject.org/latest/services/connectivity/bluetooth/shell/audio/bap_scan_delegator.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="bluetooth-basic-audio-profile-scan-delegator-shell"></a>

# 第55章\_蓝牙：基本音频配置文件扫描委托方 Shell（Bluetooth: Basic Audio Profile: Scan Delegator Shell）

原文：[官方页面](https://docs.zephyrproject.org/latest/services/connectivity/bluetooth/shell/audio/bap_scan_delegator.html)。快照读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

> 译注——操作上下文：代码块中的命令在启用了相应音频功能的目标固件 Zephyr Shell 中执行，接入与初始化见[蓝牙 Shell](P007_蓝牙Shell.md)。`uart:~$` 是提示符，后续日志是官方预期输出；不要把提示符、日志或 `<address>` 等占位符原样当作主机终端命令运行。各示例代表不同角色和操作分支，按实际连接与初始化状态选择，不连贯粘贴整章。命令缺失、初始化失败或发现未完成时，应先核对固件配置、控制器能力及当前版本帮助，再继续后续操作。

> 译注——版本与验证：原文“当前”“尚未实现”等表述均保留其快照语境。代码块完整保留原始命令、帮助和输出，本文没有执行固件构建、连接音频设备或验证互操作性。

> 译注——术语：BAP 为基本音频配置文件（Basic Audio Profile）；PA 为周期性广播（Periodic Advertising），PAST 为周期性广播同步传输（Periodic Advertising Synchronization Transfer）。

本文说明如何运行扫描委托方（Scan Delegator）功能。下方示例按原文删去了部分调试行，以缩短篇幅并便于理解整体流程。

扫描委托方可以选择支持周期性广播同步传输（PAST）协议。

扫描委托方服务端通常位于具有输入或输出的设备上。

要以交互方式使用扫描委托方，必须启用 [`CONFIG_BT_BAP_SCAN_DELEGATOR_LOG_LEVEL_DBG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_BAP_SCAN_DELEGATOR_LOG_LEVEL_DBG)。

原文说明：扫描委托方目前只能设置接收状态中的同步状态，尚不真正支持与周期性广播同步。

> 译注——版本差异：当前读取的[官方源码](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/subsys/bluetooth/audio/shell/bap_scan_delegator.c)及本仓库的[相对路径对照](../../../subsys/bluetooth/audio/shell/bap_scan_delegator.c)已包含 `bt_le_per_adv_sync_create()` 调用及同步回调。这里保留原页的历史限制；实际可用行为还取决于所用版本、配置和控制器，本批未运行同步实验。

```text
bap_scan_delegator --help
bap_scan_delegator - Bluetooth BAP Scan Delegator shell commands
Subcommands:
  init                : Initialize the service and register callbacks
  set_past_pref       : Set PAST preference <true || false>
  sync_pa             : Sync to PA <src_id>
  term_pa             : Terminate PA sync <src_id>
  add_src             : Add a PA as source <addr> <sid> <broadcast_id>
                       <enc_state> [bis_sync [metadata]]
  add_src_by_pa_sync  : Add a PA as source <broadcast_id> <enc_state> [bis_sync
                       [metadata]]
  mod_src             : Modify source <src_id> <broadcast_id> <enc_state>
                       [bis_sync [metadata]]
  rem_src             : Remove source <src_id>
  synced              : Set server scan state <src_id> <bis_syncs>
```

<a id="example-usage"></a>

## 55.1 使用示例（Example Usage）

<a id="setup"></a>

### 55.1.1 准备（Setup）

```text
uart:~$ bt init
uart:~$ bap_scan_delegator init
uart:~$ bt advertise on
Advertising started
```

<a id="adding-a-source"></a>

### 55.1.2 添加发送端（Adding a source）

```text
uart:~$ bap_scan_delegator add_src P:11:22:33:44:55:66 0 1234 0
Receive state with ID 0 updated
```

<a id="adding-a-source-from-a-pa-sync"></a>

### 55.1.3 从周期性广播同步添加发送端（Adding a source from a PA sync）

```text
uart:~$ bt scan on
Found broadcaster with ID 0x681A22 and addr R:2C:44:05:82:EB:82 and sid 0x00 (looking for 0x1000000)
uart:~$ bt scan off
uart:~$ bt per-adv-sync-create R:2C:44:05:82:EB:82 0
PA 0x2003e9b0 synced
uart:~$ bap_scan_delegator add_src_by_pa_sync 0x681A22 0
Receive state with ID 0 updated
```

<a id="when-connected"></a>

### 55.1.4 已连接时（When connected）

设置发送端的同步状态：

```text
uart:~$ bap_scan_delegator synced 0 1 3 0
```

对应官方文档源码：[doc/services/connectivity/bluetooth/shell/audio/bap_scan_delegator.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/doc/services/connectivity/bluetooth/shell/audio/bap_scan_delegator.rst)。

> 译注——源码跟踪：本仓库[对应源码](../../../doc/services/connectivity/bluetooth/shell/audio/bap_scan_delegator.rst)可用于对照，版本可能与网页不同。本批仅翻译和核对文档，未构建固件或连接音频设备。

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：BAP广播助手Shell](P054_BAP广播助手Shell.md) · [本模块主线目录](../reading/bluetooth.md) · [全部主线](../reading/README.md) · [下一篇：通用音频配置文件CAP_Shell](P056_通用音频配置文件CAP_Shell.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章](P054_BAP广播助手Shell.md) · [返回大纲](大纲.md) · [下一章](P056_通用音频配置文件CAP_Shell.md)

</details>

<!-- reading-navigation:end -->
