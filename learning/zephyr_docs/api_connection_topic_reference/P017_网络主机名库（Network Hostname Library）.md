---
id: learning.zephyr-docs.api-connection-topic-reference.page-17
title: 网络主机名库（Network Hostname Library）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__net__hostname.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第17章\_网络主机名库（Network Hostname Library）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__net__hostname.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

网络主机名配置库。

<a id="details"></a>

网络主机名配置库（Network hostname configuration library）。自 Zephyr 1.10 起提供；API 版本为 0.8.0。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 17.1\_宏定义（Macros）

<a id="r_ga9dda37a09616f2eb1bcdcb76cd868a0f"></a>

```c
#define NET_HOSTNAME_MAX_LEN
```

相关声明：[NET_HOSTNAME_MAX_LEN](#ga9dda37a09616f2eb1bcdcb76cd868a0f)。

主机名最大长度（maximum hostname length）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 17.2\_函数（Functions）

<a id="r_ga8870e80f16f934d1d8a86ea6bddbaf0b"></a>

```c
static const char * net_hostname_get (void)
```

相关声明：[net_hostname_get](#ga8870e80f16f934d1d8a86ea6bddbaf0b)。

获取设备主机名（hostname）。

<a id="r_gad15b0b79870f9ae9e295808bc58d8cef"></a>

```c
static int net_hostname_set (const char *host, size_t len)
```

相关声明：[net_hostname_set](#gad15b0b79870f9ae9e295808bc58d8cef)。

设置设备主机名。

<a id="r_ga96adbfaa629b6d450f06e19678eba9bc"></a>

```c
static void net_hostname_init (void)
```

相关声明：[net_hostname_init](#ga96adbfaa629b6d450f06e19678eba9bc)。

初始化并设置设备主机名。

<a id="r_ga6aa3799b3b0d7eec7fb8b276485ae2c5"></a>

```c
static int net_hostname_set_postfix (const uint8_t *hostname_postfix, int postfix_len)
```

相关声明：[net_hostname_set_postfix](#ga6aa3799b3b0d7eec7fb8b276485ae2c5)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

设置设备主机名后缀（postfix）。

<a id="r_ga2b9d6f604afcde27b6d1543495e2ba8b"></a>

```c
static int net_hostname_set_postfix_str (const uint8_t *hostname_postfix, int postfix_len)
```

相关声明：[net_hostname_set_postfix_str](#ga2b9d6f604afcde27b6d1543495e2ba8b)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

设置网络主机名的后缀字符串。

## 17.3\_详细说明（Detailed Documentation）

<a id="ga9dda37a09616f2eb1bcdcb76cd868a0f"></a>

### `NET_HOSTNAME_MAX_LEN`

```c
#define NET_HOSTNAME_MAX_LEN
```

```c
#include <zephyr/net/hostname.h>
```

展开值（Value）：

```c
(sizeof(CONFIG_NET_HOSTNAME) - 1 +                                                         \
 (IS_ENABLED(CONFIG_NET_HOSTNAME_UNIQUE) ? sizeof("0011223344556677") - 1 : 0))
```

主机名最大长度（maximum hostname length）。

<a id="ga8870e80f16f934d1d8a86ea6bddbaf0b"></a>

### `net_hostname_get()`

```c
const char * net_hostname_get ( void )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/hostname.h>
```

获取设备主机名（hostname）。

返回指向设备主机名（hostname）的指针。

**返回（Returns）**：返回值：指向主机名的指针；尚未设置时返回 `NULL`。

<a id="ga96adbfaa629b6d450f06e19678eba9bc"></a>

### `net_hostname_init()`

```c
void net_hostname_init ( void )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/hostname.h>
```

初始化并设置设备主机名。

<a id="gad15b0b79870f9ae9e295808bc58d8cef"></a>

### `net_hostname_set()`

```c
int net_hostname_set ( const char * host, size_t len )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/hostname.h>
```

设置设备主机名。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `host` | 以字符数组形式提供的新主机名。 |
| `len` | 主机名数组的长度。 |

**返回（Returns）**：返回值：成功时返回 0，出错时返回小于 0 的值。

<a id="ga6aa3799b3b0d7eec7fb8b276485ae2c5"></a>

### `net_hostname_set_postfix()`

```c
int net_hostname_set_postfix ( const uint8_t * hostname_postfix, int postfix_len )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/hostname.h>
```

设置设备主机名后缀（postfix）。

将主机名后缀（hostname postfix）转换为十六进制值，并使用转换后的值设置设备主机名。仅在设置 `CONFIG_NET_HOSTNAME_UNIQUE` 时使用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `hostname_postfix` | 通常为链路地址（link address），函数会将其转换为十六进制字符串。 |
| `postfix_len` | `hostname_postfix` 数组的长度。 |

返回（Returns）：成功时为0，出错时小于0。

<a id="ga2b9d6f604afcde27b6d1543495e2ba8b"></a>

### `net_hostname_set_postfix_str()`

```c
int net_hostname_set_postfix_str ( const uint8_t * hostname_postfix, int postfix_len )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/hostname.h>
```

设置网络主机名的后缀字符串。

将主机名后缀字符串原样设置为网络主机名的后缀，不进行转换。仅在设置 `CONFIG_NET_HOSTNAME_UNIQUE` 时使用。函数检查默认主机名（由 `CONFIG_NET_HOSTNAME` 定义）与后缀的合计长度是否超过 `NET_HOSTNAME_MAX_LEN`；后缀过长时返回错误。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `hostname_postfix` | 指向要附加到网络主机名的后缀字符串的指针。 |
| `postfix_len` | `hostname_postfix` 数组的长度。 |

返回（Returns）：成功时为0，出错时小于0。


## 17.4\_原页交叉引用（Cross References）

- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [zephyr/net/hostname.h](../api_file_management_reference/P021_zephyr__net__hostname.h_文件参考.md)
- [IS_ENABLED](../util_reference/P001_通用工具公共接口.md#ga111fe4e9d63758262fc6810a782cb32a)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="agroup__sys-util_html_ga111fe4e9d63758262fc6810a782cb32a"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P016_MSPI 传输 API（MSPI Transfer API）.md) · [返回大纲](大纲.md) · [下一章](P018_nRF 正交解码器（QDEC nRF）.md)
