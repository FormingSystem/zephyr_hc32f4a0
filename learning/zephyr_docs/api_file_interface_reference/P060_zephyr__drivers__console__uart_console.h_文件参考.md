---
id: learning.zephyr-docs.api-file-interface-reference.page-60
title: zephyr__drivers__console__uart_console.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/uart__console_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第60章\_zephyr\_\_drivers\_\_console\_\_uart\_console.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/uart__console_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/kernel.h>
```

查看此文件的源码。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 60.1\_函数（Functions）

<a id="r_a090eed88ce36e49ecea535d61746abd5"></a>

```c
void uart_register_input (struct k_fifo *avail, struct k_fifo *lines, uint8_t(*completion)(char *str, uint8_t len))
```

相关声明：[uart_register_input](#a090eed88ce36e49ecea535d61746abd5)、[k_fifo](../queue_reference/P004_内核FIFO结构.md)、[k_fifo](../queue_reference/P004_内核FIFO结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

注册 UART 输入处理（input processing）。

## 60.2\_详细说明（Detailed Documentation）

<a id="a090eed88ce36e49ecea535d61746abd5"></a>

### `uart_register_input()`

```c
void uart_register_input ( struct k_fifo * avail, struct k_fifo * lines, uint8_t(* completion )(char *str, uint8_t len) )
```

注册 UART 输入处理（input processing）。

当用户在控制台中键入字符串时开始处理输入。回车符会转换为空字符（原文写作 NULL），确保字符串始终以空字符终止。应用程序在调用注册函数之前，需要初始化下文提到的两个先进先出（FIFO）队列。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `avail` | 保存可用输入槽位（input slots）的 `k_fifo` 队列。 |
| `lines` | 保存已输入行的 `k_fifo` 队列，这些行随后由应用程序代码处理。 |
| `completion` | 用于补全已输入命令的 Tab 补全（tab completion）回调。 |


## 60.3\_原页交叉引用（Cross References）

- [zephyr/kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h_source.html)
- [查看此文件的源码。](../api_source_configuration_reference/P115_uart_console.h_源码浏览.md)
- [k_fifo](../queue_reference/P004_内核FIFO结构.md)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P059_zephyr__drivers__sensor__tmp108.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P061_zephyr__usb__class__usb_hid.h_文件参考.md)
