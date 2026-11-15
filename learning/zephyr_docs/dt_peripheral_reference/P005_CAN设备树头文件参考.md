---
id: learning.zephyr-docs.dt-peripheral-reference.page-5
title: CAN设备树头文件参考
kind: reference
status: maintained
domains: [zephyr, hardware, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/devicetree_2can_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第5章\_CAN设备树头文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/devicetree_2can_8h.html)。读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

> 译注——阅读位置：从[本册大纲](大纲.md)选择GPIO、SPI、CAN或显示设备树头文件，再通过接口链接进入完整说明。源码跟踪译注与官方原文分开标示。

控制器局域网（CAN）设备树宏公共 API 头文件。

查看此文件的源码。

<a id="details"></a>

控制器局域网（CAN）设备树宏公共 API 头文件。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 5.1\_宏定义（Macros）

<a id="r_ga60cb3dc5c2feb517dddcb5a57cce8a9b"></a>

```c
#define DT_CAN_TRANSCEIVER_MIN_BITRATE(node_id, min)
```

相关声明：[DT_CAN_TRANSCEIVER_MIN_BITRATE](../hardware/P373_CAN设备树宏.md#ga60cb3dc5c2feb517dddcb5a57cce8a9b)、[min](../numeric_reference/P001_最小最大值与限幅宏参考.md#ac6afabdc09a49a433ee19d8a9486056d)。

取得 CAN 控制器的收发器最低比特率（Minimum Transceiver Bitrate）。

<a id="r_ga9c56ded2142fbd8a4a7facffd3dd549d"></a>

```c
#define DT_CAN_TRANSCEIVER_MAX_BITRATE(node_id, max)
```

相关声明：[DT_CAN_TRANSCEIVER_MAX_BITRATE](../hardware/P373_CAN设备树宏.md#ga9c56ded2142fbd8a4a7facffd3dd549d)、[max](../numeric_reference/P001_最小最大值与限幅宏参考.md#affe776513b24d84b39af8ab0930fef7f)。

取得 CAN 控制器的收发器最高比特率（Maximum Transceiver Bitrate）。

<a id="r_ga5c0b8011b5ec85dd8772f33572ae2b71"></a>

```c
#define DT_INST_CAN_TRANSCEIVER_MIN_BITRATE(inst, min)
```

相关声明：[DT_INST_CAN_TRANSCEIVER_MIN_BITRATE](../hardware/P373_CAN设备树宏.md#ga5c0b8011b5ec85dd8772f33572ae2b71)、[min](../numeric_reference/P001_最小最大值与限幅宏参考.md#ac6afabdc09a49a433ee19d8a9486056d)。

取得 DT_DRV_COMPAT CAN 控制器实例的收发器最低比特率。

<a id="r_gacac28e33d8a749518485c687a563763f"></a>

```c
#define DT_INST_CAN_TRANSCEIVER_MAX_BITRATE(inst, max)
```

相关声明：[DT_INST_CAN_TRANSCEIVER_MAX_BITRATE](../hardware/P373_CAN设备树宏.md#gacac28e33d8a749518485c687a563763f)、[max](../numeric_reference/P001_最小最大值与限幅宏参考.md#affe776513b24d84b39af8ab0930fef7f)。

取得 DT_DRV_COMPAT CAN 控制器实例的收发器最高比特率。

## 5.2\_源码定位与版本边界

相对源码定位：[GPIO宏](../../../include/zephyr/devicetree/gpio.h)、[SPI宏](../../../include/zephyr/devicetree/spi.h)、[CAN宏](../../../include/zephyr/devicetree/can.h)、[显示宏](../../../include/zephyr/devicetree/display.h)、[宏生成器](../../../scripts/dts/gen_defines.py)和[显示列表绑定](../../../dts/bindings/display/zephyr,displays.yaml)。本次官方源码摘要见[来源记录](../SOURCES.md)。

> 译注——源码核对：下限取大、上限取小：MIN_BITRATE返回收发器下限与调用方min的较大值，MAX_BITRATE返回收发器上限与调用方max的较小值，相当于组合双方支持范围的边界；宏不会设置CAN比特率，也不会自动检查合并后的下限是否超过上限。

> 译注——源码核对：两条描述路径：控制器有phys属性时读取它引用的首个收发器节点；此分支min-bitrate缺失默认0，但max-bitrate使用DT_PROP，没有缺失回退。没有phys属性时读取名为can-transceiver的子节点，并分别使用调用方min／max作为默认值。不能只根据两个宏的名称对称就推断它们对缺失属性的行为相同。

> 译注——源码核对：版本边界：本批记录四份设备树头文件、gen_defines.py和zephyr,displays绑定，共六份官方源码摘要；四个源码浏览页的非注释代码与本次读取的原始头文件一致。latest、滚动main和本仓库参照版本不自动等同。本次未构建设备树、配置引脚、执行SPI／CAN传输、初始化显示设备或操作硬件。

本次验证范围为文档与源码对照，未编译宏／DTS示例、构建固件或操作硬件。

## 5.3\_原页交叉引用（Cross References）

- [查看此文件的源码](P006_CAN设备树头文件源码.md)
- [DT_CAN_TRANSCEIVER_MIN_BITRATE](../hardware/P373_CAN设备树宏.md#ga60cb3dc5c2feb517dddcb5a57cce8a9b)
- [min](../numeric_reference/P001_最小最大值与限幅宏参考.md#ac6afabdc09a49a433ee19d8a9486056d)
- [DT_CAN_TRANSCEIVER_MAX_BITRATE](../hardware/P373_CAN设备树宏.md#ga9c56ded2142fbd8a4a7facffd3dd549d)
- [max](../numeric_reference/P001_最小最大值与限幅宏参考.md#affe776513b24d84b39af8ab0930fef7f)
- [DT_INST_CAN_TRANSCEIVER_MIN_BITRATE](../hardware/P373_CAN设备树宏.md#ga5c0b8011b5ec85dd8772f33572ae2b71)
- [DT_INST_CAN_TRANSCEIVER_MAX_BITRATE](../hardware/P373_CAN设备树宏.md#gacac28e33d8a749518485c687a563763f)

<a id="header-details"></a>

---

[上一章](P004_SPI设备树头文件源码.md) · [返回大纲](大纲.md) · [下一章](P006_CAN设备树头文件源码.md)
