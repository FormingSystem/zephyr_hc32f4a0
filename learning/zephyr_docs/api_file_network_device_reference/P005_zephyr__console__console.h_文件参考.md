---
id: learning.zephyr-docs.api-file-network-device-reference.page-5
title: zephyr__console__console.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/console_2console_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第5章\_zephyr\_\_console\_\_console.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/console_2console_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <sys/types.h>
#include <zephyr/types.h>
#include <zephyr/kernel.h>
```

查看此文件的源码。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 5.1\_函数（Functions）

<a id="r_ga0bf949437e32d17992435003cf8b46b5"></a>

```c
int console_init (void)
```

相关声明：[console_init](https://docs.zephyrproject.org/latest/doxygen/html/group__console__api.html#ga0bf949437e32d17992435003cf8b46b5)。

初始化控制台设备（Console Device）。

<a id="r_ga27785534c14d4098822db2b870b7d81d"></a>

```c
ssize_t console_read (void *dummy, void *buf, size_t size)
```

相关声明：[ssize_t](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a5c5d83d87790efd59ea916c2b99f9118)、[console_read](https://docs.zephyrproject.org/latest/doxygen/html/group__console__api.html#ga27785534c14d4098822db2b870b7d81d)。

从控制台（Console）读取数据。

<a id="r_ga204fd795daf9ef6b1f2803547747545e"></a>

```c
ssize_t console_write (void *dummy, const void *buf, size_t size)
```

相关声明：[ssize_t](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a5c5d83d87790efd59ea916c2b99f9118)、[console_write](https://docs.zephyrproject.org/latest/doxygen/html/group__console__api.html#ga204fd795daf9ef6b1f2803547747545e)。

向控制台（Console）写入数据。

<a id="r_ga2ba36eb1081cd0b98aa43216ccd6fbd5"></a>

```c
int console_getchar (void)
```

相关声明：[console_getchar](https://docs.zephyrproject.org/latest/doxygen/html/group__console__api.html#ga2ba36eb1081cd0b98aa43216ccd6fbd5)。

从控制台输入缓冲区（Input Buffer）获取下一个字符。

<a id="r_ga7bd842f1cda6c8218cb1d41420e4de49"></a>

```c
int console_putchar (char c)
```

相关声明：[console_putchar](https://docs.zephyrproject.org/latest/doxygen/html/group__console__api.html#ga7bd842f1cda6c8218cb1d41420e4de49)。

向控制台输出一个字符，使用缓冲（Buffered）。

<a id="r_gacd13267df8567c63f2285ce0e1cbbc20"></a>

```c
void console_getline_init (void)
```

相关声明：[console_getline_init](https://docs.zephyrproject.org/latest/doxygen/html/group__console__api.html#gacd13267df8567c63f2285ce0e1cbbc20)。

初始化 `console_getline()` 调用所需的状态。

<a id="r_ga3454f5b84d38d46a6c2bbf7fd6baa815"></a>

```c
char * console_getline (void)
```

相关声明：[console_getline](https://docs.zephyrproject.org/latest/doxygen/html/group__console__api.html#ga3454f5b84d38d46a6c2bbf7fd6baa815)。

从控制台输入缓冲区获取下一行（Next Line）。

<a id="r_ga83d86a81638a96ae84df792265dc0219"></a>

```c
void console_set_rx_timeout (k_timeout_t timeout)
```

相关声明：[console_set_rx_timeout](https://docs.zephyrproject.org/latest/doxygen/html/group__console__api.html#ga83d86a81638a96ae84df792265dc0219)、[k_timeout_t](../timer_reference/P087_内核超时类型.md)。

设置控制台操作的接收超时（Receive Timeout）。

<a id="r_ga401af68bb10c5b5e2a99997cee7de9c7"></a>

```c
void console_set_tx_timeout (k_timeout_t timeout)
```

相关声明：[console_set_tx_timeout](https://docs.zephyrproject.org/latest/doxygen/html/group__console__api.html#ga401af68bb10c5b5e2a99997cee7de9c7)、[k_timeout_t](../timer_reference/P087_内核超时类型.md)。

设置控制台操作的发送超时（Transmit Timeout）。


## 5.2\_原页交叉引用（Cross References）

- [sys/types.h](../api_source_runtime_reference/P038_types.h_源码浏览.md)
- [zephyr/types.h](../api_source_compiler_device_reference/P014_types.h_源码浏览.md)
- [zephyr/kernel.h](../api_source_workqueue_pin_control_reference/P002_kernel.h_源码浏览.md)
- [查看此文件的源码。](../api_source_reference/P115_console.h_源码浏览.md)
- [console_init](https://docs.zephyrproject.org/latest/doxygen/html/group__console__api.html#ga0bf949437e32d17992435003cf8b46b5)
- [ssize_t](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a5c5d83d87790efd59ea916c2b99f9118)
- [console_read](https://docs.zephyrproject.org/latest/doxygen/html/group__console__api.html#ga27785534c14d4098822db2b870b7d81d)
- [console_write](https://docs.zephyrproject.org/latest/doxygen/html/group__console__api.html#ga204fd795daf9ef6b1f2803547747545e)
- [console_getchar](https://docs.zephyrproject.org/latest/doxygen/html/group__console__api.html#ga2ba36eb1081cd0b98aa43216ccd6fbd5)
- [console_putchar](https://docs.zephyrproject.org/latest/doxygen/html/group__console__api.html#ga7bd842f1cda6c8218cb1d41420e4de49)
- [console_getline_init](https://docs.zephyrproject.org/latest/doxygen/html/group__console__api.html#gacd13267df8567c63f2285ce0e1cbbc20)
- [console_getline()](https://docs.zephyrproject.org/latest/doxygen/html/group__console__api.html#ga3454f5b84d38d46a6c2bbf7fd6baa815)
- [console_set_rx_timeout](https://docs.zephyrproject.org/latest/doxygen/html/group__console__api.html#ga83d86a81638a96ae84df792265dc0219)
- [k_timeout_t](../timer_reference/P087_内核超时类型.md)
- [console_set_tx_timeout](https://docs.zephyrproject.org/latest/doxygen/html/group__console__api.html#ga401af68bb10c5b5e2a99997cee7de9c7)

---

[上一章](P004_zephyr__net__conn_mgr_connectivity_impl.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P006_zephyr__drivers__emul.h_文件参考.md)
