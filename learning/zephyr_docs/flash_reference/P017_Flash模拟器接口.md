---
id: learning.zephyr-docs.flash-reference.page-17
title: Flash模拟器接口
kind: reference
status: maintained
domains: [zephyr, flash, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/flash__simulator_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第17章\_Flash模拟器接口

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/flash__simulator_8h.html)。读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

> 译注——阅读位置：本页是Flash与EEPROM存储驱动应用程序接口（Application Programming Interface，API）参考。Flash部分配合[Flash概述](../hardware/P012_Flash闪存.md)，EEPROM部分配合[EEPROM公共接口](../hardware/P040_EEPROM接口参考.md)阅读；模拟器（Simulator）、伪函数（Fake Function）与I²C目标设备（Target Device）分别说明，不能互相当作实板验证。原始标识符、类型与常量保持不变；重复的接口摘要与详细说明均保留。

闪存模拟器（Flash Simulator）专用应用程序接口（Application Programming Interface，API）。

<a id="details"></a>

```c
#include <zephyr/device.h>
#include <zephyr/types.h>
#include <sys/types.h>
#include <zephyr/syscalls/flash_simulator.h>
```

查看此文件的源码。入口：[源码浏览译文](P020_Flash模拟器头文件源码.md)。

闪存模拟器（Flash Simulator）专用 API，用于扩展模拟器功能。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 17.1\_数据结构（Data Structures）

<a id="r_flash_5Fsimulator_5Fparams"></a>

```c
struct flash_simulator_params
```

相关声明：[flash_simulator_params](P018_Flash模拟器参数.md)。

Flash 模拟器参数结构体（Parameters Structure）。

<a id="r_flash_5Fsimulator_5Fcb"></a>

```c
struct flash_simulator_cb
```

相关声明：[flash_simulator_cb](P019_Flash模拟器回调.md)。

Flash 模拟器回调结构体（Callbacks Structure）。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 17.2\_类型定义（Typedefs）

<a id="r_a860ecc612edda863f4f86ec690bec979"></a>

```c
typedef int(* flash_simulator_write_byte_cb_t) (const struct device *dev, off_t offset, uint8_t data)
```

