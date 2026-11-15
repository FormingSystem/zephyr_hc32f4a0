---
id: learning.zephyr-docs.data-utilities.api-23
title: UUID生成与转换接口
kind: reference
status: maintained
domains: [zephyr, data, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__uuid.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第23章\_UUID生成与转换接口

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__uuid.html)。读取日期：2026-10-14；基线为保存的 `latest` 页面，HTML 摘要见[来源记录](../SOURCES.md)。

## 23.1\_阅读说明与来源

译注：本组是 `<zephyr/sys/uuid.h>` 的通用唯一标识符（Universally Unique Identifier，UUID）接口。先读[UUID 指南](P014_UUID通用唯一标识符.md)和[生成示例](P015_UUID生成示例.md)，再查询生成、比较、解析及编码转换。蓝牙专用 UUID 类型和接口另有官方页面，不与这里的 `struct uuid` 混用。

本组：[UUID生成与转换接口](P023_UUID生成与转换接口.md) · [UUID系统头文件](P024_UUID系统头文件.md) · [UUID系统头文件源码](P025_UUID系统头文件源码.md) · [UUID二进制结构](P026_UUID二进制结构.md)。

引入版本（Since）：4.2；API 版本（Version）：`0.8.0`。

## 23.2\_数据结构（Data Structures）

<a id="r_uuid"></a>

```c
struct uuid
```

UUID 的二进制表示（Binary Representation）。

相关声明：[uuid](P026_UUID二进制结构.md)。

## 23.3\_宏定义（Macros）

<a id="r_ga5db91c4b658dc322b42959cb5c851020"></a>

```c
#define UUID_SIZE 16U
```

UUID 二进制表示的字节数。

<a id="r_ga6d37dd9ad8391595db1b71ca2103a228"></a>

```c
#define UUID_STR_LEN 37U
```

UUID 规范字符串表示（Canonical String Representation）的长度，包含空字符终止符（NULL Terminator）。

<a id="r_ga1d71eb34412c3e04f9f85bb8320548d6"></a>

```c
#define UUID_BASE64_LEN 25U
```

UUID 的 Base64 字符串表示长度，包含空字符终止符。

<a id="r_gae28fa917e2f1ad587da4cf901f0de94a"></a>

```c
#define UUID_BASE64URL_LEN 23U
```

UUID 的 URL 与文件名安全（URL and Filename Safe）Base64 字符串表示长度，包含空字符终止符。

## 23.4\_函数（Functions）

<a id="r_ga1e1e2f008f5ac3366bf474de27d42b66"></a>

```c
int uuid_generate_v4 (struct uuid *out)
```

生成 UUIDv4。

相关声明：[uuid](P026_UUID二进制结构.md)。

<a id="r_ga6f692b733f600e0346317f3d25d84409"></a>

```c
int uuid_generate_v5 (const struct uuid *ns, const void *data, size_t data_size, struct uuid *out)
```

生成 UUIDv5。

相关声明：[uuid](P026_UUID二进制结构.md)。

<a id="r_ga91f227c01e8b6bc7b8df8f37a1632b36"></a>

```c
int uuid_cmp (const struct uuid *a, const struct uuid *b)
```

比较两个 UUID。

相关声明：[uuid](P026_UUID二进制结构.md)。

<a id="r_ga1ae245a3ed4e1780a7b4d0346ede1188"></a>

```c
bool uuid_is_nil (const struct uuid *data)
```

检查 UUID 是否为全零 UUID（Nil UUID）。

相关声明：[uuid](P026_UUID二进制结构.md)。

<a id="r_ga1fd6f837800e0bd9bd0e4c4e5891568e"></a>

```c
int uuid_copy (const struct uuid *data, struct uuid *out)
```

将一个 UUID 复制到另一个 UUID 中。

相关声明：[uuid](P026_UUID二进制结构.md)。

<a id="r_gacf4a46349ed1a7a6a44b3cc84c687bc1"></a>

```c
int uuid_from_buffer (const uint8_t data[16U], struct uuid *out)
```

从二进制大端序（Big-endian）格式的 UUID 创建 `uuid_t`。

相关声明：[uuid](P026_UUID二进制结构.md)。

<a id="r_gadf6084420d0ee8cc41a522ebb2c71e7d"></a>

```c
int uuid_from_string (const char data[37U], struct uuid *out)
```

从规范字符串表示（RFC 9562）解析 UUID。

相关声明：[uuid](P026_UUID二进制结构.md)。

<a id="r_ga2562309a55cbd49b70e1c60a761fb08f"></a>

```c
int uuid_to_buffer (const struct uuid *data, uint8_t out[16U])
```

