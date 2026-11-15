---
id: learning.zephyr-docs.api-transport-control-topic-reference.page-21
title: SMBus 驱动后端 API
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__smbus__interface__backend.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第21章\_SMBus 驱动后端 API

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__smbus__interface__backend.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

<a id="details"></a>

本组包含实现系统管理总线（SMBus）驱动所需的 API 类型定义、回调签名（Callback Signatures）及其他辅助接口（Helpers）。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 21.1\_数据结构（Data Structures）

<a id="r_smbus_5Fdriver_5Fapi"></a>

```c
struct smbus_driver_api
```

相关声明：[smbus_driver_api](../peripheral_bus_storage_model_reference/P092_smbus_driver_api_结构体.md)。

驱动操作（Driver Operations）：系统管理总线（SMBus）驱动操作。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 21.2\_类型定义（Typedefs）

<a id="r_ga5fa53c3cd255001a2c34b36a3d23be6f"></a>

```c
typedef int(* smbus_api_configure_t) (const struct device *dev, uint32_t dev_config)
```

相关声明：[smbus_api_configure_t](#ga5fa53c3cd255001a2c34b36a3d23be6f)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

配置 SMBus 主机控制器的运行方式。

<a id="r_gace2a4372975b44428fb39015e4b4bb25"></a>

```c
typedef int(* smbus_api_get_config_t) (const struct device *dev, uint32_t *dev_config)
```

相关声明：[smbus_api_get_config_t](#gace2a4372975b44428fb39015e4b4bb25)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

获取 SMBus 主机控制器的配置。

<a id="r_ga93ce314c2797a21ed0b01bb28c69aeaf"></a>

```c
typedef int(* smbus_api_quick_t) (const struct device *dev, uint16_t addr, enum smbus_direction)
```

相关声明：[smbus_api_quick_t](#ga93ce314c2797a21ed0b01bb28c69aeaf)、[device](../device_reference/P002_设备对象结构.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[smbus_direction](https://docs.zephyrproject.org/latest/doxygen/html/group__smbus__interface.html#gad0c28687977d0a7866bdea87aef88016)。

执行 SMBus 快速操作（Quick）。

<a id="r_ga2a59de36841ca4ff5fb65e29c512cd4e"></a>

```c
typedef int(* smbus_api_byte_write_t) (const struct device *dev, uint16_t addr, uint8_t byte)
```

相关声明：[smbus_api_byte_write_t](#ga2a59de36841ca4ff5fb65e29c512cd4e)、[device](../device_reference/P002_设备对象结构.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

执行 SMBus 字节写操作（Byte Write）。

<a id="r_gae25c3c8652730085ec31701a48f086b5"></a>

```c
typedef int(* smbus_api_byte_read_t) (const struct device *dev, uint16_t addr, uint8_t *byte)
```

相关声明：[smbus_api_byte_read_t](#gae25c3c8652730085ec31701a48f086b5)、[device](../device_reference/P002_设备对象结构.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

执行 SMBus 字节读操作（Byte Read）。

<a id="r_ga7827a1f9c5cf8c2b33c79e09d05019ca"></a>

```c
typedef int(* smbus_api_byte_data_write_t) (const struct device *dev, uint16_t addr, uint8_t cmd, uint8_t byte)
```

相关声明：[smbus_api_byte_data_write_t](#ga7827a1f9c5cf8c2b33c79e09d05019ca)、[device](../device_reference/P002_设备对象结构.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[cmd](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#gacde1ca3945cbe6c828f65051c5c3a615)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

执行 SMBus 字节数据写操作（Byte Data Write）。

<a id="r_ga36f67cfe281dea020b6036399e433f4a"></a>

```c
typedef int(* smbus_api_byte_data_read_t) (const struct device *dev, uint16_t addr, uint8_t cmd, uint8_t *byte)
```

相关声明：[smbus_api_byte_data_read_t](#ga36f67cfe281dea020b6036399e433f4a)、[device](../device_reference/P002_设备对象结构.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[cmd](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#gacde1ca3945cbe6c828f65051c5c3a615)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

执行 SMBus 字节数据读操作（Byte Data Read）。

<a id="r_ga31f2a46f83fe193f05cc5494435e2e6f"></a>

```c
typedef int(* smbus_api_word_data_write_t) (const struct device *dev, uint16_t addr, uint8_t cmd, uint16_t word)
```

相关声明：[smbus_api_word_data_write_t](#ga31f2a46f83fe193f05cc5494435e2e6f)、[device](../device_reference/P002_设备对象结构.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[cmd](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#gacde1ca3945cbe6c828f65051c5c3a615)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

执行 SMBus 字数据写操作（Word Data Write）。

<a id="r_ga94b1bf5e10799ab1f07cccb289033ca6"></a>

```c
typedef int(* smbus_api_word_data_read_t) (const struct device *dev, uint16_t addr, uint8_t cmd, uint16_t *word)
```

相关声明：[smbus_api_word_data_read_t](#ga94b1bf5e10799ab1f07cccb289033ca6)、[device](../device_reference/P002_设备对象结构.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[cmd](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#gacde1ca3945cbe6c828f65051c5c3a615)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

执行 SMBus 字数据读操作（Word Data Read）。

<a id="r_gaabd1e34153c852469e74e9fdc4118c84"></a>

```c
typedef int(* smbus_api_pcall_t) (const struct device *dev, uint16_t addr, uint8_t cmd, uint16_t send_word, uint16_t *recv_word)
```

相关声明：[smbus_api_pcall_t](#gaabd1e34153c852469e74e9fdc4118c84)、[device](../device_reference/P002_设备对象结构.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[cmd](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#gacde1ca3945cbe6c828f65051c5c3a615)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

执行 SMBus 过程调用（Process Call）。

<a id="r_gad118b4dc6c7bdea57a6d70240d804b02"></a>

```c
typedef int(* smbus_api_block_write_t) (const struct device *dev, uint16_t addr, uint8_t cmd, uint8_t count, uint8_t *buf)
```

相关声明：[smbus_api_block_write_t](#gad118b4dc6c7bdea57a6d70240d804b02)、[device](../device_reference/P002_设备对象结构.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[cmd](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#gacde1ca3945cbe6c828f65051c5c3a615)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

执行 SMBus 块写操作（Block Write）。

<a id="r_gad7453c161b4fa3c6085c186b39301659"></a>

```c
typedef int(* smbus_api_block_read_t) (const struct device *dev, uint16_t addr, uint8_t cmd, uint8_t *count, uint8_t *buf)
```

相关声明：[smbus_api_block_read_t](#gad7453c161b4fa3c6085c186b39301659)、[device](../device_reference/P002_设备对象结构.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[cmd](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#gacde1ca3945cbe6c828f65051c5c3a615)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

执行 SMBus 块读操作（Block Read）。

<a id="r_ga8e71f105c10414e4ae86b87345e70837"></a>

```c
typedef int(* smbus_api_block_pcall_t) (const struct device *dev, uint16_t addr, uint8_t cmd, uint8_t send_count, uint8_t *send_buf, uint8_t *recv_count, uint8_t *recv_buf)
```

相关声明：[smbus_api_block_pcall_t](#ga8e71f105c10414e4ae86b87345e70837)、[device](../device_reference/P002_设备对象结构.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[cmd](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#gacde1ca3945cbe6c828f65051c5c3a615)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

执行 SMBus 块过程调用（Block Process Call）。

<a id="r_ga9a81152429fd1f70e699f6767feb8702"></a>

```c
typedef int(* smbus_api_smbalert_cb_t) (const struct device *dev, struct smbus_callback *cb)
```

相关声明：[smbus_api_smbalert_cb_t](#ga9a81152429fd1f70e699f6767feb8702)、[device](../device_reference/P002_设备对象结构.md)、[smbus_callback](../peripheral_bus_storage_model_reference/P091_smbus_callback_结构体.md)。

添加或移除 `SMBALERT` 回调。

<a id="r_ga82dc504437f78c488df25ecd63a83a5e"></a>

```c
typedef int(* smbus_api_host_notify_cb_t) (const struct device *dev, struct smbus_callback *cb)
```

相关声明：[smbus_api_host_notify_cb_t](#ga82dc504437f78c488df25ecd63a83a5e)、[device](../device_reference/P002_设备对象结构.md)、[smbus_callback](../peripheral_bus_storage_model_reference/P091_smbus_callback_结构体.md)。

添加或移除主机通知（Host Notify）回调。

## 21.3\_详细说明（Detailed Documentation）

<a id="ga8e71f105c10414e4ae86b87345e70837"></a>

### `smbus_api_block_pcall_t`

```c
typedef int(* smbus_api_block_pcall_t) (const struct device *dev, uint16_t addr, uint8_t cmd, uint8_t send_count, uint8_t *send_buf, uint8_t *recv_count, uint8_t *recv_buf)
```

```c
#include <zephyr/drivers/smbus.h>
```

执行 SMBus 块过程调用（Block Process Call）。

参数说明（Argument Description）参见 `smbus_block_pcall()`。

<a id="gad7453c161b4fa3c6085c186b39301659"></a>

### `smbus_api_block_read_t`

```c
typedef int(* smbus_api_block_read_t) (const struct device *dev, uint16_t addr, uint8_t cmd, uint8_t *count, uint8_t *buf)
```

```c
#include <zephyr/drivers/smbus.h>
```

执行 SMBus 块读操作（Block Read）。

参数说明（Argument Description）参见 `smbus_block_read()`。

<a id="gad118b4dc6c7bdea57a6d70240d804b02"></a>

### `smbus_api_block_write_t`

```c
typedef int(* smbus_api_block_write_t) (const struct device *dev, uint16_t addr, uint8_t cmd, uint8_t count, uint8_t *buf)
```

```c
#include <zephyr/drivers/smbus.h>
```

执行 SMBus 块写操作（Block Write）。

参数说明（Argument Description）参见 `smbus_block_write()`。

<a id="ga36f67cfe281dea020b6036399e433f4a"></a>

### `smbus_api_byte_data_read_t`

```c
typedef int(* smbus_api_byte_data_read_t) (const struct device *dev, uint16_t addr, uint8_t cmd, uint8_t *byte)
```

```c
#include <zephyr/drivers/smbus.h>
```

执行 SMBus 字节数据读操作（Byte Data Read）。

参数说明（Argument Description）参见 `smbus_byte_data_read()`。

<a id="ga7827a1f9c5cf8c2b33c79e09d05019ca"></a>

### `smbus_api_byte_data_write_t`

```c
typedef int(* smbus_api_byte_data_write_t) (const struct device *dev, uint16_t addr, uint8_t cmd, uint8_t byte)
```

```c
#include <zephyr/drivers/smbus.h>
```

执行 SMBus 字节数据写操作（Byte Data Write）。

参数说明（Argument Description）参见 `smbus_byte_data_write()`。

<a id="gae25c3c8652730085ec31701a48f086b5"></a>

### `smbus_api_byte_read_t`

```c
typedef int(* smbus_api_byte_read_t) (const struct device *dev, uint16_t addr, uint8_t *byte)
```

```c
#include <zephyr/drivers/smbus.h>
```

执行 SMBus 字节读操作（Byte Read）。

参数说明（Argument Description）参见 `smbus_byte_read()`。

<a id="ga2a59de36841ca4ff5fb65e29c512cd4e"></a>

### `smbus_api_byte_write_t`

```c
typedef int(* smbus_api_byte_write_t) (const struct device *dev, uint16_t addr, uint8_t byte)
```

```c
#include <zephyr/drivers/smbus.h>
```

执行 SMBus 字节写操作（Byte Write）。

参数说明（Argument Description）参见 `smbus_byte_write()`。

<a id="ga5fa53c3cd255001a2c34b36a3d23be6f"></a>

### `smbus_api_configure_t`

```c
typedef int(* smbus_api_configure_t) (const struct device *dev, uint32_t dev_config)
```

```c
#include <zephyr/drivers/smbus.h>
```

配置 SMBus 主机控制器的运行方式。

参数说明（Argument Description）参见 `smbus_configure()`。

<a id="gace2a4372975b44428fb39015e4b4bb25"></a>

### `smbus_api_get_config_t`

```c
typedef int(* smbus_api_get_config_t) (const struct device *dev, uint32_t *dev_config)
```

```c
#include <zephyr/drivers/smbus.h>
```

获取 SMBus 主机控制器的配置。

参数说明（Argument Description）参见 `smbus_get_config()`。

<a id="ga82dc504437f78c488df25ecd63a83a5e"></a>

### `smbus_api_host_notify_cb_t`

```c
typedef int(* smbus_api_host_notify_cb_t) (const struct device *dev, struct smbus_callback *cb)
```

```c
#include <zephyr/drivers/smbus.h>
```

添加或移除主机通知（Host Notify）回调。

参数说明（Argument Description）参见 `smbus_host_notify_set_cb()` 和  `smbus_host_notify_remove_cb()`。

<a id="gaabd1e34153c852469e74e9fdc4118c84"></a>

### `smbus_api_pcall_t`

```c
typedef int(* smbus_api_pcall_t) (const struct device *dev, uint16_t addr, uint8_t cmd, uint16_t send_word, uint16_t *recv_word)
```

```c
#include <zephyr/drivers/smbus.h>
```

执行 SMBus 过程调用（Process Call）。

参数说明（Argument Description）参见 `smbus_pcall()`。

<a id="ga93ce314c2797a21ed0b01bb28c69aeaf"></a>

### `smbus_api_quick_t`

```c
typedef int(* smbus_api_quick_t) (const struct device *dev, uint16_t addr, enum smbus_direction)
```

```c
#include <zephyr/drivers/smbus.h>
```

执行 SMBus 快速操作（Quick）。

参数说明（Argument Description）参见 `smbus_quick()`。

<a id="ga9a81152429fd1f70e699f6767feb8702"></a>

### `smbus_api_smbalert_cb_t`

```c
typedef int(* smbus_api_smbalert_cb_t) (const struct device *dev, struct smbus_callback *cb)
```

```c
#include <zephyr/drivers/smbus.h>
```

添加或移除 `SMBALERT` 回调。

参数说明（Argument Description）参见 `smbus_smbalert_set_cb()` 和  `smbus_smbalert_remove_cb()`。

<a id="ga94b1bf5e10799ab1f07cccb289033ca6"></a>

### `smbus_api_word_data_read_t`

```c
typedef int(* smbus_api_word_data_read_t) (const struct device *dev, uint16_t addr, uint8_t cmd, uint16_t *word)
```

```c
#include <zephyr/drivers/smbus.h>
```

执行 SMBus 字数据读操作（Word Data Read）。

参数说明（Argument Description）参见 `smbus_word_data_read()`。

<a id="ga31f2a46f83fe193f05cc5494435e2e6f"></a>

### `smbus_api_word_data_write_t`

```c
typedef int(* smbus_api_word_data_write_t) (const struct device *dev, uint16_t addr, uint8_t cmd, uint16_t word)
```

```c
#include <zephyr/drivers/smbus.h>
```

执行 SMBus 字数据写操作（Word Data Write）。

参数说明（Argument Description）参见 `smbus_word_data_write()`。


## 21.4\_原页交叉引用（Cross References）

- [smbus_driver_api](../peripheral_bus_storage_model_reference/P092_smbus_driver_api_结构体.md)
- [device](../device_reference/P002_设备对象结构.md)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [smbus_direction](https://docs.zephyrproject.org/latest/doxygen/html/group__smbus__interface.html#gad0c28687977d0a7866bdea87aef88016)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [cmd](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#gacde1ca3945cbe6c828f65051c5c3a615)
- [smbus_callback](../peripheral_bus_storage_model_reference/P091_smbus_callback_结构体.md)
- [zephyr/drivers/smbus.h](../peripheral_bus_storage_header_reference/P027_zephyr__drivers__smbus.h_头文件参考.md)
- [smbus_block_pcall()](https://docs.zephyrproject.org/latest/doxygen/html/group__smbus__interface.html#ga680c3d713a615f4b62503d6f84de4290)
- [smbus_block_read()](https://docs.zephyrproject.org/latest/doxygen/html/group__smbus__interface.html#ga67603db9b44636b0b62a24fd623cfb1c)
- [smbus_block_write()](https://docs.zephyrproject.org/latest/doxygen/html/group__smbus__interface.html#ga55a867cdcb504039f274abae2d1a99e4)
- [smbus_byte_data_read()](https://docs.zephyrproject.org/latest/doxygen/html/group__smbus__interface.html#ga1f1148a7cb92e0e0aef7ae3a84615c9b)
- [smbus_byte_data_write()](https://docs.zephyrproject.org/latest/doxygen/html/group__smbus__interface.html#gadd7ec1eb3db981efceb8f959546a3b6a)
- [smbus_byte_read()](https://docs.zephyrproject.org/latest/doxygen/html/group__smbus__interface.html#gadaef9dad3470a7e4d3360e0246271ca1)
- [smbus_byte_write()](https://docs.zephyrproject.org/latest/doxygen/html/group__smbus__interface.html#ga7dd01c1e00a0f8b0315e442707332251)
- [smbus_configure()](https://docs.zephyrproject.org/latest/doxygen/html/group__smbus__interface.html#ga517305aa7cc9c93ae449b3c548d6c835)
- [smbus_get_config()](https://docs.zephyrproject.org/latest/doxygen/html/group__smbus__interface.html#ga9ca38ca95c0576bdc75b7eb8d0ca29ef)
- [smbus_host_notify_set_cb()](https://docs.zephyrproject.org/latest/doxygen/html/group__smbus__interface.html#ga5054a6de634b015f54dacbe81427d0d2)
- [smbus_host_notify_remove_cb()](https://docs.zephyrproject.org/latest/doxygen/html/group__smbus__interface.html#ga9190cfe3ce0c41c0a37d5345bad812d4)
- [smbus_pcall()](https://docs.zephyrproject.org/latest/doxygen/html/group__smbus__interface.html#ga2c1369835d3783bb5b5c3cb3711fec92)
- [smbus_quick()](https://docs.zephyrproject.org/latest/doxygen/html/group__smbus__interface.html#gab008499bca4a4096672d5909fa71b21d)
- [smbus_smbalert_set_cb()](https://docs.zephyrproject.org/latest/doxygen/html/group__smbus__interface.html#gadff533a6bc198815ee56d03a36b949e0)
- [smbus_smbalert_remove_cb()](https://docs.zephyrproject.org/latest/doxygen/html/group__smbus__interface.html#gaa18281b8f9859e46a138a874a8873366)
- [smbus_word_data_read()](https://docs.zephyrproject.org/latest/doxygen/html/group__smbus__interface.html#ga72a789110c7286a51c5cd5e2215abce1)
- [smbus_word_data_write()](https://docs.zephyrproject.org/latest/doxygen/html/group__smbus__interface.html#gade05f9bbbba609832df91fe804dd5d3c)

<a id="header-details"></a>
<a id="doc-typedef-members"></a>
<a id="header-doc-typedef-members"></a>

---

[上一章](P020_外设传感器接口（PSI5）.md) · [返回大纲](大纲.md) · [下一章](P022_TMP11X API主题.md)
