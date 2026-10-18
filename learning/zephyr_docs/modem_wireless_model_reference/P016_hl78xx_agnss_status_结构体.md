---
id: learning.zephyr-docs.modem-wireless-model-reference.page-16
title: hl78xx_agnss_status_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structhl78xx__agnss__status.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第16章\_hl78xx\_agnss\_status\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structhl78xx__agnss__status.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

辅助全球导航卫星系统（A-GNSS）的辅助数据状态结构。

```c
#include <zephyr/drivers/modem/hl78xx_apis.h>
```

<a id="details"></a>

辅助全球导航卫星系统（A-GNSS）辅助数据状态结构体。包含 `AT+GNSSAD?` 命令的已解析响应。当模式为 `VALID` 时，到期字段表示剩余时间。注意：仅在启用 Kconfig 选项 `CONFIG_HL78XX_GNSS_SUPPORT_ASSISTED_MODE` 时可用。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 16.1\_数据成员（Data Fields）

<a id="r_aead701aedc1734a4f89bd628030b0850"></a>

```c
enum hl78xx_agnss_mode mode
```

相关声明：[hl78xx_agnss_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga7d4975dffccffac27c9dccb85c02d549)、[mode](#aead701aedc1734a4f89bd628030b0850)。

有效性模式：0 表示无效或为空，1 表示有效。

<a id="r_a5c3fa9011d3d5e71d5aaacc0ecfe7e95"></a>

```c
uint8_t days
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[days](#a5c3fa9011d3d5e71d5aaacc0ecfe7e95)。

到期前剩余天数，范围为 1 至 28，仅在 `mode=1` 时有效。

<a id="r_a5e7e0613597dad81c06ca0b7b48a0aba"></a>

```c
uint8_t hours
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[hours](#a5e7e0613597dad81c06ca0b7b48a0aba)。

到期前剩余小时数，范围为 0 至 23，仅在 `mode=1` 时有效。

<a id="r_aa17d6323d9faeb81b1d3299898166a0b"></a>

```c
uint8_t minutes
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[minutes](#aa17d6323d9faeb81b1d3299898166a0b)。

到期前剩余分钟数，范围为 0 至 59，仅在 `mode=1` 时有效。

## 16.2\_详细说明（Detailed Documentation）

<a id="a5c3fa9011d3d5e71d5aaacc0ecfe7e95"></a>

### `days`

```c
uint8_t hl78xx_agnss_status::days
```

到期前剩余天数，范围为 1 至 28，仅在 `mode=1` 时有效。

<a id="a5e7e0613597dad81c06ca0b7b48a0aba"></a>

### `hours`

```c
uint8_t hl78xx_agnss_status::hours
```

到期前剩余小时数，范围为 0 至 23，仅在 `mode=1` 时有效。

<a id="aa17d6323d9faeb81b1d3299898166a0b"></a>

### `minutes`

```c
uint8_t hl78xx_agnss_status::minutes
```

到期前剩余分钟数，范围为 0 至 59，仅在 `mode=1` 时有效。

<a id="aead701aedc1734a4f89bd628030b0850"></a>

### `mode`

```c
enum hl78xx_agnss_mode hl78xx_agnss_status::mode
```

有效性模式：0 表示无效或为空，1 表示有效。

本数据类型文档由以下文件生成：

- `zephyr/drivers/modem/hl78xx_apis.h`

## 16.3\_原页交叉引用（Cross References）

- [zephyr/drivers/modem/hl78xx_apis.h](https://docs.zephyrproject.org/latest/doxygen/html/hl78xx__apis_8h_source.html)
- [hl78xx_agnss_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__hl78xx__interface.html#ga7d4975dffccffac27c9dccb85c02d549)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [CONFIG_HL78XX_GNSS_SUPPORT_ASSISTED_MODE](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HL78XX_GNSS_SUPPORT_ASSISTED_MODE)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P015_esp_wifi_mesh_status_结构体.md) · [返回大纲](大纲.md) · [下一章](P017_hl78xx_at_monitor_entry_结构体.md)
