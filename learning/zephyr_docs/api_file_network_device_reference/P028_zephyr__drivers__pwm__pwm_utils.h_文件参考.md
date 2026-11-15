---
id: learning.zephyr-docs.api-file-network-device-reference.page-28
title: zephyr__drivers__pwm__pwm_utils.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/pwm__utils_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第28章\_zephyr\_\_drivers\_\_pwm\_\_pwm\_utils.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/pwm__utils_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <stdbool.h>
#include <stdint.h>
#include <errno.h>
#include <zephyr/devicetree.h>
#include <zephyr/drivers/pwm.h>
#include <zephyr/sys/__assert.h>
#include <zephyr/sys/slist.h>
```

查看此文件的源码。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 28.1\_函数（Functions）

<a id="r_ab51f5b6439ced8b87cd5953d8f510f65"></a>

```c
static int pwm_manage_event_callback (sys_slist_t *callbacks, struct pwm_event_callback *callback, bool set)
```

相关声明：[pwm_manage_event_callback](#ab51f5b6439ced8b87cd5953d8f510f65)、[sys_slist_t](../slist_reference/P001_单向链表公共接口.md#ga44658c336b634c03938a251cdc8134f8)、[pwm_event_callback](../hardware/P257_PWM事件回调结构.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

在回调链表（Callback List）中插入或移除回调的通用函数。

<a id="r_aa5e4496e8856b41b0992c33953f60426"></a>

```c
static void pwm_fire_event_callbacks (sys_slist_t *list, const struct device *dev, uint32_t channel, pwm_events_t events)
```

相关声明：[pwm_fire_event_callbacks](#aa5e4496e8856b41b0992c33953f60426)、[sys_slist_t](../slist_reference/P001_单向链表公共接口.md#ga44658c336b634c03938a251cdc8134f8)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[pwm_events_t](../hardware/P255_PWM公共接口.md#ga5bc9607de7643cb78476ed354c51560b)。

遍历回调列表（Callback List）并调用其中回调的通用函数。

## 28.2\_详细说明（Detailed Documentation）

<a id="aa5e4496e8856b41b0992c33953f60426"></a>

### `pwm_fire_event_callbacks()`

```c
void pwm_fire_event_callbacks ( sys_slist_t * list, const struct device * dev, uint32_t channel, pwm_events_t events )
```

声明属性：`inline`、`static`。

遍历回调列表（Callback List）并调用其中回调的通用函数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `list` | 指向 PWM 事件回调列表（Event Callback List）的指针。 |
| `dev` | 指向 PWM 驱动实例（Driver Instance）的指针。 |
| `channel` | 触发该中断的通道（Channel）。 |
| `events` | 触发该中断的事件（Event）。 |

<a id="ab51f5b6439ced8b87cd5953d8f510f65"></a>

### `pwm_manage_event_callback()`

```c
int pwm_manage_event_callback ( sys_slist_t * callbacks, struct pwm_event_callback * callback, bool set )
```

声明属性：`inline`、`static`。

在回调链表（Callback List）中插入或移除回调的通用函数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `callbacks` | 指向原始回调列表（Callback List）的指针，可为 `NULL`。 |
| `callback` | 指向要插入列表或从列表移除的回调的指针。 |
| `set` | 指示插入还是移除回调的布尔值（Boolean）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时返回。 |
| `negate` | 失败时的 `errno` 错误码。 |


## 28.3\_原页交叉引用（Cross References）

- [stdbool.h](../api_source_supplement_reference/P186_stdbool.h_源码浏览.md)
- [stdint.h](../api_source_device_reference/P036_stdint.h_源码浏览.md)
- [errno.h](../error_reference/P005_错误号头文件源码.md)
- [zephyr/devicetree.h](../dt_main_reference/P002_设备树主头文件源码.md)
- [zephyr/drivers/pwm.h](../pwm_driver_reference/P002_PWM驱动头文件源码.md)
- [zephyr/sys/slist.h](../slist_reference/P003_单向链表头文件源码.md)
- [查看此文件的源码。](../api_source_reference/P685_pwm_utils.h_源码浏览.md)
- [sys_slist_t](../slist_reference/P001_单向链表公共接口.md#ga44658c336b634c03938a251cdc8134f8)
- [pwm_event_callback](../hardware/P257_PWM事件回调结构.md)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [device](../device_reference/P002_设备对象结构.md)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [pwm_events_t](../hardware/P255_PWM公共接口.md#ga5bc9607de7643cb78476ed354c51560b)

<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P027_zephyr__drivers__firmware__scmi__power.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P029_zephyr__dt-bindings__gpio__realtek-gpio.h_文件参考.md)
