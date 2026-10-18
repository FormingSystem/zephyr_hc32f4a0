---
id: learning.zephyr-docs.led-sct-ti-xpowers-binding-reference.page-20
title: zephyr_native-linux-leds
kind: reference
status: maintained
domains: [zephyr, devicetree, led]
source_url: https://docs.zephyrproject.org/latest/build/dts/api/bindings/led/zephyr,native-linux-leds.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号与导航为本地新增。 -->

# 第20章\_zephyr_native-linux-leds

原文：[官方页面](https://docs.zephyrproject.org/latest/build/dts/api/bindings/led/zephyr,native-linux-leds.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="zephyr-native-linux-leds"></a>
<a id="dtbinding-zephyr-native-linux-leds"></a>
<a id="std-dtcompatible-zephyr-native-linux-leds"></a>

兼容字符串（Compatible String）：`zephyr,native-linux-leds`。厂商：[ Zephyr Project ](https://docs.zephyrproject.org/latest/build/dts/api/bindings.html#dt-vendor-zephyr)。

采用此设备树绑定（Devicetree Binding）的开发板见[官方筛选目录](https://docs.zephyrproject.org/latest/boards/index.html#compatibles=zephyr,native-linux-leds)。

驱动源码（Driver Source）：[drivers/led/linux_leds.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/led/linux_leds.c)。

<a id="description"></a>

以Linux LED为后端（Backend）的LED设备。

<a id="examples"></a>

官方设备树配置原例：

```dts
/ {
  leds {
    compatible = "zephyr,native-linux-leds";

    led0: led_0 {
      /* /sys/class/leds/tpacpi::lid_logo_dot/brightness */
      path = "tpacpi::lid_logo_dot";
    };
    led1: led_1 {
      /* /sys/class/leds/tpacpi::power/brightness */
      path = "tpacpi::power";
    };
  };
};
```

<a id="properties"></a>

属性类型：`int` 为整数，`boolean` 为布尔属性，`string` 为字符串，`string-array` 为字符串数组，`array` 为数值数组，`compound` 为复合类型；`phandle` 为节点引用（Phandle），`phandles` 为节点引用列表，`phandle-array` 为节点引用与说明符单元数组。

<a id="top-level-properties"></a>

## 20.1\_节点专用属性

这些属性不继承自基础绑定文件。

本页没有节点专用属性。

本页没有已弃用的节点专用属性。

<a id="child-node-properties"></a>

## 子节点属性

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `path` | `string` | **必需**。原文没有提供文字说明 |
| `label` | `string` | 描述LED的可读字符串（Human-Readable String）。应用可用它识别LED，或取得此LED在父设备上的编号／索引，即子节点编号（Child Node Number）。 |

---

[上一章](P019_x-powers_axp2101-led.md) · [本册大纲](大纲.md) · [全站翻译进度](../PROGRESS.md)
