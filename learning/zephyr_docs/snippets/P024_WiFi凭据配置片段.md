---
id: learning.zephyr-docs.snippets.page-24
title: WiFi凭据配置片段
kind: reference
status: maintained
domains: [zephyr, snippets, documentation]
source_url: https://docs.zephyrproject.org/latest/snippets/wifi/wifi-credentials/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="wi-fi-credentials-snippet-wifi-credentials"></a>
<a id="snippet-wifi-credentials"></a>

# 第24章\_WiFi凭据配置片段

原文：[官方页面](https://docs.zephyrproject.org/latest/snippets/wifi/wifi-credentials/README.html)。读取日期：2026-10-14；保存的latest页面及HTML摘要见[来源记录](../SOURCES.md)。

原构建格式：

```sh
west build  -S wifi-credentials [...]
```

也可以与[Wi-Fi企业认证片段（wifi-enterprise）](P025_WiFi企业认证配置片段.md#snippet-wifi-enterprise)一起使用：

```sh
west build  -S "wifi-enterprise,wifi-credentials" [...]
```

<a id="overview"></a>

## 24.1 概述（Overview）

本片段启用Wi-Fi凭据（Credentials）支持。

<a id="requirements"></a>

## 24.2 要求（Requirements）

硬件须支持：

- [`CONFIG_WIFI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI)。
- [`CONFIG_WIFI_USE_NATIVE_NETWORKING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_USE_NATIVE_NETWORKING)。
- [`CONFIG_WIFI_NM_WPA_SUPPLICANT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NM_WPA_SUPPLICANT)。
- [`CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_ENTERPRISE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_ENTERPRISE)。

> 译注——组合语法：原例在一个`-S`参数中以逗号连接片段名。当前west收集重复的`-S`选项并用分号传给CMake；CMake另支持空格分隔，没有把逗号转成列表分隔符。对应的组合选项应写作`-S wifi-enterprise -S wifi-credentials`，其余板型和应用参数照常提供。原命令仍保留以便对照。

> 译注——持久化：当前官方配置启用Wi-Fi凭据、Settings及Zephyr内存存储（Zephyr Memory Storage，ZMS）后端，并启用Flash、页布局和Flash Map。选择片段不等于已经提供网络凭据；所需存储设备和分区仍须与目标配置匹配。


> 译注——片段源码：[snippet.yml](../../../snippets/wifi/wifi-credentials/snippet.yml)、[wifi-credentials.conf](../../../snippets/wifi/wifi-credentials/wifi-credentials.conf)。片段定义中的名称为`wifi-credentials`；本地参照版本可能与所保存的官方main版本不同。

> 译注——构建占位符：原文`[...]`表示由读者补充的板目标、应用路径等构建参数，实际执行时不能保留方括号省略号。构建位置与片段搜索方法见[使用配置片段](P002_使用配置片段.md)。本文仅翻译和核对，没有执行这些命令。

对应官方文档源码：[snippets/wifi/wifi-credentials/README.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/snippets/wifi/wifi-credentials/README.rst)。

> 译注——源码跟踪：本仓库的[对应源码](../../../snippets/wifi/wifi-credentials/README.rst)可用于对照，版本可能与网页不同。源码跟踪和实现依据不绑定作者机器目录；项目环境与实验路线另见[项目实验补充](../../zephyr_project_notes/README.md)。


[上一章](P023_WiFi配置片段目录.md) · [返回大纲](大纲.md) · [下一章](P025_WiFi企业认证配置片段.md)
