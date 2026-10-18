---
id: learning.zephyr-docs.api-device-topic-reference.page-12
title: 键位映射实用工具（Keymap utilities）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__input__keymap.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第12章\_键位映射实用工具（Keymap utilities）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__input__keymap.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

<a id="details"></a>



<a id="header-files"></a>
<a id="files"></a>

## 12.1\_文件（Files）

<a id="r_input_5Fkeymap_2Eh"></a>

```c
file input_keymap.h
```

相关声明：[input_keymap.h](../api_file_runtime_reference/P024_zephyr__input__input_keymap.h_文件参考.md)。

键映射工具（Keymap Utilities）的头文件。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 12.2\_宏定义（Macros）

<a id="r_gafd3fd33c07ccb96c0c88c1a8d340fee3"></a>

```c
#define MATRIX_ROW(keymap_entry)
```

相关声明：[MATRIX_ROW](#gafd3fd33c07ccb96c0c88c1a8d340fee3)。

从键映射条目（Keymap Entry）提取行索引（Row Index）。

<a id="r_gad3b19ba368920538444393be76bf7214"></a>

```c
#define MATRIX_COL(keymap_entry)
```

相关声明：[MATRIX_COL](#gad3b19ba368920538444393be76bf7214)。

从键映射条目（Keymap Entry）提取列索引（Column Index）。

<a id="r_ga16c8082f1ed12d9544cddff57ea5750c"></a>

```c
#define MATRIX_CODE(keymap_entry)
```

相关声明：[MATRIX_CODE](#ga16c8082f1ed12d9544cddff57ea5750c)。

从键映射条目（Keymap Entry）提取按键代码（Key Code）。

## 12.3\_详细说明（Detailed Documentation）

<a id="ga16c8082f1ed12d9544cddff57ea5750c"></a>

### `MATRIX_CODE`

```c
#define MATRIX_CODE ( keymap_entry)
```

```c
#include <zephyr/input/input_keymap.h>
```

展开值（Value）：

```c
(keymap_entry & 0xffff)
```

从键映射条目（Keymap Entry）提取按键代码（Key Code）。

此宏从 32 位按键映射条目（keymap entry）提取键码（key code）。键码存储在该条目的位 0–15 中。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `keymap_entry` | 32 位按键映射条目的值。 |

**返回（Returns）**：返回值：从按键映射条目提取的键码，范围为 0–`0xffff`。

<a id="gad3b19ba368920538444393be76bf7214"></a>

### `MATRIX_COL`

```c
#define MATRIX_COL ( keymap_entry)
```

```c
#include <zephyr/input/input_keymap.h>
```

展开值（Value）：

```c
(((keymap_entry) >> 16) & 0xff)
```

从键映射条目（Keymap Entry）提取列索引（Column Index）。

此宏从 32 位按键映射条目提取列索引（column index）。列索引存储在该条目的位 16–23 中。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `keymap_entry` | 32 位按键映射条目的值。 |

**返回（Returns）**：返回值：从按键映射条目提取的列索引，范围为 0–255。

<a id="gafd3fd33c07ccb96c0c88c1a8d340fee3"></a>

### `MATRIX_ROW`

```c
#define MATRIX_ROW ( keymap_entry)
```

```c
#include <zephyr/input/input_keymap.h>
```

展开值（Value）：

```c
(((keymap_entry) >> 24) & 0xff)
```

从键映射条目（Keymap Entry）提取行索引（Row Index）。

此宏从 32 位按键映射条目提取行索引（row index）。行索引存储在该条目的位 24–31 中。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `keymap_entry` | 32 位按键映射条目的值。 |

**返回（Returns）**：返回值：从按键映射条目提取的行索引，范围为 0–255。


## 12.4\_原页交叉引用（Cross References）

- [input_keymap.h](../api_file_runtime_reference/P024_zephyr__input__input_keymap.h_文件参考.md)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[上一章](P011_INA2XX API主题.md) · [返回大纲](大纲.md) · [下一章](P013_内核 API（Kernel APIs）.md)
