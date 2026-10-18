---
id: learning.zephyr-docs.api-file-service-reference.page-1
title: zephyr__mgmt__hawkbit__autohandler.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/autohandler_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第1章\_zephyr\_\_mgmt\_\_hawkbit\_\_autohandler.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/autohandler_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

hawkBit自动处理程序（Autohandler）的头文件。

<a id="details"></a>

```c
#include <zephyr/mgmt/hawkbit/hawkbit.h>
```

查看此文件的源码。

hawkBit自动处理程序（Autohandler）的头文件。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 1.1\_函数（Functions）

<a id="r_ga41865255aa3020a34816c23ae7977f20"></a>

```c
void hawkbit_autohandler (bool auto_reschedule)
```

相关声明：[hawkbit_autohandler](https://docs.zephyrproject.org/latest/doxygen/html/group__hawkbit__autohandler.html#ga41865255aa3020a34816c23ae7977f20)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

自动运行 hawkBit 探测（Probe）和 hawkBit 更新（Update）。

<a id="r_ga6d13b3d7b9a61d06a6eaa346189a08c6"></a>

```c
enum hawkbit_response hawkbit_autohandler_wait (uint32_t events, k_timeout_t timeout)
```

相关声明：[hawkbit_response](https://docs.zephyrproject.org/latest/doxygen/html/group__hawkbit.html#ga96c59c754178451d8dbd08b32813220b)、[hawkbit_autohandler_wait](https://docs.zephyrproject.org/latest/doxygen/html/group__hawkbit__autohandler.html#ga6d13b3d7b9a61d06a6eaa346189a08c6)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[k_timeout_t](../timer_reference/P087_内核超时类型.md)。

等待自动处理器（Autohandler）完成。

<a id="r_gabc27308bb974d6e0b9650476243e5e9a"></a>

```c
int hawkbit_autohandler_cancel (void)
```

相关声明：[hawkbit_autohandler_cancel](https://docs.zephyrproject.org/latest/doxygen/html/group__hawkbit__autohandler.html#gabc27308bb974d6e0b9650476243e5e9a)。

取消 hawkBit 自动处理器（Autohandler）的运行。

<a id="r_ga47fe3e9cd227fd4da332e9eeff81f991"></a>

```c
int hawkbit_autohandler_set_delay (k_timeout_t timeout, bool if_bigger)
```

相关声明：[hawkbit_autohandler_set_delay](https://docs.zephyrproject.org/latest/doxygen/html/group__hawkbit__autohandler.html#ga47fe3e9cd227fd4da332e9eeff81f991)、[k_timeout_t](../timer_reference/P087_内核超时类型.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

设置自动处理器（Autohandler）下次运行前的延迟（Delay）。


## 1.2\_原页交叉引用（Cross References）

- [zephyr/mgmt/hawkbit/hawkbit.h](../api_source_reference/P307_hawkbit.h_源码浏览.md)
- [查看此文件的源码。](../api_source_reference/P046_autohandler.h_源码浏览.md)
- [hawkbit_autohandler](https://docs.zephyrproject.org/latest/doxygen/html/group__hawkbit__autohandler.html#ga41865255aa3020a34816c23ae7977f20)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [hawkbit_response](https://docs.zephyrproject.org/latest/doxygen/html/group__hawkbit.html#ga96c59c754178451d8dbd08b32813220b)
- [hawkbit_autohandler_wait](https://docs.zephyrproject.org/latest/doxygen/html/group__hawkbit__autohandler.html#ga6d13b3d7b9a61d06a6eaa346189a08c6)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [k_timeout_t](../timer_reference/P087_内核超时类型.md)
- [hawkbit_autohandler_cancel](https://docs.zephyrproject.org/latest/doxygen/html/group__hawkbit__autohandler.html#gabc27308bb974d6e0b9650476243e5e9a)
- [hawkbit_autohandler_set_delay](https://docs.zephyrproject.org/latest/doxygen/html/group__hawkbit__autohandler.html#ga47fe3e9cd227fd4da332e9eeff81f991)

<a id="header-details"></a>

---

[返回大纲](大纲.md) · [下一章](P002_zephyr__llext__buf_loader.h_文件参考.md)
