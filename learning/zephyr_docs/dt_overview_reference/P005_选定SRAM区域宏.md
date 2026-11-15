---
id: learning.zephyr-docs.dt-overview-reference.page-5
title: 选定SRAM区域宏
kind: reference
status: maintained
domains: [zephyr, hardware, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__devicetree-chosen-sram.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第5章\_选定SRAM区域宏

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__devicetree-chosen-sram.html)。读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

> 译注——阅读位置：从[本册大纲](大纲.md)进入设备树API总览、电池开路电压曲线或选定SRAM接口。源码跟踪译注与官方原文分开标示。

<a id="details"></a>



<a id="header-define-members"></a>
<a id="define-members"></a>

## 5.1\_宏定义（Macros）

<a id="r_gad2693f2710d28709b0f129d5b791a29e"></a>

```c
#define DT_CHOSEN_SRAM_ADDR DT_REG_ADDR(DT_CHOSEN(zephyr_sram))
```

相关声明：[DT_CHOSEN_SRAM_ADDR](#gad2693f2710d28709b0f129d5b791a29e)、[DT_REG_ADDR](../dt_reg_reference/P001_设备树寄存器属性宏.md#gac6d8279c32351ced4c0ac7f32270974e)、[DT_CHOSEN](../dt_node_reference/P002_设备树chosen节点宏.md#ga3412d0acecffa828984cf9e2c89889ed)。

获取选定静态随机存取存储器（Chosen SRAM）节点的地址。

<a id="r_ga0a148f7de43111280b85a3ce4afaddea"></a>

```c
#define DT_CHOSEN_SRAM_SIZE DT_REG_SIZE(DT_CHOSEN(zephyr_sram))
```

相关声明：[DT_CHOSEN_SRAM_SIZE](#ga0a148f7de43111280b85a3ce4afaddea)、[DT_REG_SIZE](../dt_reg_reference/P001_设备树寄存器属性宏.md#gad223efc6c77d008e55c3588953e85bfb)、[DT_CHOSEN](../dt_node_reference/P002_设备树chosen节点宏.md#ga3412d0acecffa828984cf9e2c89889ed)。

获取选定静态随机存取存储器（Chosen SRAM）节点的大小。

## 5.2\_详细说明（Detailed Documentation）

<a id="gad2693f2710d28709b0f129d5b791a29e"></a>

### `DT_CHOSEN_SRAM_ADDR`

```c
#define DT_CHOSEN_SRAM_ADDR DT_REG_ADDR(DT_CHOSEN(zephyr_sram))
```

```c
#include <zephyr/devicetree/sram.h>
```

获取选定静态随机存取存储器（Chosen SRAM）节点的地址。

返回（Returns）：选定 SRAM 节点的绝对存储地址，前提是该节点存在。

<a id="ga0a148f7de43111280b85a3ce4afaddea"></a>

### `DT_CHOSEN_SRAM_SIZE`

```c
#define DT_CHOSEN_SRAM_SIZE DT_REG_SIZE(DT_CHOSEN(zephyr_sram))
```

```c
#include <zephyr/devicetree/sram.h>
```

获取选定静态随机存取存储器（Chosen SRAM）节点的大小。

返回（Returns）：选定 SRAM 节点的大小，前提是该节点存在。

## 5.3\_源码定位与版本边界

相对源码定位：[电池曲线常量](../../../include/zephyr/dt-bindings/battery/battery.h)、[电池查表接口](../../../include/zephyr/drivers/sensor/battery.h)、[组合电量计驱动](../../../drivers/fuel_gauge/composite/fuel_gauge_composite.c)、[电池绑定](../../../dts/bindings/battery/battery.yaml)、[组合电量计绑定](../../../dts/bindings/fuel-gauge/zephyr,fuel-gauge-composite.yaml)、[选定SRAM宏](../../../include/zephyr/devicetree/sram.h)和[架构配置](../../../arch/Kconfig)。本次官方文件摘要见[来源记录](../SOURCES.md)。

> 译注——源码核对：地址对象：DT_CHOSEN_SRAM_ADDR中的“绝对地址”（Absolute Address）指目标芯片存储地址，不是电脑文件系统路径。设备树分支通过DT_CHOSEN(zephyr_sram)解析/chosen的zephyr,sram，再由DT_REG_ADDR／DT_REG_SIZE读取第0个reg区域；不会汇总其他SRAM节点或同一节点的所有reg条目，也不直接返回可解引用的C指针。

> 译注——源码核对：两条配置分支：参考页展示设备树分支，源码页还保留CONFIG_SRAM_DEPRECATED_KCONFIG_SET分支，分别采用CONFIG_SRAM_BASE_ADDRESS和CONFIG_SRAM_SIZE * 1024。后者把旧配置中的1024字节单位换算成字节（Bytes）。arch/Kconfig在旧地址或大小与所选设备树值不同时启用此兼容分支并选择DEPRECATED；新配置应以zephyr,sram节点描述为准。

> 译注——源码核对：存在性与使用边界：原文“if it exists”不是缺少节点时返回0的保证。设备树分支直接展开DT_CHOSEN和reg访问器，没有运行时失败返回值或自动回退；调用位置应确保所选节点及对应reg信息存在。宏只提供声明的地址和长度，不分配内存、不初始化RAM，也不证明链接后的代码或数据已经放入该区域。

> 译注——源码核对：版本边界：本批记录七份官方源码／绑定的读取摘要；两个源码浏览页的非注释代码与本次读取的对应原始头文件一致。latest和main会滚动变化，本仓库参照源码与它们不自动视为相同版本；本次未编译示例、构建固件或执行硬件实验。

本次验证范围为文档与源码对照，未编译宏／DTS示例、构建固件或操作硬件。

## 5.4\_原页交叉引用（Cross References）

- [DT_REG_ADDR](../dt_reg_reference/P001_设备树寄存器属性宏.md#gac6d8279c32351ced4c0ac7f32270974e)
- [DT_CHOSEN](../dt_node_reference/P002_设备树chosen节点宏.md#ga3412d0acecffa828984cf9e2c89889ed)
- [DT_REG_SIZE](../dt_reg_reference/P001_设备树寄存器属性宏.md#gad223efc6c77d008e55c3588953e85bfb)
- [zephyr/devicetree/sram.h](P006_选定SRAM头文件参考.md)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[上一章](P004_电池曲线绑定头文件源码.md) · [返回大纲](大纲.md) · [下一章](P006_选定SRAM头文件参考.md)
