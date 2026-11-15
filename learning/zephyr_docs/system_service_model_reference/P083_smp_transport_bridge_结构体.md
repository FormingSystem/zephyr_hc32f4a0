---
id: learning.zephyr-docs.system-service-model-reference.page-83
title: smp_transport_bridge_结构体
kind: reference
status: maintained
domains: [zephyr, services, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structsmp__transport__bridge.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第83章\_smp\_transport\_bridge\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structsmp__transport__bridge.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

桥接传输（Bridged Transport）的上下文。

```c
#include <zephyr/mgmt/mcumgr/transport/smp.h>
```

<a id="details"></a>

桥接传输（Bridged Transport）的上下文。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 83.1\_数据成员（Data Fields）

<a id="r_a8999f556cdde306d93e94c501e190317"></a>

```c
uint8_t status
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[status](#a8999f556cdde306d93e94c501e190317)。

桥接状态（bridge status）：0 表示未桥接、空闲；1 表示已桥接、正在使用。

<a id="r_ae2f098cd30fa5793fb8725845a04931e"></a>

```c
struct smp_transport * incoming_transport
```

相关声明：[smp_transport](P081_smp_transport_结构体.md)、[incoming_transport](#ae2f098cd30fa5793fb8725845a04931e)。

入站传输：设备上的 MCUmgr 以服务器模式运行，接受读取和写入请求。

<a id="r_aab41981338e090d13ea6581ed9101914"></a>

```c
struct smp_transport * outgoing_transport
```

相关声明：[smp_transport](P081_smp_transport_结构体.md)、[outgoing_transport](#aab41981338e090d13ea6581ed9101914)。

出站传输：设备上的 MCUmgr 以客户端模式运行，接受读取和写入响应。

## 83.2\_详细说明（Detailed Documentation）

<a id="ae2f098cd30fa5793fb8725845a04931e"></a>

### `incoming_transport`

```c
struct smp_transport* smp_transport_bridge::incoming_transport
```

入站传输：设备上的 MCUmgr 以服务器模式运行，接受读取和写入请求。

<a id="aab41981338e090d13ea6581ed9101914"></a>

### `outgoing_transport`

```c
struct smp_transport* smp_transport_bridge::outgoing_transport
```

出站传输：设备上的 MCUmgr 以客户端模式运行，接受读取和写入响应。

<a id="a8999f556cdde306d93e94c501e190317"></a>

### `status`

```c
uint8_t smp_transport_bridge::status
```

桥接状态（bridge status）：0 表示未桥接、空闲；1 表示已桥接、正在使用。

本数据类型文档由以下文件生成：

- `zephyr/mgmt/mcumgr/transport/smp.h`

## 83.3\_原页交叉引用（Cross References）

- [zephyr/mgmt/mcumgr/transport/smp.h](https://docs.zephyrproject.org/latest/doxygen/html/mgmt_2mcumgr_2transport_2smp_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [smp_transport](P081_smp_transport_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P082_smp_transport_api_t_结构体.md) · [返回大纲](大纲.md) · [下一章](P084_stat_mgmt_entry_结构体.md)
