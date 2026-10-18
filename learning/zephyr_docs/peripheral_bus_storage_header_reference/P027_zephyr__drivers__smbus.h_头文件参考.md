---
id: learning.zephyr-docs.peripheral-bus-storage-header-reference.page-27
title: zephyr__drivers__smbus.h_头文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/smbus_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第27章\_zephyr\_\_drivers\_\_smbus.h\_头文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/smbus_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

系统管理总线（System Management Bus，SMBus）驱动API的主头文件。

<a id="details"></a>

```c
#include <errno.h>
#include <zephyr/sys/slist.h>
#include <zephyr/types.h>
#include <zephyr/device.h>
#include <zephyr/stats/stats.h>
#include <zephyr/syscalls/smbus.h>
```

查看此文件的源码。

系统管理总线（System Management Bus，SMBus）驱动API的主头文件。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 27.1\_数据结构（Data Structures）

<a id="r_smbus_5Fcallback"></a>

```c
struct smbus_callback
```

相关声明：[smbus_callback](../peripheral_bus_storage_model_reference/P091_smbus_callback_结构体.md)。

系统管理总线（SMBus）的回调结构。

<a id="r_smbus_5Fdt_5Fspec"></a>

```c
struct smbus_dt_spec
```

相关声明：[smbus_dt_spec](../peripheral_bus_storage_model_reference/P093_smbus_dt_spec_结构体.md)。

完整的系统管理总线（SMBus）设备树（DT）信息。

<a id="r_smbus_5Fdriver_5Fapi"></a>

```c
struct smbus_driver_api
```

相关声明：[smbus_driver_api](../peripheral_bus_storage_model_reference/P092_smbus_driver_api_结构体.md)。

驱动操作（Driver Operations）：系统管理总线（SMBus）驱动操作。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 27.2\_宏定义（Macros）

<a id="r_ga5ccde036931dc54e684ae5b955ff80d3"></a>

```c
#define SMBUS_BLOCK_BYTES_MAX 32
```

