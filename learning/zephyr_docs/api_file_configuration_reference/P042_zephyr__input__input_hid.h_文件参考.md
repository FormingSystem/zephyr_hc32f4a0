---
id: learning.zephyr-docs.api-file-configuration-reference.page-42
title: zephyr__input__input_hid.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/input__hid_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第42章\_zephyr\_\_input\_\_input\_hid.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/input__hid_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

输入代码到HID代码/修饰键（Code / Modifier）转换工具的头文件。

查看此文件的源码。

<a id="details"></a>

输入代码到HID代码/修饰键（Code / Modifier）转换工具的头文件。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 42.1\_函数（Functions）

<a id="r_ga094b3ccfc2e111c4b2a000e9c2fe133c"></a>

```c
int16_t input_to_hid_code (uint16_t input_code)
```

相关声明：[int16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#afe270aee8d96ad7f279a4020b9d58bdf)、[input_to_hid_code](https://docs.zephyrproject.org/latest/doxygen/html/group__input__interface.html#ga094b3ccfc2e111c4b2a000e9c2fe133c)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

将输入代码（Input Code）转换为人机接口设备代码（HID Code）。

<a id="r_ga86ac2267d08e91bcc09c5b091042cfde"></a>

```c
uint8_t input_to_hid_modifier (uint16_t input_code)
```

相关声明：[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[input_to_hid_modifier](https://docs.zephyrproject.org/latest/doxygen/html/group__input__interface.html#ga86ac2267d08e91bcc09c5b091042cfde)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

将输入代码（Input Code）转换为人机接口设备修饰符（HID Modifier）。


## 42.2\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_reference/P380_input_hid.h_源码浏览.md)
- [int16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#afe270aee8d96ad7f279a4020b9d58bdf)
- [input_to_hid_code](https://docs.zephyrproject.org/latest/doxygen/html/group__input__interface.html#ga094b3ccfc2e111c4b2a000e9c2fe133c)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [input_to_hid_modifier](https://docs.zephyrproject.org/latest/doxygen/html/group__input__interface.html#ga86ac2267d08e91bcc09c5b091042cfde)

<a id="header-details"></a>

---

[上一章](P041_zephyr__drivers__sensor__ina2xx.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P043_zephyr__input__input_paw32xx.h_文件参考.md)
