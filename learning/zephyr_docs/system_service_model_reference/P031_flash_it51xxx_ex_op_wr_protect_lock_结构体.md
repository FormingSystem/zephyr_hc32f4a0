---
id: learning.zephyr-docs.system-service-model-reference.page-31
title: flash_it51xxx_ex_op_wr_protect_lock_结构体
kind: reference
status: maintained
domains: [zephyr, services, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structflash__it51xxx__ex__op__wr__protect__lock.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第31章\_flash\_it51xxx\_ex\_op\_wr\_protect\_lock\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structflash__it51xxx__ex__op__wr__protect__lock.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

嵌入式闪存（EFlash）写入/读取保护锁定的请求/结果。

```c
#include <zephyr/drivers/flash/it51xxx_flash_api_ex.h>
```

<a id="details"></a>

嵌入式闪存（EFlash）写入/读取保护锁定的请求/结果。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 31.1\_数据成员（Data Fields）

<a id="r_a1702b7b51516aeb5cc0195ea2db1689e"></a>

```c
uint8_t path
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[path](#a1702b7b51516aeb5cc0195ea2db1689e)。

要锁定的保护路径位图，参见 `PROTECT_PATH_*`。

<a id="r_a9e3607562530d062a8ac22f6b1b1cc72"></a>

```c
bool is_locked
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[is_locked](#a9e3607562530d062a8ac22f6b1b1cc72)。

指定保护路径的锁定状态。

## 31.2\_详细说明（Detailed Documentation）

<a id="a9e3607562530d062a8ac22f6b1b1cc72"></a>

### `is_locked`

```c
bool flash_it51xxx_ex_op_wr_protect_lock::is_locked
```

指定保护路径的锁定状态。

对于请求，因为只支持锁定操作，所以不使用此字段。对于结果，它表示指定的保护路径是否已锁定。

<a id="a1702b7b51516aeb5cc0195ea2db1689e"></a>

### `path`

```c
uint8_t flash_it51xxx_ex_op_wr_protect_lock::path
```

要锁定的保护路径位图，参见 `PROTECT_PATH_*`。

本数据类型文档由以下文件生成：

- `zephyr/drivers/flash/it51xxx_flash_api_ex.h`

## 31.3\_原页交叉引用（Cross References）

- [zephyr/drivers/flash/it51xxx_flash_api_ex.h](https://docs.zephyrproject.org/latest/doxygen/html/it51xxx__flash__api__ex_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P030_flash_it51xxx_ex_op_addr_protection_结构体.md) · [返回大纲](大纲.md) · [下一章](P032_flash_mchp_ex_op_userrow_data_结构体.md)
