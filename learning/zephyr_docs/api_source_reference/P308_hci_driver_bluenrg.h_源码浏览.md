---
id: learning.zephyr-docs.api-source-reference.page-308
title: hci_driver_bluenrg.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/hci__driver__bluenrg_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第308章\_hci\_driver\_bluenrg.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/hci__driver__bluenrg_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/hci__driver__bluenrg_8h.html)。

## 308.1\_原始可见代码（Source Code）

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
<a id="l00019"></a>
<a id="l00020"></a>
<a id="l00021"></a>
<a id="l00022"></a>
<a id="l00023"></a>
<a id="l00024"></a>
<a id="l00025"></a>
<a id="l00036"></a>
<a id="l00037"></a>
<a id="l00038"></a>
<a id="l00039"></a>
<a id="l00040"></a>
<a id="l00041"></a>
<a id="l00042"></a>
<a id="l00046"></a>
<a id="l00047"></a>
<a id="agroup__bluenrg__hci__driver_html_gaa76b4af2fc2076deaeeb845514475483"></a>
<a id="astdbool_8h_html"></a>

```c


/*
 * Copyright (c) 2024 STMicroelectronics
 *
 * SPDX-License-Identifier: Apache-2.0
 */
#ifndef ZEPHYR_INCLUDE_DRIVERS_BLUETOOTH_HCI_DRIVER_BLUENRG_H_
#define ZEPHYR_INCLUDE_DRIVERS_BLUETOOTH_HCI_DRIVER_BLUENRG_H_


#include <stdbool.h>

#ifdef __cplusplus
extern "C" {
#endif


int bluenrg_bt_reset(bool updater_mode);

#ifdef __cplusplus
}
#endif


#endif /* ZEPHYR_INCLUDE_DRIVERS_BLUETOOTH_HCI_DRIVER_BLUENRG_H_ */
```

## 308.2\_可见注释译文（Comments）

### 注释 1：原第 5 行

版权（Copyright）：© 2024 STMicroelectronics。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 47 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DRIVERS_BLUETOOTH_HCI_DRIVER_BLUENRG_H_`。

## 308.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/hci__driver__bluenrg_8h.html)
- [stdbool.h](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html)
- [bluenrg_bt_reset](https://docs.zephyrproject.org/latest/doxygen/html/group__bluenrg__hci__driver.html#gaa76b4af2fc2076deaeeb845514475483)

---

[上一章](P307_hawkbit.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P309_hci_lockstep.h_源码浏览.md)