相关声明：[flash_simulator_write_byte_cb_t](#a860ecc612edda863f4f86ec690bec979)、[device](../device_reference/P002_设备对象结构.md)、[off_t](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a98a5cc5f4a350bf5652565021a2f239f)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

Flash 模拟器的单字节写入回调（Write Byte Callback）类型。

<a id="r_a24b9919bf5776683d1890c46ed961bd5"></a>

```c
typedef int(* flash_simulator_erase_unit_cb_t) (const struct device *dev, off_t unit_offset)
```

相关声明：[flash_simulator_erase_unit_cb_t](#a24b9919bf5776683d1890c46ed961bd5)、[device](../device_reference/P002_设备对象结构.md)、[off_t](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a98a5cc5f4a350bf5652565021a2f239f)。

Flash 模拟器的单元擦除回调（Erase Unit Callback）类型。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 17.3\_函数（Functions）

<a id="r_ac944ca905ff40848d2a566e45e446096"></a>

```c
const struct flash_simulator_params * flash_simulator_get_params (const struct device *dev)
```

相关声明：[flash_simulator_params](P018_Flash模拟器参数.md)、[flash_simulator_get_params](#ac944ca905ff40848d2a566e45e446096)、[device](../device_reference/P002_设备对象结构.md)。

取得 Flash 模拟器参数。

<a id="r_a0ba212692f650a34238b0f2763a541c7"></a>

```c
void flash_simulator_set_callbacks (const struct device *dev, const struct flash_simulator_cb *cb)
```

相关声明：[flash_simulator_set_callbacks](#a0ba212692f650a34238b0f2763a541c7)、[device](../device_reference/P002_设备对象结构.md)、[flash_simulator_cb](P019_Flash模拟器回调.md)。

设置 Flash 模拟器回调。

<a id="r_a71cca7b794f8e9402d81491c7e93cc3f"></a>

```c
void * flash_simulator_get_memory (const struct device *dev, size_t *mock_size)
```

相关声明：[flash_simulator_get_memory](#a71cca7b794f8e9402d81491c7e93cc3f)、[device](../device_reference/P002_设备对象结构.md)。

取得指向模拟器所使用的随机存取存储器（Random Access Memory，RAM）缓冲区的指针。

## 17.4\_详细说明（Detailed Documentation）

<a id="a24b9919bf5776683d1890c46ed961bd5"></a>

### `flash_simulator_erase_unit_cb_t`

```c
typedef int(* flash_simulator_erase_unit_cb_t) (const struct device *dev, off_t unit_offset)
```

Flash 模拟器的单元擦除回调（Erase Unit Callback）类型。

该回调用于替代单元擦除操作，接收擦除单元偏移作为参数；偏移采用传给 Flash 擦除操作的同一偏移坐标。成功必须返回 0，出错时返回负值。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | Flash 模拟器设备指针。 |
| `unit_offset` | Flash 模拟器存储空间内的偏移。 |

**说明（Note）**：设置此回调后，Flash 模拟器驱动本身不再执行擦除操作。

**返回（Returns）**：成功返回 0，出错时返回负值。

> 译注——源码核对：当前实现按擦除单元循环调用回调，每次传入该单元起点，并非多单元请求每次都传最初offset。安装回调后驱动不再执行默认memset；若回调只返回0而不修改模拟存储区，该单元内容不会因此自动变成erase_value。

<a id="a860ecc612edda863f4f86ec690bec979"></a>

### `flash_simulator_write_byte_cb_t`

```c
typedef int(* flash_simulator_write_byte_cb_t) (const struct device *dev, off_t offset, uint8_t data)
```

Flash 模拟器的单字节写入回调（Write Byte Callback）类型。

该回调用于替代单字节写入，接收请求写入的数据和偏移；偏移采用传给 Flash 写入操作的同一偏移坐标。回调必须返回要写到指定偏移处的值，出错时返回负值。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | Flash 模拟器设备指针。 |
| `offset` | Flash 模拟器存储空间内的偏移。 |
| `data` | 要写入的数据字节。 |

**返回（Returns）**：返回要写到指定偏移处的值，出错时返回负值。

> 译注——源码核对：这里的成功结果是要写入的字节值，不是通用状态码0。当前驱动先按显式擦除模式对数据执行按位与／或，再把得到的数据和offset+i传给回调；非负返回值转换为uint8_t后写入，负值终止操作。测试应返回预期的0～255字节值，不能无条件return 0并期待原数据被保留。

<a id="a71cca7b794f8e9402d81491c7e93cc3f"></a>

### `flash_simulator_get_memory()`

```c
void * flash_simulator_get_memory ( const struct device * dev, size_t * mock_size )
```

取得指向模拟器所使用的随机存取存储器（Random Access Memory，RAM）缓冲区的指针。

调用者通过此函数取得 RAM 缓冲区的地址和大小；Flash 模拟器在这个缓冲区中模拟闪存内容。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] dev` | Flash 模拟器设备指针。 |
| `[out] mock_size` | RAM 缓冲区大小。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `pointer` | 指向 RAM 缓冲区的指针。 |

> 译注——源码核对：mock_size在当前实现中被直接解引用，必须提供有效的size_t输出地址，不能传NULL。返回的是模拟存储的底层缓冲区；直接修改它会绕过Flash读写接口的对齐、擦除和回调路径。

<a id="ac944ca905ff40848d2a566e45e446096"></a>

### `flash_simulator_get_params()`

```c
const struct flash_simulator_params * flash_simulator_get_params ( const struct device * dev)
```

取得 Flash 模拟器参数。

调用者通过此函数取得驱动使用的 Flash 模拟器参数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] dev` | Flash 模拟器设备指针。 |

**返回（Returns）**：返回指向 Flash 模拟器参数结构体的指针。

> 译注——源码核对：当前驱动只有在CONFIG_FLASH_SIMULATOR_CALLBACKS启用时返回参数指针，否则返回NULL。头文件有声明不代表该配置下会返回可用参数，调用方应检查结果。

<a id="a0ba212692f650a34238b0f2763a541c7"></a>

### `flash_simulator_set_callbacks()`

```c
void flash_simulator_set_callbacks ( const struct device * dev, const struct flash_simulator_cb * cb )
```

设置 Flash 模拟器回调。

调用者通过此函数，为 Flash 模拟器执行的单字节写入和单元擦除操作设置自定义回调（Custom Callback）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] dev` | Flash 模拟器设备指针。 |
| `[in] cb` | 指向包含回调的结构体的指针。 |

> 译注——源码核对：当前实现保存cb指针，不复制结构体。回调结构及其关联状态须在被使用期间保持有效；不要传入即将退出作用域的局部结构。回调路径和此设置实现依赖CONFIG_FLASH_SIMULATOR_CALLBACKS。

## 17.5\_源码定位与使用边界

本组包含[模拟器API](P017_Flash模拟器接口.md)、[参数](P018_Flash模拟器参数.md)、[回调结构](P019_Flash模拟器回调.md)及[头文件源码](P020_Flash模拟器头文件源码.md)。源码跟踪：[flash_simulator.h](../../../include/zephyr/drivers/flash/flash_simulator.h)和[flash_simulator.c](../../../drivers/flash/flash_simulator.c)。译注核对的官方[头文件](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/drivers/flash/flash_simulator.h)与[驱动实现](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/flash/flash_simulator.c)分别记录摘要；本地版本可能不同。

各页官方来源及源码摘要见[来源记录](../SOURCES.md)。本批仅翻译和核对代码，没有运行模拟测试、构建、擦写存储或执行实板通信。

## 17.6\_原页交叉引用（Cross References）

- [zephyr/device.h](../device_reference/P008_设备模型头文件源码.md)
- [zephyr/types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2types_8h_source.html)
- [sys/types.h](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h_source.html)
- [查看此文件源码](P020_Flash模拟器头文件源码.md)
- [flash_simulator_params](P018_Flash模拟器参数.md)
- [flash_simulator_cb](P019_Flash模拟器回调.md)
- [device](../device_reference/P002_设备对象结构.md)
- [off_t](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a98a5cc5f4a350bf5652565021a2f239f)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="header-details"></a>
<a id="doc-typedef-members"></a>
<a id="header-doc-typedef-members"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P016_M95P32扩展头文件源码.md) · [返回大纲](大纲.md) · [下一章](P018_Flash模拟器参数.md)
