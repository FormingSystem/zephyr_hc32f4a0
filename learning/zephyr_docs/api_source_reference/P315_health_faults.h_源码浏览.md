---
id: learning.zephyr-docs.api-source-reference.page-315
title: health_faults.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/health__faults_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第315章\_health\_faults.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/health__faults_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/health__faults_8h.html)。

## 315.1\_原始可见代码（Source Code）

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
<a id="l00021"></a>
<a id="l00022"></a>
<a id="l00024"></a>
<a id="l00026"></a>
<a id="l00028"></a>
<a id="l00030"></a>
<a id="l00032"></a>
<a id="l00034"></a>
<a id="l00036"></a>
<a id="l00038"></a>
<a id="l00040"></a>
<a id="l00042"></a>
<a id="l00044"></a>
<a id="l00046"></a>
<a id="l00048"></a>
<a id="l00050"></a>
<a id="l00052"></a>
<a id="l00054"></a>
<a id="l00056"></a>
<a id="l00058"></a>
<a id="l00060"></a>
<a id="l00062"></a>
<a id="l00064"></a>
<a id="l00066"></a>
<a id="l00068"></a>
<a id="l00070"></a>
<a id="l00072"></a>
<a id="l00074"></a>
<a id="l00076"></a>
<a id="l00078"></a>
<a id="l00080"></a>
<a id="l00082"></a>
<a id="l00084"></a>
<a id="l00086"></a>
<a id="l00088"></a>
<a id="l00090"></a>
<a id="l00092"></a>
<a id="l00094"></a>
<a id="l00096"></a>
<a id="l00098"></a>
<a id="l00100"></a>
<a id="l00102"></a>
<a id="l00104"></a>
<a id="l00106"></a>
<a id="l00108"></a>
<a id="l00110"></a>
<a id="l00112"></a>
<a id="l00114"></a>
<a id="l00116"></a>
<a id="l00118"></a>
<a id="l00120"></a>
<a id="l00122"></a>
<a id="l00123"></a>
<a id="l00129"></a>
<a id="l00130"></a>
<a id="l00134"></a>
<a id="l00135"></a>

