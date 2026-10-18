---
id: learning.zephyr-docs.api-source-configuration-reference.page-22
title: emul_stub_device.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/emul__stub__device_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第22章\_emul\_stub\_device.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/emul__stub__device_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/emul__stub__device_8h.html)。

## 22.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00012"></a>
<a id="l00013"></a>
<a id="l00014"></a>
<a id="l00015"></a>
<a id="l00016"></a>
<a id="l00017"></a>
<a id="l00018"></a>
<a id="l00019"></a>
<a id="l00020"></a>
<a id="l00021"></a>
<a id="l00022"></a>
<a id="l00024"></a>
<a id="l00025"></a>
<a id="l00026"></a>
<a id="l00027"></a>
<a id="l00028"></a>
<a id="l00029"></a>
<a id="l00030"></a>
<a id="l00031"></a>
<a id="l00032"></a>
<a id="l00034"></a>
<a id="foldopen00043"></a>
<a id="l00043"></a>
<a id="l00044"></a>
<a id="l00045"></a>
<a id="l00046"></a>
<a id="l00047"></a>
<a id="l00048"></a>
<a id="l00049"></a>
<a id="l00050"></a>
<a id="l00051"></a>
<a id="l00052"></a>
<a id="l00053"></a>
<a id="l00054"></a>
<a id="l00055"></a>
<a id="l00056"></a>
<a id="adevice_8h_html"></a>
<a id="adevicetree_8h_html"></a>

```c
/*
 * Copyright 2023 Google LLC
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_EMUL_STUB_DEVICE_H_
#define ZEPHYR_INCLUDE_EMUL_STUB_DEVICE_H_

#include <zephyr/device.h>
#include <zephyr/devicetree.h>

/*
 * Needed for emulators without corresponding DEVICE_DT_DEFINE drivers
 */

struct emul_stub_dev_data {
        /* Stub */
};
struct emul_stub_dev_config {
        /* Stub */
};
struct emul_stub_dev_api {
        /* Stub */
};

#define EMUL_STUB_DEVICE(n)                                                                        \
        __maybe_unused static int emul_init_stub_##n(const struct device *dev)                     \
        {                                                                                          \
                ARG_UNUSED(dev);                                                                   \
                return 0;                                                                          \
        }                                                                                          \
                                                                                                   \
        static struct emul_stub_dev_data stub_data_##n;                                            \
        static struct emul_stub_dev_config stub_config_##n;                                        \
        static struct emul_stub_dev_api stub_api_##n;                                              \
        DEVICE_DT_INST_DEFINE(n, &emul_init_stub_##n, NULL, &stub_data_##n, &stub_config_##n,      \
                              POST_KERNEL, CONFIG_KERNEL_INIT_PRIORITY_DEVICE, &stub_api_##n);

#endif /* ZEPHYR_INCLUDE_EMUL_STUB_DEVICE_H_ */
```

## 22.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：2023 Google LLC。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 19 行

没有对应 `DEVICE_DT_DEFINE` 驱动的仿真器需要此项。

### 注释 3：原第 25 行

桩实现（Stub）。

### 注释 4：原第 28 行

桩实现（Stub）。

### 注释 5：原第 31 行

桩实现（Stub）。

### 注释 6：原第 56 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_EMUL_STUB_DEVICE_H_`。

## 22.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/emul__stub__device_8h.html)
- [zephyr/device.h](../device_reference/P007_设备模型头文件参考.md)
- [zephyr/devicetree.h](../dt_main_reference/P001_设备树主头文件参考.md)
- [device.h](../device_reference/P007_设备模型头文件参考.md)
- [devicetree.h](../dt_main_reference/P001_设备树主头文件参考.md)

---

[上一章](P021_renesas_cpg_mssr.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P023_esp-esp32c2-intmux.h_源码浏览.md)
