---
id: learning.zephyr-docs.driver-model-reference.page-10
title: Andes原位执行锁定参数
kind: reference
status: maintained
domains: [zephyr, hardware, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structandes__xip__ex__ops__lock__in.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第10章\_Andes原位执行锁定参数

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structandes__xip__ex__ops__lock__in.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

`FLASH_ANDES_XIP_EX_OP_LOCK` 操作的输入参数。

```c
#include <zephyr/drivers/flash/andes_flash_xip_api_ex.h>
```

<a id="details"></a>

`FLASH_ANDES_XIP_EX_OP_LOCK` 操作的输入参数。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 10.1\_数据成员（Data Fields）

<a id="r_a3d640ec6d0177dbf33670b02a2a36891"></a>

```c
bool enable
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[enable](#a3d640ec6d0177dbf33670b02a2a36891)。

设为 `true` 启用锁定，设为 `false` 禁用锁定。

## 10.2\_详细说明（Detailed Documentation）

<a id="a3d640ec6d0177dbf33670b02a2a36891"></a>

### `enable`

```c
bool andes_xip_ex_ops_lock_in::enable
```

设为 `true` 启用锁定，设为 `false` 禁用锁定。

本结构体文档由以下文件生成：

- `zephyr/drivers/flash/andes_flash_xip_api_ex.h`

## 10.3\_原页交叉引用（Cross References）

- [FLASH_ANDES_XIP_EX_OP_LOCK](https://docs.zephyrproject.org/latest/doxygen/html/group__andes__flash__xip__ex__op.html#gga4b46df3b8254c20bf81be3957f9a0d1eae40ae84ea8da6a831c1ed37ea40d37c0)
- [zephyr/drivers/flash/andes_flash_xip_api_ex.h](https://docs.zephyrproject.org/latest/doxygen/html/andes__flash__xip__api__ex_8h_source.html)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P009_Andes原位执行读取参数.md) · [返回大纲](大纲.md) · [下一章](P011_Andes原位执行锁状态.md)
