---
id: learning.zephyr-docs.api-source-reference.page-310
title: hci_nxp_setup.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/hci__nxp__setup_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第310章\_hci\_nxp\_setup.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/hci__nxp__setup_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/hci__nxp__setup_8h.html)。

## 310.1\_原始可见代码（Source Code）

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
<a id="l00013"></a>
<a id="l00014"></a>
<a id="l00015"></a>
<a id="l00069"></a>
<a id="l00070"></a>
<a id="l00071"></a>
<a id="adevice_8h_html"></a>
<a id="ahci__nxp__setup_8h_html_ab07ac59e57ce5a1c59aa6f5c07c6bd73"></a>
<a id="astructdevice_html"></a>

```c


/*
 * Copyright 2026 NXP
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_ZEPHYR_DRIVERS_BLUETOOTH_HCI_NXP_SETUP_H_
#define ZEPHYR_INCLUDE_ZEPHYR_DRIVERS_BLUETOOTH_HCI_NXP_SETUP_H_

#include <zephyr/device.h>

int bt_nxp_trigger_ir(const struct device *dev);

#endif /* ZEPHYR_INCLUDE_ZEPHYR_DRIVERS_BLUETOOTH_HCI_NXP_SETUP_H_ */
```

## 310.2\_可见注释译文（Comments）

### 注释 1：原第 5 行

版权（Copyright）：2026 NXP。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 71 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_ZEPHYR_DRIVERS_BLUETOOTH_HCI_NXP_SETUP_H_`。

## 310.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/hci__nxp__setup_8h.html)
- [zephyr/device.h](../device_reference/P007_设备模型头文件参考.md)
- [bt_nxp_trigger_ir](https://docs.zephyrproject.org/latest/doxygen/html/hci__nxp__setup_8h.html#ab07ac59e57ce5a1c59aa6f5c07c6bd73)
- [device](../device_reference/P002_设备对象结构.md)
- [device.h](../device_reference/P007_设备模型头文件参考.md)

---

[上一章](P309_hci_lockstep.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P311_hci_pkt.h_源码浏览.md)
