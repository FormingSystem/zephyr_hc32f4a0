---
id: learning.zephyr-docs.api-file-configuration-reference.page-36
title: zephyr__bluetooth__hci_raw.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/hci__raw_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第36章\_zephyr\_\_bluetooth\_\_hci\_raw.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/hci__raw_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

蓝牙HCI原始通道（RAW Channel）的处理。

<a id="details"></a>

```c
#include <stdint.h>
#include <stddef.h>
#include <zephyr/kernel.h>
#include <zephyr/net_buf.h>
```

查看此文件的源码。

蓝牙HCI原始通道（RAW Channel）的处理。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 36.1\_函数（Functions）

<a id="r_ga8de934e01eb9a16a3c9d096151e58313"></a>

```c
int bt_send (struct net_buf *buf)
```

相关声明：[bt_send](https://docs.zephyrproject.org/latest/doxygen/html/group__hci__raw.html#ga8de934e01eb9a16a3c9d096151e58313)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

向蓝牙控制器（Bluetooth Controller）发送数据包（Packet）。

<a id="r_gaae30308fe69b1b2fd2972dbcd5a34d9f"></a>

```c
int bt_enable_raw (struct k_fifo *rx_queue)
```

相关声明：[bt_enable_raw](https://docs.zephyrproject.org/latest/doxygen/html/group__hci__raw.html#gaae30308fe69b1b2fd2972dbcd5a34d9f)、[k_fifo](../queue_reference/P004_内核FIFO结构.md)。

启用蓝牙原始通道（Bluetooth RAW Channel）：


## 36.2\_原页交叉引用（Cross References）

- [stdint.h](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h_source.html)
- [zephyr/kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h_source.html)
- [zephyr/net_buf.h](https://docs.zephyrproject.org/latest/doxygen/html/net__buf_8h_source.html)
- [查看此文件的源码。](../api_source_reference/P312_hci_raw.h_源码浏览.md)
- [bt_send](https://docs.zephyrproject.org/latest/doxygen/html/group__hci__raw.html#ga8de934e01eb9a16a3c9d096151e58313)
- [net_buf](../network_core_model_reference/P046_net_buf_结构体.md)
- [bt_enable_raw](https://docs.zephyrproject.org/latest/doxygen/html/group__hci__raw.html#gaae30308fe69b1b2fd2972dbcd5a34d9f)
- [k_fifo](../queue_reference/P004_内核FIFO结构.md)

<a id="header-details"></a>

---

[上一章](P035_zephyr__mgmt__mcumgr__mgmt__handlers.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P037_zephyr__net__prometheus__histogram.h_文件参考.md)
