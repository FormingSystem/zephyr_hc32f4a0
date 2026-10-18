---
id: learning.zephyr-docs.bluetooth.page-57
title: 通话控制配置文件CCP_Shell
kind: reference
status: maintained
domains: [zephyr, bluetooth, documentation]
source_url: https://docs.zephyrproject.org/latest/services/connectivity/bluetooth/shell/audio/ccp.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="bluetooth-call-control-profile-shell"></a>

# 第57章\_蓝牙：通话控制配置文件 Shell（Bluetooth: Call Control Profile Shell）

原文：[官方页面](https://docs.zephyrproject.org/latest/services/connectivity/bluetooth/shell/audio/ccp.html)。快照读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

> 译注——操作上下文：代码块中的命令在启用了相应音频功能的目标固件 Zephyr Shell 中执行，接入与初始化见[蓝牙 Shell](P007_蓝牙Shell.md)。`uart:~$` 是提示符，后续日志是官方预期输出；不要把提示符、日志或 `<address>` 等占位符原样当作主机终端命令运行。各示例代表不同角色和操作分支，按实际连接与初始化状态选择，不连贯粘贴整章。命令缺失、初始化失败或发现未完成时，应先核对固件配置、控制器能力及当前版本帮助，再继续后续操作。

> 译注——版本与验证：原文“当前”“尚未实现”等表述均保留其快照语境。代码块完整保留原始命令、帮助和输出，本文没有执行固件构建、连接音频设备或验证互操作性。

> 译注——术语：CCP 为通话控制配置文件（Call Control Profile）；UCI 为统一呼叫标识符（Uniform Caller Identifier），URI 为统一资源标识符（Uniform Resource Identifier）；GAP 为通用访问配置文件（Generic Access Profile）。

<a id="call-control-server"></a>

## 57.1 通话控制服务端（Call Control Server）

通话控制服务端角色通常位于能发起通话的设备，例如智能手机与 PC，也包括通过 Skype 等应用发起的通话。这类设备通常承担 GAP 中心设备（Central）角色。

<a id="using-the-call-control-server"></a>

### 57.1.1 使用通话控制服务端（Using the Call Control Server）

服务端可以由本地控制，也可以在通话中由远端设备控制。例如远端设备可以向服务端发起通话，服务端也可以在没有客户端参与的情况下向远端设备发起通话。

对于接受可选 `index` 参数的所有命令，省略该参数时默认使用 `0`，对应通用电话承载服务（Generic Telephone Bearer Service，GTBS）承载。

```text
ccp_call_control_server --help
ccp_call_control_server - Bluetooth CCP Call Control Server shell commands
Subcommands:
  init                    : Initialize CCP Call Control Server
  set_bearer_name         : Set bearer name [index] <name>
  get_bearer_name         : Get bearer name [index]
  get_bearer_uci          : Get bearer UCI [index]
  set_bearer_tech         : Set bearer technology [index] <technology>
  get_bearer_tech         : Get bearer technology [index]
  set_bearer_uri_schemes  : Set bearer URI schemes supported list [index] <URI schemes>
                           (e.g. "tel,skype")
  get_bearer_uri_schemes  : Get bearer URI schemes supported list [index]
```

<a id="example-usage"></a>

### 57.1.2 使用示例（Example Usage）

<a id="setup"></a>

#### 57.1.2.1 准备（Setup）

```text
uart:~$ bt init
uart:~$ ccp_call_control_server init
Registered GTBS bearer
Registered bearer[1]
uart:~$ bt connect P:xx:xx:xx:xx:xx:xx
```

<a id="setting-and-getting-the-bearer-name"></a>

#### 57.1.2.2 设置与获取承载名称（Setting and getting the bearer name）

```text
uart:~$ ccp_call_control_server get_bearer_name
Bearer[0] name: Generic TBS
uart:~$ ccp_call_control_server set_bearer_name "New name"
Bearer[0] name: New name
uart:~$ ccp_call_control_server get_bearer_name
Bearer[0] name: New name
uart:~$ ccp_call_control_server get_bearer_name 1
Bearer[1] name: Telephone Bearer #1
uart:~$ ccp_call_control_server set_bearer_name 1 "New TBS name"
Bearer[1] name: New TBS name
uart:~$ ccp_call_control_server get_bearer_name 1
Bearer[1] name: New TBS name
```

<a id="getting-the-bearer-uci"></a>

#### 57.1.2.3 获取承载 UCI（Getting the bearer UCI）

```text
uart:~$ ccp_call_control_server get_bearer_uci
Bearer[0] UCI: un999
uart:~$ ccp_call_control_server get_bearer_uci 1
Bearer[1] UCI: skype
```

<a id="setting-and-getting-the-bearer-technology"></a>

#### 57.1.2.4 设置与获取承载技术类型（Setting and getting the bearer technology）

```text
uart:~$ ccp_call_control_server get_bearer_tech
Bearer[0] technology: 3G (0x01)
uart:~$ ccp_call_control_server set_bearer_tech 0x02
Bearer[0] new technology: 4G (0x02)
```

<a id="setting-and-getting-the-bearer-uri-supported-schemes-list"></a>

#### 57.1.2.5 设置与获取承载支持的 URI 方案列表（Setting and getting the bearer URI supported schemes list）

```text
uart:~$ ccp_call_control_server get_bearer_uri_schemes
Bearer[0] URI schemes supported list: tel,skype
uart:~$ ccp_call_control_server set_bearer_uri_schemes "tel,teamspeak"
Bearer[0] new URI schemes supported list: tel,teamspeak
```

<a id="call-control-client"></a>

## 57.2 通话控制客户端（Call Control Client）

通话控制客户端角色通常位于资源受限的设备，例如耳塞或头戴式耳机。

<a id="using-the-call-control-client"></a>

### 57.2.1 使用通话控制客户端（Using the Call Control Client）

客户端可以控制远端 CCP 服务端设备。例如远端设备收到来电时，可以由客户端接听。

```text
uart:~$ ccp_call_control_client --help
ccp_call_control_client - Bluetooth CCP Call Control Client shell commands
Subcommands:
  discover  : Discover GTBS and TBS on remote device
```

<a id="example-usage-when-connected"></a>

### 57.2.2 已连接时的使用示例（Example Usage when connected）

```text
uart:~$ ccp_call_control_client discover
Discovery completed with GTBS and 1 TBS bearers
```

```text
uart:~$ ccp_call_control_client read_bearer_name
Bearer 0x20046254 name: Generic TBS
uart:~$ ccp_call_control_client read_bearer_name 1
Bearer 0x20046256 name: Telephone Bearer #1
uart:~$ ccp_call_control_client read_bearer_uci
Bearer 0x20046254 UCI: un999
uart:~$ ccp_call_control_client read_bearer_uci 1
Bearer 0x20046256 UCI: skype
```

对应官方文档源码：[doc/services/connectivity/bluetooth/shell/audio/ccp.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/doc/services/connectivity/bluetooth/shell/audio/ccp.rst)。

> 译注——源码跟踪：本仓库[对应源码](../../../doc/services/connectivity/bluetooth/shell/audio/ccp.rst)可用于对照，版本可能与网页不同。本批仅翻译和核对文档，未构建固件或连接音频设备。

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：通用音频配置文件CAP_Shell](P056_通用音频配置文件CAP_Shell.md) · [本模块主线目录](../reading/bluetooth.md) · [全部主线](../reading/README.md) · [下一篇：协调集标识配置文件CSIP_Shell](P058_协调集标识配置文件CSIP_Shell.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章](P056_通用音频配置文件CAP_Shell.md) · [返回大纲](大纲.md) · [下一章](P058_协调集标识配置文件CSIP_Shell.md)

</details>

<!-- reading-navigation:end -->
