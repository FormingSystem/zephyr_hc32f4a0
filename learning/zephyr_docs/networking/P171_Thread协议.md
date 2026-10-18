---
id: learning.zephyr-docs.networking.page-171
title: Thread协议
kind: reference
status: maintained
domains: [zephyr, networking, development]
source_url: https://docs.zephyrproject.org/latest/services/connectivity/networking/api/thread.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第171章\_Thread协议

原文：[官方页面](https://docs.zephyrproject.org/latest/services/connectivity/networking/api/thread.html)。读取日期：2026-10-14；保存的 latest 页面及 HTML 摘要见[来源记录](../SOURCES.md)。

## 1. 概述（Overview）

Thread 是一种低功耗网状网络（Low-Power Mesh Networking）技术，专为家庭自动化应用设计。它以 IPv6 为基础，在 IEEE 802.15.4 上使用低功耗无线个域网 IPv6（6LoWPAN）。借助 IP 连通性，可以通过 Thread 边界路由器（Thread Border Router）把 Thread 网状网络连接到互联网。

原文说明，Thread 规范提供较高等级的网络安全：只有经过认证的设备才能加入网络，网状网络内部通信经过加密。协议详情见[Thread Group 官方网站](https://www.threadgroup.org)。

Zephyr 集成了名为 OpenThread 的开源 Thread 协议实现，其文档位于[OpenThread 官方网站](https://openthread.io/)。

## 2. 互联网连接（Internet Connectivity）

将 Thread 网状网络连接到互联网需要 Thread Border Router。OpenThread 社区提供开源边界路由器实现，搭建步骤见[OpenThread 边界路由器指南](https://openthread.io/guides/border-router)。

## 3. 示例用法（Sample Usage）

Zephyr 的 Echo 回显服务器和客户端提供现成 OpenThread 配置，可用来试验该协议。构建时加入 `overlay-ot.conf` 覆盖配置文件，以启用 OpenThread 支持。详情见[高级回显服务器](P047_高级回显服务器示例.md#sockets-echo-server)和[高级回显客户端](P048_高级回显客户端示例.md#sockets-echo-client)。

Zephyr 还提供[OpenThread 命令行示例](P176_OpenThread命令行示例.md#openthread-shell)，用于测试、调试 Thread 及底层 IEEE 802.15.4 驱动。

## 4. Thread 相关 API

### 4.1 OpenThread 驱动 API

OpenThread L2 在内部使用不绑定上层协议的 Zephyr IEEE 802.15.4 驱动 API。需要为 OpenThread 提供支持的驱动开发者应关注这一接口。

该接口属于[IEEE 802.15.4 驱动子系统](P170_IEEE802154无线网络.md#ieee802154-driver-api)，在该处说明。

### 4.2 OpenThread L2 适配层 API

OpenThread 二层平台适配层（L2 Platform Adaptation Layer）把外部 OpenThread 协议栈与 Zephyr IEEE 802.15.4 驱动 API 接合起来，主要供 OpenThread L2 子系统贡献者使用。

### 4.3 OpenThread 平台 API

OpenThread 平台 API（Platform API）由 OpenThread 协议栈定义，在 Zephyr 中作为 OpenThread 模块实现。应用既可直接使用该实现，也可通过 L2 适配层访问。

#### 4.3.1 通过 L2 适配层使用

把 [`CONFIG_NET_L2_OPENTHREAD`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_L2_OPENTHREAD) 和 [`CONFIG_NETWORKING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NETWORKING) 都设置为 `y`。适配层使用 `modules/openthread/platform/radio.c` 中的 OpenThread 无线电 API 实现，并负责初始化和管理 OpenThread 协议栈。

#### 4.3.2 直接使用平台 API

也可以绕过 L2 适配层，直接使用 OpenThread 平台 API。但这种方式要求提供与所用无线电驱动兼容的 OpenThread 无线电 API 实现。

把 [`CONFIG_OPENTHREAD`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_OPENTHREAD) 设置为 `y`，不启用 [`CONFIG_NET_L2_OPENTHREAD`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_L2_OPENTHREAD)。原文要求使用自己的无线电驱动实现以下[OpenThread 无线电 API](https://openthread.io/reference/group/radio-config)函数，完整清单如下：

| 函数 | 功能提示（译注，仅解释名称） |
| --- | --- |
| `otPlatRadioGetPromiscuous` | 获取混杂模式状态。 |
| `otPlatRadioGetCcaEnergyDetectThreshold` | 获取空闲信道评估（Clear Channel Assessment，CCA）能量检测门限。 |
| `otPlatRadioGetTransmitPower` | 获取发射功率。 |
| `otPlatRadioGetIeeeEui64` | 获取 IEEE 扩展唯一标识符（EUI-64）。 |
| `otPlatRadioSetPromiscuous` | 设置混杂模式。 |
| `otPlatRadioGetCaps` | 获取无线电能力。 |
| `otPlatRadioGetTransmitBuffer` | 获取发送缓冲区。 |
| `otPlatRadioSetPanId` | 设置个域网标识符（PAN ID）。 |
| `otPlatRadioEnable` | 启用无线电。 |
| `otPlatRadioDisable` | 禁用无线电。 |
| `otPlatRadioReceive` | 进入接收状态。 |
| `otPlatRadioGetRssi` | 获取接收信号强度指示（RSSI）。 |
| `otPlatRadioGetReceiveSensitivity` | 获取接收灵敏度。 |
| `otPlatRadioEnergyScan` | 执行能量扫描。 |
| `otPlatRadioSetExtendedAddress` | 设置扩展地址。 |
| `otPlatRadioSetShortAddress` | 设置短地址。 |
| `otPlatRadioAddSrcMatchExtEntry` | 添加扩展地址源匹配条目。 |
| `otPlatRadioTransmit` | 发送帧。 |
| `otPlatRadioClearSrcMatchShortEntries` | 清除全部短地址源匹配条目。 |
| `otPlatRadioClearSrcMatchExtEntries` | 清除全部扩展地址源匹配条目。 |
| `otPlatRadioEnableSrcMatch` | 启用源地址匹配（Source Address Matching）。 |
| `otPlatRadioAddSrcMatchShortEntry` | 添加短地址源匹配条目。 |
| `otPlatRadioClearSrcMatchShortEntry` | 清除指定短地址源匹配条目。 |
| `otPlatRadioClearSrcMatchExtEntry` | 清除指定扩展地址源匹配条目。 |

另外，还需实现无线电初始化和事件处理函数 `platformRadioInit()`、`platformRadioProcess()`；原文指向[include/zephyr/net/openthread.h](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/net/openthread.h)。

这种接入方式下，可以在应用中调用 `ot_platform_init()` 初始化协议栈，也可以启用 [`CONFIG_OPENTHREAD_SYS_INIT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_OPENTHREAD_SYS_INIT)，在系统启动时自动初始化；优先级通过 [`CONFIG_OPENTHREAD_SYS_INIT_PRIORITY`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_OPENTHREAD_SYS_INIT_PRIORITY) 设置。

> 源码对照：当前 `platformRadioInit()` 和 `platformRadioProcess()` 的直接声明位于官方[platform-zephyr.h](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/openthread/platform/platform-zephyr.h)，由[platform.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/openthread/platform/platform.c)中的 `otSysInit()`、`otSysProcessDrivers()` 调用。原文所指的公开头文件目前主要声明上下文并包含 OpenThread 头文件，不能仅在其中查找这两个平台函数。

> 构建边界：当前[平台 CMakeLists.txt](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/openthread/platform/CMakeLists.txt)还区分 L2 的 `radio.c`、[`CONFIG_HDLC_RCP_IF`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HDLC_RCP_IF) 对应的 Spinel 无线电路径，以及厂商无线电实现。厂商实现文件名可按应用目录或模块的 `vendor` 目录解析相对路径；因此，直接使用平台 API 并不意味着必须在所有平台上重新手写全部已有驱动。仍需根据实际构建选择提供匹配实现，上表是原文要求的函数清单，不是所有功能组合的完整 ABI 保证。

## 5. 完整参考与相关示例

完整接口入口：[OpenThread 协议栈 API](https://docs.zephyrproject.org/latest/doxygen/html/group__openthread.html)，该生成参考页另行跟踪翻译状态。

- [OpenThread 协处理器](P175_OpenThread协处理器.md#openthread-coprocessor)：使用协处理器设计构建 Thread 边界路由器。
- [OpenThread CoAP 客户端与服务器](P174_OpenThread的CoAP示例.md#ot-coap)：构建完整 Thread 设备（Full Thread Device，FTD）的 CoAP 服务端和客户端。


<a id="thread-protocol"></a>
<a id="thread-protocol-interface"></a>
<a id="contents"></a>
<a id="id1"></a>
<a id="id2"></a>
<a id="id3"></a>
<a id="id4"></a>
<a id="id5"></a>
<a id="id6"></a>
<a id="id7"></a>
<a id="overview"></a>
<a id="internet-connectivity"></a>
<a id="sample-usage"></a>
<a id="thread-related-apis"></a>
<a id="openthread-driver-api"></a>
<a id="openthread-l2-adaptation-layer-api"></a>
<a id="openthread-platform-api"></a>
<a id="using-the-openthread-l2-adaptation-layer-api"></a>
<a id="using-the-openthread-platform-api-directly"></a>

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：IEEE802154无线网络](P170_IEEE802154无线网络.md) · [本模块主线目录](../reading/networking.md) · [全部主线](../reading/README.md) · [下一篇：MCP服务器](P178_MCP服务器.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章](P170_IEEE802154无线网络.md) · [返回大纲](大纲.md) · [下一章](P172_OpenThread示例目录.md)

</details>

<!-- reading-navigation:end -->
