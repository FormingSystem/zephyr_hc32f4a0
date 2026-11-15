---
id: learning.zephyr-docs.api-file-network-device-reference.page-37
title: zephyr__net__socketutils.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/socketutils_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第37章\_zephyr\_\_net\_\_socketutils.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/socketutils_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

套接字工具函数（Socket Utility Functions）。

<a id="details"></a>

```c
#include <zephyr/net/socket.h>
```

查看此文件的源码。

套接字工具函数（Socket Utility Functions）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 37.1\_函数（Functions）

<a id="r_aae0889a4a96fd9763e3f5337b4703205"></a>

```c
const char * net_addr_str_find_port (const char *addr_str)
```

相关声明：[net_addr_str_find_port](#aae0889a4a96fd9763e3f5337b4703205)。

在 `addr:port` 字符串中查找端口（Port）。

<a id="r_ab60f526101571078d9b24055f130b1a0"></a>

```c
int net_getaddrinfo_addr_str (const char *addr_str, const char *def_port, const struct zsock_addrinfo *hints, struct zsock_addrinfo **res)
```

相关声明：[net_getaddrinfo_addr_str](#ab60f526101571078d9b24055f130b1a0)、[zsock_addrinfo](../posix_system_model_reference/P029_zsock_addrinfo_结构体.md)、[zsock_addrinfo](../posix_system_model_reference/P029_zsock_addrinfo_结构体.md)。

对 `addr:port` 字符串调用 `getaddrinfo()`。

## 37.2\_详细说明（Detailed Documentation）

<a id="aae0889a4a96fd9763e3f5337b4703205"></a>

### `net_addr_str_find_port()`

```c
const char * net_addr_str_find_port ( const char * addr_str)
```

在 `addr:port` 字符串中查找端口（Port）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `addr_str` | 格式为 `addr[:port]` 的字符串。 |

**返回（Returns）**：**返回值（Returns）：**指向端口（`port`）部分的指针；若不存在则为 `NULL`。

<a id="ab60f526101571078d9b24055f130b1a0"></a>

### `net_getaddrinfo_addr_str()`

```c
int net_getaddrinfo_addr_str ( const char * addr_str, const char * def_port, const struct zsock_addrinfo * hints, struct zsock_addrinfo ** res )
```

对 `addr:port` 字符串调用 `getaddrinfo()`。

便捷函数：将 `addr[:port]` 字符串拆分为地址和端口部分，必要时使用默认端口号，再对拆分结果调用 `getaddrinfo()`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `addr_str` | 格式为 `addr[:port]` 的字符串。 |
| `def_port` | `addr_str` 中不包含端口时使用的默认端口号（Default Port Number）。 |
| `hints` | `getaddrinfo()` 的提示参数（Hints）。 |
| `res` | `getaddrinfo()` 的结果，应照常对其调用 `freeaddrinfo()`。 |

**返回（Returns）**：**返回值（Returns）：**`getaddrinfo()` 调用的结果。


## 37.3\_原页交叉引用（Cross References）

- [zephyr/net/socket.h](../api_source_socket_ethernet_reference/P006_socket.h_源码浏览.md)
- [查看此文件的源码。](../api_source_reference/P804_socketutils.h_源码浏览.md)
- [zsock_addrinfo](../posix_system_model_reference/P029_zsock_addrinfo_结构体.md)
- [getaddrinfo()](../api_file_supplement_reference/P079_zephyr__posix__netdb.h_文件参考.md#adc9ea491d9008de7cd9e0a5b9147ca70)
- [freeaddrinfo()](../api_file_supplement_reference/P079_zephyr__posix__netdb.h_文件参考.md#ae854ec9955d62f1791342f9c2b8abcee)

<a id="header-details"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P036_zephyr__net__socketcan.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P038_zephyr__dt-bindings__pinctrl__stm32-pinctrl.h_文件参考.md)
