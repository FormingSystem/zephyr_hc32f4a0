---
id: learning.zephyr-docs.api-file-interface-reference.page-15
title: zephyr__drivers__console__console.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/drivers_2console_2console_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第15章\_zephyr\_\_drivers\_\_console\_\_console.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2console_2console_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

查看此文件的源码。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 15.1\_数据结构（Data Structures）

<a id="r_console_5Finput"></a>

```c
struct console_input
```

相关声明：[console_input](../system_service_model_reference/P005_console_input_结构体.md)。

控制台输入（Console Input）的表示。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 15.2\_宏定义（Macros）

<a id="r_ae5aa23edbc2609d1b766340c14fd5a68"></a>

```c
#define CONSOLE_MAX_LINE_LEN CONFIG_CONSOLE_INPUT_MAX_LINE_LEN
```

相关声明：[CONSOLE_MAX_LINE_LEN](#ae5aa23edbc2609d1b766340c14fd5a68)。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 15.3\_类型定义（Typedefs）

<a id="r_a0dab6d89950bb4c2bbb17571b9b1461f"></a>

```c
typedef void(* console_input_fn) (struct k_fifo *avail, struct k_fifo *lines, uint8_t(*completion) (char *str, uint8_t len))
```

相关声明：[console_input_fn](#a0dab6d89950bb4c2bbb17571b9b1461f)、[k_fifo](../queue_reference/P004_内核FIFO结构.md)、[k_fifo](../queue_reference/P004_内核FIFO结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

控制台输入处理函数（console input processing handler）的签名。

## 15.4\_详细说明（Detailed Documentation）

<a id="ae5aa23edbc2609d1b766340c14fd5a68"></a>

### `CONSOLE_MAX_LINE_LEN`

```c
#define CONSOLE_MAX_LINE_LEN CONFIG_CONSOLE_INPUT_MAX_LINE_LEN
```

<a id="a0dab6d89950bb4c2bbb17571b9b1461f"></a>

### `console_input_fn`

```c
typedef void(* console_input_fn) (struct k_fifo *avail, struct k_fifo *lines, uint8_t(*completion)(char *str, uint8_t len))
```

控制台输入处理函数（console input processing handler）的签名。

当用户在控制台中键入字符串时开始处理输入。回车符会转换为空字符（原文写作 NULL），确保字符串始终以空字符终止。应用程序在调用注册函数之前，需要初始化下文提到的两个先进先出（FIFO）队列。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `avail` | 保存可用输入槽位（input slots）的 `k_fifo` 队列。 |
| `lines` | 保存已输入行的 `k_fifo` 队列，这些行随后由应用程序代码处理。 |
| `completion` | 用于补全已输入命令的 Tab 补全（tab completion）回调。 |


## 15.5\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_reference/P151_console.h_源码浏览.md)
- [console_input](../system_service_model_reference/P005_console_input_结构体.md)
- [k_fifo](../queue_reference/P004_内核FIFO结构.md)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="doc-typedef-members"></a>
<a id="header-doc-typedef-members"></a>

---

[上一章](P014_zephyr__drivers__clock_control__atmel_sam_pmc.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P016_zephyr__drivers__emul_sensor.h_文件参考.md)
