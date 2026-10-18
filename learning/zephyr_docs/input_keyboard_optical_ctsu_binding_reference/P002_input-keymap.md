---
id: learning.zephyr-docs.input-keyboard-optical-ctsu-binding-reference.page-2
title: input-keymap
kind: reference
status: maintained
domains: [zephyr, devicetree, input]
source_url: https://docs.zephyrproject.org/latest/build/dts/api/bindings/input/input-keymap.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号与导航为本地新增。 -->

# 第2章\_input-keymap

原文：[官方页面](https://docs.zephyrproject.org/latest/build/dts/api/bindings/input/input-keymap.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="input-keymap"></a>
<a id="dtbinding-input-keymap"></a>
<a id="std-dtcompatible-input-keymap"></a>

兼容字符串（Compatible String）：`input-keymap`。厂商：[ 无厂商前缀 ](https://docs.zephyrproject.org/latest/build/dts/api/bindings.html#dt-no-vendor)。

采用此设备树绑定（Devicetree Binding）的开发板见[官方筛选目录](https://docs.zephyrproject.org/latest/boards/index.html#compatibles=input-keymap)。

<a id="description"></a>

行列到按键映射器（Row-Column to Key Mapper）。监听父设备的行列事件，并上报按键事件。

<a id="examples"></a>

官方设备树配置原例：

```dts
#include <zephyr/dt-bindings/input/input-event-codes.h>
#include <zephyr/dt-bindings/input/keymap.h>

kbd {
    /* ... */
    keymap {
        compatible = "input-keymap";
        keymap = <
            MATRIX_KEY(0, 0, INPUT_KEY_1)
            MATRIX_KEY(0, 1, INPUT_KEY_2)
            MATRIX_KEY(0, 2, INPUT_KEY_3)
            MATRIX_KEY(1, 0, INPUT_KEY_4)
            MATRIX_KEY(1, 1, INPUT_KEY_5)
            MATRIX_KEY(1, 2, INPUT_KEY_6)
            MATRIX_KEY(2, 0, INPUT_KEY_7)
            MATRIX_KEY(2, 1, INPUT_KEY_8)
            MATRIX_KEY(2, 2, INPUT_KEY_9)
        >;
        row-size = <3>;
        col-size = <3>;
    };
};
```

<a id="properties"></a>

属性类型：`int` 为整数，`boolean` 为布尔属性，`string` 为字符串，`string-array` 为字符串数组，`array` 为数值数组，`uint8-array` 为8位无符号整数数组，`compound` 为复合类型；`phandle` 为节点引用（Phandle），`phandles` 为节点引用列表，`phandle-array` 为节点引用与说明符单元数组。

## 2.1\_节点专用属性

这些属性不继承自基础绑定文件。

| 属性 | 类型 | 中文说明与约束 |
| --- | --- | --- |
| `keymap` | `array` | **必需**。使用 `MATRIX_KEY()` 宏定义的按键码列表（Key Code List）。 |
| `row-size` | `int` | **必需**。键位映射（Keymap）的行数。；范围：`1 to 255` |
| `col-size` | `int` | **必需**。键位映射（Keymap）的列数。；范围：`1 to 255` |

本页没有已弃用的节点专用属性。

---

[上一章](P001_ilitek_ili2132a.md) · [本册大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P003_ite_it51xxx-kbd.md)
