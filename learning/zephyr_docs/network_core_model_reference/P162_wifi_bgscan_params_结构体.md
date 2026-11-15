---
id: learning.zephyr-docs.network-core-model-reference.page-162
title: wifi_bgscan_params_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structwifi__bgscan__params.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第162章\_wifi\_bgscan\_params\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structwifi__bgscan__params.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

Wi-Fi后台扫描参数（Background Scan Parameters）。

```c
#include <zephyr/net/wifi_mgmt.h>
```

<a id="details"></a>

Wi-Fi后台扫描参数（Background Scan Parameters）。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 162.1\_数据成员（Data Fields）

<a id="r_a1a6cc39e71f94c9fae639a886f5c3030"></a>

```c
enum wifi_bgscan_type type
```

相关声明：[wifi_bgscan_type](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gaacc27e95277622f56ef35e129aaac4d0)、[type](#a1a6cc39e71f94c9fae639a886f5c3030)。

后台扫描类型（Background scanning type）。

<a id="r_ae1e3e6bf419e7f810e5ba7b085be7c12"></a>

```c
uint16_t short_interval
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[short_interval](#ae1e3e6bf419e7f810e5ba7b085be7c12)。

短扫描间隔（Short scan interval），单位为秒。

<a id="r_a5ec94a609155573cedfe7772b940d183"></a>

```c
uint16_t long_interval
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[long_interval](#a5ec94a609155573cedfe7772b940d183)。

长扫描间隔（Long scan interval），单位为秒。

<a id="r_ab73566a1db6e31c15c575cab21f24bfb"></a>

```c
int8_t rssi_threshold
```

相关声明：[int8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#accbd6432732c88ad6adc5365800433b6)、[rssi_threshold](#ab73566a1db6e31c15c575cab21f24bfb)。

信号强度阈值（Signal strength threshold），单位为 dBm。

<a id="r_a8d12ab3d7d589d06c79874ea374ae327"></a>

```c
uint16_t btm_queries
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[btm_queries](#a8d12ab3d7d589d06c79874ea374ae327)。

基本服务集转换管理查询（BSS Transition Management，BTM queries）次数。

## 162.2\_详细说明（Detailed Documentation）

<a id="a8d12ab3d7d589d06c79874ea374ae327"></a>

### `btm_queries`

```c
uint16_t wifi_bgscan_params::btm_queries
```

基本服务集转换管理查询（BSS Transition Management，BTM queries）次数。

<a id="a5ec94a609155573cedfe7772b940d183"></a>

### `long_interval`

```c
uint16_t wifi_bgscan_params::long_interval
```

长扫描间隔（Long scan interval），单位为秒。

<a id="ab73566a1db6e31c15c575cab21f24bfb"></a>

### `rssi_threshold`

```c
int8_t wifi_bgscan_params::rssi_threshold
```

信号强度阈值（Signal strength threshold），单位为 dBm。

<a id="ae1e3e6bf419e7f810e5ba7b085be7c12"></a>

### `short_interval`

```c
uint16_t wifi_bgscan_params::short_interval
```

短扫描间隔（Short scan interval），单位为秒。

<a id="a1a6cc39e71f94c9fae639a886f5c3030"></a>

### `type`

```c
enum wifi_bgscan_type wifi_bgscan_params::type
```

后台扫描类型（Background scanning type）。

本数据类型文档由以下文件生成：

- `zephyr/net/wifi_mgmt.h`

## 162.3\_原页交叉引用（Cross References）

- [zephyr/net/wifi_mgmt.h](https://docs.zephyrproject.org/latest/doxygen/html/wifi__mgmt_8h_source.html)
- [wifi_bgscan_type](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gaacc27e95277622f56ef35e129aaac4d0)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [int8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#accbd6432732c88ad6adc5365800433b6)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P161_wifi_band_channel_结构体.md) · [返回大纲](大纲.md) · [下一章](P163_wifi_btwt_params_结构体.md)
