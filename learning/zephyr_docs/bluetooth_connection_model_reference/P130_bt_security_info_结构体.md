---
id: learning.zephyr-docs.bluetooth-connection-model-reference.page-130
title: bt_security_info_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__security__info.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第130章\_bt\_security\_info\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__security__info.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

安全信息（Security Info）结构。

```c
#include <zephyr/bluetooth/conn.h>
```

<a id="details"></a>

安全信息（Security Info）结构。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 130.1\_数据成员（Data Fields）

<a id="r_a7b18849fad25b3f2da6b8c85a56d86e1"></a>

```c
bt_security_t level
```

相关声明：[bt_security_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gaf0c56cd26c4147f6c9f0faa11fa01783)、[level](#a7b18849fad25b3f2da6b8c85a56d86e1)。

安全等级（Security Level）。

<a id="r_a6567ffb82b7fa8093cc57ef4662873ba"></a>

```c
uint8_t enc_key_size
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[enc_key_size](#a6567ffb82b7fa8093cc57ef4662873ba)。

加密密钥大小（Encryption Key Size）。

<a id="r_a99cb4af08bfa1dab182821d956368526"></a>

```c
enum bt_security_flag flags
```

相关声明：[bt_security_flag](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ga2f8712bbf3410de5cbe6ce489fe30e5e)、[flags](#a99cb4af08bfa1dab182821d956368526)。

标志（Flags）。

## 130.2\_详细说明（Detailed Documentation）

<a id="a6567ffb82b7fa8093cc57ef4662873ba"></a>

### `enc_key_size`

```c
uint8_t bt_security_info::enc_key_size
```

加密密钥大小（Encryption Key Size）。

<a id="a99cb4af08bfa1dab182821d956368526"></a>

### `flags`

```c
enum bt_security_flag bt_security_info::flags
```

标志（Flags）。

<a id="a7b18849fad25b3f2da6b8c85a56d86e1"></a>

### `level`

```c
bt_security_t bt_security_info::level
```

安全等级（Security Level）。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/conn.h`

## 130.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/conn.h](https://docs.zephyrproject.org/latest/doxygen/html/conn_8h_source.html)
- [bt_security_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#gaf0c56cd26c4147f6c9f0faa11fa01783)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bt_security_flag](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html#ga2f8712bbf3410de5cbe6ce489fe30e5e)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P129_bt_le_scan_recv_info_结构体.md) · [返回大纲](大纲.md) · [下一章](P131_bt_uuid_结构体.md)
