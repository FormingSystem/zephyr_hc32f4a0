---
id: learning.zephyr-docs.driver-model-reference.page-12
title: Andes原位执行存储器读命令
kind: reference
status: maintained
domains: [zephyr, hardware, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structandes__xip__ex__ops__mem__read__cmd__in.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第12章\_Andes原位执行存储器读命令

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structandes__xip__ex__ops__mem__read__cmd__in.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

`FLASH_ANDES_XIP_EX_OP_MEM_READ_CMD` 操作的输入参数。

```c
#include <zephyr/drivers/flash/andes_flash_xip_api_ex.h>
```

<a id="details"></a>

`FLASH_ANDES_XIP_EX_OP_MEM_READ_CMD` 操作的输入参数。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 12.1\_数据成员（Data Fields）

<a id="r_aa642d9ed612a34c20332ea0396207bfa"></a>

```c
enum flash_andes_xip_mem_rd_cmd cmd
```

相关声明：[flash_andes_xip_mem_rd_cmd](https://docs.zephyrproject.org/latest/doxygen/html/group__andes__flash__xip__ex__op.html#gabb24a40e5fd9462fe0cd06f426e0583f)、[cmd](#aa642d9ed612a34c20332ea0396207bfa)。

内存映射模式（Memory-mapped Mode）使用的 SPI 命令。

## 12.2\_详细说明（Detailed Documentation）

<a id="aa642d9ed612a34c20332ea0396207bfa"></a>

### `cmd`

```c
enum flash_andes_xip_mem_rd_cmd andes_xip_ex_ops_mem_read_cmd_in::cmd
```

内存映射模式（Memory-mapped Mode）使用的 SPI 命令。

本结构体文档由以下文件生成：

- `zephyr/drivers/flash/andes_flash_xip_api_ex.h`

## 12.3\_原页交叉引用（Cross References）

- [FLASH_ANDES_XIP_EX_OP_MEM_READ_CMD](https://docs.zephyrproject.org/latest/doxygen/html/group__andes__flash__xip__ex__op.html#gga4b46df3b8254c20bf81be3957f9a0d1ea06bff51aaa30f75f7fd26154c512d6fc)
- [zephyr/drivers/flash/andes_flash_xip_api_ex.h](https://docs.zephyrproject.org/latest/doxygen/html/andes__flash__xip__api__ex_8h_source.html)
- [flash_andes_xip_mem_rd_cmd](https://docs.zephyrproject.org/latest/doxygen/html/group__andes__flash__xip__ex__op.html#gabb24a40e5fd9462fe0cd06f426e0583f)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P011_Andes原位执行锁状态.md) · [返回大纲](大纲.md) · [下一章](P013_Andes原位执行设置参数.md)