将 UUID 保存到二进制大端序格式的缓冲区。

相关声明：[uuid](P026_UUID二进制结构.md)。

<a id="r_gaac4b9f9b243c9ecbeac94f0b4947ede1"></a>

```c
int uuid_to_string (const struct uuid *data, char out[37U])
```

将 UUID 转换为规范字符串表示（RFC 9562）。

相关声明：[uuid](P026_UUID二进制结构.md)。

<a id="r_ga2c73bd8b52693f1c28dbbc10e145e098"></a>

```c
int uuid_to_base64 (const struct uuid *data, char out[25U])
```

将 UUID 转换为 Base64 字符串表示（RFC 3548、RFC 4648）。

相关声明：[uuid](P026_UUID二进制结构.md)。

<a id="r_ga68dcce718b9e98d4873fe7c40d99ad4c"></a>

```c
int uuid_to_base64url (const struct uuid *data, char out[23U])
```

将 UUID 转换为 Base64 字符串表示。

相关声明：[uuid](P026_UUID二进制结构.md)。

## 23.5\_详细说明（Detailed Documentation）

<a id="ga1d71eb34412c3e04f9f85bb8320548d6"></a>

### `UUID_BASE64_LEN`

```c
#define UUID_BASE64_LEN 25U
```

```c
#include <zephyr/sys/uuid.h>
```

UUID 的 Base64 字符串表示长度，包含空字符终止符。

<a id="gae28fa917e2f1ad587da4cf901f0de94a"></a>

### `UUID_BASE64URL_LEN`

```c
#define UUID_BASE64URL_LEN 23U
```

```c
#include <zephyr/sys/uuid.h>
```

UUID 的 URL 与文件名安全（URL and Filename Safe）Base64 字符串表示长度，包含空字符终止符。

<a id="ga5db91c4b658dc322b42959cb5c851020"></a>

### `UUID_SIZE`

```c
#define UUID_SIZE 16U
```

```c
#include <zephyr/sys/uuid.h>
```

UUID 二进制表示的字节数。

<a id="ga6d37dd9ad8391595db1b71ca2103a228"></a>

### `UUID_STR_LEN`

```c
#define UUID_STR_LEN 37U
```

```c
#include <zephyr/sys/uuid.h>
```

UUID 规范字符串表示（Canonical String Representation）的长度，包含空字符终止符（NULL Terminator）。

<a id="ga91f227c01e8b6bc7b8df8f37a1632b36"></a>

### `uuid_cmp()`

```c
int uuid_cmp ( const struct uuid * a, const struct uuid * b )
```

```c
#include <zephyr/sys/uuid.h>
```

比较两个 UUID。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `a` | 待比较的第一个 UUID。 |
| `b` | 待比较的第二个 UUID。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 两个 UUID 相等。 |
| `nonzero` | 两个 UUID 不相等。 |

> 译注（源码核对）：当前实现返回 `memcmp()` 的结果。判断相等应写 `uuid_cmp(a, b) == 0`，不要反用为“非零表示相等”，也不要假定不相等时一定返回 1。两个输入对象都必须有效。

<a id="ga1fd6f837800e0bd9bd0e4c4e5891568e"></a>

### `uuid_copy()`

```c
int uuid_copy ( const struct uuid * data, struct uuid * out )
```

```c
#include <zephyr/sys/uuid.h>
```

将一个 UUID 复制到另一个 UUID 中。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `data` | 要复制的输入数据。 |
| `out` | 复制操作的目标。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | UUID 已正确复制到 `out`。 |
| `-EINVAL` | `out` 不满足要求。 |

<a id="gacf4a46349ed1a7a6a44b3cc84c687bc1"></a>

### `uuid_from_buffer()`

```c
int uuid_from_buffer ( const uint8_t data[16U], struct uuid * out )
```

```c
#include <zephyr/sys/uuid.h>
```

从二进制大端序（Big-endian）格式的 UUID 创建 `uuid_t`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `data` | 以大端字节序存放二进制 UUID 的缓冲区。 |
| `out` | 用于写入结果的 UUID。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | UUID 已正确解析并保存到 `out`。 |
| `-EINVAL` | `data` 或 `out` 不满足要求。 |

> 译注（源码核对）：原说明使用 `uuid_t`，当前头文件实际声明的是 `struct uuid`，本接口的输出参数也是 `struct uuid *`。实现复制 16 字节，不解析文本，也不根据主机端序对各字段做交换；输入必须已按 UUID 的规定字节顺序排列。

<a id="gadf6084420d0ee8cc41a522ebb2c71e7d"></a>

