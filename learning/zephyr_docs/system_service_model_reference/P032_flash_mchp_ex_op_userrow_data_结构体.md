---
id: learning.zephyr-docs.system-service-model-reference.page-32
title: flash_mchp_ex_op_userrow_data_结构体
kind: reference
status: maintained
domains: [zephyr, services, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structflash__mchp__ex__op__userrow__data.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第32章\_flash\_mchp\_ex\_op\_userrow\_data\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structflash__mchp__ex__op__userrow__data.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

MCHP NVMCTRL G1闪存用户行（User Row）数据操作的参数。

```c
#include <zephyr/drivers/flash/mchp_nvmctrl_g1.h>
```

<a id="details"></a>

MCHP NVMCTRL G1 Flash 用户行（user row）数据操作的参数。作为 `FLASH_EX_OP_USER_ROW_WRITE` 的输入参数，用于指定源数据缓冲区及用户行区域内的目标位置。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 32.1\_数据成员（Data Fields）

<a id="r_a47930c1edb14b8b15f5800c7f05cf287"></a>

```c
const void * data
```

相关声明：[data](#a47930c1edb14b8b15f5800c7f05cf287)。

指向待写入数据缓冲区的指针。

<a id="r_ae69ed8df0f2a63ab836df7fe7c35f1df"></a>

```c
size_t data_len
```

相关声明：[data_len](#ae69ed8df0f2a63ab836df7fe7c35f1df)。

数据缓冲区长度，单位为字节。

<a id="r_aeecffa84916b2be1f5118fc405ae5279"></a>

```c
off_t offset
```

相关声明：[off_t](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a98a5cc5f4a350bf5652565021a2f239f)、[offset](#aeecffa84916b2be1f5118fc405ae5279)。

写入起点在用户行区域内的字节偏移量。

## 32.2\_详细说明（Detailed Documentation）

<a id="a47930c1edb14b8b15f5800c7f05cf287"></a>

### `data`

```c
const void* flash_mchp_ex_op_userrow_data::data
```

指向待写入数据缓冲区的指针。

<a id="ae69ed8df0f2a63ab836df7fe7c35f1df"></a>

### `data_len`

```c
size_t flash_mchp_ex_op_userrow_data::data_len
```

数据缓冲区长度，单位为字节。

必须按写入块大小对齐。

<a id="aeecffa84916b2be1f5118fc405ae5279"></a>

### `offset`

```c
off_t flash_mchp_ex_op_userrow_data::offset
```

写入起点在用户行区域内的字节偏移量。

必须按写入块大小对齐。

本数据类型文档由以下文件生成：

- `zephyr/drivers/flash/mchp_nvmctrl_g1.h`

## 32.3\_原页交叉引用（Cross References）

- [zephyr/drivers/flash/mchp_nvmctrl_g1.h](https://docs.zephyrproject.org/latest/doxygen/html/mchp__nvmctrl__g1_8h_source.html)
- [off_t](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a98a5cc5f4a350bf5652565021a2f239f)
- [FLASH_EX_OP_USER_ROW_WRITE](https://docs.zephyrproject.org/latest/doxygen/html/group__mchp__nvmctrl__g1__flash__ex__op.html#gga4dae21b9b6e0a90faddfa045b30e19a8a1a4c0eddbc371ca9cf9f4fd11f06847d)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P031_flash_it51xxx_ex_op_wr_protect_lock_结构体.md) · [返回大纲](大纲.md) · [下一章](P033_flash_sector_结构体.md)
