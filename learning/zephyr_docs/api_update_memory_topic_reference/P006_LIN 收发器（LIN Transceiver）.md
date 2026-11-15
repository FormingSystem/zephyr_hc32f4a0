---
id: learning.zephyr-docs.api-update-memory-topic-reference.page-6
title: LIN 收发器（LIN Transceiver）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__lin__transceiver.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第6章\_LIN 收发器（LIN Transceiver）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__lin__transceiver.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

LIN 收发器接口。

<a id="details"></a>

本地互联网络（LIN）收发器接口（Transceiver Interfaces）。**引入版本（Since）：**4.5。**版本（Version）：**0.1.0。

<a id="header-files"></a>
<a id="files"></a>

## 6.1\_文件（Files）

<a id="r_transceiver_2Eh"></a>

```c
file transceiver.h
```

相关声明：[transceiver.h](../api_file_runtime_reference/P033_zephyr__drivers__lin__transceiver.h_文件参考.md)。

LIN收发器（Transceiver）的驱动API。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 6.2\_函数（Functions）

<a id="r_ga8a81eb11fe36f6a1a4db51015367ed36"></a>

```c
static int lin_transceiver_enable (const struct device *dev, uint8_t flags)
```

相关声明：[lin_transceiver_enable](#ga8a81eb11fe36f6a1a4db51015367ed36)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[标志（Flags）。](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)。

启用 LIN 收发器（Transceiver）。

<a id="r_ga898972c2e62cd45e53a901801502b2f9"></a>

```c
static int lin_transceiver_disable (const struct device *dev)
```

相关声明：[lin_transceiver_disable](#ga898972c2e62cd45e53a901801502b2f9)、[device](../device_reference/P002_设备对象结构.md)。

禁用 LIN 收发器（Transceiver）。

## 6.3\_详细说明（Detailed Documentation）

<a id="ga898972c2e62cd45e53a901801502b2f9"></a>

### `lin_transceiver_disable()`

```c
int lin_transceiver_disable ( const struct device * dev)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/drivers/lin/transceiver.h>
```

禁用 LIN 收发器（Transceiver）。

禁用 LIN 收发器（Transceiver）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向 LIN 收发器设备结构体的指针。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时。 |
| `-EALREADY` | 收发器已禁用时。 |
| `-EIO` | 通用输入／输出错误（General I/O Error），未能禁用收发器。 |

**说明（Note）**：**注意（Note）：**LIN 收发器由 LIN 控制器驱动控制，应用程序通常不应直接控制它。

**参阅（See Also）**：**另请参见（See Also）：**`lin_stop()`。

<a id="ga8a81eb11fe36f6a1a4db51015367ed36"></a>

### `lin_transceiver_enable()`

```c
int lin_transceiver_enable ( const struct device * dev, uint8_t flags )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/drivers/lin/transceiver.h>
```

启用 LIN 收发器（Transceiver）。

启用 LIN 收发器（Transceiver）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向 LIN 收发器设备结构体的指针。 |
| `flags` | 控制收发器行为的标志（Flags），具体定义因收发器而异。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时。 |
| `-EALREADY` | 收发器已启用时。 |
| `-EIO` | 通用输入／输出错误（General I/O Error），未能启用收发器。 |

**说明（Note）**：**注意（Note）：**LIN 收发器由 LIN 控制器驱动控制，应用程序通常不应直接控制它。

**参阅（See Also）**：**另请参见（See Also）：**`lin_start()`。


## 6.4\_原页交叉引用（Cross References）

- [transceiver.h](../api_file_runtime_reference/P033_zephyr__drivers__lin__transceiver.h_文件参考.md)
- [device](../device_reference/P002_设备对象结构.md)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [标志（Flags）。](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)
- [lin_stop()](https://docs.zephyrproject.org/latest/doxygen/html/group__lin__controller.html#gaefe6f3853ea2f70d8ba4d6ab86f62b57)
- [lin_start()](https://docs.zephyrproject.org/latest/doxygen/html/group__lin__controller.html#ga752004d89d50932711c3aa6189874478)

<a id="header-details"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P005_Realtek RTS5817中断源（Interrupt Sources）.md) · [返回大纲](大纲.md) · [下一章](P007_LIS2DU12 API主题.md)
