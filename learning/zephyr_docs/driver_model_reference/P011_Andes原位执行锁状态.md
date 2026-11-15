---
id: learning.zephyr-docs.driver-model-reference.page-11
title: Andes原位执行锁状态
kind: reference
status: maintained
domains: [zephyr, hardware, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structandes__xip__ex__ops__lock__state__out.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第11章\_Andes原位执行锁状态

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structandes__xip__ex__ops__lock__state__out.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

`FLASH_ANDES_XIP_EX_OP_LOCK_STATE` 操作的输出参数。

```c
#include <zephyr/drivers/flash/andes_flash_xip_api_ex.h>
```

<a id="details"></a>

`FLASH_ANDES_XIP_EX_OP_LOCK_STATE` 操作的输出参数。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 11.1\_数据成员（Data Fields）

<a id="r_a58c0503aa43c700ed986362c6f974afa"></a>

```c
bool state
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[state](#a58c0503aa43c700ed986362c6f974afa)。

当前锁定状态（Lock State）。

## 11.2\_详细说明（Detailed Documentation）

<a id="a58c0503aa43c700ed986362c6f974afa"></a>

### `state`

```c
bool andes_xip_ex_ops_lock_state_out::state
```

当前锁定状态（Lock State）。

本结构体文档由以下文件生成：

- `zephyr/drivers/flash/andes_flash_xip_api_ex.h`

## 11.3\_原页交叉引用（Cross References）

- [FLASH_ANDES_XIP_EX_OP_LOCK_STATE](https://docs.zephyrproject.org/latest/doxygen/html/group__andes__flash__xip__ex__op.html#gga4b46df3b8254c20bf81be3957f9a0d1eadb8562975bd289b303b26e0227ac853f)
- [zephyr/drivers/flash/andes_flash_xip_api_ex.h](https://docs.zephyrproject.org/latest/doxygen/html/andes__flash__xip__api__ex_8h_source.html)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P010_Andes原位执行锁定参数.md) · [返回大纲](大纲.md) · [下一章](P012_Andes原位执行存储器读命令.md)
