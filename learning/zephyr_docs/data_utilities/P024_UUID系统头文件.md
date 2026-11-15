---
id: learning.zephyr-docs.data-utilities.api-24
title: UUID系统头文件
kind: reference
status: maintained
domains: [zephyr, data, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/sys_2uuid_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第24章\_UUID系统头文件

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/sys_2uuid_8h.html)。读取日期：2026-10-14；基线为保存的 `latest` 页面，HTML 摘要见[来源记录](../SOURCES.md)。

## 24.1\_阅读说明与来源

译注：本组是 `<zephyr/sys/uuid.h>` 的通用唯一标识符（Universally Unique Identifier，UUID）接口。先读[UUID 指南](P014_UUID通用唯一标识符.md)和[生成示例](P015_UUID生成示例.md)，再查询生成、比较、解析及编码转换。蓝牙专用 UUID 类型和接口另有官方页面，不与这里的 `struct uuid` 混用。

本组：[UUID生成与转换接口](P023_UUID生成与转换接口.md) · [UUID系统头文件](P024_UUID系统头文件.md) · [UUID系统头文件源码](P025_UUID系统头文件源码.md) · [UUID二进制结构](P026_UUID二进制结构.md)。

用于生成和解析通用唯一标识符（Universally Unique Identifier，UUID）的实用函数。

```c
#include <zephyr/kernel.h>
```

```c
#include <zephyr/types.h>
```

