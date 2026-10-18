---
id: learning.zephyr-docs.api-source-supplement-reference.page-177
title: serial_test.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/serial__test_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第177章\_serial\_test.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/serial__test_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/serial__test_8h.html)。

## 177.1\_原始可见代码（Source Code）

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
<a id="l00013"></a>
<a id="l00014"></a>
<a id="l00015"></a>
<a id="l00016"></a>
<a id="l00017"></a>
<a id="l00032"></a>
<a id="l00033"></a>
<a id="l00041"></a>
<a id="l00042"></a>
<a id="l00061"></a>
<a id="l00062"></a>
<a id="l00081"></a>
<a id="l00082"></a>
<a id="l00089"></a>
<a id="l00090"></a>
<a id="l00099"></a>
<a id="l00100"></a>
<a id="l00101"></a>
<a id="l00102"></a>
<a id="l00103"></a>
<a id="l00104"></a>
<a id="l00105"></a>
<a id="l00106"></a>
<a id="adevice_8h_html"></a>
<a id="aerrno_8h_html"></a>
<a id="aserial__test_8h_html_a04f02df85d720ccd5ce02ab9e217dba3"></a>
<a id="aserial__test_8h_html_a1e2a3d82504b34d5b4590afc67172c9e"></a>
<a id="aserial__test_8h_html_a2b7d97302cb3546cfc8f384f4a7c1a4a"></a>
<a id="aserial__test_8h_html_a4275edbc443677d2c0f08100834977a7"></a>
<a id="aserial__test_8h_html_a4908343c26e5846abf977befe2c5dbbe"></a>
<a id="aserial__test_8h_html_ab9b60bf8d62db2be3ad530cd0a78aedd"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astructdevice_html"></a>

```c
/*
 * Copyright 2022 The ChromiumOS Authors.
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_DRIVERS_UART_SERIAL_TEST_H_
#define ZEPHYR_INCLUDE_DRIVERS_UART_SERIAL_TEST_H_

#include <errno.h>

#include <zephyr/device.h>

#ifdef __cplusplus
extern "C" {
#endif /* __cplusplus */

int serial_vnd_queue_in_data(const struct device *dev, const unsigned char *data, uint32_t size);

uint32_t serial_vnd_out_data_size_get(const struct device *dev);

uint32_t serial_vnd_read_out_data(const struct device *dev, unsigned char *data, uint32_t size);

uint32_t serial_vnd_peek_out_data(const struct device *dev, unsigned char *data, uint32_t size);

typedef void (*serial_vnd_write_cb_t)(const struct device *dev, void *user_data);

void serial_vnd_set_callback(const struct device *dev, serial_vnd_write_cb_t callback,
                             void *user_data);

#ifdef __cplusplus
}
#endif /* __cplusplus */

#endif /* ZEPHYR_INCLUDE_DRIVERS_UART_SERIAL_TEST_H_ */
```

## 177.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：2022 The ChromiumOS Authors.。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 16 行

条件编译标记：`__cplusplus`。

### 注释 3：原第 104 行

条件编译标记：`__cplusplus`。

### 注释 4：原第 106 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DRIVERS_UART_SERIAL_TEST_H_`。

## 177.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/serial__test_8h.html)
- [errno.h](../error_reference/P004_错误号头文件参考.md)
- [zephyr/device.h](../device_reference/P007_设备模型头文件参考.md)
- [serial_vnd_queue_in_data](https://docs.zephyrproject.org/latest/doxygen/html/serial__test_8h.html#a2b7d97302cb3546cfc8f384f4a7c1a4a)
- [device](../device_reference/P002_设备对象结构.md)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [serial_vnd_out_data_size_get](https://docs.zephyrproject.org/latest/doxygen/html/serial__test_8h.html#a4275edbc443677d2c0f08100834977a7)
- [serial_vnd_read_out_data](https://docs.zephyrproject.org/latest/doxygen/html/serial__test_8h.html#ab9b60bf8d62db2be3ad530cd0a78aedd)
- [serial_vnd_peek_out_data](https://docs.zephyrproject.org/latest/doxygen/html/serial__test_8h.html#a1e2a3d82504b34d5b4590afc67172c9e)
- [serial_vnd_write_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/serial__test_8h.html#a04f02df85d720ccd5ce02ab9e217dba3)
- [serial_vnd_set_callback](https://docs.zephyrproject.org/latest/doxygen/html/serial__test_8h.html#a4908343c26e5846abf977befe2c5dbbe)
- [device.h](../device_reference/P007_设备模型头文件参考.md)

---

[上一章](P176_seagate_legend_b1414.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P178_silabs-pinctrl-dbus.h_源码浏览.md)
