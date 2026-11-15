---
id: learning.zephyr-docs.peripheral-bus-storage-model-reference.page-96
title: w1_master_config_结构体
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structw1__master__config.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第96章\_w1\_master\_config\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structw1__master__config.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

全部单总线（1-Wire）主机实现共用的配置。

```c
#include <zephyr/drivers/w1.h>
```

<a id="details"></a>

所有 1-Wire 主机实现共用的配置。此结构体为所有 1-Wire 主机实现所共用，应作为 `device` 结构体的 `config` 字段所指对象的第一个成员。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 96.1\_数据成员（Data Fields）

<a id="r_a5cf7b0808d939ad7a6fec4540c36f4c4"></a>

```c
uint16_t slave_count
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[slave_count](#a5cf7b0808d939ad7a6fec4540c36f4c4)。

已连接从设备的数量。

## 96.2\_详细说明（Detailed Documentation）

<a id="a5cf7b0808d939ad7a6fec4540c36f4c4"></a>

### `slave_count`

```c
uint16_t w1_master_config::slave_count
```

已连接从设备的数量。

本数据类型文档由以下文件生成：

- `zephyr/drivers/w1.h`

## 96.3\_原页交叉引用（Cross References）

- [zephyr/drivers/w1.h](https://docs.zephyrproject.org/latest/doxygen/html/w1_8h_source.html)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P095_w1_driver_api_结构体.md) · [返回大纲](大纲.md) · [下一章](P097_w1_master_data_结构体.md)
