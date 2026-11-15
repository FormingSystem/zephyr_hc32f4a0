---
id: learning.zephyr-docs.api-file-reference.page-228
title: zephyr__modem__backend__tty.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/modem_2backend_2tty_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第228章\_zephyr\_\_modem\_\_backend\_\_tty.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/modem_2backend_2tty_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/kernel.h>
#include <zephyr/types.h>
#include <zephyr/device.h>
#include <zephyr/sys/ring_buffer.h>
#include <zephyr/sys/atomic.h>
#include <zephyr/modem/pipe.h>
```

查看此文件的源码。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 228.1\_数据结构（Data Structures）

<a id="r_modem_5Fbackend_5Ftty"></a>

```c
struct modem_backend_tty
```

相关声明：[modem_backend_tty](../modem_wireless_model_reference/P041_modem_backend_tty_结构体.md)。

<a id="r_modem_5Fbackend_5Ftty_5Fconfig"></a>

```c
struct modem_backend_tty_config
```

相关声明：[modem_backend_tty_config](../modem_wireless_model_reference/P042_modem_backend_tty_config_结构体.md)。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 228.2\_函数（Functions）

<a id="r_a507f79d94144e3e4a75ec7fed1501f80"></a>

```c
struct modem_pipe * modem_backend_tty_init (struct modem_backend_tty *backend, const struct modem_backend_tty_config *config)
```

相关声明：[modem_backend_tty_init](#a507f79d94144e3e4a75ec7fed1501f80)、[modem_backend_tty](../modem_wireless_model_reference/P041_modem_backend_tty_结构体.md)、[modem_backend_tty_config](../modem_wireless_model_reference/P042_modem_backend_tty_config_结构体.md)。

## 228.3\_详细说明（Detailed Documentation）

<a id="a507f79d94144e3e4a75ec7fed1501f80"></a>

### `modem_backend_tty_init()`

```c
struct modem_pipe * modem_backend_tty_init ( struct modem_backend_tty * backend, const struct modem_backend_tty_config * config )
```


## 228.4\_原页交叉引用（Cross References）

- [zephyr/kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h_source.html)
- [zephyr/types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2types_8h_source.html)
- [zephyr/device.h](../device_reference/P008_设备模型头文件源码.md)
- [zephyr/sys/ring_buffer.h](../ringbuffer_reference/P004_环形缓冲区头文件源码.md)
- [zephyr/sys/atomic.h](../atomic_reference/P003_原子操作公共头文件源码.md)
- [zephyr/modem/pipe.h](../api_source_supplement_reference/P145_pipe.h_源码浏览.md)
- [查看此文件的源码。](../api_source_reference/P538_tty.h_源码浏览.md)
- [modem_backend_tty](../modem_wireless_model_reference/P041_modem_backend_tty_结构体.md)
- [modem_backend_tty_config](../modem_wireless_model_reference/P042_modem_backend_tty_config_结构体.md)

<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P227_zephyr__posix__sys__mman.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P229_zephyr__modem__backend__uart.h_文件参考.md)