### `uuid_from_string()`

```c
int uuid_from_string ( const char data[37U], struct uuid * out )
```

```c
#include <zephyr/sys/uuid.h>
```

从规范字符串表示（RFC 9562）解析 UUID。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `data` | 指向待解析字符串的指针。 |
| `out` | 用于写入结果的 UUID。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | UUID 已正确解析并保存到 `out`。 |
| `-EINVAL` | `data` 或 `out` 不满足要求。 |

> 译注（源码核对）：当前实现要求以空字符终止的字符串，总长度为 36 个可见字符，在索引 8、13、18、23 处为连字符，其余位置为十六进制数字。它通过 `strlen()` 检查长度，没有独立输入容量参数。解析成功表示格式正确，不代表只接受 v4／v5，也没有额外验证版本位或变体位。

<a id="ga1e1e2f008f5ac3366bf474de27d42b66"></a>

### `uuid_generate_v4()`

```c
int uuid_generate_v4 ( struct uuid * out)
```

```c
#include <zephyr/sys/uuid.h>
```

生成 UUIDv4。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `out` | 用于写入结果的 UUID。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | UUID 已正确生成并保存到 `out`。 |
| `-EINVAL` | `out` 不满足要求。 |

**注意（Attention）**：仅在启用 Kconfig 选项 `CONFIG_UUID_V4` 时可用。

> 译注（源码核对）：当前实现调用 `sys_rand_get()` 填满 16 字节，再设置版本（Version）与变体（Variant）位；因此随机源的质量取决于构建配置。本接口不作秘密凭据用途的保证。

<a id="ga6f692b733f600e0346317f3d25d84409"></a>

### `uuid_generate_v5()`

```c
int uuid_generate_v5 ( const struct uuid * ns, const void * data, size_t data_size, struct uuid * out )
```

```c
#include <zephyr/sys/uuid.h>
```

生成 UUIDv5。

