---
id: learning.zephyr-docs.dt-overview-reference.page-1
title: 设备树API总览
kind: reference
status: maintained
domains: [zephyr, hardware, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__devicetree.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第1章\_设备树API总览

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__devicetree.html)。读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

> 译注——阅读位置：从[本册大纲](大纲.md)进入设备树API总览、电池开路电压曲线或选定SRAM接口。源码跟踪译注与官方原文分开标示。

`devicetree.h` 应用程序编程接口（API）。

<a id="details"></a>

`devicetree.h` 应用程序编程接口（API）。

引入版本（Since）：2.2。

API 版本（Version）：1.2.0。

<a id="header-groups"></a>
<a id="groups"></a>

## 1.1\_主题（Topics）

<a id="r_devicetree-generic-foreach"></a>

相关声明：[逐项展开宏（For-each Macros）](../dt_foreach_reference/P001_设备树遍历宏.md)。

重要：不能在设备树逐项展开宏（DT For-each Macros）自身的展开过程中再次使用同一个宏。

<a id="r_devicetree-generic-bus"></a>

相关声明：[总线辅助宏（Bus Helpers）](../dt_node_reference/P001_设备树总线查询宏.md)。

<a id="r_devicetree-generic-chosen"></a>

相关声明：[选定节点（Chosen Nodes）](../dt_node_reference/P002_设备树chosen节点宏.md)。

<a id="r_devicetree-dep-ord"></a>

相关声明：[依赖跟踪（Dependency Tracking）](../dt_node_reference/P004_设备树依赖顺序宏.md)。

<a id="r_devicetree-can"></a>

相关声明：[设备树控制器局域网接口（Devicetree CAN API）](../hardware/P373_CAN设备树宏.md)。

<a id="r_devicetree-clocks"></a>

相关声明：[设备树时钟接口（Devicetree Clocks API）](../timer_reference/P107_设备树时钟获取宏.md)。

<a id="r_devicetree-counter-captures"></a>

相关声明：[设备树计数器捕获接口（Devicetree Counter Captures API）](../timer_reference/P034_计数器捕获设备树宏.md)。

<a id="r_devicetree-dmas"></a>

相关声明：[设备树直接存储器访问接口（Devicetree DMA API）](../dma_reference/P008_DMA设备树宏.md)。

<a id="r_devicetree-display"></a>

相关声明：[设备树显示接口（Devicetree Display API）](../hardware/P227_设备树显示接口.md)。

<a id="r_devicetree-fixed-partition"></a>

相关声明：[设备树固定分区接口（Devicetree Fixed Partition API）](../dt_partition_reference/P002_设备树固定分区宏.md)。

<a id="r_devicetree-gpio"></a>

相关声明：[设备树通用输入输出接口（Devicetree GPIO API）](../hardware/P290_设备树GPIO宏.md)。

<a id="r_devicetree-hwspinlock"></a>

相关声明：[设备树硬件自旋锁接口（Devicetree HW Spinlock API）](../intercore_reference/P008_硬件自旋锁设备树宏.md)。

<a id="r_devicetree-io-channels"></a>

相关声明：[设备树输入输出通道接口（Devicetree IO Channels API）](../dt_connection_reference/P001_设备树I_O通道宏.md)。

<a id="r_devicetree-cpu"></a>

相关声明：[设备树中断CPU接口（Devicetree Interrupt CPU API）](../dt_node_reference/P003_设备树CPU节点宏.md)。

<a id="r_devicetree-interrupt_5Fcontroller"></a>

相关声明：[设备树中断控制器接口（Devicetree Interrupt Controller API）](../dt_irq_reference/P002_设备树中断控制器宏.md)。

<a id="r_devicetree-mbox"></a>

相关声明：[设备树邮箱接口（Devicetree MBOX API）](../intercore_reference/P021_邮箱设备树访问宏.md)。

<a id="r_devicetree-mux"></a>