用于生成和解析通用唯一标识符（Universally Unique Identifier，UUID）的实用函数。本驱动符合 [RFC 9562](https://datatracker.ietf.org/doc/rfc9562/)。

## 24.2\_数据结构（Data Structures）

<a id="r_uuid"></a>

```c
struct uuid
```

UUID 的二进制表示（Binary Representation）。

相关声明：[uuid](P026_UUID二进制结构.md)。

## 24.3\_宏定义（Macros）

<a id="r_ga5db91c4b658dc322b42959cb5c851020"></a>

```c
#define UUID_SIZE 16U
```

UUID 二进制表示的字节数。

相关声明：[UUID_SIZE](P023_UUID生成与转换接口.md#ga5db91c4b658dc322b42959cb5c851020)。

<a id="r_ga6d37dd9ad8391595db1b71ca2103a228"></a>

```c
#define UUID_STR_LEN 37U
```

UUID 规范字符串表示（Canonical String Representation）的长度，包含空字符终止符（NULL Terminator）。

相关声明：[UUID_STR_LEN](P023_UUID生成与转换接口.md#ga6d37dd9ad8391595db1b71ca2103a228)。

<a id="r_ga1d71eb34412c3e04f9f85bb8320548d6"></a>

```c
#define UUID_BASE64_LEN 25U
```

UUID 的 Base64 字符串表示长度，包含空字符终止符。

相关声明：[UUID_BASE64_LEN](P023_UUID生成与转换接口.md#ga1d71eb34412c3e04f9f85bb8320548d6)。

<a id="r_gae28fa917e2f1ad587da4cf901f0de94a"></a>

```c
#define UUID_BASE64URL_LEN 23U
```

UUID 的 URL 与文件名安全（URL and Filename Safe）Base64 字符串表示长度，包含空字符终止符。

相关声明：[UUID_BASE64URL_LEN](P023_UUID生成与转换接口.md#gae28fa917e2f1ad587da4cf901f0de94a)。

## 24.4\_函数（Functions）

<a id="r_ga1e1e2f008f5ac3366bf474de27d42b66"></a>

```c
int uuid_generate_v4 (struct uuid *out)
```

生成 UUIDv4。

相关声明：[uuid_generate_v4](P023_UUID生成与转换接口.md#ga1e1e2f008f5ac3366bf474de27d42b66)、[uuid](P026_UUID二进制结构.md)。

<a id="r_ga6f692b733f600e0346317f3d25d84409"></a>

```c
int uuid_generate_v5 (const struct uuid *ns, const void *data, size_t data_size, struct uuid *out)
```

生成 UUIDv5。

相关声明：[uuid_generate_v5](P023_UUID生成与转换接口.md#ga6f692b733f600e0346317f3d25d84409)、[uuid](P026_UUID二进制结构.md)。

<a id="r_ga91f227c01e8b6bc7b8df8f37a1632b36"></a>

```c
int uuid_cmp (const struct uuid *a, const struct uuid *b)
```

比较两个 UUID。

相关声明：[uuid_cmp](P023_UUID生成与转换接口.md#ga91f227c01e8b6bc7b8df8f37a1632b36)、[uuid](P026_UUID二进制结构.md)。

<a id="r_ga1ae245a3ed4e1780a7b4d0346ede1188"></a>

```c
bool uuid_is_nil (const struct uuid *data)
```

检查 UUID 是否为全零 UUID（Nil UUID）。

相关声明：[uuid_is_nil](P023_UUID生成与转换接口.md#ga1ae245a3ed4e1780a7b4d0346ede1188)、[uuid](P026_UUID二进制结构.md)。

<a id="r_ga1fd6f837800e0bd9bd0e4c4e5891568e"></a>

```c
int uuid_copy (const struct uuid *data, struct uuid *out)
```

将一个 UUID 复制到另一个 UUID 中。

相关声明：[uuid_copy](P023_UUID生成与转换接口.md#ga1fd6f837800e0bd9bd0e4c4e5891568e)、[uuid](P026_UUID二进制结构.md)。

<a id="r_gacf4a46349ed1a7a6a44b3cc84c687bc1"></a>

```c
int uuid_from_buffer (const uint8_t data[16U], struct uuid *out)
```

从二进制大端序（Big-endian）格式的 UUID 创建 `uuid_t`。

相关声明：[uuid_from_buffer](P023_UUID生成与转换接口.md#gacf4a46349ed1a7a6a44b3cc84c687bc1)、[uuid](P026_UUID二进制结构.md)。

<a id="r_gadf6084420d0ee8cc41a522ebb2c71e7d"></a>

```c
int uuid_from_string (const char data[37U], struct uuid *out)
```

从规范字符串表示（RFC 9562）解析 UUID。

相关声明：[uuid_from_string](P023_UUID生成与转换接口.md#gadf6084420d0ee8cc41a522ebb2c71e7d)、[uuid](P026_UUID二进制结构.md)。

<a id="r_ga2562309a55cbd49b70e1c60a761fb08f"></a>

```c
int uuid_to_buffer (const struct uuid *data, uint8_t out[16U])
```

将 UUID 保存到二进制大端序格式的缓冲区。

相关声明：[uuid_to_buffer](P023_UUID生成与转换接口.md#ga2562309a55cbd49b70e1c60a761fb08f)、[uuid](P026_UUID二进制结构.md)。

<a id="r_gaac4b9f9b243c9ecbeac94f0b4947ede1"></a>

```c
int uuid_to_string (const struct uuid *data, char out[37U])
```

将 UUID 转换为规范字符串表示（RFC 9562）。

相关声明：[uuid_to_string](P023_UUID生成与转换接口.md#gaac4b9f9b243c9ecbeac94f0b4947ede1)、[uuid](P026_UUID二进制结构.md)。

<a id="r_ga2c73bd8b52693f1c28dbbc10e145e098"></a>

```c
int uuid_to_base64 (const struct uuid *data, char out[25U])
```

将 UUID 转换为 Base64 字符串表示（RFC 3548、RFC 4648）。

相关声明：[uuid_to_base64](P023_UUID生成与转换接口.md#ga2c73bd8b52693f1c28dbbc10e145e098)、[uuid](P026_UUID二进制结构.md)。

<a id="r_ga68dcce718b9e98d4873fe7c40d99ad4c"></a>

```c
int uuid_to_base64url (const struct uuid *data, char out[23U])
```

将 UUID 转换为 Base64 字符串表示。

相关声明：[uuid_to_base64url](P023_UUID生成与转换接口.md#ga68dcce718b9e98d4873fe7c40d99ad4c)、[uuid](P026_UUID二进制结构.md)。

## 24.5\_相关源码与使用边界

声明来自 `<zephyr/sys/uuid.h>`。可通过本仓库[对应头文件](../../../include/zephyr/sys/uuid.h)追踪源码；本仓库版本可能与官网 `latest` 不同。译注核对依据为保存的[官方头文件](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/sys/uuid.h)、[官方实现](https://github.com/zephyrproject-rtos/zephyr/blob/main/lib/uuid/uuid.c)和[Kconfig](https://github.com/zephyrproject-rtos/zephyr/blob/main/lib/uuid/Kconfig)，摘要见[来源记录](../SOURCES.md)。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>
<a id="header-define-members"></a>
<a id="define-members"></a>
<a id="header-func-members"></a>
<a id="func-members"></a>
<a id="details"></a>
<a id="header-details"></a>

[上一章](P023_UUID生成与转换接口.md) · [返回大纲](大纲.md) · [下一章](P025_UUID系统头文件源码.md)
