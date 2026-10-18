---
id: learning.zephyr-docs.api-file-transfer-device-reference.page-22
title: zephyr__dt-bindings__lvgl__lvgl.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/lvgl_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第22章\_zephyr\_\_dt-bindings\_\_lvgl\_\_lvgl.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/lvgl_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

LVGL键盘输入按键（Keypad Input Keys）的设备树定义。

查看此文件的源码。

<a id="details"></a>

LVGL键盘输入按键（Keypad Input Keys）的设备树定义。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 22.1\_宏定义（Macros）

<a id="r_ga1c8b58f3efc157565749586f93737e0e"></a>

```c
#define LV_KEY_UP 17
```

相关声明：[LV_KEY_UP](../api_interaction_transport_topic_reference/P005_LVGL 键盘按键（Keypad keys）.md#ga1c8b58f3efc157565749586f93737e0e)。

向上移动或增大数值（Move Up/Increase Value）。

<a id="r_gae49f8f5c72c13dc6eb4a5589e2f780ea"></a>

```c
#define LV_KEY_DOWN 18
```

相关声明：[LV_KEY_DOWN](../api_interaction_transport_topic_reference/P005_LVGL 键盘按键（Keypad keys）.md#gae49f8f5c72c13dc6eb4a5589e2f780ea)。

向下移动或减小数值（Move Down/Decrease Value）。

<a id="r_ga83b368e839504a6842616059b605c81b"></a>

```c
#define LV_KEY_RIGHT 19
```

相关声明：[LV_KEY_RIGHT](../api_interaction_transport_topic_reference/P005_LVGL 键盘按键（Keypad keys）.md#ga83b368e839504a6842616059b605c81b)。

向右移动或增大数值（Move Right/Increase Value）。

<a id="r_ga6ffddd2dac77d37538a6137e2adaac2e"></a>

```c
#define LV_KEY_LEFT 20
```

相关声明：[LV_KEY_LEFT](../api_interaction_transport_topic_reference/P005_LVGL 键盘按键（Keypad keys）.md#ga6ffddd2dac77d37538a6137e2adaac2e)。

向左移动或减小数值（Move Left/Decrease Value）。

<a id="r_gaebb20f88787d9588485f0c4669b98e77"></a>

```c
#define LV_KEY_ESC 27
```

相关声明：[LV_KEY_ESC](../api_interaction_transport_topic_reference/P005_LVGL 键盘按键（Keypad keys）.md#gaebb20f88787d9588485f0c4669b98e77)。

关闭或退出（Close/Exit），例如：

<a id="r_ga093b17aabff2b8d39e6d1c9157eba5c0"></a>

```c
#define LV_KEY_DEL 127
```

相关声明：[LV_KEY_DEL](../api_interaction_transport_topic_reference/P005_LVGL 键盘按键（Keypad keys）.md#ga093b17aabff2b8d39e6d1c9157eba5c0)。

删除（Delete）。

<a id="r_ga17753764ea3cae6cd93836a817af2545"></a>

```c
#define LV_KEY_BACKSPACE 8
```

相关声明：[LV_KEY_BACKSPACE](../api_interaction_transport_topic_reference/P005_LVGL 键盘按键（Keypad keys）.md#ga17753764ea3cae6cd93836a817af2545)。

删除左侧字符（Delete Character to the Left）。

<a id="r_gaeed4a52fc34da0944b5e11921513565a"></a>

```c
#define LV_KEY_ENTER 10
```

相关声明：[LV_KEY_ENTER](../api_interaction_transport_topic_reference/P005_LVGL 键盘按键（Keypad keys）.md#gaeed4a52fc34da0944b5e11921513565a)。

确认、选择或切换编辑模式（Confirm/Select/Toggle Edit Mode）。

<a id="r_ga11afbd5429841e10a2feacec95fb5635"></a>

```c
#define LV_KEY_NEXT 9
```

相关声明：[LV_KEY_NEXT](../api_interaction_transport_topic_reference/P005_LVGL 键盘按键（Keypad keys）.md#ga11afbd5429841e10a2feacec95fb5635)。

聚焦组中的下一个对象（Focus Next Object）。

<a id="r_gab14253e4ae44cba9cdb5ea421ab8ac1f"></a>

```c
#define LV_KEY_PREV 11
```

相关声明：[LV_KEY_PREV](../api_interaction_transport_topic_reference/P005_LVGL 键盘按键（Keypad keys）.md#gab14253e4ae44cba9cdb5ea421ab8ac1f)。

聚焦组中的上一个对象（Focus Previous Object）。

<a id="r_ga94253183c5b548d8e969c2776deb1e66"></a>

```c
#define LV_KEY_HOME 2
```

相关声明：[LV_KEY_HOME](../api_interaction_transport_topic_reference/P005_LVGL 键盘按键（Keypad keys）.md#ga94253183c5b548d8e969c2776deb1e66)。

转到开头／顶部（Beginning/Top）。

<a id="r_ga2f8f0e6a0ade01bc8888e30c1b5192b7"></a>

```c
#define LV_KEY_END 3
```

相关声明：[LV_KEY_END](../api_interaction_transport_topic_reference/P005_LVGL 键盘按键（Keypad keys）.md#ga2f8f0e6a0ade01bc8888e30c1b5192b7)。

转到末尾／底部（End/Bottom）。


## 22.2\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_reference/P467_lvgl.h_源码浏览.md)
- [LV_KEY_UP](../api_interaction_transport_topic_reference/P005_LVGL 键盘按键（Keypad keys）.md#ga1c8b58f3efc157565749586f93737e0e)
- [LV_KEY_DOWN](../api_interaction_transport_topic_reference/P005_LVGL 键盘按键（Keypad keys）.md#gae49f8f5c72c13dc6eb4a5589e2f780ea)
- [LV_KEY_RIGHT](../api_interaction_transport_topic_reference/P005_LVGL 键盘按键（Keypad keys）.md#ga83b368e839504a6842616059b605c81b)
- [LV_KEY_LEFT](../api_interaction_transport_topic_reference/P005_LVGL 键盘按键（Keypad keys）.md#ga6ffddd2dac77d37538a6137e2adaac2e)
- [LV_KEY_ESC](../api_interaction_transport_topic_reference/P005_LVGL 键盘按键（Keypad keys）.md#gaebb20f88787d9588485f0c4669b98e77)
- [LV_KEY_DEL](../api_interaction_transport_topic_reference/P005_LVGL 键盘按键（Keypad keys）.md#ga093b17aabff2b8d39e6d1c9157eba5c0)
- [LV_KEY_BACKSPACE](../api_interaction_transport_topic_reference/P005_LVGL 键盘按键（Keypad keys）.md#ga17753764ea3cae6cd93836a817af2545)
- [LV_KEY_ENTER](../api_interaction_transport_topic_reference/P005_LVGL 键盘按键（Keypad keys）.md#gaeed4a52fc34da0944b5e11921513565a)
- [LV_KEY_NEXT](../api_interaction_transport_topic_reference/P005_LVGL 键盘按键（Keypad keys）.md#ga11afbd5429841e10a2feacec95fb5635)
- [LV_KEY_PREV](../api_interaction_transport_topic_reference/P005_LVGL 键盘按键（Keypad keys）.md#gab14253e4ae44cba9cdb5ea421ab8ac1f)
- [LV_KEY_HOME](../api_interaction_transport_topic_reference/P005_LVGL 键盘按键（Keypad keys）.md#ga94253183c5b548d8e969c2776deb1e66)
- [LV_KEY_END](../api_interaction_transport_topic_reference/P005_LVGL 键盘按键（Keypad keys）.md#ga2f8f0e6a0ade01bc8888e30c1b5192b7)

<a id="header-details"></a>

---

[上一章](P021_zephyr__sys__linear_range.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P023_zephyr__net__lwm2m_send_scheduler.h_文件参考.md)
