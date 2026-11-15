---
id: learning.zephyr-docs.bluetooth.page-37
title: A2DP_Shell
kind: reference
status: maintained
domains: [zephyr, bluetooth, documentation]
source_url: https://docs.zephyrproject.org/latest/services/connectivity/bluetooth/shell/classic/a2dp.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="bluetooth-a2dp-shell"></a>

# 第37章\_A2DP\_Shell

原文：[官方页面](https://docs.zephyrproject.org/latest/services/connectivity/bluetooth/shell/classic/a2dp.html)。读取日期：2026-10-14；保存的 latest 页面及 HTML 摘要见[来源记录](../SOURCES.md)。

> 译注——使用前提：以下命令在启用了对应蓝牙功能的目标固件Zephyr Shell中执行，初始化与接入方式见[蓝牙Shell](P007_蓝牙Shell.md)。代码中的 `uart:~$` 是提示符，其后输出是原文预期结果；输入命令时不复制提示符和日志。若命令不可用或初始化失败，应先检查目标配置、控制器能力及当前版本帮助，再继续连接或传输步骤。本批仅翻译与核对文档，未连接设备或执行这些命令。

> 译注——术语：ACL 指异步面向连接链路（Asynchronous Connection-oriented Link）；SBC 指低复杂度子带编解码器（Low Complexity Subband Codec）。本页 `sbc` 是命令参数，保持原样。

`a2dp` 命令开放高级音频分发配置文件（Advanced Audio Distribution Profile，A2DP）的部分 API 功能。

以下示例假定已经连接了两台设备。

<a id="a2dp-connection"></a>
<a id="a2dp-conn-disconn"></a>

## 37.1 A2DP 连接（A2DP Connection）

建立 A2DP 连接的流程如下：

双方使用 `a2dp register_cb` 注册 A2DP 回调（callback）。

任一方使用 `a2dp connect` 建立 A2DP 连接，这会创建音视频分发传输协议（Audio/Video Distribution Transport Protocol，AVDTP）的信令通道（Signaling channel）。

任一方都可以使用 `a2dp get_conn` 获取 ACL 连接。

任一方都可以使用 `a2dp disconnect` 断开 A2DP 连接。

**设备 A：发起方（Device A (initiator)）**

<a id="tab-0-RGV2aWNlIEEgKGluaXRpYXRvcik="></a>
<a id="panel-0-RGV2aWNlIEEgKGluaXRpYXRvcik="></a>

```text
uart:~$ a2dp register_cb
success
uart:~$ a2dp connect
Bonded with XX:XX:XX:XX:XX:XX
Security changed: XX:XX:XX:XX:XX:XX level 2
a2dp connected
uart:~$ a2dp get_conn
a2dp conn is: 0xXXXXXXXX
uart:~$ a2dp disconnect
a2dp disconnected
```

**设备 B：接受方（Device B (acceptor)）**

<a id="tab-0-RGV2aWNlIEIgKGFjY2VwdG9yKQ=="></a>
<a id="panel-0-RGV2aWNlIEIgKGFjY2VwdG9yKQ=="></a>

```text
uart:~$ a2dp register_cb
success
<input `a2dp connect` in initiator side>
Connected: XX:XX:XX:XX:XX:XX
Bonded with XX:XX:XX:XX:XX:XX
Security changed: XX:XX:XX:XX:XX:XX level 2
a2dp connected
<input `a2dp disconnect` in initiator side>
a2dp disconnected
```

<a id="basic-a2dp-operations"></a>
<a id="a2dp-basic-operations"></a>

## 37.2 A2DP 基本操作（Basic A2DP Operations）

A2DP 基本操作流程如下：

发送端（Source）和接收端（Sink）分别使用 `a2dp register_ep source sbc` 和 `a2dp register_ep sink sbc` 注册流端点（stream endpoint）。

按照 [A2DP 连接](#a2dp-conn-disconn)一节建立 A2DP 连接。

发起方使用 `a2dp discover_peer_eps 0x0104` 发现远端设备的流端点。

发现远端端点后，发起方使用 `a2dp configure` 配置并创建流（stream）。

发起方使用 `a2dp establish` 建立流。

接收端使用 `a2dp send_delay_report` 发送延迟报告（delay report）。

发起方使用 `a2dp start` 启动媒体传输。

发送端使用 `a2dp send_media` 发送一个测试数据包，测试媒体发送功能。

发起方使用 `a2dp suspend` 暂停媒体传输。

发起方使用 `a2dp release` 释放媒体流。

**注意（Note）**

在下方日志中，发起方承担 A2DP 发送端角色，接受方承担 A2DP 接收端角色。只有接收端能发送延迟报告；只有发送端能发送媒体数据。

**设备 A：发起方（Device A (initiator)）**

<a id="tab-1-RGV2aWNlIEEgKGluaXRpYXRvcik="></a>
<a id="panel-1-RGV2aWNlIEEgKGluaXRpYXRvcik="></a>

```text
uart:~$ a2dp register_ep source sbc
SBC source endpoint is registered
uart:~$ a2dp discover_peer_eps 0x0104
endpoint id: 1, (sink), (idle):
  codec type: SBC
  sample frequency:
          44100
          48000
  channel mode:
          Mono
          Stereo
          Joint-Stereo
  Block Length:
          16
  Subbands:
          8
  Allocation Method:
          Loudness
  Bitpool Range: 18 - 35
uart:~$ a2dp configure
success to configure
stream configured
uart:~$ a2dp establish
success to establish
stream established
<input `a2dp send_delay_report` in sink side>
receive delay report and accept
received delay report: 1 1/10ms
uart:~$ a2dp start
success to start
stream started
uart:~$ a2dp send_media
frames num: 1, data length: 160
data: 1, 2, 3, 4, 5, 6 ......
uart:~$ a2dp suspend
success to suspend
stream suspended
uart:~$ a2dp release
success to release
stream released
```

**设备 B：接受方（Device B (acceptor)）**

<a id="tab-1-RGV2aWNlIEIgKGFjY2VwdG9yKQ=="></a>
<a id="panel-1-RGV2aWNlIEIgKGFjY2VwdG9yKQ=="></a>

```text
uart:~$ a2dp register_ep sink sbc
SBC sink endpoint is registered
<input `a2dp configure` in initiator side>
receive requesting config and accept
sample rate 44100Hz
stream configured
<input `a2dp establish` in initiator side>
receive requesting establishment and accept
stream established
uart:~$ a2dp send_delay_report
success to send report delay
<input `a2dp start` in initiator side>
receive requesting start and accept
stream started
<input `a2dp send_media` in source side>
received, num of frames: 1, data length: 160
data: 1, 2, 3, 4, 5, 6 ......
<input `a2dp suspend` in initiator side>
receive requesting suspend and accept
stream suspended
<input `a2dp release` in initiator side>
receive requesting release and accept
stream released
```

> 译注——结果边界：原日志分别展示发起方与接受方的操作，`send_media` 仅发送一个测试包；收到测试数据不等于已经验证连续音频播放。两端地址和对象指针是原示例运行值。

<a id="abort-operation"></a>

## 37.3 中止操作（Abort Operation）

中止操作流程如下：

按照 [A2DP 基本操作](#a2dp-basic-operations)一节建立 A2DP 流。

发起方使用 `a2dp abort` 中止流。

**设备 A：发起方（Device A (initiator)）**

<a id="tab-2-RGV2aWNlIEEgKGluaXRpYXRvcik="></a>
<a id="panel-2-RGV2aWNlIEEgKGluaXRpYXRvcik="></a>

```text
uart:~$ a2dp abort
success to abort
stream released
```

**设备 B：接受方（Device B (acceptor)）**

<a id="tab-2-RGV2aWNlIEIgKGFjY2VwdG9yKQ=="></a>
<a id="panel-2-RGV2aWNlIEIgKGFjY2VwdG9yKQ=="></a>

```text
<input `a2dp abort` in initiator side>
receive requesting abort and accept
stream released
```

<a id="get-configuration-and-reconfigure-operation"></a>

## 37.4 获取配置与重新配置（Get Configuration and Reconfigure Operation）

获取配置和重新配置的流程如下：

按照 [A2DP 基本操作](#a2dp-basic-operations)一节建立 A2DP 流。

发起方使用 `a2dp get_config` 获取配置。

发起方使用 `a2dp reconfigure` 重新配置流。

**设备 A：发起方（Device A (initiator)）**

<a id="tab-3-RGV2aWNlIEEgKGluaXRpYXRvcik="></a>
<a id="panel-3-RGV2aWNlIEEgKGluaXRpYXRvcik="></a>

```text
uart:~$ a2dp get_config
get config result: 0
sample rate 44100Hz
uart:~$ a2dp reconfigure
success to configure
stream configured
```

**设备 B：接受方（Device B (acceptor)）**

<a id="tab-3-RGV2aWNlIEIgKGFjY2VwdG9yKQ=="></a>
<a id="panel-3-RGV2aWNlIEIgKGFjY2VwdG9yKQ=="></a>

```text
<input `a2dp get_config` in initiator side>
receive get config request and accept
<input `a2dp reconfigure` in initiator side>
receive requesting reconfig and accept
sample rate 44100Hz
stream configured
```


对应官方文档源码：[doc/services/connectivity/bluetooth/shell/classic/a2dp.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/doc/services/connectivity/bluetooth/shell/classic/a2dp.rst)。

> 译注——源码跟踪：本仓库的[对应源码](../../../doc/services/connectivity/bluetooth/shell/classic/a2dp.rst)可用于跟踪，版本可能与网页不同；本批仅翻译和核对文档，没有执行固件构建、模拟运行或烧录。

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：服务发现协议SDP](P036_服务发现协议SDP.md) · [本模块主线目录](../reading/bluetooth.md) · [全部主线](../reading/README.md) · [下一篇：AVRCP_Shell](P038_AVRCP_Shell.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章](P036_服务发现协议SDP.md) · [返回大纲](大纲.md) · [下一章](P038_AVRCP_Shell.md)

</details>

<!-- reading-navigation:end -->
