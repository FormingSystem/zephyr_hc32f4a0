---
id: learning.zephyr-docs.api-source-reference.page-879
title: uart_bridge.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/uart__bridge_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第879章\_uart\_bridge.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/uart__bridge_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](../hardware/P358_UART桥接接口.md)。

## 879.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00007"></a>
<a id="l00008"></a>
<a id="l00009"></a>
<a id="l00010"></a>
<a id="l00011"></a>
<a id="l00012"></a>
<a id="l00022"></a>
<a id="l00023"></a>
<a id="l00024"></a>
<a id="l00025"></a>
<a id="l00026"></a>
<a id="l00027"></a>
<a id="adevice_8h_html"></a>
<a id="astructdevice_html"></a>
<a id="auart__bridge_8h_html_a05e43f34092fbbe84c868e6ec8966313"></a>

```c
/*
 * Copyright 2025 Google LLC
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#include <zephyr/device.h>

#ifdef __cplusplus
extern "C" {
#endif

void uart_bridge_settings_update(const struct device *dev,
                                 const struct device *bridge_dev);

#ifdef __cplusplus
}
#endif
```

## 879.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：2025 Google LLC。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

## 879.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](../hardware/P358_UART桥接接口.md)
- [zephyr/device.h](../device_reference/P007_设备模型头文件参考.md)
- [uart_bridge_settings_update](https://docs.zephyrproject.org/latest/doxygen/html/uart__bridge_8h.html#a05e43f34092fbbe84c868e6ec8966313)
- [device](../device_reference/P002_设备对象结构.md)
- [device.h](../device_reference/P007_设备模型头文件参考.md)

---

[上一章](P878_uaol.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P880_uart_emul.h_源码浏览.md)