相关声明：[SMBUS_BLOCK_BYTES_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__smbus__interface.html#ga5ccde036931dc54e684ae5b955ff80d3)。

SMBus 块协议（Block protocol）的最大字节数。

<a id="r_gaf489d1b6c6aaaa1b3b1e9db823b24241"></a>

```c
#define SMBUS_DT_SPEC_GET(node_id)
```

相关声明：[SMBUS_DT_SPEC_GET](https://docs.zephyrproject.org/latest/doxygen/html/group__smbus__interface.html#gaf489d1b6c6aaaa1b3b1e9db823b24241)。

根据设备树生成 `smbus_dt_spec` 的结构体初始化器。

<a id="r_ga7e5bf5ecea7cbadf5d2a8b0c1e7a91af"></a>

```c
#define SMBUS_DT_SPEC_INST_GET(inst)
```

相关声明：[SMBUS_DT_SPEC_INST_GET](https://docs.zephyrproject.org/latest/doxygen/html/group__smbus__interface.html#ga7e5bf5ecea7cbadf5d2a8b0c1e7a91af)。

根据设备树实例生成 `smbus_dt_spec` 的结构体初始化器。

<a id="r_gaab024b741eb2c126d41d6db6e76333ee"></a>

```c
#define SMBUS_DEVICE_DT_DEFINE(node_id, init_fn, pm_device, data_ptr, cfg_ptr, level, prio, api_ptr, ...)
```

相关声明：[SMBUS_DEVICE_DT_DEFINE](https://docs.zephyrproject.org/latest/doxygen/html/group__smbus__interface.html#gaab024b741eb2c126d41d6db6e76333ee)、[pm_device](../power/P039_通用设备运行时电源结构.md)。

类似于 `DEVICE_DT_DEFINE()`，但包含 SMBus 专用设置。

<a id="r_ga610bc9c96bb22741c850696127f16b92"></a>

```c
#define SMBUS_DEVICE_DT_INST_DEFINE(inst, ...)
```

相关声明：[SMBUS_DEVICE_DT_INST_DEFINE](https://docs.zephyrproject.org/latest/doxygen/html/group__smbus__interface.html#ga610bc9c96bb22741c850696127f16b92)。

面向 `DT_DRV_COMPAT` 兼容设备实例的 `SMBUS_DEVICE_DT_DEFINE()` 对应形式。

<a id="define-members-0"></a>

### SMBus 协议命令（Protocol commands）

SMBus 规范定义了以下 SMBus 协议操作。

<a id="r_ga7cf2e52d836b28041f9aeb7ac3c172e4"></a>

```c
#define SMBUS_CMD_QUICK 0b000
```

相关声明：[SMBUS_CMD_QUICK](https://docs.zephyrproject.org/latest/doxygen/html/group__smbus__interface.html#ga7cf2e52d836b28041f9aeb7ac3c172e4)。

SMBus 快速协议（Quick protocol）是非常简单的命令，不发送或接收数据。

<a id="r_gafa607ea7083ad73873716282e1f55c8e"></a>

```c
#define SMBUS_CMD_BYTE 0b001
```

相关声明：[SMBUS_CMD_BYTE](https://docs.zephyrproject.org/latest/doxygen/html/group__smbus__interface.html#gafa607ea7083ad73873716282e1f55c8e)。

SMBus 字节协议（Byte protocol）可发送或接收一个字节的数据。

<a id="r_gabf5306ea95a2e8e5dc0270331218ea3d"></a>

```c
#define SMBUS_CMD_BYTE_DATA 0b010
```

相关声明：[SMBUS_CMD_BYTE_DATA](https://docs.zephyrproject.org/latest/doxygen/html/group__smbus__interface.html#gabf5306ea95a2e8e5dc0270331218ea3d)。

SMBus 字节数据协议（Byte Data protocol）先发送第一个字节，即命令，然后读取或写入一个字节。

<a id="r_ga70743c58b580018e567d2cb8595bea6f"></a>

```c
#define SMBUS_CMD_WORD_DATA 0b011
```

相关声明：[SMBUS_CMD_WORD_DATA](https://docs.zephyrproject.org/latest/doxygen/html/group__smbus__interface.html#ga70743c58b580018e567d2cb8595bea6f)。

SMBus 字数据协议（Word Data protocol）先发送第一个字节，即命令，然后读取或写入两个字节。

<a id="r_ga4400135f39814e328cf5e8ae11f27e3c"></a>

```c
#define SMBUS_CMD_PROC_CALL 0b100
```

相关声明：[SMBUS_CMD_PROC_CALL](https://docs.zephyrproject.org/latest/doxygen/html/group__smbus__interface.html#ga4400135f39814e328cf5e8ae11f27e3c)。

SMBus 过程调用协议（Process Call protocol）先写一个字（Write Word），再读一个字（Read Word）。

<a id="r_gaa8d81258230e67e4f87b5908ab66b08d"></a>

```c
#define SMBUS_CMD_BLOCK 0b101
```

相关声明：[SMBUS_CMD_BLOCK](https://docs.zephyrproject.org/latest/doxygen/html/group__smbus__interface.html#gaa8d81258230e67e4f87b5908ab66b08d)。

SMBus 块协议（Block protocol）读取或写入一个最多 32 字节的数据块。

<a id="r_ga9505b622875799e381c51f2df601c57a"></a>

```c
#define SMBUS_CMD_BLOCK_PROC 0b111
```

相关声明：[SMBUS_CMD_BLOCK_PROC](https://docs.zephyrproject.org/latest/doxygen/html/group__smbus__interface.html#ga9505b622875799e381c51f2df601c57a)。

SMBus 块写入—块读取过程调用协议（Block Write - Block Read Process Call）先执行块写入，再执行块读取。

<a id="define-members-1"></a>

### SMBus 设备功能（Device functionality）

以下参数描述 SMBus 设备的功能。

<a id="r_ga440a66ac32cf89d4a37782a0b51bda2c"></a>

```c
#define SMBUS_MODE_CONTROLLER BIT(0)
```

相关声明：[SMBUS_MODE_CONTROLLER](https://docs.zephyrproject.org/latest/doxygen/html/group__smbus__interface.html#ga440a66ac32cf89d4a37782a0b51bda2c)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

使外设作为控制器（Controller）运行。

<a id="r_ga6b9ddfb187688f3b1e1a3fdace9ecc76"></a>

```c
#define SMBUS_MODE_PEC BIT(1)
```

相关声明：[SMBUS_MODE_PEC](https://docs.zephyrproject.org/latest/doxygen/html/group__smbus__interface.html#ga6b9ddfb187688f3b1e1a3fdace9ecc76)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

支持数据包错误码（Packet Error Code，PEC）检查。

<a id="r_ga0633fc1ff48d806b6ca0e408f29141fe"></a>

```c
#define SMBUS_MODE_HOST_NOTIFY BIT(2)
```

相关声明：[SMBUS_MODE_HOST_NOTIFY](https://docs.zephyrproject.org/latest/doxygen/html/group__smbus__interface.html#ga0633fc1ff48d806b6ca0e408f29141fe)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

支持主机通知（Host Notify）功能。

<a id="r_ga7675e48d824e97df4c07c0e2496bee3d"></a>

```c
#define SMBUS_MODE_SMBALERT BIT(3)
```

相关声明：[SMBUS_MODE_SMBALERT](https://docs.zephyrproject.org/latest/doxygen/html/group__smbus__interface.html#ga7675e48d824e97df4c07c0e2496bee3d)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

支持 `SMBALERT` 信号功能。

<a id="define-members-2"></a>

### SMBus 特殊保留地址（Special reserved addresses）

以下地址由 SMBus 规范保留。

<a id="r_ga1d282b18efccf83456acd14a8f4cd970"></a>

```c
#define SMBUS_ADDRESS_ARA 0x0c
```

相关声明：[SMBUS_ADDRESS_ARA](https://docs.zephyrproject.org/latest/doxygen/html/group__smbus__interface.html#ga1d282b18efccf83456acd14a8f4cd970)。

告警响应地址（Alert Response Address，ARA）。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 27.3\_类型定义（Typedefs）

<a id="r_ga6d6ee9d29de5c0007d34328eb7c9f7c9"></a>

```c
typedef void(* smbus_callback_handler_t) (const struct device *dev, struct smbus_callback *cb, uint8_t addr)
```

相关声明：[smbus_callback_handler_t](https://docs.zephyrproject.org/latest/doxygen/html/group__smbus__interface.html#ga6d6ee9d29de5c0007d34328eb7c9f7c9)、[device](../device_reference/P002_设备对象结构.md)、[smbus_callback](../peripheral_bus_storage_model_reference/P091_smbus_callback_结构体.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

定义 SMBus 回调处理函数签名。

<a id="r_ga5fa53c3cd255001a2c34b36a3d23be6f"></a>

```c
typedef int(* smbus_api_configure_t) (const struct device *dev, uint32_t dev_config)
```

相关声明：[smbus_api_configure_t](https://docs.zephyrproject.org/latest/doxygen/html/group__smbus__interface__backend.html#ga5fa53c3cd255001a2c34b36a3d23be6f)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)。

配置 SMBus 主机控制器的运行方式。

<a id="r_gace2a4372975b44428fb39015e4b4bb25"></a>

```c
typedef int(* smbus_api_get_config_t) (const struct device *dev, uint32_t *dev_config)
```

相关声明：[smbus_api_get_config_t](https://docs.zephyrproject.org/latest/doxygen/html/group__smbus__interface__backend.html#gace2a4372975b44428fb39015e4b4bb25)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)。

获取 SMBus 主机控制器的配置。

<a id="r_ga93ce314c2797a21ed0b01bb28c69aeaf"></a>

```c
typedef int(* smbus_api_quick_t) (const struct device *dev, uint16_t addr, enum smbus_direction)
```

相关声明：[smbus_api_quick_t](https://docs.zephyrproject.org/latest/doxygen/html/group__smbus__interface__backend.html#ga93ce314c2797a21ed0b01bb28c69aeaf)、[device](../device_reference/P002_设备对象结构.md)、[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[smbus_direction](https://docs.zephyrproject.org/latest/doxygen/html/group__smbus__interface.html#gad0c28687977d0a7866bdea87aef88016)。

执行 SMBus 快速操作（Quick）。

<a id="r_ga2a59de36841ca4ff5fb65e29c512cd4e"></a>

```c
typedef int(* smbus_api_byte_write_t) (const struct device *dev, uint16_t addr, uint8_t byte)
```

相关声明：[smbus_api_byte_write_t](https://docs.zephyrproject.org/latest/doxygen/html/group__smbus__interface__backend.html#ga2a59de36841ca4ff5fb65e29c512cd4e)、[device](../device_reference/P002_设备对象结构.md)、[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

执行 SMBus 字节写操作（Byte Write）。

<a id="r_gae25c3c8652730085ec31701a48f086b5"></a>

```c
typedef int(* smbus_api_byte_read_t) (const struct device *dev, uint16_t addr, uint8_t *byte)
```

相关声明：[smbus_api_byte_read_t](https://docs.zephyrproject.org/latest/doxygen/html/group__smbus__interface__backend.html#gae25c3c8652730085ec31701a48f086b5)、[device](../device_reference/P002_设备对象结构.md)、[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

执行 SMBus 字节读操作（Byte Read）。

<a id="r_ga7827a1f9c5cf8c2b33c79e09d05019ca"></a>

```c
typedef int(* smbus_api_byte_data_write_t) (const struct device *dev, uint16_t addr, uint8_t cmd, uint8_t byte)
```

相关声明：[smbus_api_byte_data_write_t](https://docs.zephyrproject.org/latest/doxygen/html/group__smbus__interface__backend.html#ga7827a1f9c5cf8c2b33c79e09d05019ca)、[device](../device_reference/P002_设备对象结构.md)、[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[cmd](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#gacde1ca3945cbe6c828f65051c5c3a615)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

执行 SMBus 字节数据写操作（Byte Data Write）。

<a id="r_ga36f67cfe281dea020b6036399e433f4a"></a>

```c
typedef int(* smbus_api_byte_data_read_t) (const struct device *dev, uint16_t addr, uint8_t cmd, uint8_t *byte)
```

相关声明：[smbus_api_byte_data_read_t](https://docs.zephyrproject.org/latest/doxygen/html/group__smbus__interface__backend.html#ga36f67cfe281dea020b6036399e433f4a)、[device](../device_reference/P002_设备对象结构.md)、[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[cmd](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#gacde1ca3945cbe6c828f65051c5c3a615)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

执行 SMBus 字节数据读操作（Byte Data Read）。

<a id="r_ga31f2a46f83fe193f05cc5494435e2e6f"></a>

```c
typedef int(* smbus_api_word_data_write_t) (const struct device *dev, uint16_t addr, uint8_t cmd, uint16_t word)
```

相关声明：[smbus_api_word_data_write_t](https://docs.zephyrproject.org/latest/doxygen/html/group__smbus__interface__backend.html#ga31f2a46f83fe193f05cc5494435e2e6f)、[device](../device_reference/P002_设备对象结构.md)、[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[cmd](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#gacde1ca3945cbe6c828f65051c5c3a615)、[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)。

执行 SMBus 字数据写操作（Word Data Write）。

<a id="r_ga94b1bf5e10799ab1f07cccb289033ca6"></a>

```c
typedef int(* smbus_api_word_data_read_t) (const struct device *dev, uint16_t addr, uint8_t cmd, uint16_t *word)
```

相关声明：[smbus_api_word_data_read_t](https://docs.zephyrproject.org/latest/doxygen/html/group__smbus__interface__backend.html#ga94b1bf5e10799ab1f07cccb289033ca6)、[device](../device_reference/P002_设备对象结构.md)、[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[cmd](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#gacde1ca3945cbe6c828f65051c5c3a615)、[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)。

执行 SMBus 字数据读操作（Word Data Read）。

<a id="r_gaabd1e34153c852469e74e9fdc4118c84"></a>

```c
typedef int(* smbus_api_pcall_t) (const struct device *dev, uint16_t addr, uint8_t cmd, uint16_t send_word, uint16_t *recv_word)
```

相关声明：[smbus_api_pcall_t](https://docs.zephyrproject.org/latest/doxygen/html/group__smbus__interface__backend.html#gaabd1e34153c852469e74e9fdc4118c84)、[device](../device_reference/P002_设备对象结构.md)、[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[cmd](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#gacde1ca3945cbe6c828f65051c5c3a615)、[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)。

执行 SMBus 过程调用（Process Call）。

<a id="r_gad118b4dc6c7bdea57a6d70240d804b02"></a>

```c
typedef int(* smbus_api_block_write_t) (const struct device *dev, uint16_t addr, uint8_t cmd, uint8_t count, uint8_t *buf)
```

相关声明：[smbus_api_block_write_t](https://docs.zephyrproject.org/latest/doxygen/html/group__smbus__interface__backend.html#gad118b4dc6c7bdea57a6d70240d804b02)、[device](../device_reference/P002_设备对象结构.md)、[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[cmd](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#gacde1ca3945cbe6c828f65051c5c3a615)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

执行 SMBus 块写操作（Block Write）。

<a id="r_gad7453c161b4fa3c6085c186b39301659"></a>

```c
typedef int(* smbus_api_block_read_t) (const struct device *dev, uint16_t addr, uint8_t cmd, uint8_t *count, uint8_t *buf)
```

相关声明：[smbus_api_block_read_t](https://docs.zephyrproject.org/latest/doxygen/html/group__smbus__interface__backend.html#gad7453c161b4fa3c6085c186b39301659)、[device](../device_reference/P002_设备对象结构.md)、[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[cmd](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#gacde1ca3945cbe6c828f65051c5c3a615)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

执行 SMBus 块读操作（Block Read）。

<a id="r_ga8e71f105c10414e4ae86b87345e70837"></a>

```c
typedef int(* smbus_api_block_pcall_t) (const struct device *dev, uint16_t addr, uint8_t cmd, uint8_t send_count, uint8_t *send_buf, uint8_t *recv_count, uint8_t *recv_buf)
```

相关声明：[smbus_api_block_pcall_t](https://docs.zephyrproject.org/latest/doxygen/html/group__smbus__interface__backend.html#ga8e71f105c10414e4ae86b87345e70837)、[device](../device_reference/P002_设备对象结构.md)、[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[cmd](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#gacde1ca3945cbe6c828f65051c5c3a615)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

执行 SMBus 块过程调用（Block Process Call）。

<a id="r_ga9a81152429fd1f70e699f6767feb8702"></a>

```c
typedef int(* smbus_api_smbalert_cb_t) (const struct device *dev, struct smbus_callback *cb)
```

相关声明：[smbus_api_smbalert_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__smbus__interface__backend.html#ga9a81152429fd1f70e699f6767feb8702)、[device](../device_reference/P002_设备对象结构.md)、[smbus_callback](../peripheral_bus_storage_model_reference/P091_smbus_callback_结构体.md)。

添加或移除 `SMBALERT` 回调。

<a id="r_ga82dc504437f78c488df25ecd63a83a5e"></a>

```c
typedef int(* smbus_api_host_notify_cb_t) (const struct device *dev, struct smbus_callback *cb)
```

相关声明：[smbus_api_host_notify_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__smbus__interface__backend.html#ga82dc504437f78c488df25ecd63a83a5e)、[device](../device_reference/P002_设备对象结构.md)、[smbus_callback](../peripheral_bus_storage_model_reference/P091_smbus_callback_结构体.md)。

添加或移除主机通知（Host Notify）回调。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 27.4\_枚举（Enumerations）

<a id="enum-members-0"></a>

### SMBus 读写方向（Read / write direction）

<a id="r_gad0c28687977d0a7866bdea87aef88016"></a>

```c
enum smbus_direction { SMBUS_MSG_WRITE = 0 , SMBUS_MSG_READ = 1 }
```

相关声明：[smbus_direction](https://docs.zephyrproject.org/latest/doxygen/html/group__smbus__interface.html#gad0c28687977d0a7866bdea87aef88016)、[SMBUS_MSG_WRITE](https://docs.zephyrproject.org/latest/doxygen/html/group__smbus__interface.html#ggad0c28687977d0a7866bdea87aef88016a9c9dec19cbada732cef85784b0eedc54)、[SMBUS_MSG_READ](https://docs.zephyrproject.org/latest/doxygen/html/group__smbus__interface.html#ggad0c28687977d0a7866bdea87aef88016aa87094fdacefac89c0b1a03be1c0d22f)。

SMBus 读写方向。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 27.5\_函数（Functions）

<a id="r_ga0a63b800c14f5831730372b9bad41864"></a>

```c
static void smbus_xfer_stats (const struct device *dev, uint8_t sent, uint8_t recv)
```

相关声明：[smbus_xfer_stats](https://docs.zephyrproject.org/latest/doxygen/html/group__smbus__interface.html#ga0a63b800c14f5831730372b9bad41864)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[recv](https://docs.zephyrproject.org/latest/doxygen/html/posix_2sys_2socket_8h.html#adee01662b0cf762a014efd87ab811276)。

更新 SMBus 统计信息（Stats）。

<a id="r_ga517305aa7cc9c93ae449b3c548d6c835"></a>

```c
int smbus_configure (const struct device *dev, uint32_t dev_config)
```

相关声明：[smbus_configure](https://docs.zephyrproject.org/latest/doxygen/html/group__smbus__interface.html#ga517305aa7cc9c93ae449b3c548d6c835)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)。

配置 SMBus 主机控制器的运行方式。

<a id="r_ga9ca38ca95c0576bdc75b7eb8d0ca29ef"></a>

```c
int smbus_get_config (const struct device *dev, uint32_t *dev_config)
```

相关声明：[smbus_get_config](https://docs.zephyrproject.org/latest/doxygen/html/group__smbus__interface.html#ga9ca38ca95c0576bdc75b7eb8d0ca29ef)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)。

获取 SMBus 主机控制器的配置。

<a id="r_gadff533a6bc198815ee56d03a36b949e0"></a>

```c
static int smbus_smbalert_set_cb (const struct device *dev, struct smbus_callback *cb)
```

相关声明：[smbus_smbalert_set_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__smbus__interface.html#gadff533a6bc198815ee56d03a36b949e0)、[device](../device_reference/P002_设备对象结构.md)、[smbus_callback](../peripheral_bus_storage_model_reference/P091_smbus_callback_结构体.md)。

为 SMBus 主机控制器添加 `SMBALERT` 回调。

<a id="r_gaa18281b8f9859e46a138a874a8873366"></a>

```c
static int smbus_smbalert_remove_cb (const struct device *dev, struct smbus_callback *cb)
```

相关声明：[smbus_smbalert_remove_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__smbus__interface.html#gaa18281b8f9859e46a138a874a8873366)、[device](../device_reference/P002_设备对象结构.md)、[smbus_callback](../peripheral_bus_storage_model_reference/P091_smbus_callback_结构体.md)。

从 SMBus 主机控制器移除 `SMBALERT` 回调。

<a id="r_ga5054a6de634b015f54dacbe81427d0d2"></a>

```c
static int smbus_host_notify_set_cb (const struct device *dev, struct smbus_callback *cb)
```

相关声明：[smbus_host_notify_set_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__smbus__interface.html#ga5054a6de634b015f54dacbe81427d0d2)、[device](../device_reference/P002_设备对象结构.md)、[smbus_callback](../peripheral_bus_storage_model_reference/P091_smbus_callback_结构体.md)。

为 SMBus 主机控制器添加主机通知（Host Notify）回调。

<a id="r_ga9190cfe3ce0c41c0a37d5345bad812d4"></a>

```c
static int smbus_host_notify_remove_cb (const struct device *dev, struct smbus_callback *cb)
```

相关声明：[smbus_host_notify_remove_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__smbus__interface.html#ga9190cfe3ce0c41c0a37d5345bad812d4)、[device](../device_reference/P002_设备对象结构.md)、[smbus_callback](../peripheral_bus_storage_model_reference/P091_smbus_callback_结构体.md)。

从 SMBus 主机控制器移除主机通知（Host Notify）回调。

<a id="r_gab008499bca4a4096672d5909fa71b21d"></a>

```c
int smbus_quick (const struct device *dev, uint16_t addr, enum smbus_direction direction)
```

相关声明：[smbus_quick](https://docs.zephyrproject.org/latest/doxygen/html/group__smbus__interface.html#gab008499bca4a4096672d5909fa71b21d)、[device](../device_reference/P002_设备对象结构.md)、[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[smbus_direction](https://docs.zephyrproject.org/latest/doxygen/html/group__smbus__interface.html#gad0c28687977d0a7866bdea87aef88016)。

执行 SMBus 快速操作（Quick）。

<a id="r_ga7dd01c1e00a0f8b0315e442707332251"></a>

```c
int smbus_byte_write (const struct device *dev, uint16_t addr, uint8_t byte)
```

相关声明：[smbus_byte_write](https://docs.zephyrproject.org/latest/doxygen/html/group__smbus__interface.html#ga7dd01c1e00a0f8b0315e442707332251)、[device](../device_reference/P002_设备对象结构.md)、[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

执行 SMBus 字节写操作（Byte Write）。

<a id="r_gadaef9dad3470a7e4d3360e0246271ca1"></a>

```c
int smbus_byte_read (const struct device *dev, uint16_t addr, uint8_t *byte)
```

相关声明：[smbus_byte_read](https://docs.zephyrproject.org/latest/doxygen/html/group__smbus__interface.html#gadaef9dad3470a7e4d3360e0246271ca1)、[device](../device_reference/P002_设备对象结构.md)、[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

执行 SMBus 字节读操作（Byte Read）。

<a id="r_gadd7ec1eb3db981efceb8f959546a3b6a"></a>

```c
int smbus_byte_data_write (const struct device *dev, uint16_t addr, uint8_t cmd, uint8_t byte)
```

相关声明：[smbus_byte_data_write](https://docs.zephyrproject.org/latest/doxygen/html/group__smbus__interface.html#gadd7ec1eb3db981efceb8f959546a3b6a)、[device](../device_reference/P002_设备对象结构.md)、[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[cmd](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#gacde1ca3945cbe6c828f65051c5c3a615)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

执行 SMBus 字节数据写操作（Byte Data Write）。

<a id="r_ga1f1148a7cb92e0e0aef7ae3a84615c9b"></a>

```c
int smbus_byte_data_read (const struct device *dev, uint16_t addr, uint8_t cmd, uint8_t *byte)
```

相关声明：[smbus_byte_data_read](https://docs.zephyrproject.org/latest/doxygen/html/group__smbus__interface.html#ga1f1148a7cb92e0e0aef7ae3a84615c9b)、[device](../device_reference/P002_设备对象结构.md)、[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[cmd](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#gacde1ca3945cbe6c828f65051c5c3a615)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

执行 SMBus 字节数据读操作（Byte Data Read）。

<a id="r_gade05f9bbbba609832df91fe804dd5d3c"></a>

```c
int smbus_word_data_write (const struct device *dev, uint16_t addr, uint8_t cmd, uint16_t word)
```

相关声明：[smbus_word_data_write](https://docs.zephyrproject.org/latest/doxygen/html/group__smbus__interface.html#gade05f9bbbba609832df91fe804dd5d3c)、[device](../device_reference/P002_设备对象结构.md)、[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[cmd](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#gacde1ca3945cbe6c828f65051c5c3a615)、[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)。

执行 SMBus 字数据写操作（Word Data Write）。

<a id="r_ga72a789110c7286a51c5cd5e2215abce1"></a>

```c
int smbus_word_data_read (const struct device *dev, uint16_t addr, uint8_t cmd, uint16_t *word)
```

相关声明：[smbus_word_data_read](https://docs.zephyrproject.org/latest/doxygen/html/group__smbus__interface.html#ga72a789110c7286a51c5cd5e2215abce1)、[device](../device_reference/P002_设备对象结构.md)、[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[cmd](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#gacde1ca3945cbe6c828f65051c5c3a615)、[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)。

执行 SMBus 字数据读操作（Word Data Read）。

<a id="r_ga2c1369835d3783bb5b5c3cb3711fec92"></a>

```c
int smbus_pcall (const struct device *dev, uint16_t addr, uint8_t cmd, uint16_t send_word, uint16_t *recv_word)
```

相关声明：[smbus_pcall](https://docs.zephyrproject.org/latest/doxygen/html/group__smbus__interface.html#ga2c1369835d3783bb5b5c3cb3711fec92)、[device](../device_reference/P002_设备对象结构.md)、[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[cmd](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#gacde1ca3945cbe6c828f65051c5c3a615)、[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)。

执行 SMBus 过程调用（Process Call）。

<a id="r_ga55a867cdcb504039f274abae2d1a99e4"></a>

```c
int smbus_block_write (const struct device *dev, uint16_t addr, uint8_t cmd, uint8_t count, uint8_t *buf)
```

相关声明：[smbus_block_write](https://docs.zephyrproject.org/latest/doxygen/html/group__smbus__interface.html#ga55a867cdcb504039f274abae2d1a99e4)、[device](../device_reference/P002_设备对象结构.md)、[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[cmd](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#gacde1ca3945cbe6c828f65051c5c3a615)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

执行 SMBus 块写操作（Block Write）。

<a id="r_ga67603db9b44636b0b62a24fd623cfb1c"></a>

```c
int smbus_block_read (const struct device *dev, uint16_t addr, uint8_t cmd, uint8_t *count, uint8_t *buf)
```

相关声明：[smbus_block_read](https://docs.zephyrproject.org/latest/doxygen/html/group__smbus__interface.html#ga67603db9b44636b0b62a24fd623cfb1c)、[device](../device_reference/P002_设备对象结构.md)、[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[cmd](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#gacde1ca3945cbe6c828f65051c5c3a615)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

执行 SMBus 块读操作（Block Read）。

<a id="r_ga680c3d713a615f4b62503d6f84de4290"></a>

```c
int smbus_block_pcall (const struct device *dev, uint16_t addr, uint8_t cmd, uint8_t snd_count, uint8_t *snd_buf, uint8_t *rcv_count, uint8_t *rcv_buf)
```

相关声明：[smbus_block_pcall](https://docs.zephyrproject.org/latest/doxygen/html/group__smbus__interface.html#ga680c3d713a615f4b62503d6f84de4290)、[device](../device_reference/P002_设备对象结构.md)、[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[cmd](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#gacde1ca3945cbe6c828f65051c5c3a615)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

执行 SMBus 块过程调用（Block Process Call）。


## 27.6\_原页交叉引用（Cross References）

- [errno.h](../error_reference/P005_错误号头文件源码.md)
- [zephyr/sys/slist.h](../slist_reference/P003_单向链表头文件源码.md)
- [zephyr/types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2types_8h_source.html)
- [zephyr/device.h](../device_reference/P008_设备模型头文件源码.md)
- [zephyr/stats/stats.h](https://docs.zephyrproject.org/latest/doxygen/html/stats_2stats_8h_source.html)
- [查看此文件的源码](https://docs.zephyrproject.org/latest/doxygen/html/smbus_8h_source.html)
- [smbus_callback](../peripheral_bus_storage_model_reference/P091_smbus_callback_结构体.md)
- [smbus_dt_spec](../peripheral_bus_storage_model_reference/P093_smbus_dt_spec_结构体.md)
- [smbus_driver_api](../peripheral_bus_storage_model_reference/P092_smbus_driver_api_结构体.md)
- [SMBUS_BLOCK_BYTES_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__smbus__interface.html#ga5ccde036931dc54e684ae5b955ff80d3)
- [SMBUS_DT_SPEC_GET](https://docs.zephyrproject.org/latest/doxygen/html/group__smbus__interface.html#gaf489d1b6c6aaaa1b3b1e9db823b24241)
- [SMBUS_DT_SPEC_INST_GET](https://docs.zephyrproject.org/latest/doxygen/html/group__smbus__interface.html#ga7e5bf5ecea7cbadf5d2a8b0c1e7a91af)
- [SMBUS_DEVICE_DT_DEFINE](https://docs.zephyrproject.org/latest/doxygen/html/group__smbus__interface.html#gaab024b741eb2c126d41d6db6e76333ee)
- [pm_device](../power/P039_通用设备运行时电源结构.md)
- [DEVICE_DT_DEFINE()](../device_reference/P001_设备模型公共接口.md#gac49e26fbe91a14307d5ea08d41561dd1)
- [SMBUS_DEVICE_DT_INST_DEFINE](https://docs.zephyrproject.org/latest/doxygen/html/group__smbus__interface.html#ga610bc9c96bb22741c850696127f16b92)
- [SMBUS_CMD_QUICK](https://docs.zephyrproject.org/latest/doxygen/html/group__smbus__interface.html#ga7cf2e52d836b28041f9aeb7ac3c172e4)
- [SMBUS_CMD_BYTE](https://docs.zephyrproject.org/latest/doxygen/html/group__smbus__interface.html#gafa607ea7083ad73873716282e1f55c8e)
- [SMBUS_CMD_BYTE_DATA](https://docs.zephyrproject.org/latest/doxygen/html/group__smbus__interface.html#gabf5306ea95a2e8e5dc0270331218ea3d)
- [SMBUS_CMD_WORD_DATA](https://docs.zephyrproject.org/latest/doxygen/html/group__smbus__interface.html#ga70743c58b580018e567d2cb8595bea6f)
- [SMBUS_CMD_PROC_CALL](https://docs.zephyrproject.org/latest/doxygen/html/group__smbus__interface.html#ga4400135f39814e328cf5e8ae11f27e3c)
- [SMBUS_CMD_BLOCK](https://docs.zephyrproject.org/latest/doxygen/html/group__smbus__interface.html#gaa8d81258230e67e4f87b5908ab66b08d)
- [SMBUS_CMD_BLOCK_PROC](https://docs.zephyrproject.org/latest/doxygen/html/group__smbus__interface.html#ga9505b622875799e381c51f2df601c57a)
- [SMBUS_MODE_CONTROLLER](https://docs.zephyrproject.org/latest/doxygen/html/group__smbus__interface.html#ga440a66ac32cf89d4a37782a0b51bda2c)
- [BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)
- [SMBUS_MODE_PEC](https://docs.zephyrproject.org/latest/doxygen/html/group__smbus__interface.html#ga6b9ddfb187688f3b1e1a3fdace9ecc76)
- [SMBUS_MODE_HOST_NOTIFY](https://docs.zephyrproject.org/latest/doxygen/html/group__smbus__interface.html#ga0633fc1ff48d806b6ca0e408f29141fe)
- [SMBUS_MODE_SMBALERT](https://docs.zephyrproject.org/latest/doxygen/html/group__smbus__interface.html#ga7675e48d824e97df4c07c0e2496bee3d)
- [SMBUS_ADDRESS_ARA](https://docs.zephyrproject.org/latest/doxygen/html/group__smbus__interface.html#ga1d282b18efccf83456acd14a8f4cd970)
- [smbus_callback_handler_t](https://docs.zephyrproject.org/latest/doxygen/html/group__smbus__interface.html#ga6d6ee9d29de5c0007d34328eb7c9f7c9)
- [device](../device_reference/P002_设备对象结构.md)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [smbus_api_configure_t](https://docs.zephyrproject.org/latest/doxygen/html/group__smbus__interface__backend.html#ga5fa53c3cd255001a2c34b36a3d23be6f)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [smbus_api_get_config_t](https://docs.zephyrproject.org/latest/doxygen/html/group__smbus__interface__backend.html#gace2a4372975b44428fb39015e4b4bb25)
- [smbus_api_quick_t](https://docs.zephyrproject.org/latest/doxygen/html/group__smbus__interface__backend.html#ga93ce314c2797a21ed0b01bb28c69aeaf)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [smbus_direction](https://docs.zephyrproject.org/latest/doxygen/html/group__smbus__interface.html#gad0c28687977d0a7866bdea87aef88016)
- [smbus_api_byte_write_t](https://docs.zephyrproject.org/latest/doxygen/html/group__smbus__interface__backend.html#ga2a59de36841ca4ff5fb65e29c512cd4e)
- [smbus_api_byte_read_t](https://docs.zephyrproject.org/latest/doxygen/html/group__smbus__interface__backend.html#gae25c3c8652730085ec31701a48f086b5)
- [smbus_api_byte_data_write_t](https://docs.zephyrproject.org/latest/doxygen/html/group__smbus__interface__backend.html#ga7827a1f9c5cf8c2b33c79e09d05019ca)
- [cmd](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#gacde1ca3945cbe6c828f65051c5c3a615)
- [smbus_api_byte_data_read_t](https://docs.zephyrproject.org/latest/doxygen/html/group__smbus__interface__backend.html#ga36f67cfe281dea020b6036399e433f4a)
- [smbus_api_word_data_write_t](https://docs.zephyrproject.org/latest/doxygen/html/group__smbus__interface__backend.html#ga31f2a46f83fe193f05cc5494435e2e6f)
- [smbus_api_word_data_read_t](https://docs.zephyrproject.org/latest/doxygen/html/group__smbus__interface__backend.html#ga94b1bf5e10799ab1f07cccb289033ca6)
- [smbus_api_pcall_t](https://docs.zephyrproject.org/latest/doxygen/html/group__smbus__interface__backend.html#gaabd1e34153c852469e74e9fdc4118c84)
- [smbus_api_block_write_t](https://docs.zephyrproject.org/latest/doxygen/html/group__smbus__interface__backend.html#gad118b4dc6c7bdea57a6d70240d804b02)
- [smbus_api_block_read_t](https://docs.zephyrproject.org/latest/doxygen/html/group__smbus__interface__backend.html#gad7453c161b4fa3c6085c186b39301659)
- [smbus_api_block_pcall_t](https://docs.zephyrproject.org/latest/doxygen/html/group__smbus__interface__backend.html#ga8e71f105c10414e4ae86b87345e70837)
- [smbus_api_smbalert_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__smbus__interface__backend.html#ga9a81152429fd1f70e699f6767feb8702)
- [smbus_api_host_notify_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__smbus__interface__backend.html#ga82dc504437f78c488df25ecd63a83a5e)
- [SMBUS_MSG_WRITE](https://docs.zephyrproject.org/latest/doxygen/html/group__smbus__interface.html#ggad0c28687977d0a7866bdea87aef88016a9c9dec19cbada732cef85784b0eedc54)
- [SMBUS_MSG_READ](https://docs.zephyrproject.org/latest/doxygen/html/group__smbus__interface.html#ggad0c28687977d0a7866bdea87aef88016aa87094fdacefac89c0b1a03be1c0d22f)
- [smbus_xfer_stats](https://docs.zephyrproject.org/latest/doxygen/html/group__smbus__interface.html#ga0a63b800c14f5831730372b9bad41864)
- [recv](https://docs.zephyrproject.org/latest/doxygen/html/posix_2sys_2socket_8h.html#adee01662b0cf762a014efd87ab811276)
- [smbus_configure](https://docs.zephyrproject.org/latest/doxygen/html/group__smbus__interface.html#ga517305aa7cc9c93ae449b3c548d6c835)
- [smbus_get_config](https://docs.zephyrproject.org/latest/doxygen/html/group__smbus__interface.html#ga9ca38ca95c0576bdc75b7eb8d0ca29ef)
- [smbus_smbalert_set_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__smbus__interface.html#gadff533a6bc198815ee56d03a36b949e0)
- [smbus_smbalert_remove_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__smbus__interface.html#gaa18281b8f9859e46a138a874a8873366)
- [smbus_host_notify_set_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__smbus__interface.html#ga5054a6de634b015f54dacbe81427d0d2)
- [smbus_host_notify_remove_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__smbus__interface.html#ga9190cfe3ce0c41c0a37d5345bad812d4)
- [smbus_quick](https://docs.zephyrproject.org/latest/doxygen/html/group__smbus__interface.html#gab008499bca4a4096672d5909fa71b21d)
- [smbus_byte_write](https://docs.zephyrproject.org/latest/doxygen/html/group__smbus__interface.html#ga7dd01c1e00a0f8b0315e442707332251)
- [smbus_byte_read](https://docs.zephyrproject.org/latest/doxygen/html/group__smbus__interface.html#gadaef9dad3470a7e4d3360e0246271ca1)
- [smbus_byte_data_write](https://docs.zephyrproject.org/latest/doxygen/html/group__smbus__interface.html#gadd7ec1eb3db981efceb8f959546a3b6a)
- [smbus_byte_data_read](https://docs.zephyrproject.org/latest/doxygen/html/group__smbus__interface.html#ga1f1148a7cb92e0e0aef7ae3a84615c9b)
- [smbus_word_data_write](https://docs.zephyrproject.org/latest/doxygen/html/group__smbus__interface.html#gade05f9bbbba609832df91fe804dd5d3c)
- [smbus_word_data_read](https://docs.zephyrproject.org/latest/doxygen/html/group__smbus__interface.html#ga72a789110c7286a51c5cd5e2215abce1)
- [smbus_pcall](https://docs.zephyrproject.org/latest/doxygen/html/group__smbus__interface.html#ga2c1369835d3783bb5b5c3cb3711fec92)
- [smbus_block_write](https://docs.zephyrproject.org/latest/doxygen/html/group__smbus__interface.html#ga55a867cdcb504039f274abae2d1a99e4)
- [smbus_block_read](https://docs.zephyrproject.org/latest/doxygen/html/group__smbus__interface.html#ga67603db9b44636b0b62a24fd623cfb1c)
- [smbus_block_pcall](https://docs.zephyrproject.org/latest/doxygen/html/group__smbus__interface.html#ga680c3d713a615f4b62503d6f84de4290)

<a id="header-details"></a>

---

[上一章](P026_zephyr__drivers__sent__sent.h_头文件参考.md) · [返回大纲](大纲.md) · [下一章](P028_zephyr__drivers__swdp.h_头文件参考.md)
