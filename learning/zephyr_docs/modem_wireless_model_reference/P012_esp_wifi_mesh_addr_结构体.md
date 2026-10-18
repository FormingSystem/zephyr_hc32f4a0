---
id: learning.zephyr-docs.modem-wireless-model-reference.page-12
title: esp_wifi_mesh_addr_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structesp__wifi__mesh__addr.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第12章\_esp\_wifi\_mesh\_addr\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structesp__wifi__mesh__addr.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

Mesh节点地址（Node Address），即6字节MAC地址。

```c
#include <zephyr/drivers/wifi/esp_wifi/esp_wifi_mesh.h>
```

<a id="details"></a>

Mesh节点地址（Node Address），即6字节MAC地址。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 12.1\_数据成员（Data Fields）

<a id="r_abc17d248b689dd7c2ee2b0ce953fa8ff"></a>

```c
uint8_t addr [6]
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[addr](#abc17d248b689dd7c2ee2b0ce953fa8ff)。

Mesh 节点的 6 字节 MAC 地址。

## 12.2\_详细说明（Detailed Documentation）

<a id="abc17d248b689dd7c2ee2b0ce953fa8ff"></a>

### `addr`

```c
uint8_t esp_wifi_mesh_addr::addr[6]
```

Mesh 节点的 6 字节 MAC 地址。

本数据类型文档由以下文件生成：

- `zephyr/drivers/wifi/esp_wifi/esp_wifi_mesh.h`

## 12.3\_原页交叉引用（Cross References）

- [zephyr/drivers/wifi/esp_wifi/esp_wifi_mesh.h](https://docs.zephyrproject.org/latest/doxygen/html/esp__wifi__mesh_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P011_conn_mgr_conn_impl_结构体.md) · [返回大纲](大纲.md) · [下一章](P013_esp_wifi_mesh_config_结构体.md)
