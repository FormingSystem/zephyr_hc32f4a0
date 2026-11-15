---
id: learning.zephyr-docs.snippets.page-25
title: WiFi企业认证配置片段
kind: reference
status: maintained
domains: [zephyr, snippets, documentation]
source_url: https://docs.zephyrproject.org/latest/snippets/wifi/wifi-enterprise/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="wi-fi-enterprise-snippet-wifi-enterprise"></a>
<a id="snippet-wifi-enterprise"></a>

# 第25章\_WiFi企业认证配置片段

原文：[官方页面](https://docs.zephyrproject.org/latest/snippets/wifi/wifi-enterprise/README.html)。读取日期：2026-10-14；保存的latest页面及HTML摘要见[来源记录](../SOURCES.md)。

原构建格式：

```sh
west build  -S wifi-enterprise [...]
```

也可以与[Wi-Fi IPv4片段（wifi-ipv4）](P027_WiFi_IPv4配置片段.md#snippet-wifi-ipv4)一起使用：

```sh
west build  -S "wifi-enterprise,wifi-ipv4" [...]
```

<a id="overview"></a>

## 25.1 概述（Overview）

本片段启用企业级Wi-Fi（Enterprise Wi-Fi）支持。

更多用法见[Wi-Fi管理（Wi-Fi Management）](../networking/P163_WiFi管理接口.md#wifi-mgmt)。

<a id="requirements"></a>

## 25.2 要求（Requirements）

硬件须支持：

- [`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)。
- [`CONFIG_WIFI_USE_NATIVE_NETWORKING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_USE_NATIVE_NETWORKING)。
- [`CONFIG_WIFI_NM_WPA_SUPPLICANT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NM_WPA_SUPPLICANT)。
- [`CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_ENTERPRISE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_ENTERPRISE)。

> 译注——组合与凭据：原逗号组合命令保留用于核对。根据当前west和CMake的列表处理，组合选项应写作`-S wifi-enterprise -S wifi-ipv4`，而不是把逗号包含在单个片段名内。当前企业片段启用企业认证密码支持、可变大小网络缓冲区、Mbed TLS专用堆，以及传输层安全（Transport Layer Security，TLS）凭据和Shell支持；具体证书、身份与网络参数仍须按Wi-Fi管理说明提供。它不会自动生成有效的企业网络认证材料。


> 译注——片段源码：[snippet.yml](../../../snippets/wifi/wifi-enterprise/snippet.yml)、[wifi-enterprise.conf](../../../snippets/wifi/wifi-enterprise/wifi-enterprise.conf)。片段定义中的名称为`wifi-enterprise`；本地参照版本可能与所保存的官方main版本不同。

> 译注——构建占位符：原文`[...]`表示由读者补充的板目标、应用路径等构建参数，实际执行时不能保留方括号省略号。构建位置与片段搜索方法见[使用配置片段](P002_使用配置片段.md)。本文仅翻译和核对，没有执行这些命令。

对应官方文档源码：[snippets/wifi/wifi-enterprise/README.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/snippets/wifi/wifi-enterprise/README.rst)。

> 译注——源码跟踪：本仓库的[对应源码](../../../snippets/wifi/wifi-enterprise/README.rst)可用于对照，版本可能与网页不同。源码跟踪和实现依据不绑定作者机器目录；项目环境与实验路线另见[项目实验补充](../../zephyr_project_notes/README.md)。


[上一章](P024_WiFi凭据配置片段.md) · [返回大纲](大纲.md) · [下一章](P026_WiFi双栈配置片段.md)
