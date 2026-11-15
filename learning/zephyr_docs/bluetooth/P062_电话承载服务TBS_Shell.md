---
id: learning.zephyr-docs.bluetooth.page-62
title: 电话承载服务TBS_Shell
kind: reference
status: maintained
domains: [zephyr, bluetooth, documentation]
source_url: https://docs.zephyrproject.org/latest/services/connectivity/bluetooth/shell/audio/tbs.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="bluetooth-telephone-bearer-service-shell"></a>

# 第62章\_蓝牙：电话承载服务 Shell（Bluetooth: Telephone Bearer Service Shell）

原文：[官方页面](https://docs.zephyrproject.org/latest/services/connectivity/bluetooth/shell/audio/tbs.html)。快照读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

> 译注——操作上下文：代码块中的命令在启用了相应音频功能的目标固件 Zephyr Shell 中执行，接入与初始化见[蓝牙 Shell](P007_蓝牙Shell.md)。`uart:~$` 是提示符，后续日志是官方预期输出；不要把提示符、日志或 `<address>` 等占位符原样当作主机终端命令运行。各示例代表不同角色和操作分支，按实际连接与初始化状态选择，不连贯粘贴整章。命令缺失、初始化失败或发现未完成时，应先核对固件配置、控制器能力及当前版本帮助，再继续后续操作。

> 译注——版本与验证：原文“当前”“尚未实现”等表述均保留其快照语境。代码块完整保留原始命令、帮助和输出，本文没有执行固件构建、连接音频设备或验证互操作性。

> 译注——术语：TBS 为电话承载服务（Telephone Bearer Service），GTBS 为通用电话承载服务（Generic Telephone Bearer Service）；UCI 为统一呼叫标识符（Uniform Caller Identifier），URI 为统一资源标识符（Uniform Resource Identifier）。

本文说明如何以客户端和电话承载服务（Telephone Bearer Service，TBS）服务端两种角色运行通话控制功能。下方示例按原文删去了部分调试行，以缩短篇幅并便于理解整体流程。

<a id="telephone-bearer-service-client"></a>

## 62.1 电话承载服务客户端（Telephone Bearer Service Client）

TBS 客户端通常位于资源受限的设备，例如耳机，也可能位于手机或笔记本电脑。因此，通话控制客户端通常也承担广播方角色。客户端可以通过通话控制点控制服务端上的通话状态。

要以交互方式使用客户端，必须启用 [`CONFIG_BT_TBS_CLIENT_LOG_LEVEL_DBG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_TBS_CLIENT_LOG_LEVEL_DBG)。

<a id="using-the-telephone-bearer-service-client"></a>

### 62.1.1 使用电话承载服务客户端（Using the telephone bearer service client）

蓝牙协议栈完成初始化（`bt init`）且已经连接设备后，可以调用 `tbs_client discover`，在已连接设备上发现 TBS。该命令开始发现 TBS 的 UUID，保存句柄，并可选地订阅所有通知；默认全部订阅。

服务端可能有多个 TBS 实例，因此大多数 `tbs_client` 命令接受从 0 开始的索引作为输入。合并通话至少需要 2 个通话标识，且所有通话索引必须属于同一个 TBS 实例。

服务端还会有一个 GTBS 实例，为其所有电话承载提供抽象层。若服务端同时具有 GTBS 与 TBS，且启用了 `BT_TBS_CLIENT_GTBS`，客户端可以订阅两者，并在发送请求时选择使用其中之一。

```text
tbs_client --help
tbs_client - Bluetooth TBS_CLIENT shell commands
Subcommands:
   discover                       :Discover TBS [subscribe]
   set_signal_reporting_interval  :Set the signal reporting interval
                                    [<{instance_index, gtbs}>] <interval>
   originate                      :Originate a call [<{instance_index, gtbs}>]
                                    <uri>
   terminate                      :terminate a call [<{instance_index, gtbs}>]
                                    <id>
   accept                         :Accept a call [<{instance_index, gtbs}>] <id>
   hold                           :Place a call on hold [<{instance_index,
                                    gtbs}>] <id>
   retrieve                       :Retrieve a held call [<{instance_index,
                                    gtbs}>] <id>
   read_provider_name             :Read the bearer name [<{instance_index,
                                    gtbs}>]
   read_bearer_uci                :Read the bearer UCI [<{instance_index, gtbs}>]
   read_technology                :Read the bearer technology [<{instance_index,
                                    gtbs}>]
   read_uri_list                  :Read the bearer's supported URI list
                                    [<{instance_index, gtbs}>]
   read_signal_strength           :Read the bearer signal strength
                                    [<{instance_index, gtbs}>]
   read_signal_interval           :Read the bearer signal strength reporting
                                    interval [<{instance_index, gtbs}>]
   read_current_calls             :Read the current calls [<{instance_index,
                                    gtbs}>]
   read_ccid                      :Read the CCID [<{instance_index, gtbs}>]
   read_status_flags              :Read the in feature and status value
                                    [<{instance_index, gtbs}>]
   read_uri                       :Read the incoming call target URI
                                    [<{instance_index, gtbs}>]
   read_call_state                :Read the call state [<{instance_index, gtbs}>]
   read_remote_uri                :Read the incoming remote URI
                                    [<{instance_index, gtbs}>]
   read_friendly_name             :Read the friendly name of an incoming call
                                    [<{instance_index, gtbs}>]
   read_optional_opcodes          :Read the optional opcodes [<{instance_index,
                                    gtbs}>]
```

下方示例除非另有说明，否则忽略来自 GTBS 的通知。

<a id="example-usage"></a>

### 62.1.2 使用示例（Example usage）

<a id="setup"></a>

#### 62.1.2.1 准备（Setup）

```text
uart:~$ bt init
uart:~$ bt advertise on
Advertising started
```

<a id="when-connected"></a>

#### 62.1.2.2 已连接时（When connected）

发起通话：

```text
uart:~$ tbs_client discover
<dbg> bt_tbs_client.primary_discover_func: Discover complete, found 1 instances (GTBS found)
<dbg> bt_tbs_client.discover_func: Setup complete for 1 / 1 TBS
<dbg> bt_tbs_client.discover_func: Setup complete GTBS
uart:~$ tbs_client originate 0 tel:123
<dbg> bt_tbs_client.notify_handler: Index 0
<dbg> bt_tbs_client.current_calls_notify_handler: Call 0x01 is in the dialing state with URI tel:123
<dbg> bt_tbs_client.call_cp_notify_handler: Status: success for the originate opcode for call 0x00
<dbg> bt_tbs_client.notify_handler: Index 0
<dbg> bt_tbs_client.current_calls_notify_handler: Call 0x01 is in the alerting state with URI tel:123
<call answered by peer device, and status notified by TBS server>
<dbg> bt_tbs_client.notify_handler: Index 0
<dbg> bt_tbs_client.current_calls_notify_handler: Call 0x01 is in the active state with URI tel:123
```

通过 GTBS 发起通话：

```text
uart:~$ tbs_client originate 0 tel:123
<dbg> bt_tbs_client.notify_handler: Index 0
<dbg> bt_tbs_client.current_calls_notify_handler: Call 0x01 is in the dialing state with URI tel:123
<dbg> bt_tbs_client.call_cp_notify_handler: Status: success for the originate opcode for call 0x00
<dbg> bt_tbs_client.notify_handler: Index 0
<dbg> bt_tbs_client.current_calls_notify_handler: Call 0x01 is in the alerting state with URI tel:123
<call answered by peer device, and status notified by TBS server>
<dbg> bt_tbs_client.notify_handler: Index 0
<dbg> bt_tbs_client.current_calls_notify_handler: Call 0x01 is in the active state with URI tel:123
```

发起通话前，必须设置呼出方标识（outgoing caller ID）。

接听来自对端设备的来电：

```text
<dbg> bt_tbs_client.incoming_uri_notify_handler: tel:123
<dbg> bt_tbs_client.in_call_notify_handler: tel:456
<dbg> bt_tbs_client.friendly_name_notify_handler: Peter
<dbg> bt_tbs_client.current_calls_notify_handler: Call 0x05 is in the incoming state with URI tel:456
uart:~$ tbs_client accept 0 5
<dbg> bt_tbs_client.call_cp_callback_handler: Status: success for the accept opcode for call 0x05
<dbg> bt_tbs_client.current_calls_notify_handler: Call 0x05 is in the active state with URI tel
```

终止通话：

```text
uart:~$ tbs_client terminate 0 5
<dbg> bt_tbs_client.termination_reason_notify_handler: ID 0x05, reason 0x06
<dbg> bt_tbs_client.call_cp_notify_handler: Status: success for the terminate opcode for call 0x05
<dbg> bt_tbs_client.current_calls_notify_handler:
```

<a id="telephone-bearer-service-tbs"></a>

## 62.2 电话承载服务（Telephone Bearer Service，TBS）

TBS 通常位于能够发起通话的设备，例如智能手机和 PC，也包括通过 Skype 等应用发起的通话。

要以交互方式使用 TBS 服务端，必须启用 [`CONFIG_BT_TBS_LOG_LEVEL_DBG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_TBS_LOG_LEVEL_DBG)。

<a id="using-the-telephone-bearer-service"></a>

### 62.2.1 使用电话承载服务（Using the telephone bearer service）

TBS 可以由本地控制，也可以在通话中由远端设备控制。例如远端设备可以向运行 TBS 服务端的设备发起通话，TBS 服务端也可以在没有 TBS_CLIENT 客户端的情况下向远端设备发起通话。TBS 实现能够完全控制任何通话。对于允许指定 `<instance_index>` 的命令，省略索引时默认使用 GTBS 承载。

```text
tbs --help
tbs - Bluetooth TBS shell commands
Subcommands:
   init                        :Initialize TBS
   authorize                   :Authorize the current connection
   accept                      :Accept call <call_index>
   terminate                   :Terminate call <call_index>
   hold                        :Hold call <call_index>
   retrieve                    :Retrieve call <call_index>
   originate                   :Originate call [<instance_index>] <uri>
   join                        :Join calls <id> <id> [<id> [<id> [...]]]
   incoming                    :Simulate incoming remote call [<{instance_index,
                                 gtbs}>] <local_uri> <remote_uri>
                                 <remote_friendly_name>
   remote_answer               :Simulate remote answer outgoing call <call_index>
   remote_retrieve             :Simulate remote retrieve <call_index>
   remote_terminate            :Simulate remote terminate <call_index>
   remote_hold                 :Simulate remote hold <call_index>
   set_bearer_provider_name    :Set the bearer provider name [<{instance_index,
                                 gtbs}>] <name>
   set_bearer_technology       :Set the bearer technology [<{instance_index,
                                 gtbs}>] <technology>
   set_bearer_signal_strength  :Set the bearer signal strength [<{instance_index,
                                 gtbs}>] <strength>
   set_status_flags            :Set the bearer feature and status value
                                 [<{instance_index, gtbs}>] <feature_and_status>
   set_uri_scheme              :Set the URI prefix list <bearer_idx> <uri1[,uri2[,uri3[,...]]]>
   print_calls                 :Output all calls in the debug log
```

<a id="id1"></a>

### 62.2.2 使用示例（Example Usage）

<a id="id2"></a>

#### 62.2.2.1 准备（Setup）

```text
uart:~$ bt init
uart:~$ bt connect P:xx:xx:xx:xx:xx:xx
```

<a id="id3"></a>

#### 62.2.2.2 已连接时（When connected）

应答客户端发起的、面向对端设备的通话：

```text
<dbg> bt_tbs.write_call_cp: Index 0: Processing the originate opcode
<dbg> bt_tbs.originate_call: New call with call index 1
<dbg> bt_tbs.write_call_cp: Index 0: Processed the originate opcode with status success for call index 1
uart:~$ tbs remote_answer 1
TBS succeeded for call_id: 1
```

来自对端设备的来电，由客户端接听：

```text
uart:~$ tbs incoming 0 tel:123 tel:456 Peter
TBS succeeded for call_id: 4
<dbg> bt_tbs.bt_tbs_remote_incoming: New call with call index 4
<dbg> bt_tbs.write_call_cp: Index 0: Processed the accept opcode with status success for call index 4
```

对应官方文档源码：[doc/services/connectivity/bluetooth/shell/audio/tbs.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/doc/services/connectivity/bluetooth/shell/audio/tbs.rst)。

> 译注——源码跟踪：本仓库[对应源码](../../../doc/services/connectivity/bluetooth/shell/audio/tbs.rst)可用于对照，版本可能与网页不同。本批仅翻译和核对文档，未构建固件或连接音频设备。

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：公共广播配置文件PBP_Shell](P061_公共广播配置文件PBP_Shell.md) · [本模块主线目录](../reading/bluetooth.md) · [全部主线](../reading/README.md) · [下一篇：电话与媒体音频配置文件TMAP_Shell](P063_电话与媒体音频配置文件TMAP_Shell.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章](P061_公共广播配置文件PBP_Shell.md) · [返回大纲](大纲.md) · [下一章](P063_电话与媒体音频配置文件TMAP_Shell.md)

</details>

<!-- reading-navigation:end -->
