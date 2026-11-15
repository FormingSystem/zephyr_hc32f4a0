---
id: learning.zephyr-docs.api-lifecycle-capability-topic-reference.page-22
title: 安全Shell（SSH）密钥生成（Keygen）的API。
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__keygen.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第22章\_安全Shell（SSH）密钥生成（Keygen）的API。

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__keygen.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

<a id="details"></a>

自 4.5 版提供（Since 4.5）；接口版本（Version）0.1.0。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 22.1\_枚举（Enumerations）

<a id="r_ga233f6b99069e88b2fd16dd0fda0a25d2"></a>

```c
enum ssh_host_key_type { SSH_HOST_KEY_TYPE_RSA }
```

相关声明：[ssh_host_key_type](#ga233f6b99069e88b2fd16dd0fda0a25d2)、[SSH_HOST_KEY_TYPE_RSA](#gga233f6b99069e88b2fd16dd0fda0a25d2a1215ac3bb911207c3e31e7935a341a0a)。

可生成的主机密钥（host keys）类型。

<a id="r_ga527dec6fda5f6d56214f12d708c1b5d4"></a>

```c
enum ssh_host_key_format { SSH_HOST_KEY_FORMAT_DER , SSH_HOST_KEY_FORMAT_PEM }
```

相关声明：[ssh_host_key_format](#ga527dec6fda5f6d56214f12d708c1b5d4)、[SSH_HOST_KEY_FORMAT_DER](#gga527dec6fda5f6d56214f12d708c1b5d4ac14e3b8241a8da8d555144c38e889cfc)、[SSH_HOST_KEY_FORMAT_PEM](#gga527dec6fda5f6d56214f12d708c1b5d4ac84b189d99a0ad42c97a0125e4662d92)。

SSH 主机密钥可导出／导入的格式。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 22.2\_函数（Functions）

<a id="r_ga2a7b4b68a5ac02a60f92d4f05f6adcd6"></a>

```c
int ssh_keygen (int key_index, enum ssh_host_key_type key_type, size_t key_size_bits)
```

相关声明：[ssh_keygen](#ga2a7b4b68a5ac02a60f92d4f05f6adcd6)、[ssh_host_key_type](#ga233f6b99069e88b2fd16dd0fda0a25d2)。

生成新的 SSH 主机密钥。

<a id="r_ga04750b02826f13fe5b2e5f18b00502eb"></a>

```c
int ssh_keygen_export (int key_index, bool private_key, enum ssh_host_key_format fmt, void *buf, size_t buf_len)
```

相关声明：[ssh_keygen_export](#ga04750b02826f13fe5b2e5f18b00502eb)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[ssh_host_key_format](#ga527dec6fda5f6d56214f12d708c1b5d4)。

导出已生成的 SSH 主机密钥。

<a id="r_ga7447ca57ca8a3ff9a2f7dd024cfe338e"></a>

```c
int ssh_keygen_import (int key_index, bool private_key, enum ssh_host_key_format fmt, const void *buf, size_t buf_len)
```

相关声明：[ssh_keygen_import](#ga7447ca57ca8a3ff9a2f7dd024cfe338e)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[ssh_host_key_format](#ga527dec6fda5f6d56214f12d708c1b5d4)。

导入 SSH 主机密钥。

<a id="r_gac37edb233d0cf4c3ea3a07d89e26dbdc"></a>

```c
int ssh_keygen_free (int key_index)
```

相关声明：[ssh_keygen_free](#gac37edb233d0cf4c3ea3a07d89e26dbdc)。

释放已生成的 SSH 主机密钥。

## 22.3\_详细说明（Detailed Documentation）

<a id="ga527dec6fda5f6d56214f12d708c1b5d4"></a>

### `ssh_host_key_format`

```c
enum ssh_host_key_format
```

```c
#include <zephyr/net/ssh/keygen.h>
```

SSH 主机密钥可导出／导入的格式。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `SSH_HOST_KEY_FORMAT_DER` | DER 格式（Format）。 |
| `SSH_HOST_KEY_FORMAT_PEM` | PEM 格式（Format）。 |

<a id="ga233f6b99069e88b2fd16dd0fda0a25d2"></a>

### `ssh_host_key_type`

```c
enum ssh_host_key_type
```

```c
#include <zephyr/net/ssh/keygen.h>
```

可生成的主机密钥（host keys）类型。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `SSH_HOST_KEY_TYPE_RSA` | RSA 主机密钥类型（Host Key Type）。 |

<a id="ga2a7b4b68a5ac02a60f92d4f05f6adcd6"></a>

### `ssh_keygen()`

```c
int ssh_keygen ( int key_index, enum ssh_host_key_type key_type, size_t key_size_bits )
```

```c
#include <zephyr/net/ssh/keygen.h>
```

生成新的 SSH 主机密钥。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `key_index` | 要生成的密钥索引（Key Index），必须在 `0` 到 `CONFIG_SSH_MAX_HOST_KEYS - 1` 之间。 |
| `key_type` | 要生成的密钥类型（Key Type）。 |
| `key_size_bits` | 要生成的密钥大小（Key Size），单位为位。RSA 密钥必须至少为 2048 位。 |

返回（Returns）：成功时为0，失败时为负错误码。

<a id="ga04750b02826f13fe5b2e5f18b00502eb"></a>

### `ssh_keygen_export()`

```c
int ssh_keygen_export ( int key_index, bool private_key, enum ssh_host_key_format fmt, void * buf, size_t buf_len )
```

```c
#include <zephyr/net/ssh/keygen.h>
```

导出已生成的 SSH 主机密钥。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `key_index` | 要导出的密钥索引（Key Index），必须在 `0` 到 `CONFIG_SSH_MAX_HOST_KEYS - 1` 之间。 |
| `private_key` | 导出私钥（Private Key，`true`）还是公钥（Public Key，`false`）。 |
| `fmt` | 导出密钥使用的格式（Format）。 |
| `buf` | 用于写入导出密钥（Exported Key）的缓冲区。 |
| `buf_len` | 缓冲区长度（Buffer Length），单位为字节。 |

**返回（Returns）**：**返回值（Returns）：**成功返回写入缓冲区的字节数；失败返回负错误码（Negative Error Code）。

<a id="gac37edb233d0cf4c3ea3a07d89e26dbdc"></a>

### `ssh_keygen_free()`

```c
int ssh_keygen_free ( int key_index)
```

```c
#include <zephyr/net/ssh/keygen.h>
```

释放已生成的 SSH 主机密钥。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `key_index` | 要释放的密钥索引（Key Index），必须在 `0` 到 `CONFIG_SSH_MAX_HOST_KEYS - 1` 之间。 |

返回（Returns）：成功时为0，失败时为负错误码。

<a id="ga7447ca57ca8a3ff9a2f7dd024cfe338e"></a>

### `ssh_keygen_import()`

```c
int ssh_keygen_import ( int key_index, bool private_key, enum ssh_host_key_format fmt, const void * buf, size_t buf_len )
```

```c
#include <zephyr/net/ssh/keygen.h>
```

导入 SSH 主机密钥。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `key_index` | 要导入的密钥索引（Key Index），必须在 `0` 到 `CONFIG_SSH_MAX_HOST_KEYS - 1` 之间。 |
| `private_key` | 导入的是私钥（Private Key，`true`）还是公钥（Public Key，`false`）。 |
| `fmt` | 密钥当前采用的格式（Format）。 |
| `buf` | 包含要导入密钥（Key to Import）的缓冲区。 |
| `buf_len` | 缓冲区长度（Buffer Length），单位为字节。 |

返回（Returns）：成功时为0，失败时为负错误码。


## 22.4\_原页交叉引用（Cross References）

- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [zephyr/net/ssh/keygen.h](../api_file_management_reference/P025_zephyr__net__ssh__keygen.h_文件参考.md)

<a id="header-details"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="gga527dec6fda5f6d56214f12d708c1b5d4ac14e3b8241a8da8d555144c38e889cfc"></a>
<a id="gga527dec6fda5f6d56214f12d708c1b5d4ac84b189d99a0ad42c97a0125e4662d92"></a>
<a id="gga233f6b99069e88b2fd16dd0fda0a25d2a1215ac3bb911207c3e31e7935a341a0a"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P021_安全外壳（SSH）客户端库.md) · [返回大纲](大纲.md) · [下一章](P023_ST87Mxx API主题.md)
