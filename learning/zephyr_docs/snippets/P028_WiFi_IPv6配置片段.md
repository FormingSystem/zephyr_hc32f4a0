---
id: learning.zephyr-docs.snippets.page-28
title: WiFi_IPv6配置片段
kind: reference
status: maintained
domains: [zephyr, snippets, documentation]
source_url: https://docs.zephyrproject.org/latest/snippets/wifi/wifi-ipv6/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="wi-fi-ipv6-snippet-wifi-ipv6"></a>
<a id="snippet-wifi-ipv6"></a>

# 第28章\_WiFi\_IPv6配置片段

原文：[官方页面](https://docs.zephyrproject.org/latest/snippets/wifi/wifi-ipv6/README.html)。读取日期：2026-10-14；保存的latest页面及HTML摘要见[来源记录](../SOURCES.md)。

原构建格式：

```sh
west build -S wifi-ipv6 [...]
```

<a id="overview"></a>

## 28.1 概述（Overview）

本片段启用IPv6的Wi-Fi支持。IPv4与IPv6分别是互联网协议（Internet Protocol）的第4版和第6版。

使用Wi-Fi Shell连接Wi-Fi网络：

```sh
wifi connect -s <SSID> -k <key_management> -p <passphrase>
```

<a id="requirements"></a>

## 28.2 要求（Requirements）

硬件须支持：

- [`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)。
- [`CONFIG_WIFI_USE_NATIVE_NETWORKING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_USE_NATIVE_NETWORKING)。

> 译注——命令位置：`west build`在主机构建环境中执行；`wifi connect`在运行固件的Wi-Fi Shell中执行。`<SSID>`为服务集标识（Service Set Identifier），`<key_management>`为密钥管理方式，`<passphrase>`为口令，均需替换为当前网络适用的值；不能原样输入尖括号占位内容。

> 译注——协议配置：当前片段启用IPv6及DHCPv6，关闭IPv4和IPv4配置需求，并启用DNS解析器、连接管理器及Wi-Fi Shell。实际IPv6地址、路由与DNS可用性仍取决于网络环境。


> 译注——片段源码：[snippet.yml](../../../snippets/wifi/wifi-ipv6/snippet.yml)、[wifi-ipv6.conf](../../../snippets/wifi/wifi-ipv6/wifi-ipv6.conf)。片段定义中的名称为`wifi-ipv6`；本地参照版本可能与所保存的官方main版本不同。

> 译注——构建占位符：原文`[...]`表示由读者补充的板目标、应用路径等构建参数，实际执行时不能保留方括号省略号。构建位置与片段搜索方法见[使用配置片段](P002_使用配置片段.md)。本文仅翻译和核对，没有执行这些命令。

对应官方文档源码：[snippets/wifi/wifi-ipv6/README.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/snippets/wifi/wifi-ipv6/README.rst)。

> 译注——源码跟踪：本仓库的[对应源码](../../../snippets/wifi/wifi-ipv6/README.rst)可用于对照，版本可能与网页不同。源码跟踪和实现依据不绑定作者机器目录；项目环境与实验路线另见[项目实验补充](../../zephyr_project_notes/README.md)。


[上一章](P027_WiFi_IPv4配置片段.md) · [返回大纲](大纲.md) · [下一章](P029_Espressif配置片段目录.md)
