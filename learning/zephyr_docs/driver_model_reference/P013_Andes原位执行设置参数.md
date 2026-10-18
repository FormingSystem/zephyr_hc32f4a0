---
id: learning.zephyr-docs.driver-model-reference.page-13
title: Andes原位执行设置参数
kind: reference
status: maintained
domains: [zephyr, hardware, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structandes__xip__ex__ops__set__in.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第13章\_Andes原位执行设置参数

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structandes__xip__ex__ops__set__in.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

`FLASH_ANDES_XIP_EX_OP_SET_STATUS_REGS` 操作的输入参数。

```c
#include <zephyr/drivers/flash/andes_flash_xip_api_ex.h>
```

<a id="details"></a>

`FLASH_ANDES_XIP_EX_OP_SET_STATUS_REGS` 操作的输入参数。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 13.1\_数据成员（Data Fields）

<a id="r_afb0c626010d671ddb496ac3dcce4e667"></a>

```c
uint8_t regs [3]
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[regs](#afb0c626010d671ddb496ac3dcce4e667)。

要写入的状态寄存器值。

<a id="r_a2210892b339e0ab05c27eacef4d84128"></a>

```c
uint8_t masks [3]
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[masks](#a2210892b339e0ab05c27eacef4d84128)。

指定要修改的状态寄存器位的掩码（Mask）。

<a id="r_a75b6d154c433edb2f179c50c4b962881"></a>

```c
bool volatile_write
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[volatile_write](#a75b6d154c433edb2f179c50c4b962881)。

使用易失性写入（Volatile Write）。

## 13.2\_详细说明（Detailed Documentation）

<a id="a2210892b339e0ab05c27eacef4d84128"></a>

### `masks`

```c
uint8_t andes_xip_ex_ops_set_in::masks[3]
```

指定要修改的状态寄存器位的掩码（Mask）。

<a id="afb0c626010d671ddb496ac3dcce4e667"></a>

### `regs`

```c
uint8_t andes_xip_ex_ops_set_in::regs[3]
```

要写入的状态寄存器值。

<a id="a75b6d154c433edb2f179c50c4b962881"></a>

### `volatile_write`

```c
bool andes_xip_ex_ops_set_in::volatile_write
```

使用易失性写入（Volatile Write）。

本结构体文档由以下文件生成：

- `zephyr/drivers/flash/andes_flash_xip_api_ex.h`

## 13.3\_原页交叉引用（Cross References）

- [FLASH_ANDES_XIP_EX_OP_SET_STATUS_REGS](https://docs.zephyrproject.org/latest/doxygen/html/group__andes__flash__xip__ex__op.html#gga4b46df3b8254c20bf81be3957f9a0d1ea90ae34480ccec850be7ac347f64fbb8f)
- [zephyr/drivers/flash/andes_flash_xip_api_ex.h](https://docs.zephyrproject.org/latest/doxygen/html/andes__flash__xip__api__ex_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P012_Andes原位执行存储器读命令.md) · [返回大纲](大纲.md) · [下一章](P014_Arm时钟控制.md)
