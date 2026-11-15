---
id: learning.zephyr-docs.api-source-reference.page-312
title: hci_raw.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/hci__raw_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第312章\_hci\_raw.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/hci__raw_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/hci__raw_8h.html)。

## 312.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00007"></a>
<a id="l00008"></a>
<a id="l00009"></a>
<a id="l00010"></a>
<a id="l00011"></a>
<a id="l00012"></a>
<a id="l00021"></a>
<a id="l00022"></a>
<a id="l00023"></a>
<a id="l00024"></a>
<a id="l00025"></a>
<a id="l00026"></a>
<a id="l00027"></a>
<a id="l00028"></a>
<a id="l00029"></a>
<a id="l00030"></a>
<a id="l00031"></a>
<a id="l00041"></a>
<a id="l00042"></a>
<a id="l00053"></a>
<a id="l00054"></a>
<a id="l00055"></a>
<a id="l00056"></a>
<a id="l00057"></a>
<a id="l00061"></a>
<a id="l00062"></a>
<a id="agroup__hci__raw_html_ga8de934e01eb9a16a3c9d096151e58313"></a>
<a id="agroup__hci__raw_html_gaae30308fe69b1b2fd2972dbcd5a34d9f"></a>
<a id="akernel_8h_html"></a>
<a id="anet__buf_8h_html"></a>
<a id="astdint_8h_html"></a>
<a id="astructk__fifo_html"></a>
<a id="astructnet__buf_html"></a>

```c


/*
 * Copyright (c) 2016 Intel Corporation
 *
 * SPDX-License-Identifier: Apache-2.0
 */
#ifndef ZEPHYR_INCLUDE_BLUETOOTH_HCI_RAW_H_
#define ZEPHYR_INCLUDE_BLUETOOTH_HCI_RAW_H_


#include <stdint.h>
#include <stddef.h>

#include <zephyr/kernel.h>
#include <zephyr/net_buf.h>

#ifdef __cplusplus
extern "C" {
#endif

int bt_send(struct net_buf *buf);

int bt_enable_raw(struct k_fifo *rx_queue);

#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_BLUETOOTH_HCI_RAW_H_ */
```

## 312.2\_可见注释译文（Comments）

### 注释 1：原第 5 行

版权（Copyright）：© 2016 Intel Corporation。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 62 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_BLUETOOTH_HCI_RAW_H_`。

## 312.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/hci__raw_8h.html)
- [stdint.h](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html)
- [zephyr/kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [zephyr/net_buf.h](https://docs.zephyrproject.org/latest/doxygen/html/net__buf_8h.html)
- [bt_send](https://docs.zephyrproject.org/latest/doxygen/html/group__hci__raw.html#ga8de934e01eb9a16a3c9d096151e58313)
- [net_buf](../network_core_model_reference/P046_net_buf_结构体.md)
- [bt_enable_raw](https://docs.zephyrproject.org/latest/doxygen/html/group__hci__raw.html#gaae30308fe69b1b2fd2972dbcd5a34d9f)
- [k_fifo](../queue_reference/P004_内核FIFO结构.md)
- [kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [net_buf.h](https://docs.zephyrproject.org/latest/doxygen/html/net__buf_8h.html)

---

[上一章](P311_hci_pkt.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P313_hdr_ddr.h_源码浏览.md)