```c


/*
 * Copyright (c) 2019 Nordic Semiconductor ASA
 *
 * SPDX-License-Identifier: Apache-2.0
 */
#ifndef ZEPHYR_INCLUDE_BLUETOOTH_MESH_HEALTH_FAULTS_H__
#define ZEPHYR_INCLUDE_BLUETOOTH_MESH_HEALTH_FAULTS_H__


#define BT_MESH_HEALTH_FAULT_NO_FAULT                           0x00

#define BT_MESH_HEALTH_FAULT_BATTERY_LOW_WARNING                0x01
#define BT_MESH_HEALTH_FAULT_BATTERY_LOW_ERROR                  0x02
#define BT_MESH_HEALTH_FAULT_SUPPLY_VOLTAGE_TOO_LOW_WARNING     0x03
#define BT_MESH_HEALTH_FAULT_SUPPLY_VOLTAGE_TOO_LOW_ERROR       0x04
#define BT_MESH_HEALTH_FAULT_SUPPLY_VOLTAGE_TOO_HIGH_WARNING    0x05
#define BT_MESH_HEALTH_FAULT_SUPPLY_VOLTAGE_TOO_HIGH_ERROR      0x06
#define BT_MESH_HEALTH_FAULT_POWER_SUPPLY_INTERRUPTED_WARNING   0x07
#define BT_MESH_HEALTH_FAULT_POWER_SUPPLY_INTERRUPTED_ERROR     0x08
#define BT_MESH_HEALTH_FAULT_NO_LOAD_WARNING                    0x09
#define BT_MESH_HEALTH_FAULT_NO_LOAD_ERROR                      0x0A
#define BT_MESH_HEALTH_FAULT_OVERLOAD_WARNING                   0x0B
#define BT_MESH_HEALTH_FAULT_OVERLOAD_ERROR                     0x0C
#define BT_MESH_HEALTH_FAULT_OVERHEAT_WARNING                   0x0D
#define BT_MESH_HEALTH_FAULT_OVERHEAT_ERROR                     0x0E
#define BT_MESH_HEALTH_FAULT_CONDENSATION_WARNING               0x0F
#define BT_MESH_HEALTH_FAULT_CONDENSATION_ERROR                 0x10
#define BT_MESH_HEALTH_FAULT_VIBRATION_WARNING                  0x11
#define BT_MESH_HEALTH_FAULT_VIBRATION_ERROR                    0x12
#define BT_MESH_HEALTH_FAULT_CONFIGURATION_WARNING              0x13
#define BT_MESH_HEALTH_FAULT_CONFIGURATION_ERROR                0x14
#define BT_MESH_HEALTH_FAULT_ELEMENT_NOT_CALIBRATED_WARNING     0x15
#define BT_MESH_HEALTH_FAULT_ELEMENT_NOT_CALIBRATED_ERROR       0x16
#define BT_MESH_HEALTH_FAULT_MEMORY_WARNING                     0x17
#define BT_MESH_HEALTH_FAULT_MEMORY_ERROR                       0x18
#define BT_MESH_HEALTH_FAULT_SELF_TEST_WARNING                  0x19
#define BT_MESH_HEALTH_FAULT_SELF_TEST_ERROR                    0x1A
#define BT_MESH_HEALTH_FAULT_INPUT_TOO_LOW_WARNING              0x1B
#define BT_MESH_HEALTH_FAULT_INPUT_TOO_LOW_ERROR                0x1C
#define BT_MESH_HEALTH_FAULT_INPUT_TOO_HIGH_WARNING             0x1D
#define BT_MESH_HEALTH_FAULT_INPUT_TOO_HIGH_ERROR               0x1E
#define BT_MESH_HEALTH_FAULT_INPUT_NO_CHANGE_WARNING            0x1F
#define BT_MESH_HEALTH_FAULT_INPUT_NO_CHANGE_ERROR              0x20
#define BT_MESH_HEALTH_FAULT_ACTUATOR_BLOCKED_WARNING           0x21
#define BT_MESH_HEALTH_FAULT_ACTUATOR_BLOCKED_ERROR             0x22
#define BT_MESH_HEALTH_FAULT_HOUSING_OPENED_WARNING             0x23
#define BT_MESH_HEALTH_FAULT_HOUSING_OPENED_ERROR               0x24
#define BT_MESH_HEALTH_FAULT_TAMPER_WARNING                     0x25
#define BT_MESH_HEALTH_FAULT_TAMPER_ERROR                       0x26
#define BT_MESH_HEALTH_FAULT_DEVICE_MOVED_WARNING               0x27
#define BT_MESH_HEALTH_FAULT_DEVICE_MOVED_ERROR                 0x28
#define BT_MESH_HEALTH_FAULT_DEVICE_DROPPED_WARNING             0x29
#define BT_MESH_HEALTH_FAULT_DEVICE_DROPPED_ERROR               0x2A
#define BT_MESH_HEALTH_FAULT_OVERFLOW_WARNING                   0x2B
#define BT_MESH_HEALTH_FAULT_OVERFLOW_ERROR                     0x2C
#define BT_MESH_HEALTH_FAULT_EMPTY_WARNING                      0x2D
#define BT_MESH_HEALTH_FAULT_EMPTY_ERROR                        0x2E
#define BT_MESH_HEALTH_FAULT_INTERNAL_BUS_WARNING               0x2F
#define BT_MESH_HEALTH_FAULT_INTERNAL_BUS_ERROR                 0x30
#define BT_MESH_HEALTH_FAULT_MECHANISM_JAMMED_WARNING           0x31
#define BT_MESH_HEALTH_FAULT_MECHANISM_JAMMED_ERROR             0x32

#define BT_MESH_HEALTH_FAULT_VENDOR_SPECIFIC_START              0x80


#endif /* ZEPHYR_INCLUDE_BLUETOOTH_MESH_HEALTH_FAULTS_H__ */
```

## 315.2\_可见注释译文（Comments）

### 注释 1：原第 5 行

版权（Copyright）：© 2019 Nordic Semiconductor ASA。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 135 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_BLUETOOTH_MESH_HEALTH_FAULTS_H__`。

## 315.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/health__faults_8h.html)

---

[上一章](P314_health_cli.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P316_health_srv.h_源码浏览.md)
