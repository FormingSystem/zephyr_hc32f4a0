---
id: learning.zephyr-docs.api-file-system-device-reference.page-21
title: zephyr__drivers__led__is31fl3733.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/is31fl3733_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第21章\_zephyr\_\_drivers\_\_led\_\_is31fl3733.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/is31fl3733_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

查看此文件的源码。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 21.1\_函数（Functions）

<a id="r_a70f023bdbfc7c2b86173bebca80d6977"></a>

```c
int is31fl3733_blank (const struct device *dev, bool blank_en)
```

相关声明：[is31fl3733_blank](#a70f023bdbfc7c2b86173bebca80d6977)、[device](../device_reference/P002_设备对象结构.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

使 IS31FL3733 LED 显示屏消隐（blanking）。

<a id="r_ad3de611ed4641cccaaa0920cee160eed"></a>

```c
int is31fl3733_current_limit (const struct device *dev, uint8_t limit)
```

相关声明：[is31fl3733_current_limit](#ad3de611ed4641cccaaa0920cee160eed)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

设置 LED 电流限制（current limit）。

## 21.2\_详细说明（Detailed Documentation）

<a id="a70f023bdbfc7c2b86173bebca80d6977"></a>

### `is31fl3733_blank()`

```c
int is31fl3733_blank ( const struct device * dev, bool blank_en )
```

使 IS31FL3733 LED 显示屏消隐（blanking）。

设置 `blank_en` 时，将禁用 LED 显示。这可用于无闪烁显示更新（flicker-free display updates）或节省电能。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | LED 设备结构体。 |
| `blank_en` | 是否应启用消隐（blanking）。 |

**返回（Returns）**：返回值：成功时返回 0，出错时返回负值。

<a id="ad3de611ed4641cccaaa0920cee160eed"></a>

### `is31fl3733_current_limit()`

```c
int is31fl3733_current_limit ( const struct device * dev, uint8_t limit )
```

设置 LED 电流限制（current limit）。

设置 LED 驱动的电流限制。此值独立于每个 LED 的亮度设置，并作用于全部 LED。输出电流限制按公式 `(840/R_ISET) * (limit/256)` 设置。更多信息参见数据手册表 14。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | LED 设备结构体。 |
| `limit` | 要应用的电流限制。 |

**返回（Returns）**：返回值：成功时返回 0，出错时返回负值。


## 21.3\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_reference/P412_is31fl3733.h_源码浏览.md)
- [device](../device_reference/P002_设备对象结构.md)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P020_zephyr__kernel__internal__mm.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P022_zephyr__drivers__led__led_fake.h_文件参考.md)
