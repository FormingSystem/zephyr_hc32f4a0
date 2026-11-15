---
id: learning.zephyr-docs.api-interaction-transport-topic-reference.page-5
title: LVGL 键盘按键（Keypad keys）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__lvgl__keypad__dt.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第5章\_LVGL 键盘按键（Keypad keys）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__lvgl__keypad__dt.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

供设备树（Devicetree）使用的预定义 LVGL 按键。

<a id="details"></a>

供设备树（Devicetree）使用的预定义 LVGL 按键（Keys）。在 `zephyr,lvgl-keypad-input` 节点的 `lvgl-codes` 属性中使用，将输入事件代码映射为 LVGL 按键；取值与 LVGL 的 `lv_group.h` 中的 `enum _lv_key_t` 对应。设备树用法见下方原始示例。**另请参见（See Also）：**[LVGL 按键说明](https://lvgl.io/docs/open/main-modules/indev/keypad#keys)。

```c
#include <zephyr/dt-bindings/input/input-event-codes.h>
#include <zephyr/dt-bindings/lvgl/lvgl.h>

keypad {
        compatible = "zephyr,lvgl-keypad-input";
        input = <&buttons>;
        input-codes = <INPUT_KEY_1 INPUT_KEY_2>;
        lvgl-codes = <LV_KEY_NEXT LV_KEY_PREV>;
};
```

<a id="header-files"></a>
<a id="files"></a>

## 5.1\_文件（Files）

<a id="r_lvgl_2Eh"></a>

```c
file lvgl.h
```

相关声明：[lvgl.h](https://docs.zephyrproject.org/latest/doxygen/html/lvgl_8h.html)。

LVGL键盘输入按键（Keypad Input Keys）的设备树定义。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 5.2\_宏定义（Macros）

<a id="r_ga1c8b58f3efc157565749586f93737e0e"></a>

```c
#define LV_KEY_UP 17
```

相关声明：[LV_KEY_UP](#ga1c8b58f3efc157565749586f93737e0e)。

向上移动或增大数值（Move Up/Increase Value）。

<a id="r_gae49f8f5c72c13dc6eb4a5589e2f780ea"></a>

```c
#define LV_KEY_DOWN 18
```

相关声明：[LV_KEY_DOWN](#gae49f8f5c72c13dc6eb4a5589e2f780ea)。

向下移动或减小数值（Move Down/Decrease Value）。

<a id="r_ga83b368e839504a6842616059b605c81b"></a>

```c
#define LV_KEY_RIGHT 19
```

相关声明：[LV_KEY_RIGHT](#ga83b368e839504a6842616059b605c81b)。

向右移动或增大数值（Move Right/Increase Value）。

<a id="r_ga6ffddd2dac77d37538a6137e2adaac2e"></a>

```c
#define LV_KEY_LEFT 20
```

相关声明：[LV_KEY_LEFT](#ga6ffddd2dac77d37538a6137e2adaac2e)。

向左移动或减小数值（Move Left/Decrease Value）。

<a id="r_gaebb20f88787d9588485f0c4669b98e77"></a>

```c
#define LV_KEY_ESC 27
```

相关声明：[LV_KEY_ESC](#gaebb20f88787d9588485f0c4669b98e77)。

关闭或退出（Close/Exit），例如：

<a id="r_ga093b17aabff2b8d39e6d1c9157eba5c0"></a>

```c
#define LV_KEY_DEL 127
```

相关声明：[LV_KEY_DEL](#ga093b17aabff2b8d39e6d1c9157eba5c0)。

删除（Delete）。

<a id="r_ga17753764ea3cae6cd93836a817af2545"></a>

```c
#define LV_KEY_BACKSPACE 8
```

相关声明：[LV_KEY_BACKSPACE](#ga17753764ea3cae6cd93836a817af2545)。

删除左侧字符（Delete Character to the Left）。

<a id="r_gaeed4a52fc34da0944b5e11921513565a"></a>

```c
#define LV_KEY_ENTER 10
```

相关声明：[LV_KEY_ENTER](#gaeed4a52fc34da0944b5e11921513565a)。

确认、选择或切换编辑模式（Confirm/Select/Toggle Edit Mode）。

<a id="r_ga11afbd5429841e10a2feacec95fb5635"></a>

```c
#define LV_KEY_NEXT 9
```

相关声明：[LV_KEY_NEXT](#ga11afbd5429841e10a2feacec95fb5635)。

聚焦组中的下一个对象（Focus Next Object）。

<a id="r_gab14253e4ae44cba9cdb5ea421ab8ac1f"></a>

```c
#define LV_KEY_PREV 11
```

相关声明：[LV_KEY_PREV](#gab14253e4ae44cba9cdb5ea421ab8ac1f)。

聚焦组中的上一个对象（Focus Previous Object）。

<a id="r_ga94253183c5b548d8e969c2776deb1e66"></a>

```c
#define LV_KEY_HOME 2
```

相关声明：[LV_KEY_HOME](#ga94253183c5b548d8e969c2776deb1e66)。

转到开头／顶部（Beginning/Top）。

<a id="r_ga2f8f0e6a0ade01bc8888e30c1b5192b7"></a>

```c
#define LV_KEY_END 3
```

相关声明：[LV_KEY_END](#ga2f8f0e6a0ade01bc8888e30c1b5192b7)。

转到末尾／底部（End/Bottom）。

## 5.3\_详细说明（Detailed Documentation）

<a id="ga17753764ea3cae6cd93836a817af2545"></a>

### `LV_KEY_BACKSPACE`

```c
#define LV_KEY_BACKSPACE 8
```

```c
#include <zephyr/dt-bindings/lvgl/lvgl.h>
```

删除左侧字符（Delete Character to the Left）。

<a id="ga093b17aabff2b8d39e6d1c9157eba5c0"></a>

### `LV_KEY_DEL`

```c
#define LV_KEY_DEL 127
```

```c
#include <zephyr/dt-bindings/lvgl/lvgl.h>
```

删除（Delete）。

<a id="gae49f8f5c72c13dc6eb4a5589e2f780ea"></a>

### `LV_KEY_DOWN`

```c
#define LV_KEY_DOWN 18
```

```c
#include <zephyr/dt-bindings/lvgl/lvgl.h>
```

向下移动或减小数值（Move Down/Decrease Value）。

<a id="ga2f8f0e6a0ade01bc8888e30c1b5192b7"></a>

### `LV_KEY_END`

```c
#define LV_KEY_END 3
```

```c
#include <zephyr/dt-bindings/lvgl/lvgl.h>
```

转到末尾／底部（End/Bottom）。

<a id="gaeed4a52fc34da0944b5e11921513565a"></a>

### `LV_KEY_ENTER`

```c
#define LV_KEY_ENTER 10
```

```c
#include <zephyr/dt-bindings/lvgl/lvgl.h>
```

确认、选择或切换编辑模式（Confirm/Select/Toggle Edit Mode）。

<a id="gaebb20f88787d9588485f0c4669b98e77"></a>

### `LV_KEY_ESC`

```c
#define LV_KEY_ESC 27
```

```c
#include <zephyr/dt-bindings/lvgl/lvgl.h>
```

关闭或退出（Close/Exit），例如：

退出编辑模式（Leave Edit Mode）。

<a id="ga94253183c5b548d8e969c2776deb1e66"></a>

### `LV_KEY_HOME`

```c
#define LV_KEY_HOME 2
```

```c
#include <zephyr/dt-bindings/lvgl/lvgl.h>
```

转到开头／顶部（Beginning/Top）。

<a id="ga6ffddd2dac77d37538a6137e2adaac2e"></a>

### `LV_KEY_LEFT`

```c
#define LV_KEY_LEFT 20
```

```c
#include <zephyr/dt-bindings/lvgl/lvgl.h>
```

向左移动或减小数值（Move Left/Decrease Value）。

<a id="ga11afbd5429841e10a2feacec95fb5635"></a>

### `LV_KEY_NEXT`

```c
#define LV_KEY_NEXT 9
```

```c
#include <zephyr/dt-bindings/lvgl/lvgl.h>
```

聚焦组中的下一个对象（Focus Next Object）。

<a id="gab14253e4ae44cba9cdb5ea421ab8ac1f"></a>

### `LV_KEY_PREV`

```c
#define LV_KEY_PREV 11
```

```c
#include <zephyr/dt-bindings/lvgl/lvgl.h>
```

聚焦组中的上一个对象（Focus Previous Object）。

<a id="ga83b368e839504a6842616059b605c81b"></a>

### `LV_KEY_RIGHT`

```c
#define LV_KEY_RIGHT 19
```

```c
#include <zephyr/dt-bindings/lvgl/lvgl.h>
```

向右移动或增大数值（Move Right/Increase Value）。

<a id="ga1c8b58f3efc157565749586f93737e0e"></a>

### `LV_KEY_UP`

```c
#define LV_KEY_UP 17
```

```c
#include <zephyr/dt-bindings/lvgl/lvgl.h>
```

向上移动或增大数值（Move Up/Increase Value）。


## 5.4\_原页交叉引用（Cross References）

- [lvgl.h](https://docs.zephyrproject.org/latest/doxygen/html/lvgl_8h.html)
- [zephyr,lvgl-keypad-input](../input_touch_lvgl_gesture_binding_reference/P019_zephyr_lvgl-keypad-input.md#std-dtcompatible-zephyr-lvgl-keypad-input)
- [https://lvgl.io/docs/open/main-modules/indev/keypad#keys](https://lvgl.io/docs/open/main-modules/indev/keypad#keys)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[上一章](P004_FTDI FT8xx API主题.md) · [返回大纲](大纲.md) · [下一章](P006_浮点到定点转换（Float to Fixed point conversions）.md)