此函数根据命名空间 UUID（Namespace UUID）和二进制数据计算确定性 UUID（Deterministic UUID）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ns` | 指向用作命名空间的 UUID 的指针。 |
| `data` | 指向待散列（Hash）数据的指针，这些数据用于生成 UUID。 |
| `data_size` | 数据缓冲区的大小。 |
| `out` | 用于写入结果的 UUID。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | UUID 已正确生成并保存到 `out`。 |
| `-EINVAL` | `out` 为 `NULL`。 |
| `-ENOMEM` | 内存分配失败。 |
| `-ENOTSUP` | PSA Crypto 提供方不支持所需的密码学算法 SHA-1。 |
| `-EIO` | 一般性错误。 |

**注意（Attention）**：仅在启用 Kconfig 选项 `CONFIG_UUID_V5` 时可用。

> 译注（源码核对）：当前实现对命名空间的 16 字节和指定长度的名称数据依次执行 PSA SHA-1，再取前 16 字节并设置版本与变体位。确定性取决于相同命名空间和完全相同的输入字节；不会自动获取 URL 内容、转换字符编码或规范化名称。实现只显式检查 `out` 是否为空，调用方仍必须提供有效的 `ns` 和输入数据。

<a id="ga1ae245a3ed4e1780a7b4d0346ede1188"></a>

### `uuid_is_nil()`

```c
bool uuid_is_nil ( const struct uuid * data)
```

```c
#include <zephyr/sys/uuid.h>
```

检查 UUID 是否为全零 UUID（Nil UUID）。

全零 UUID（Nil UUID）是 RFC 9562 第 5.9 节定义的一种特殊形式，其全部 128 位均设为零。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `data` | 待检查的 UUID。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `true` | `data` 是全零 UUID。 |
| `false` | `data` 是其他任意值。 |

> 译注（源码核对）：Nil UUID 是 16 字节全零的实际 UUID 值，不是 `NULL` 指针。当前实现读取 `data->val`，传入空指针不在接口约定内。

<a id="ga2c73bd8b52693f1c28dbbc10e145e098"></a>

### `uuid_to_base64()`

```c
int uuid_to_base64 ( const struct uuid * data, char out[25U] )
```

```c
#include <zephyr/sys/uuid.h>
```

将 UUID 转换为 Base64 字符串表示（RFC 3548、RFC 4648）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `data` | 要转换为字符串的 UUID。 |
| `out` | 指向预先分配的结果缓冲区的指针。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | UUID 已完成转换并写入 `out`。 |
| `-EINVAL` | `out` 不满足要求。 |

**注意（Attention）**：仅在启用 Kconfig 选项 `CONFIG_UUID_BASE64` 时可用。

> 译注（源码核对）：输出含两个 `=` 填充字符，共 24 个可见字符；`UUID_BASE64_LEN`（25）还包含末尾空字符。它编码的是 16 字节 UUID，不是 36 字符的 UUID 文本。

<a id="ga68dcce718b9e98d4873fe7c40d99ad4c"></a>

### `uuid_to_base64url()`

```c
int uuid_to_base64url ( const struct uuid * data, char out[23U] )
```

```c
#include <zephyr/sys/uuid.h>
```

将 UUID 转换为 Base64 字符串表示。

使用 RFC 4648 第 5 节规定的 URL 与文件名安全（URL and Filename Safe）形式。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `data` | 要转换为字符串的 UUID。 |
| `out` | 指向预先分配的结果缓冲区的指针。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | UUID 已完成转换并写入 `out`。 |
| `-EINVAL` | `out` 不满足要求。 |

> 译注（源码核对）：当前实现与 `uuid_to_base64()` 一起位于 `CONFIG_UUID_BASE64` 条件编译块内，虽然本函数的原说明没有重复标出这一依赖。它将 `+` 替换为 `-`、`/` 替换为 `_`，去掉末尾的两个 `=` 填充字符，再写入空字符。输出是 22 个可见字符，需要 23 字节缓冲区。

<a id="ga2562309a55cbd49b70e1c60a761fb08f"></a>

### `uuid_to_buffer()`

```c
int uuid_to_buffer ( const struct uuid * data, uint8_t out[16U] )
```

```c
#include <zephyr/sys/uuid.h>
```

将 UUID 保存到二进制大端序格式的缓冲区。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `data` | 要保存到缓冲区的输入 UUID。 |
| `out` | 以大端字节序存放二进制 UUID 的缓冲区。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | UUID 已正确解析并保存到 `out`。 |
| `-EINVAL` | `out` 不满足要求。 |

<a id="gaac4b9f9b243c9ecbeac94f0b4947ede1"></a>

### `uuid_to_string()`

```c
int uuid_to_string ( const struct uuid * data, char out[37U] )
```

```c
#include <zephyr/sys/uuid.h>
```

将 UUID 转换为规范字符串表示（RFC 9562）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `data` | 要转换为字符串的 UUID。 |
| `out` | 指向预先分配的结果缓冲区的指针。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | UUID 已完成转换并写入 `out`。 |
| `-EINVAL` | `out` 不满足要求。 |

> 译注（源码核对）：当前实现以小写十六进制输出 8-4-4-4-12 格式。调用方须预留 `UUID_STR_LEN`（37）字节；数组形式的函数形参不携带实际分配容量，函数不会检测一个非空指针是否指向足够大的缓冲区。

## 23.6\_相关源码与使用边界

声明来自 `<zephyr/sys/uuid.h>`。可通过本仓库[对应头文件](../../../include/zephyr/sys/uuid.h)追踪源码；本仓库版本可能与官网 `latest` 不同。译注核对依据为保存的[官方头文件](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/sys/uuid.h)、[官方实现](https://github.com/zephyrproject-rtos/zephyr/blob/main/lib/uuid/uuid.c)和[Kconfig](https://github.com/zephyrproject-rtos/zephyr/blob/main/lib/uuid/Kconfig)，摘要见[来源记录](../SOURCES.md)。

> 译注——结构与缓冲区：Doxygen 结构参考隐藏了 `val` 成员，当前官方头文件实际为 `uint8_t val[UUID_SIZE]`，即 16 字节。规范文本的容量为 37 字节、Base64 为 25 字节、Base64URL 为 23 字节，这些文本容量均包含末尾空字符，不能与二进制的 16 字节互换。复制、比较和转换接口需要有效的输入对象；仅检查输出指针的函数不承诺对空输入返回错误码。

> 译注——配置依赖：当前 `CONFIG_UUID_V4` 依赖 `ENTROPY_GENERATOR`；`CONFIG_UUID_V5` 依赖 `PSA_WANT_ALG_SHA_1` 且要求未启用 `BUILD_WITH_TFM`；`CONFIG_UUID_BASE64` 依赖 `BASE64`。头文件中可见声明不表示相应实现已进入本次固件。API 版本 `0.8.0` 与 Zephyr 引入版本 `4.2` 含义不同，也不能把它们当作本批 `latest` 的发布版本号。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>
<a id="header-define-members"></a>
<a id="define-members"></a>
<a id="header-func-members"></a>
<a id="func-members"></a>
<a id="details"></a>
<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

[上一章](P022_二进制描述符句柄结构.md) · [返回大纲](大纲.md) · [下一章](P024_UUID系统头文件.md)
