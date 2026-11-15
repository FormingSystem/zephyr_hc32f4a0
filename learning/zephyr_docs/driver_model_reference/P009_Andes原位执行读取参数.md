---
id: learning.zephyr-docs.driver-model-reference.page-9
title: Andes原位执行读取参数
kind: reference
status: maintained
domains: [zephyr, hardware, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structandes__xip__ex__ops__get__out.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第9章\_Andes原位执行读取参数

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structandes__xip__ex__ops__get__out.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

`FLASH_ANDES_XIP_EX_OP_GET_STATUS_REGS` 操作的输出参数。

```c
#include <zephyr/drivers/flash/andes_flash_xip_api_ex.h>
```

<a id="details"></a>

`FLASH_ANDES_XIP_EX_OP_GET_STATUS_REGS` 操作的输出参数。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 9.1\_数据成员（Data Fields）

<a id="r_a70bbb5025fbfed276ff31b5f0024f32e"></a>

```c
uint8_t regs [3]
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[regs](#a70bbb5025fbfed276ff31b5f0024f32e)。

用于保存所读取状态寄存器（Status Registers）的缓冲区。

## 9.2\_详细说明（Detailed Documentation）

<a id="a70bbb5025fbfed276ff31b5f0024f32e"></a>

### `regs`

```c
uint8_t andes_xip_ex_ops_get_out::regs[3]
```

用于保存所读取状态寄存器（Status Registers）的缓冲区。

本结构体文档由以下文件生成：

- `zephyr/drivers/flash/andes_flash_xip_api_ex.h`

## 9.3\_原页交叉引用（Cross References）

- [FLASH_ANDES_XIP_EX_OP_GET_STATUS_REGS](https://docs.zephyrproject.org/latest/doxygen/html/group__andes__flash__xip__ex__op.html#gga4b46df3b8254c20bf81be3957f9a0d1ead7dc137a0bc5b2511b85d194f27bd6c7)
- [zephyr/drivers/flash/andes_flash_xip_api_ex.h](https://docs.zephyrproject.org/latest/doxygen/html/andes__flash__xip__api__ex_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P008_模拟轴校准.md) · [返回大纲](大纲.md) · [下一章](P010_Andes原位执行锁定参数.md)
