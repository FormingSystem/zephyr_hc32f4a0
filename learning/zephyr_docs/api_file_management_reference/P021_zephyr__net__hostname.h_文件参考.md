---
id: learning.zephyr-docs.api-file-management-reference.page-21
title: zephyr__net__hostname.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/hostname_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第21章\_zephyr\_\_net\_\_hostname.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/hostname_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

主机名配置（Hostname Configuration）的定义。

<a id="details"></a>

```c
#include <errno.h>
#include <zephyr/sys/util.h>
#include <zephyr/toolchain.h>
```

查看此文件的源码。

主机名配置（Hostname Configuration）的定义。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 21.1\_宏定义（Macros）

<a id="r_ga9dda37a09616f2eb1bcdcb76cd868a0f"></a>

```c
#define NET_HOSTNAME_MAX_LEN
```

相关声明：[NET_HOSTNAME_MAX_LEN](https://docs.zephyrproject.org/latest/doxygen/html/group__net__hostname.html#ga9dda37a09616f2eb1bcdcb76cd868a0f)。

主机名最大长度（maximum hostname length）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 21.2\_函数（Functions）

<a id="r_ga8870e80f16f934d1d8a86ea6bddbaf0b"></a>

```c
static const char * net_hostname_get (void)
```

相关声明：[net_hostname_get](https://docs.zephyrproject.org/latest/doxygen/html/group__net__hostname.html#ga8870e80f16f934d1d8a86ea6bddbaf0b)。

获取设备主机名（hostname）。

<a id="r_gad15b0b79870f9ae9e295808bc58d8cef"></a>

```c
static int net_hostname_set (const char *host, size_t len)
```

相关声明：[net_hostname_set](https://docs.zephyrproject.org/latest/doxygen/html/group__net__hostname.html#gad15b0b79870f9ae9e295808bc58d8cef)。

设置设备主机名。

<a id="r_ga96adbfaa629b6d450f06e19678eba9bc"></a>

```c
static void net_hostname_init (void)
```

相关声明：[net_hostname_init](https://docs.zephyrproject.org/latest/doxygen/html/group__net__hostname.html#ga96adbfaa629b6d450f06e19678eba9bc)。

初始化并设置设备主机名。

<a id="r_ga6aa3799b3b0d7eec7fb8b276485ae2c5"></a>

```c
static int net_hostname_set_postfix (const uint8_t *hostname_postfix, int postfix_len)
```

相关声明：[net_hostname_set_postfix](https://docs.zephyrproject.org/latest/doxygen/html/group__net__hostname.html#ga6aa3799b3b0d7eec7fb8b276485ae2c5)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

设置设备主机名后缀（postfix）。

<a id="r_ga2b9d6f604afcde27b6d1543495e2ba8b"></a>

```c
static int net_hostname_set_postfix_str (const uint8_t *hostname_postfix, int postfix_len)
```

相关声明：[net_hostname_set_postfix_str](https://docs.zephyrproject.org/latest/doxygen/html/group__net__hostname.html#ga2b9d6f604afcde27b6d1543495e2ba8b)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

设置网络主机名的后缀字符串。


## 21.3\_原页交叉引用（Cross References）

- [errno.h](../error_reference/P005_错误号头文件源码.md)
- [zephyr/sys/util.h](../util_reference/P003_通用工具头文件源码.md)
- [zephyr/toolchain.h](../api_source_compiler_device_reference/P023_toolchain.h_源码浏览.md)
- [查看此文件的源码。](../api_source_reference/P322_hostname.h_源码浏览.md)
- [NET_HOSTNAME_MAX_LEN](https://docs.zephyrproject.org/latest/doxygen/html/group__net__hostname.html#ga9dda37a09616f2eb1bcdcb76cd868a0f)
- [net_hostname_get](https://docs.zephyrproject.org/latest/doxygen/html/group__net__hostname.html#ga8870e80f16f934d1d8a86ea6bddbaf0b)
- [net_hostname_set](https://docs.zephyrproject.org/latest/doxygen/html/group__net__hostname.html#gad15b0b79870f9ae9e295808bc58d8cef)
- [net_hostname_init](https://docs.zephyrproject.org/latest/doxygen/html/group__net__hostname.html#ga96adbfaa629b6d450f06e19678eba9bc)
- [net_hostname_set_postfix](https://docs.zephyrproject.org/latest/doxygen/html/group__net__hostname.html#ga6aa3799b3b0d7eec7fb8b276485ae2c5)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [net_hostname_set_postfix_str](https://docs.zephyrproject.org/latest/doxygen/html/group__net__hostname.html#ga2b9d6f604afcde27b6d1543495e2ba8b)

<a id="header-details"></a>

---

[上一章](P020_zephyr__sys__heap_kasan.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P022_zephyr__net__http__client.h_文件参考.md)
