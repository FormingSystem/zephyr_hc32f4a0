---
id: learning.zephyr-docs.api-hid-pipeline-topic-reference.page-5
title: IT8XXX2 电压比较器（Voltage comparator）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__it8xxx2__vcmp__interface.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第5章\_IT8XXX2 电压比较器（Voltage comparator）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__it8xxx2__vcmp__interface.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

ITE IT8xxx2 电压比较器（Voltage comparator）

<a id="details"></a>

ITE IT8xxx2 电压比较器（Voltage comparator）

<a id="header-files"></a>
<a id="files"></a>

## 5.1\_文件（Files）

<a id="r_it8xxx2_5Fvcmp_2Eh"></a>

```c
file it8xxx2_vcmp.h
```

相关声明：[it8xxx2_vcmp.h](https://docs.zephyrproject.org/latest/doxygen/html/dt-bindings_2sensor_2it8xxx2__vcmp_8h.html)。

the ITE IT8xxx2 voltage comparator的设备树绑定常量（Devicetree Binding Constants）。

<a id="header-member-group"></a>
<a id="member-group"></a>

## 5.2\_电压比较器通道（Voltage Comparator Channels）

设备树属性（Devicetree Property）`vcmp-ch` 的取值。

<a id="r_ga04c6b4af3a7fa2c266f9bc4cf8f580f8"></a>

```c
#define VCMP_CHANNEL_0 0
```

相关声明：[VCMP_CHANNEL_0](#ga04c6b4af3a7fa2c266f9bc4cf8f580f8)。

通道（Channel）0。

<a id="r_gab284eddb8412223f865380f69311884c"></a>

```c
#define VCMP_CHANNEL_1 1
```

相关声明：[VCMP_CHANNEL_1](#gab284eddb8412223f865380f69311884c)。

通道（Channel）1。

<a id="r_gabf666272da5df739c38349f8dc0673d7"></a>

```c
#define VCMP_CHANNEL_2 2
```

相关声明：[VCMP_CHANNEL_2](#gabf666272da5df739c38349f8dc0673d7)。

通道（Channel）2。

<a id="r_gaad5d65c9659dedf702b54d8a7d3857ea"></a>

```c
#define VCMP_CHANNEL_3 3
```

相关声明：[VCMP_CHANNEL_3](#gaad5d65c9659dedf702b54d8a7d3857ea)。

通道（Channel）3。

<a id="r_ga3148e4a63af5791c0d88e3ede54c1443"></a>

```c
#define VCMP_CHANNEL_4 4
```

相关声明：[VCMP_CHANNEL_4](#ga3148e4a63af5791c0d88e3ede54c1443)。

通道（Channel）4。

<a id="r_ga1460631599e37050e844032297578d2c"></a>

```c
#define VCMP_CHANNEL_5 5
```

相关声明：[VCMP_CHANNEL_5](#ga1460631599e37050e844032297578d2c)。

通道（Channel）5。

<a id="r_gad7d3ef8e2a0157c43c68ef12f02b6181"></a>

```c
#define VCMP_CHANNEL_CNT 6
```

相关声明：[VCMP_CHANNEL_CNT](#gad7d3ef8e2a0157c43c68ef12f02b6181)。

通道数量。

## 5.3\_遍历全部通道的扫描周期（Scan Period across All Channels）

设备树属性（Devicetree Property）`scan-period` 的取值。

<a id="r_gafee8d841314119709484eeb1a7919fc4"></a>

```c
#define IT8XXX2_VCMP_SCAN_PERIOD_100US 0x10
```

相关声明：[IT8XXX2_VCMP_SCAN_PERIOD_100US](#gafee8d841314119709484eeb1a7919fc4)。

100 µs（微秒）。

<a id="r_gac22de93d09665b40b736f638bb106143"></a>

```c
#define IT8XXX2_VCMP_SCAN_PERIOD_200US 0x20
```

相关声明：[IT8XXX2_VCMP_SCAN_PERIOD_200US](#gac22de93d09665b40b736f638bb106143)。

200 µs（微秒）。

<a id="r_gac4cd52baa765f7f9e148f49e3a5eb137"></a>

```c
#define IT8XXX2_VCMP_SCAN_PERIOD_400US 0x30
```

相关声明：[IT8XXX2_VCMP_SCAN_PERIOD_400US](#gac4cd52baa765f7f9e148f49e3a5eb137)。

400 µs（微秒）。

<a id="r_ga3e98391265d430652e996798979d6e32"></a>

```c
#define IT8XXX2_VCMP_SCAN_PERIOD_600US 0x40
```

相关声明：[IT8XXX2_VCMP_SCAN_PERIOD_600US](#ga3e98391265d430652e996798979d6e32)。

600 µs（微秒）。

<a id="r_gace0bbf4e49fe2e939926c8973b1d9e6c"></a>

```c
#define IT8XXX2_VCMP_SCAN_PERIOD_800US 0x50
```

相关声明：[IT8XXX2_VCMP_SCAN_PERIOD_800US](#gace0bbf4e49fe2e939926c8973b1d9e6c)。

800 µs（微秒）。

<a id="r_gadd00ffb6d51398fb9207d9709d35f294"></a>

```c
#define IT8XXX2_VCMP_SCAN_PERIOD_1MS 0x60
```

相关声明：[IT8XXX2_VCMP_SCAN_PERIOD_1MS](#gadd00ffb6d51398fb9207d9709d35f294)。

1 ms（毫秒）。

<a id="r_ga1aa53f56577acc7cbd34f9f37d166e7c"></a>

```c
#define IT8XXX2_VCMP_SCAN_PERIOD_1_5MS 0x70
```

相关声明：[IT8XXX2_VCMP_SCAN_PERIOD_1_5MS](#ga1aa53f56577acc7cbd34f9f37d166e7c)。

1.5 ms（毫秒）。

<a id="r_ga012e4fcc993d9aed16203e1cdbbeca05"></a>

```c
#define IT8XXX2_VCMP_SCAN_PERIOD_2MS 0x80
```

相关声明：[IT8XXX2_VCMP_SCAN_PERIOD_2MS](#ga012e4fcc993d9aed16203e1cdbbeca05)。

2 ms（毫秒）。

<a id="r_gaa702079843ff113a79589c6daca88587"></a>

```c
#define IT8XXX2_VCMP_SCAN_PERIOD_2_5MS 0x90
```

相关声明：[IT8XXX2_VCMP_SCAN_PERIOD_2_5MS](#gaa702079843ff113a79589c6daca88587)。

2.5 ms（毫秒）。

<a id="r_gaad950cc6bec74a685ec3d37f451e1a10"></a>

```c
#define IT8XXX2_VCMP_SCAN_PERIOD_3MS 0xa0
```

相关声明：[IT8XXX2_VCMP_SCAN_PERIOD_3MS](#gaad950cc6bec74a685ec3d37f451e1a10)。

3 ms（毫秒）。

<a id="r_ga4f296f81c2a751d53977abf2aff5d6dd"></a>

```c
#define IT8XXX2_VCMP_SCAN_PERIOD_4MS 0xb0
```

相关声明：[IT8XXX2_VCMP_SCAN_PERIOD_4MS](#ga4f296f81c2a751d53977abf2aff5d6dd)。

4 ms（毫秒）。

<a id="r_ga7c31ca003dc472e5e567c6274f62dceb"></a>

```c
#define IT8XXX2_VCMP_SCAN_PERIOD_5MS 0xc0
```

相关声明：[IT8XXX2_VCMP_SCAN_PERIOD_5MS](#ga7c31ca003dc472e5e567c6274f62dceb)。

5 ms（毫秒）。

## 5.4\_中断触发模式（Interrupt Trigger Mode）

设备树属性（Devicetree Property）`comparison` 的取值。

<a id="r_ga46e65d3ca651e9a75d90d0d456e6bc28"></a>

```c
#define IT8XXX2_VCMP_LESS_OR_EQUAL 0
```

相关声明：[IT8XXX2_VCMP_LESS_OR_EQUAL](#ga46e65d3ca651e9a75d90d0d456e6bc28)。

当数值小于或等于阈值（Threshold）时触发。

<a id="r_ga2f1ccc3b8b3d0ff5b1fab7d401adb2c7"></a>

```c
#define IT8XXX2_VCMP_GREATER 1
```

相关声明：[IT8XXX2_VCMP_GREATER](#ga2f1ccc3b8b3d0ff5b1fab7d401adb2c7)。

当数值大于阈值（Threshold）时触发。

<a id="r_gac54b4d008105b4d2ad956cf076c29acc"></a>

```c
#define IT8XXX2_VCMP_UNDEFINED 0xffff
```

相关声明：[IT8XXX2_VCMP_UNDEFINED](#gac54b4d008105b4d2ad956cf076c29acc)。

未定义／未使用（Undefined/Unused）。

## 5.5\_详细说明（Detailed Documentation）

<a id="ga2f1ccc3b8b3d0ff5b1fab7d401adb2c7"></a>

### `IT8XXX2_VCMP_GREATER`

```c
#define IT8XXX2_VCMP_GREATER 1
```

```c
#include <zephyr/dt-bindings/sensor/it8xxx2_vcmp.h>
```

当数值大于阈值（Threshold）时触发。

<a id="ga46e65d3ca651e9a75d90d0d456e6bc28"></a>

### `IT8XXX2_VCMP_LESS_OR_EQUAL`

```c
#define IT8XXX2_VCMP_LESS_OR_EQUAL 0
```

```c
#include <zephyr/dt-bindings/sensor/it8xxx2_vcmp.h>
```

当数值小于或等于阈值（Threshold）时触发。

<a id="gafee8d841314119709484eeb1a7919fc4"></a>

### `IT8XXX2_VCMP_SCAN_PERIOD_100US`

```c
#define IT8XXX2_VCMP_SCAN_PERIOD_100US 0x10
```

```c
#include <zephyr/dt-bindings/sensor/it8xxx2_vcmp.h>
```

100 µs（微秒）。

<a id="ga1aa53f56577acc7cbd34f9f37d166e7c"></a>

### `IT8XXX2_VCMP_SCAN_PERIOD_1_5MS`

```c
#define IT8XXX2_VCMP_SCAN_PERIOD_1_5MS 0x70
```

```c
#include <zephyr/dt-bindings/sensor/it8xxx2_vcmp.h>
```

1.5 ms（毫秒）。

<a id="gadd00ffb6d51398fb9207d9709d35f294"></a>

### `IT8XXX2_VCMP_SCAN_PERIOD_1MS`

```c
#define IT8XXX2_VCMP_SCAN_PERIOD_1MS 0x60
```

```c
#include <zephyr/dt-bindings/sensor/it8xxx2_vcmp.h>
```

1 ms（毫秒）。

<a id="gac22de93d09665b40b736f638bb106143"></a>

### `IT8XXX2_VCMP_SCAN_PERIOD_200US`

```c
#define IT8XXX2_VCMP_SCAN_PERIOD_200US 0x20
```

```c
#include <zephyr/dt-bindings/sensor/it8xxx2_vcmp.h>
```

200 µs（微秒）。

<a id="gaa702079843ff113a79589c6daca88587"></a>

### `IT8XXX2_VCMP_SCAN_PERIOD_2_5MS`

```c
#define IT8XXX2_VCMP_SCAN_PERIOD_2_5MS 0x90
```

```c
#include <zephyr/dt-bindings/sensor/it8xxx2_vcmp.h>
```

2.5 ms（毫秒）。

<a id="ga012e4fcc993d9aed16203e1cdbbeca05"></a>

### `IT8XXX2_VCMP_SCAN_PERIOD_2MS`

```c
#define IT8XXX2_VCMP_SCAN_PERIOD_2MS 0x80
```

```c
#include <zephyr/dt-bindings/sensor/it8xxx2_vcmp.h>
```

2 ms（毫秒）。

<a id="gaad950cc6bec74a685ec3d37f451e1a10"></a>

### `IT8XXX2_VCMP_SCAN_PERIOD_3MS`

```c
#define IT8XXX2_VCMP_SCAN_PERIOD_3MS 0xa0
```

```c
#include <zephyr/dt-bindings/sensor/it8xxx2_vcmp.h>
```

3 ms（毫秒）。

<a id="gac4cd52baa765f7f9e148f49e3a5eb137"></a>

### `IT8XXX2_VCMP_SCAN_PERIOD_400US`

```c
#define IT8XXX2_VCMP_SCAN_PERIOD_400US 0x30
```

```c
#include <zephyr/dt-bindings/sensor/it8xxx2_vcmp.h>
```

400 µs（微秒）。

<a id="ga4f296f81c2a751d53977abf2aff5d6dd"></a>

### `IT8XXX2_VCMP_SCAN_PERIOD_4MS`

```c
#define IT8XXX2_VCMP_SCAN_PERIOD_4MS 0xb0
```

```c
#include <zephyr/dt-bindings/sensor/it8xxx2_vcmp.h>
```

4 ms（毫秒）。

<a id="ga7c31ca003dc472e5e567c6274f62dceb"></a>

### `IT8XXX2_VCMP_SCAN_PERIOD_5MS`

```c
#define IT8XXX2_VCMP_SCAN_PERIOD_5MS 0xc0
```

```c
#include <zephyr/dt-bindings/sensor/it8xxx2_vcmp.h>
```

5 ms（毫秒）。

<a id="ga3e98391265d430652e996798979d6e32"></a>

### `IT8XXX2_VCMP_SCAN_PERIOD_600US`

```c
#define IT8XXX2_VCMP_SCAN_PERIOD_600US 0x40
```

```c
#include <zephyr/dt-bindings/sensor/it8xxx2_vcmp.h>
```

600 µs（微秒）。

<a id="gace0bbf4e49fe2e939926c8973b1d9e6c"></a>

### `IT8XXX2_VCMP_SCAN_PERIOD_800US`

```c
#define IT8XXX2_VCMP_SCAN_PERIOD_800US 0x50
```

```c
#include <zephyr/dt-bindings/sensor/it8xxx2_vcmp.h>
```

800 µs（微秒）。

<a id="gac54b4d008105b4d2ad956cf076c29acc"></a>

### `IT8XXX2_VCMP_UNDEFINED`

```c
#define IT8XXX2_VCMP_UNDEFINED 0xffff
```

```c
#include <zephyr/dt-bindings/sensor/it8xxx2_vcmp.h>
```

未定义／未使用（Undefined/Unused）。

<a id="ga04c6b4af3a7fa2c266f9bc4cf8f580f8"></a>

### `VCMP_CHANNEL_0`

```c
#define VCMP_CHANNEL_0 0
```

```c
#include <zephyr/dt-bindings/sensor/it8xxx2_vcmp.h>
```

通道（Channel）0。

<a id="gab284eddb8412223f865380f69311884c"></a>

### `VCMP_CHANNEL_1`

```c
#define VCMP_CHANNEL_1 1
```

```c
#include <zephyr/dt-bindings/sensor/it8xxx2_vcmp.h>
```

通道（Channel）1。

<a id="gabf666272da5df739c38349f8dc0673d7"></a>

### `VCMP_CHANNEL_2`

```c
#define VCMP_CHANNEL_2 2
```

```c
#include <zephyr/dt-bindings/sensor/it8xxx2_vcmp.h>
```

通道（Channel）2。

<a id="gaad5d65c9659dedf702b54d8a7d3857ea"></a>

### `VCMP_CHANNEL_3`

```c
#define VCMP_CHANNEL_3 3
```

```c
#include <zephyr/dt-bindings/sensor/it8xxx2_vcmp.h>
```

通道（Channel）3。

<a id="ga3148e4a63af5791c0d88e3ede54c1443"></a>

### `VCMP_CHANNEL_4`

```c
#define VCMP_CHANNEL_4 4
```

```c
#include <zephyr/dt-bindings/sensor/it8xxx2_vcmp.h>
```

通道（Channel）4。

<a id="ga1460631599e37050e844032297578d2c"></a>

### `VCMP_CHANNEL_5`

```c
#define VCMP_CHANNEL_5 5
```

```c
#include <zephyr/dt-bindings/sensor/it8xxx2_vcmp.h>
```

通道（Channel）5。

<a id="gad7d3ef8e2a0157c43c68ef12f02b6181"></a>

### `VCMP_CHANNEL_CNT`

```c
#define VCMP_CHANNEL_CNT 6
```

```c
#include <zephyr/dt-bindings/sensor/it8xxx2_vcmp.h>
```

通道数量。


## 5.6\_原页交叉引用（Cross References）

- [it8xxx2_vcmp.h](https://docs.zephyrproject.org/latest/doxygen/html/dt-bindings_2sensor_2it8xxx2__vcmp_8h.html)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[上一章](P004_麦克风控制配置文件（Microphone Control Profile，MICP）.md) · [返回大纲](大纲.md) · [下一章](P006_MC3419 API主题.md)