相关声明：[设备树多路复用器接口（Devicetree MUX API）](../dt_connection_reference/P007_设备树多路复用器宏.md)。

<a id="r_devicetree-mapped-partition"></a>

相关声明：[设备树映射分区接口（Devicetree Mapped Partition API）](../dt_partition_reference/P005_设备树映射分区宏.md)。

<a id="r_devicetree-pwms"></a>

相关声明：[设备树脉宽调制接口（Devicetree PWMs API）](../hardware/P264_设备树PWM宏.md)。

<a id="r_devicetree-partition"></a>

相关声明：[设备树分区接口（Devicetree Partition API）](../dt_partition_reference/P001_设备树通用分区宏.md)。

<a id="r_devicetree-port-endpoint"></a>

相关声明：[设备树端口与端点接口（Devicetree Port Endpoint API）](../dt_connection_reference/P010_设备树端口与端点宏.md)。

<a id="r_devicetree-regulator"></a>

相关声明：[设备树稳压器接口（Devicetree Regulator API）](../power/P081_设备树稳压器辅助接口目录.md)。

<a id="r_dt_5Frenesas_5Fra_5Felc"></a>

相关声明：[设备树Renesas RA事件链接控制器辅助宏（Devicetree Renesas RA ELC Helpers）](https://docs.zephyrproject.org/latest/doxygen/html/group__dt__renesas__ra__elc.html)。

<a id="r_devicetree-reset-controller"></a>

相关声明：[设备树复位控制器接口（Devicetree Reset Controller API）](../reset_reference/P007_复位控制器设备树辅助宏.md)。

<a id="r_devicetree-spi"></a>

相关声明：[设备树串行外设接口（Devicetree SPI API）](../hardware/P329_SPI设备树宏.md)。

<a id="r_devicetree-chosen-sram"></a>

相关声明：[设备树静态随机存取存储器接口（Devicetree SRAM API）](P005_选定SRAM区域宏.md)。

<a id="r_devicetree-wakeup-controller"></a>

相关声明：[设备树唤醒控制器接口（Devicetree WUC Controller API）](../dt_irq_reference/P005_设备树唤醒控制器宏.md)。

<a id="r_devicetree-battery"></a>

相关声明：[设备树电池辅助宏（Devicetree Battery Helpers）](P002_电池开路电压曲线宏.md)。

<a id="r_dt_5Fmemory_5Fattr"></a>

相关声明：[设备树内存属性（Devicetree Memory Attributes）](../dt_memory_attribute_reference/P001_设备树内存属性总览.md)。

用于内存属性（Memory Attributes）的设备树宏。

<a id="r_devicetree-generic-exist"></a>

相关声明：[存在性检查（Existence Checks）](../dt_identity_reference/P002_设备树存在性与状态宏.md)。

<a id="r_devicetree-inst"></a>

相关声明：[基于实例的设备树接口（Instance-based Devicetree APIs）](../dt_instance_reference/P001_设备树驱动实例宏.md)。

<a id="r_devicetree-map"></a>

相关声明：[映射辅助宏（Map Helpers）](../dt_connection_reference/P004_设备树描述符映射宏.md)。

<a id="r_devicetree-nvmem"></a>

相关声明：[非易失性存储器设备树辅助宏（NVMEM Devicetree Helpers）](../storage/P018_NVMEM设备树辅助宏.md)。

非易失性存储器（Non-Volatile Memory，NVMEM）的设备树支持。

<a id="r_imx952_5Fpower_5Fdomains"></a>

相关声明：[NXP i.MX952电源域（Power Domains）](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__power__domains.html)。

i.MX952 系统级芯片（SoC）的电源域分区索引（Power Domain Slice Indices）。

<a id="r_devicetree-generic-id"></a>

相关声明：[节点标识符及辅助宏（Node Identifiers and Helpers）](../dt_identity_reference/P001_设备树节点标识宏.md)。

<a id="r_devicetree-pinctrl"></a>

相关声明：[引脚控制（Pin Control）](../pinctrl_reference/P005_引脚控制设备树宏.md)。

<a id="r_devicetree-generic-prop"></a>

相关声明：[属性访问器（Property Accessors）](../dt_property_reference/P001_设备树属性读取宏.md)。

<a id="r_devicetree-generic-vendor"></a>

相关声明：[厂商与型号名称辅助宏（Vendor and Model Name Helpers）](../dt_identity_reference/P003_设备树厂商与型号宏.md)。

<a id="r_devicetree-interrupts-prop"></a>

相关声明：[中断属性（interrupts Property）](../dt_irq_reference/P001_设备树中断属性宏.md)。

<a id="r_devicetree-ranges-prop"></a>

相关声明：[地址范围映射属性（ranges Property）](../dt_reg_reference/P002_设备树地址范围映射宏.md)。

<a id="r_devicetree-reg-prop"></a>

相关声明：[寄存器区域属性（reg Property）](../dt_reg_reference/P001_设备树寄存器属性宏.md)。

## 1.2\_源码定位与版本边界

相对源码定位：[电池曲线常量](../../../include/zephyr/dt-bindings/battery/battery.h)、[电池查表接口](../../../include/zephyr/drivers/sensor/battery.h)、[组合电量计驱动](../../../drivers/fuel_gauge/composite/fuel_gauge_composite.c)、[电池绑定](../../../dts/bindings/battery/battery.yaml)、[组合电量计绑定](../../../dts/bindings/fuel-gauge/zephyr,fuel-gauge-composite.yaml)、[选定SRAM宏](../../../include/zephyr/devicetree/sram.h)和[架构配置](../../../arch/Kconfig)。本次官方文件摘要见[来源记录](../SOURCES.md)。

> 译注——源码核对：入口范围：此页是设备树（Devicetree）API的主题总览，保留原有41个主题及链接；已翻译目标使用相对链接，尚未翻译目标保留官方入口。完成本总览不代表其所有子主题均已翻译，逐页状态以全站清单为准。

> 译注——源码核对：版本字段：Since 2.2表示该API文档所列的引入版本，Version 1.2.0是这里标示的API版本，不是当前Zephyr发行版，也不是本仓库源码版本。

> 译注——源码核对：版本边界：本批记录七份官方源码／绑定的读取摘要；两个源码浏览页的非注释代码与本次读取的对应原始头文件一致。latest和main会滚动变化，本仓库参照源码与它们不自动视为相同版本；本次未编译示例、构建固件或执行硬件实验。

本次验证范围为文档与源码对照，未编译宏／DTS示例、构建固件或操作硬件。

## 1.3\_原页交叉引用（Cross References）

- [逐项展开宏（For-each Macros）](../dt_foreach_reference/P001_设备树遍历宏.md)
- [总线辅助宏（Bus Helpers）](../dt_node_reference/P001_设备树总线查询宏.md)
- [选定节点（Chosen Nodes）](../dt_node_reference/P002_设备树chosen节点宏.md)
- [依赖跟踪（Dependency Tracking）](../dt_node_reference/P004_设备树依赖顺序宏.md)
- [设备树控制器局域网接口（Devicetree CAN API）](../hardware/P373_CAN设备树宏.md)
- [设备树时钟接口（Devicetree Clocks API）](../timer_reference/P107_设备树时钟获取宏.md)
- [设备树计数器捕获接口（Devicetree Counter Captures API）](../timer_reference/P034_计数器捕获设备树宏.md)
- [设备树直接存储器访问接口（Devicetree DMA API）](../dma_reference/P008_DMA设备树宏.md)
- [设备树显示接口（Devicetree Display API）](../hardware/P227_设备树显示接口.md)
- [设备树固定分区接口（Devicetree Fixed Partition API）](../dt_partition_reference/P002_设备树固定分区宏.md)
- [设备树通用输入输出接口（Devicetree GPIO API）](../hardware/P290_设备树GPIO宏.md)
- [设备树硬件自旋锁接口（Devicetree HW Spinlock API）](../intercore_reference/P008_硬件自旋锁设备树宏.md)
- [设备树输入输出通道接口（Devicetree IO Channels API）](../dt_connection_reference/P001_设备树I_O通道宏.md)
- [设备树中断CPU接口（Devicetree Interrupt CPU API）](../dt_node_reference/P003_设备树CPU节点宏.md)
- [设备树中断控制器接口（Devicetree Interrupt Controller API）](../dt_irq_reference/P002_设备树中断控制器宏.md)
- [设备树邮箱接口（Devicetree MBOX API）](../intercore_reference/P021_邮箱设备树访问宏.md)
- [设备树多路复用器接口（Devicetree MUX API）](../dt_connection_reference/P007_设备树多路复用器宏.md)
- [设备树映射分区接口（Devicetree Mapped Partition API）](../dt_partition_reference/P005_设备树映射分区宏.md)
- [设备树脉宽调制接口（Devicetree PWMs API）](../hardware/P264_设备树PWM宏.md)
- [设备树分区接口（Devicetree Partition API）](../dt_partition_reference/P001_设备树通用分区宏.md)
- [设备树端口与端点接口（Devicetree Port Endpoint API）](../dt_connection_reference/P010_设备树端口与端点宏.md)
- [设备树稳压器接口（Devicetree Regulator API）](../power/P081_设备树稳压器辅助接口目录.md)
- [设备树Renesas RA事件链接控制器辅助宏（Devicetree Renesas RA ELC Helpers）](https://docs.zephyrproject.org/latest/doxygen/html/group__dt__renesas__ra__elc.html)
- [设备树复位控制器接口（Devicetree Reset Controller API）](../reset_reference/P007_复位控制器设备树辅助宏.md)
- [设备树串行外设接口（Devicetree SPI API）](../hardware/P329_SPI设备树宏.md)
- [设备树静态随机存取存储器接口（Devicetree SRAM API）](P005_选定SRAM区域宏.md)
- [设备树唤醒控制器接口（Devicetree WUC Controller API）](../dt_irq_reference/P005_设备树唤醒控制器宏.md)
- [设备树电池辅助宏（Devicetree Battery Helpers）](P002_电池开路电压曲线宏.md)
- [设备树内存属性（Devicetree Memory Attributes）](../dt_memory_attribute_reference/P001_设备树内存属性总览.md)
- [存在性检查（Existence Checks）](../dt_identity_reference/P002_设备树存在性与状态宏.md)
- [基于实例的设备树接口（Instance-based Devicetree APIs）](../dt_instance_reference/P001_设备树驱动实例宏.md)
- [映射辅助宏（Map Helpers）](../dt_connection_reference/P004_设备树描述符映射宏.md)
- [非易失性存储器设备树辅助宏（NVMEM Devicetree Helpers）](../storage/P018_NVMEM设备树辅助宏.md)
- [NXP i.MX952电源域（Power Domains）](https://docs.zephyrproject.org/latest/doxygen/html/group__imx952__power__domains.html)
- [节点标识符及辅助宏（Node Identifiers and Helpers）](../dt_identity_reference/P001_设备树节点标识宏.md)
- [引脚控制（Pin Control）](../pinctrl_reference/P005_引脚控制设备树宏.md)
- [属性访问器（Property Accessors）](../dt_property_reference/P001_设备树属性读取宏.md)
- [厂商与型号名称辅助宏（Vendor and Model Name Helpers）](../dt_identity_reference/P003_设备树厂商与型号宏.md)
- [中断属性（interrupts Property）](../dt_irq_reference/P001_设备树中断属性宏.md)
- [地址范围映射属性（ranges Property）](../dt_reg_reference/P002_设备树地址范围映射宏.md)
- [寄存器区域属性（reg Property）](../dt_reg_reference/P001_设备树寄存器属性宏.md)

<a id="header-details"></a>

---

[返回大纲](大纲.md) · [下一章](P002_电池开路电压曲线宏.md)
