---
id: learning.zephyr-docs.input-touch-lvgl-gesture-binding-reference.page-10
title: tsc-keys
kind: reference
status: maintained
domains: [zephyr, devicetree, input]
source_url: https://docs.zephyrproject.org/latest/build/dts/api/bindings/input/tsc-keys.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号与导航为本地新增。 -->

# 第10章\_tsc-keys

原文：[官方页面](https://docs.zephyrproject.org/latest/build/dts/api/bindings/input/tsc-keys.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="tsc-keys"></a>
<a id="dtbinding-tsc-keys"></a>
<a id="std-dtcompatible-tsc-keys"></a>

兼容字符串（Compatible String）：`tsc-keys`。厂商：[ 无厂商前缀 ](https://docs.zephyrproject.org/latest/build/dts/api/bindings.html#dt-no-vendor)。

采用此设备树绑定（Devicetree Binding）的开发板见[官方筛选目录](https://docs.zephyrproject.org/latest/boards/index.html#compatibles=tsc-keys)。

<a id="description"></a>

STM32触摸感测控制器（Touch Sensing Controller，TSC）的输入驱动。

该节点是 `st,stm32-tsc` 的孙节点，通过滤波和计算检测父分组的输入事件；分组自身是 `st,stm32-tsc` 的子节点。原文进一步说明指向 `drivers/misc/st,stm32-tsc.yaml`，对应的[官方TSC绑定页](P007_st_stm32-tsc.md)也收录于本批。

<a id="examples"></a>

官方设备树配置原例：

```dts
#include <zephyr/dt-bindings/input/input-event-codes.h>

&tsc {
  compatible = "st,stm32-tsc";

  tsc_group6: g6 {
    /* ... */
    ts1 {
      compatible = "tsc-keys";
      sampling-interval-ms = <10>;
      oversampling = <10>;
      noise-threshold = <50>;
      zephyr,code = <INPUT_KEY_0>;
    };
  };
};
```

译注：原文说明提到过采样默认10和释放超时默认10秒，但属性表将相关字段标为必需，且没有列出默认值；原例也未填写 `sticky-key-timeout-ms`。这里分别保留原说明、约束与代码，不将文字中的默认行为改写为可省略配置。

<a id="properties"></a>

属性类型：`int` 为整数，`boolean` 为布尔属性，`string` 为字符串，`string-array` 为字符串数组，`array` 为数值数组，`uint8-array` 为8位无符号整数数组，`compound` 为复合类型；`phandle` 为节点引用（Phandle），`phandles` 为节点引用列表，`phandle-array` 为节点引用与说明符单元数组。

## 10.1\_节点专用属性

这些属性不继承自基础绑定文件。

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `sampling-interval-ms` | `int` | **必需**。采样间隔（Sampling Interval），单位为毫秒。 |
| `oversampling` | `int` | **必需**。过采样系数（Oversampling Factor）。驱动对采样间隔内获得的样本求平均，再与上一次样本比较。值越大，噪声越小但延迟越大。原文说明默认值为10，因此每 `10 * sampling-interval-ms` 毫秒计算一次斜率。 |
| `noise-threshold` | `int` | **必需**。用于抑制斜率两个方向上的噪声（Noise Rejection）的值。 |
| `sticky-key-timeout-ms` | `int` | **必需**。释放按键前等待的时间（Key Release Timeout），单位为毫秒。原文说明默认情况下，若按键仍处于按下状态，会在最后一次按下事件后10秒生成释放事件。 |
| `zephyr,code` | `int` | **必需**。要上报的按键码（Key Code）。 |

本页没有已弃用的节点专用属性。

## 10.2\_基础属性

以下属性继承自基础绑定（Base Binding），定义可用于许多节点的通用属性，**并非全部一定适用于本兼容字符串**。

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `status` | `string` | 节点代表的硬件或其他资源的运行状态（Operational Status）。`okay` 表示资源可运行，例如可供驱动使用；`disabled` 表示资源不可运行，系统应将其视为不存在。参见《设备树规范》（Devicetree Specification）v0.4第2.3.4节；合法值：`okay, disabled, reserved, fail, fail-sss` |
| `compatible` | `string-array` | **必需**。字符串列表定义节点代表的硬件或其他资源类型。设备驱动通过特定兼容字符串（Compatible String）寻找应由自身管理的设备。推荐格式为 `vendor,device`：前者是厂商简称，后者通常来自数据手册。多个值从最具体到最通用排列，让具体设备匹配当前可用的最具体驱动。参见规范v0.4第2.3.1节 |
| `label` | `string` | 描述设备的可读字符串；除逐案确有需要外，已不推荐使用此属性。参见规范 v0.4 第 4.1.2 节“其他属性” |
| `zephyr,deferred-init` | `boolean` | 延迟初始化（Deferred Initialization）：启动时不自动初始化设备，应由应用使用 `device_init()` 手动初始化 |

属性说明中的“重要属性”参见[设备树语法与结构](../devicetree/P003_语法与结构.md#dt-important-props)。

---

[上一章](P009_tbs_crsf.md) · [本册大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P011_vishay_vs1838b.md)
