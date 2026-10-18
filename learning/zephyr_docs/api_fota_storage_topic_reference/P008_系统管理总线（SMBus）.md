---
id: learning.zephyr-docs.api-fota-storage-topic-reference.page-8
title: 系统管理总线（SMBus）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__smbus__interface.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第8章\_系统管理总线（SMBus）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__smbus__interface.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

系统管理总线（System Management Bus，SMBus）接口。

<a id="details"></a>

系统管理总线（System Management Bus，SMBus）接口。自（Since）3.4 起提供，版本（Version）0.8.0。

<a id="header-groups"></a>
<a id="groups"></a>

## 8.1\_主题（Topics）

<a id="r_smbus_5Finterface_5Fbackend"></a>

相关声明：[SMBus 驱动后端 API](../api_transport_control_topic_reference/P021_SMBus 驱动后端 API.md)。

<a id="header-files"></a>
<a id="files"></a>

## 8.2\_文件（Files）

<a id="r_smbus_2Eh"></a>

```c
file smbus.h
```

相关声明：[smbus.h](../peripheral_bus_storage_header_reference/P027_zephyr__drivers__smbus.h_头文件参考.md)。

系统管理总线（System Management Bus，SMBus）驱动API的主头文件。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 8.3\_数据结构（Data Structures）

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

<a id="header-define-members"></a>
<a id="define-members"></a>

## 8.4\_宏定义（Macros）

<a id="r_ga5ccde036931dc54e684ae5b955ff80d3"></a>

```c
#define SMBUS_BLOCK_BYTES_MAX 32
```

相关声明：[SMBUS_BLOCK_BYTES_MAX](#ga5ccde036931dc54e684ae5b955ff80d3)。

SMBus 块协议（Block protocol）的最大字节数。

<a id="r_gaf489d1b6c6aaaa1b3b1e9db823b24241"></a>

```c
#define SMBUS_DT_SPEC_GET(node_id)
```

相关声明：[SMBUS_DT_SPEC_GET](#gaf489d1b6c6aaaa1b3b1e9db823b24241)。

根据设备树生成 `smbus_dt_spec` 的结构体初始化器。

<a id="r_ga7e5bf5ecea7cbadf5d2a8b0c1e7a91af"></a>

```c
#define SMBUS_DT_SPEC_INST_GET(inst)
```

相关声明：[SMBUS_DT_SPEC_INST_GET](#ga7e5bf5ecea7cbadf5d2a8b0c1e7a91af)。

根据设备树实例生成 `smbus_dt_spec` 的结构体初始化器。

<a id="r_gaab024b741eb2c126d41d6db6e76333ee"></a>

```c
#define SMBUS_DEVICE_DT_DEFINE(node_id, init_fn, pm_device, data_ptr, cfg_ptr, level, prio, api_ptr, ...)
```

相关声明：[SMBUS_DEVICE_DT_DEFINE](#gaab024b741eb2c126d41d6db6e76333ee)、[pm_device](../power/P039_通用设备运行时电源结构.md)。

类似于 `DEVICE_DT_DEFINE()`，但包含 SMBus 专用设置。

<a id="r_ga610bc9c96bb22741c850696127f16b92"></a>

```c
#define SMBUS_DEVICE_DT_INST_DEFINE(inst, ...)
```

相关声明：[SMBUS_DEVICE_DT_INST_DEFINE](#ga610bc9c96bb22741c850696127f16b92)。

面向 `DT_DRV_COMPAT` 兼容设备实例的 `SMBUS_DEVICE_DT_DEFINE()` 对应形式。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 8.5\_类型定义（Typedefs）

<a id="r_ga6d6ee9d29de5c0007d34328eb7c9f7c9"></a>

```c
typedef void(* smbus_callback_handler_t) (const struct device *dev, struct smbus_callback *cb, uint8_t addr)
```

相关声明：[smbus_callback_handler_t](#ga6d6ee9d29de5c0007d34328eb7c9f7c9)、[device](../device_reference/P002_设备对象结构.md)、[smbus_callback](../peripheral_bus_storage_model_reference/P091_smbus_callback_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

定义 SMBus 回调处理函数签名。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 8.6\_函数（Functions）

<a id="r_ga0a63b800c14f5831730372b9bad41864"></a>

```c
static void smbus_xfer_stats (const struct device *dev, uint8_t sent, uint8_t recv)
```

相关声明：[smbus_xfer_stats](#ga0a63b800c14f5831730372b9bad41864)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[recv](../api_file_reference/P307_zephyr__posix__sys__socket.h_文件参考.md#adee01662b0cf762a014efd87ab811276)。

更新 SMBus 统计信息（Stats）。

<a id="r_ga517305aa7cc9c93ae449b3c548d6c835"></a>

```c
int smbus_configure (const struct device *dev, uint32_t dev_config)
```

相关声明：[smbus_configure](#ga517305aa7cc9c93ae449b3c548d6c835)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

配置 SMBus 主机控制器的运行方式。

<a id="r_ga9ca38ca95c0576bdc75b7eb8d0ca29ef"></a>

```c
int smbus_get_config (const struct device *dev, uint32_t *dev_config)
```

相关声明：[smbus_get_config](#ga9ca38ca95c0576bdc75b7eb8d0ca29ef)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

获取 SMBus 主机控制器的配置。

<a id="r_gadff533a6bc198815ee56d03a36b949e0"></a>

```c
static int smbus_smbalert_set_cb (const struct device *dev, struct smbus_callback *cb)
```

相关声明：[smbus_smbalert_set_cb](#gadff533a6bc198815ee56d03a36b949e0)、[device](../device_reference/P002_设备对象结构.md)、[smbus_callback](../peripheral_bus_storage_model_reference/P091_smbus_callback_结构体.md)。

为 SMBus 主机控制器添加 `SMBALERT` 回调。

<a id="r_gaa18281b8f9859e46a138a874a8873366"></a>

```c
static int smbus_smbalert_remove_cb (const struct device *dev, struct smbus_callback *cb)
```

相关声明：[smbus_smbalert_remove_cb](#gaa18281b8f9859e46a138a874a8873366)、[device](../device_reference/P002_设备对象结构.md)、[smbus_callback](../peripheral_bus_storage_model_reference/P091_smbus_callback_结构体.md)。

从 SMBus 主机控制器移除 `SMBALERT` 回调。

<a id="r_ga5054a6de634b015f54dacbe81427d0d2"></a>

```c
static int smbus_host_notify_set_cb (const struct device *dev, struct smbus_callback *cb)
```

相关声明：[smbus_host_notify_set_cb](#ga5054a6de634b015f54dacbe81427d0d2)、[device](../device_reference/P002_设备对象结构.md)、[smbus_callback](../peripheral_bus_storage_model_reference/P091_smbus_callback_结构体.md)。

为 SMBus 主机控制器添加主机通知（Host Notify）回调。

<a id="r_ga9190cfe3ce0c41c0a37d5345bad812d4"></a>

```c
static int smbus_host_notify_remove_cb (const struct device *dev, struct smbus_callback *cb)
```

相关声明：[smbus_host_notify_remove_cb](#ga9190cfe3ce0c41c0a37d5345bad812d4)、[device](../device_reference/P002_设备对象结构.md)、[smbus_callback](../peripheral_bus_storage_model_reference/P091_smbus_callback_结构体.md)。

从 SMBus 主机控制器移除主机通知（Host Notify）回调。

<a id="r_gab008499bca4a4096672d5909fa71b21d"></a>

```c
int smbus_quick (const struct device *dev, uint16_t addr, enum smbus_direction direction)
```

相关声明：[smbus_quick](#gab008499bca4a4096672d5909fa71b21d)、[device](../device_reference/P002_设备对象结构.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[smbus_direction](#gad0c28687977d0a7866bdea87aef88016)。

执行 SMBus 快速操作（Quick）。

<a id="r_ga7dd01c1e00a0f8b0315e442707332251"></a>

```c
int smbus_byte_write (const struct device *dev, uint16_t addr, uint8_t byte)
```

相关声明：[smbus_byte_write](#ga7dd01c1e00a0f8b0315e442707332251)、[device](../device_reference/P002_设备对象结构.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

执行 SMBus 字节写操作（Byte Write）。

<a id="r_gadaef9dad3470a7e4d3360e0246271ca1"></a>

```c
int smbus_byte_read (const struct device *dev, uint16_t addr, uint8_t *byte)
```

相关声明：[smbus_byte_read](#gadaef9dad3470a7e4d3360e0246271ca1)、[device](../device_reference/P002_设备对象结构.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

执行 SMBus 字节读操作（Byte Read）。

<a id="r_gadd7ec1eb3db981efceb8f959546a3b6a"></a>

```c
int smbus_byte_data_write (const struct device *dev, uint16_t addr, uint8_t cmd, uint8_t byte)
```

相关声明：[smbus_byte_data_write](#gadd7ec1eb3db981efceb8f959546a3b6a)、[device](../device_reference/P002_设备对象结构.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[cmd](../api_scoped_clock_topic_reference/P012_FT8xx 参考 API.md#gacde1ca3945cbe6c828f65051c5c3a615)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

执行 SMBus 字节数据写操作（Byte Data Write）。

<a id="r_ga1f1148a7cb92e0e0aef7ae3a84615c9b"></a>

```c
int smbus_byte_data_read (const struct device *dev, uint16_t addr, uint8_t cmd, uint8_t *byte)
```

相关声明：[smbus_byte_data_read](#ga1f1148a7cb92e0e0aef7ae3a84615c9b)、[device](../device_reference/P002_设备对象结构.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[cmd](../api_scoped_clock_topic_reference/P012_FT8xx 参考 API.md#gacde1ca3945cbe6c828f65051c5c3a615)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

执行 SMBus 字节数据读操作（Byte Data Read）。

<a id="r_gade05f9bbbba609832df91fe804dd5d3c"></a>

```c
int smbus_word_data_write (const struct device *dev, uint16_t addr, uint8_t cmd, uint16_t word)
```

相关声明：[smbus_word_data_write](#gade05f9bbbba609832df91fe804dd5d3c)、[device](../device_reference/P002_设备对象结构.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[cmd](../api_scoped_clock_topic_reference/P012_FT8xx 参考 API.md#gacde1ca3945cbe6c828f65051c5c3a615)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

执行 SMBus 字数据写操作（Word Data Write）。

<a id="r_ga72a789110c7286a51c5cd5e2215abce1"></a>

```c
int smbus_word_data_read (const struct device *dev, uint16_t addr, uint8_t cmd, uint16_t *word)
```

相关声明：[smbus_word_data_read](#ga72a789110c7286a51c5cd5e2215abce1)、[device](../device_reference/P002_设备对象结构.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[cmd](../api_scoped_clock_topic_reference/P012_FT8xx 参考 API.md#gacde1ca3945cbe6c828f65051c5c3a615)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

执行 SMBus 字数据读操作（Word Data Read）。

<a id="r_ga2c1369835d3783bb5b5c3cb3711fec92"></a>

```c
int smbus_pcall (const struct device *dev, uint16_t addr, uint8_t cmd, uint16_t send_word, uint16_t *recv_word)
```

相关声明：[smbus_pcall](#ga2c1369835d3783bb5b5c3cb3711fec92)、[device](../device_reference/P002_设备对象结构.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[cmd](../api_scoped_clock_topic_reference/P012_FT8xx 参考 API.md#gacde1ca3945cbe6c828f65051c5c3a615)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

执行 SMBus 过程调用（Process Call）。

<a id="r_ga55a867cdcb504039f274abae2d1a99e4"></a>

```c
int smbus_block_write (const struct device *dev, uint16_t addr, uint8_t cmd, uint8_t count, uint8_t *buf)
```

相关声明：[smbus_block_write](#ga55a867cdcb504039f274abae2d1a99e4)、[device](../device_reference/P002_设备对象结构.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[cmd](../api_scoped_clock_topic_reference/P012_FT8xx 参考 API.md#gacde1ca3945cbe6c828f65051c5c3a615)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

执行 SMBus 块写操作（Block Write）。

<a id="r_ga67603db9b44636b0b62a24fd623cfb1c"></a>

```c
int smbus_block_read (const struct device *dev, uint16_t addr, uint8_t cmd, uint8_t *count, uint8_t *buf)
```

相关声明：[smbus_block_read](#ga67603db9b44636b0b62a24fd623cfb1c)、[device](../device_reference/P002_设备对象结构.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[cmd](../api_scoped_clock_topic_reference/P012_FT8xx 参考 API.md#gacde1ca3945cbe6c828f65051c5c3a615)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

执行 SMBus 块读操作（Block Read）。

<a id="r_ga680c3d713a615f4b62503d6f84de4290"></a>

```c
int smbus_block_pcall (const struct device *dev, uint16_t addr, uint8_t cmd, uint8_t snd_count, uint8_t *snd_buf, uint8_t *rcv_count, uint8_t *rcv_buf)
```

相关声明：[smbus_block_pcall](#ga680c3d713a615f4b62503d6f84de4290)、[device](../device_reference/P002_设备对象结构.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[cmd](../api_scoped_clock_topic_reference/P012_FT8xx 参考 API.md#gacde1ca3945cbe6c828f65051c5c3a615)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

执行 SMBus 块过程调用（Block Process Call）。

<a id="header-member-group"></a>
<a id="member-group"></a>

## 8.7\_SMBus 读写方向（Read / write direction）

<a id="r_gad0c28687977d0a7866bdea87aef88016"></a>

```c
enum smbus_direction { SMBUS_MSG_WRITE = 0 , SMBUS_MSG_READ = 1 }
```

相关声明：[smbus_direction](#gad0c28687977d0a7866bdea87aef88016)、[SMBUS_MSG_WRITE](#ggad0c28687977d0a7866bdea87aef88016a9c9dec19cbada732cef85784b0eedc54)、[SMBUS_MSG_READ](#ggad0c28687977d0a7866bdea87aef88016aa87094fdacefac89c0b1a03be1c0d22f)。

SMBus 读写方向。

## 8.8\_SMBus 协议命令（Protocol commands）

SMBus 规范定义了以下 SMBus 协议操作。

<a id="r_ga7cf2e52d836b28041f9aeb7ac3c172e4"></a>

```c
#define SMBUS_CMD_QUICK 0b000
```

相关声明：[SMBUS_CMD_QUICK](#ga7cf2e52d836b28041f9aeb7ac3c172e4)。

SMBus 快速协议（Quick protocol）是非常简单的命令，不发送或接收数据。

<a id="r_gafa607ea7083ad73873716282e1f55c8e"></a>

```c
#define SMBUS_CMD_BYTE 0b001
```

相关声明：[SMBUS_CMD_BYTE](#gafa607ea7083ad73873716282e1f55c8e)。

SMBus 字节协议（Byte protocol）可发送或接收一个字节的数据。

<a id="r_gabf5306ea95a2e8e5dc0270331218ea3d"></a>

```c
#define SMBUS_CMD_BYTE_DATA 0b010
```

相关声明：[SMBUS_CMD_BYTE_DATA](#gabf5306ea95a2e8e5dc0270331218ea3d)。

SMBus 字节数据协议（Byte Data protocol）先发送第一个字节，即命令，然后读取或写入一个字节。

<a id="r_ga70743c58b580018e567d2cb8595bea6f"></a>

```c
#define SMBUS_CMD_WORD_DATA 0b011
```

相关声明：[SMBUS_CMD_WORD_DATA](#ga70743c58b580018e567d2cb8595bea6f)。

SMBus 字数据协议（Word Data protocol）先发送第一个字节，即命令，然后读取或写入两个字节。

<a id="r_ga4400135f39814e328cf5e8ae11f27e3c"></a>

```c
#define SMBUS_CMD_PROC_CALL 0b100
```

相关声明：[SMBUS_CMD_PROC_CALL](#ga4400135f39814e328cf5e8ae11f27e3c)。

SMBus 过程调用协议（Process Call protocol）先写一个字（Write Word），再读一个字（Read Word）。

<a id="r_gaa8d81258230e67e4f87b5908ab66b08d"></a>

```c
#define SMBUS_CMD_BLOCK 0b101
```

相关声明：[SMBUS_CMD_BLOCK](#gaa8d81258230e67e4f87b5908ab66b08d)。

SMBus 块协议（Block protocol）读取或写入一个最多 32 字节的数据块。

<a id="r_ga9505b622875799e381c51f2df601c57a"></a>

```c
#define SMBUS_CMD_BLOCK_PROC 0b111
```

相关声明：[SMBUS_CMD_BLOCK_PROC](#ga9505b622875799e381c51f2df601c57a)。

SMBus 块写入—块读取过程调用协议（Block Write - Block Read Process Call）先执行块写入，再执行块读取。

## 8.9\_SMBus 设备功能（Device functionality）

以下参数描述 SMBus 设备的功能。

<a id="r_ga440a66ac32cf89d4a37782a0b51bda2c"></a>

```c
#define SMBUS_MODE_CONTROLLER BIT(0)
```

相关声明：[SMBUS_MODE_CONTROLLER](#ga440a66ac32cf89d4a37782a0b51bda2c)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

使外设作为控制器（Controller）运行。

<a id="r_ga6b9ddfb187688f3b1e1a3fdace9ecc76"></a>

```c
#define SMBUS_MODE_PEC BIT(1)
```

相关声明：[SMBUS_MODE_PEC](#ga6b9ddfb187688f3b1e1a3fdace9ecc76)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

支持数据包错误码（Packet Error Code，PEC）检查。

<a id="r_ga0633fc1ff48d806b6ca0e408f29141fe"></a>

```c
#define SMBUS_MODE_HOST_NOTIFY BIT(2)
```

相关声明：[SMBUS_MODE_HOST_NOTIFY](#ga0633fc1ff48d806b6ca0e408f29141fe)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

支持主机通知（Host Notify）功能。

<a id="r_ga7675e48d824e97df4c07c0e2496bee3d"></a>

```c
#define SMBUS_MODE_SMBALERT BIT(3)
```

相关声明：[SMBUS_MODE_SMBALERT](#ga7675e48d824e97df4c07c0e2496bee3d)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

支持 `SMBALERT` 信号功能。

## 8.10\_SMBus 特殊保留地址（Special reserved addresses）

以下地址由 SMBus 规范保留。

<a id="r_ga1d282b18efccf83456acd14a8f4cd970"></a>

```c
#define SMBUS_ADDRESS_ARA 0x0c
```

相关声明：[SMBUS_ADDRESS_ARA](#ga1d282b18efccf83456acd14a8f4cd970)。

告警响应地址（Alert Response Address，ARA）。

## 8.11\_详细说明（Detailed Documentation）

<a id="ga1d282b18efccf83456acd14a8f4cd970"></a>

### `SMBUS_ADDRESS_ARA`

```c
#define SMBUS_ADDRESS_ARA 0x0c
```

```c
#include <zephyr/drivers/smbus.h>
```

告警响应地址（Alert Response Address，ARA）。

系统主机在告警响应协议（Alert Response Protocol）中使用的广播地址（Broadcast Address）。

<a id="ga5ccde036931dc54e684ae5b955ff80d3"></a>

### `SMBUS_BLOCK_BYTES_MAX`

```c
#define SMBUS_BLOCK_BYTES_MAX 32
```

```c
#include <zephyr/drivers/smbus.h>
```

SMBus 块协议（Block protocol）的最大字节数。

<a id="gaa8d81258230e67e4f87b5908ab66b08d"></a>

### `SMBUS_CMD_BLOCK`

```c
#define SMBUS_CMD_BLOCK 0b101
```

```c
#include <zephyr/drivers/smbus.h>
```

SMBus 块协议（Block protocol）读取或写入一个最多 32 字节的数据块。

计数字节（Count Byte）指定数据量。

原始示例（Example）：

```c
SMBus Block Write

0                   1                   2
0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|S| Periph Addr |W|A|  Command code |A| Send Count=N  |A|
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|  Data Write 1 |A|      ...      |A|  Data Write N |A|P|
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+

SMBus Block Read

0                   1                   2
0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|S| Periph Addr |W|A|  Command code |A|S| Periph Addr |R|
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|A|  Recv Count=N |A|  Data Read 1  |A|      ...      |A|
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|  Data Read N  |N|P|
+-+-+-+-+-+-+-+-+-+-+
```

<a id="ga9505b622875799e381c51f2df601c57a"></a>

### `SMBUS_CMD_BLOCK_PROC`

```c
#define SMBUS_CMD_BLOCK_PROC 0b111
```

```c
#include <zephyr/drivers/smbus.h>
```

SMBus 块写入—块读取过程调用协议（Block Write - Block Read Process Call）先执行块写入，再执行块读取。

原始示例（Example）：

```c
0                   1                   2
0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|S| Periph Addr |W|A|  Command code |A|   Count = N   |A|
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|  Data Write 1 |A|      ...      |A|  Data Write N |A|S|
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
| Periph Addr |R|A|  Recv Count=N |A|  Data Read 1  |A| |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|     ...     |A|  Data Read N  |N|P|
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
```

<a id="gafa607ea7083ad73873716282e1f55c8e"></a>

### `SMBUS_CMD_BYTE`

```c
#define SMBUS_CMD_BYTE 0b001
```

```c
#include <zephyr/drivers/smbus.h>
```

SMBus 字节协议（Byte protocol）可发送或接收一个字节的数据。

原始示例（Example）：

```c
Byte Write

0                   1                   2
0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|S| Periph Addr |W|A| Command code  |A|P|
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+

Byte Read

0                   1                   2
0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|S| Periph Addr |R|A| Byte received |N|P|
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
```

<a id="gabf5306ea95a2e8e5dc0270331218ea3d"></a>

### `SMBUS_CMD_BYTE_DATA`

```c
#define SMBUS_CMD_BYTE_DATA 0b010
```

```c
#include <zephyr/drivers/smbus.h>
```

SMBus 字节数据协议（Byte Data protocol）先发送第一个字节，即命令，然后读取或写入一个字节。

原始示例（Example）：

```c
Byte Data Write

0                   1                   2
0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|S| Periph Addr |W|A|  Command code |A|   Data Write  |A|P|
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+

Byte Data Read

0                   1                   2
0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|S| Periph Addr |W|A|  Command code |A|S| Periph Addr |R|A|
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|   Data Read   |N|P|
+-+-+-+-+-+-+-+-+-+-+
```

<a id="ga4400135f39814e328cf5e8ae11f27e3c"></a>

### `SMBUS_CMD_PROC_CALL`

```c
#define SMBUS_CMD_PROC_CALL 0b100
```

```c
#include <zephyr/drivers/smbus.h>
```

SMBus 过程调用协议（Process Call protocol）先写一个字（Write Word），再读一个字（Read Word）。

之所以这样命名，是因为该命令会发送数据并等待外设返回应答。

原始示例（Example）：

```c
0                   1                   2
0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|S| Periph Addr |W|A|  Command code |A| Data Write Low|A|
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
| Data Write Hi |A|S| Periph Addr |R|A| Data Read Low |A|
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
| Data Read Hi  |N|P|
+-+-+-+-+-+-+-+-+-+-+
```

<a id="ga7cf2e52d836b28041f9aeb7ac3c172e4"></a>

### `SMBUS_CMD_QUICK`

```c
#define SMBUS_CMD_QUICK 0b000
```

```c
#include <zephyr/drivers/smbus.h>
```

SMBus 快速协议（Quick protocol）是非常简单的命令，不发送或接收数据。

外设可能仅解释读／写位（R/W Bit），但仍可用其管理外设，例如开关外设。快速协议（Quick Protocol）也可用于扫描外设。

原始示例（Example）：

```c
0                   1
0 1 2 3 4 5 6 7 8 9 0
+-+-+-+-+-+-+-+-+-+-+-+
|S| Periph Addr |D|A|P|
+-+-+-+-+-+-+-+-+-+-+-+
```

<a id="ga70743c58b580018e567d2cb8595bea6f"></a>

### `SMBUS_CMD_WORD_DATA`

```c
#define SMBUS_CMD_WORD_DATA 0b011
```

```c
#include <zephyr/drivers/smbus.h>
```

SMBus 字数据协议（Word Data protocol）先发送第一个字节，即命令，然后读取或写入两个字节。

原始示例（Example）：

```c
Word Data Write

0                   1                   2
0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|S| Periph Addr |W|A|  Command code |A| Data Write Low|A|
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
| Data Write Hi |A|P|
+-+-+-+-+-+-+-+-+-+-+

Word Data Read

0                   1                   2
0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|S| Periph Addr |W|A|  Command code |A|S| Periph Addr |R|
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|A| Data Read Low |A|  Data Read Hi |N|P|
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
```

<a id="gaab024b741eb2c126d41d6db6e76333ee"></a>

### `SMBUS_DEVICE_DT_DEFINE`

```c
#define SMBUS_DEVICE_DT_DEFINE ( node_id, init_fn, pm_device, data_ptr, cfg_ptr, level, prio, api_ptr, ... )
```

```c
#include <zephyr/drivers/smbus.h>
```

展开值（Value）：

```c
Z_SMBUS_DEVICE_STATE_DEFINE(node_id,                            \
                            Z_DEVICE_DT_DEV_NAME(node_id));     \
Z_SMBUS_INIT_FN(Z_DEVICE_DT_DEV_NAME(node_id), init_fn)         \
Z_DEVICE_DEFINE(node_id, Z_DEVICE_DT_DEV_NAME(node_id),         \
                DEVICE_DT_NAME(node_id),                        \
                &UTIL_CAT(Z_DEVICE_DT_DEV_NAME(node_id), _init),\
                NULL, Z_DEVICE_DT_FLAGS(node_id), pm_device,    \
                data_ptr, cfg_ptr, level, prio,                 \
                api_ptr,                                        \
                &(Z_DEVICE_STATE_NAME(Z_DEVICE_DT_DEV_NAME      \
                                      (node_id)).devstate),     \
                __VA_ARGS__)
```

类似于 `DEVICE_DT_DEFINE()`，但包含 SMBus 专用设置。

定义实现 SMBus API 的设备。根据 SMBus 的 `CONFIG_SMBUS_STATS` 配置，必要时可能生成自定义 `device_state` 容器结构体和 `init_fn` 包装函数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `node_id` | 设备树节点标识符。 |
| `init_fn` | 驱动初始化函数（Init Function）的名称。 |
| `pm_device` | 电源管理（PM）设备资源引用；设备不使用 PM 时为 `NULL`。 |
| `data_ptr` | 指向设备私有数据（Private Data）的指针。 |
| `cfg_ptr` | 包含此驱动实例配置信息（Configuration Information）的结构体地址。 |
| `level` | 初始化级别（Initialization Level），详情参见 `SYS_INIT()`。 |
| `prio` | 所选初始化级别内的优先级（Priority），详情参见 `SYS_INIT()`。 |
| `api_ptr` | 提供驱动使用的 API 函数结构体（API Function Struct）的初始指针，可以为 `NULL`。 |

<a id="ga610bc9c96bb22741c850696127f16b92"></a>

### `SMBUS_DEVICE_DT_INST_DEFINE`

```c
#define SMBUS_DEVICE_DT_INST_DEFINE ( inst, ... )
```

```c
#include <zephyr/drivers/smbus.h>
```

展开值（Value）：

```c
SMBUS_DEVICE_DT_DEFINE(DT_DRV_INST(inst), __VA_ARGS__)
```

面向 `DT_DRV_COMPAT` 兼容设备实例的 `SMBUS_DEVICE_DT_DEFINE()` 对应形式。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `inst` | 实例编号。在调用 `SMBUS_DEVICE_DT_DEFINE()` 时，它将被替换为 `DT_DRV_INST(inst)`。 |
| `...` | `SMBUS_DEVICE_DT_DEFINE()` 所需的其他参数。 |

<a id="gaf489d1b6c6aaaa1b3b1e9db823b24241"></a>

### `SMBUS_DT_SPEC_GET`

```c
#define SMBUS_DT_SPEC_GET ( node_id)
```

```c
#include <zephyr/drivers/smbus.h>
```

展开值（Value）：

```c
{                                                       \
        .bus = DEVICE_DT_GET(DT_BUS(node_id)),          \
        .addr = DT_REG_ADDR(node_id)                    \
}
```

根据设备树生成 `smbus_dt_spec` 的结构体初始化器。

此辅助宏读取设备树（Devicetree）中的相关总线与地址数据，展开为 `struct smbus_dt_spec` 的静态初始化器（Static Initializer）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `node_id` | SMBus 设备的设备树节点标识符（Devicetree Node Identifier）；将为该设备的 `struct smbus_dt_spec` 创建初始化器。 |

<a id="ga7e5bf5ecea7cbadf5d2a8b0c1e7a91af"></a>

### `SMBUS_DT_SPEC_INST_GET`

```c
#define SMBUS_DT_SPEC_INST_GET ( inst)
```

```c
#include <zephyr/drivers/smbus.h>
```

展开值（Value）：

```c
SMBUS_DT_SPEC_GET(DT_DRV_INST(inst))
```

根据设备树实例生成 `smbus_dt_spec` 的结构体初始化器。

这等价于 `SMBUS_DT_SPEC_GET(DT_DRV_INST(inst))`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `inst` | 设备树实例编号。 |

<a id="ga440a66ac32cf89d4a37782a0b51bda2c"></a>

### `SMBUS_MODE_CONTROLLER`

```c
#define SMBUS_MODE_CONTROLLER BIT(0)
```

```c
#include <zephyr/drivers/smbus.h>
```

使外设作为控制器（Controller）运行。

<a id="ga0633fc1ff48d806b6ca0e408f29141fe"></a>

### `SMBUS_MODE_HOST_NOTIFY`

```c
#define SMBUS_MODE_HOST_NOTIFY BIT(2)
```

```c
#include <zephyr/drivers/smbus.h>
```

支持主机通知（Host Notify）功能。

<a id="ga6b9ddfb187688f3b1e1a3fdace9ecc76"></a>

### `SMBUS_MODE_PEC`

```c
#define SMBUS_MODE_PEC BIT(1)
```

```c
#include <zephyr/drivers/smbus.h>
```

支持数据包错误码（Packet Error Code，PEC）检查。

<a id="ga7675e48d824e97df4c07c0e2496bee3d"></a>

### `SMBUS_MODE_SMBALERT`

```c
#define SMBUS_MODE_SMBALERT BIT(3)
```

```c
#include <zephyr/drivers/smbus.h>
```

支持 `SMBALERT` 信号功能。

<a id="ga6d6ee9d29de5c0007d34328eb7c9f7c9"></a>

### `smbus_callback_handler_t`

```c
typedef void(* smbus_callback_handler_t) (const struct device *dev, struct smbus_callback *cb, uint8_t addr)
```

```c
#include <zephyr/drivers/smbus.h>
```

定义 SMBus 回调处理函数签名。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向 SMBus 驱动实例的设备结构体的指针。 |
| `cb` | 拥有此处理函数的 `smbus_callback` 结构体。 |
| `addr` | SMBus 外设的地址。 |

<a id="gad0c28687977d0a7866bdea87aef88016"></a>

### `smbus_direction`

```c
enum smbus_direction
```

```c
#include <zephyr/drivers/smbus.h>
```

SMBus 读写方向。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `SMBUS_MSG_WRITE` | 向 SMBus 外设写入一条消息（Message）。 |
| `SMBUS_MSG_READ` | 从 SMBus 外设读取一条消息（Message）。 |

<a id="ga680c3d713a615f4b62503d6f84de4290"></a>

### `smbus_block_pcall()`

```c
int smbus_block_pcall ( const struct device * dev, uint16_t addr, uint8_t cmd, uint8_t snd_count, uint8_t * snd_buf, uint8_t * rcv_count, uint8_t * rcv_buf )
```

```c
#include <zephyr/drivers/smbus.h>
```

执行 SMBus 块过程调用（Block Process Call）。

此例程提供执行 SMBus 块处理调用操作（Block Process Call）的通用接口。该操作基本上是先块写（Block Write），再块读（Block Read）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向 SMBus 驱动实例的设备结构体的指针。 |
| `addr` | SMBus 外设的地址。 |
| `cmd` | 首先发送给外设的命令字节（Command Byte）。 |
| `snd_count` | 要发送的数据块缓冲区大小。 |
| `snd_buf` | 发送给外设的数据块缓冲区（Data Block Buffer）。 |
| `rcv_count` | 外设发送的数据大小。 |
| `rcv_buf` | 从外设接收的数据块缓冲区（Data Block Buffer）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时返回。 |
| `-EIO` | 一般输入／输出错误（I/O error）。 |
| `-ENOSYS` | 驱动尚未实现函数 `smbus_block_pcall()`。 |

<a id="ga67603db9b44636b0b62a24fd623cfb1c"></a>

### `smbus_block_read()`

```c
int smbus_block_read ( const struct device * dev, uint16_t addr, uint8_t cmd, uint8_t * count, uint8_t * buf )
```

```c
#include <zephyr/drivers/smbus.h>
```

执行 SMBus 块读操作（Block Read）。

此例程提供执行 SMBus 块读操作（Block Read）的通用接口。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向 SMBus 驱动实例的设备结构体的指针。 |
| `addr` | SMBus 外设的地址。 |
| `cmd` | 首先发送给外设的命令字节（Command Byte）。 |
| `count` | 外设发送的数据大小，最大为 32 字节。 |
| `buf` | 从外设接收的数据块缓冲区（Data Block Buffer）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时返回。 |
| `-EIO` | 一般输入／输出错误（I/O error）。 |
| `-ENOSYS` | 驱动尚未实现函数 `smbus_block_read()`。 |

<a id="ga55a867cdcb504039f274abae2d1a99e4"></a>

### `smbus_block_write()`

```c
int smbus_block_write ( const struct device * dev, uint16_t addr, uint8_t cmd, uint8_t count, uint8_t * buf )
```

```c
#include <zephyr/drivers/smbus.h>
```

执行 SMBus 块写操作（Block Write）。

此例程提供执行 SMBus 块写操作（Block Write）的通用接口。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向 SMBus 驱动实例的设备结构体的指针。 |
| `addr` | SMBus 外设的地址。 |
| `cmd` | 首先发送给外设的命令字节（Command Byte）。 |
| `count` | 数据块缓冲区大小，最大为 32 字节。 |
| `buf` | 要发送给外设的数据块缓冲区（Data Block Buffer）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时返回。 |
| `-EIO` | 一般输入／输出错误（I/O error）。 |
| `-ENOSYS` | 驱动尚未实现函数 `smbus_block_write()`。 |

<a id="ga1f1148a7cb92e0e0aef7ae3a84615c9b"></a>

### `smbus_byte_data_read()`

```c
int smbus_byte_data_read ( const struct device * dev, uint16_t addr, uint8_t cmd, uint8_t * byte )
```

```c
#include <zephyr/drivers/smbus.h>
```

执行 SMBus 字节数据读操作（Byte Data Read）。

此例程提供执行 SMBus 字节数据读操作（Byte Data Read）的通用接口。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向 SMBus 驱动实例的设备结构体的指针。 |
| `addr` | SMBus 外设的地址。 |
| `cmd` | 首先发送给外设的命令字节（Command Byte）。 |
| `byte` | 从外设接收的字节（Byte）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时返回。 |
| `-EIO` | 一般输入／输出错误（I/O error）。 |
| `-ENOSYS` | 驱动尚未实现函数 `smbus_byte_data_read()`。 |

<a id="gadd7ec1eb3db981efceb8f959546a3b6a"></a>

### `smbus_byte_data_write()`

```c
int smbus_byte_data_write ( const struct device * dev, uint16_t addr, uint8_t cmd, uint8_t byte )
```

```c
#include <zephyr/drivers/smbus.h>
```

执行 SMBus 字节数据写操作（Byte Data Write）。

此例程提供执行 SMBus 字节数据写操作（Byte Data Write）的通用接口。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向 SMBus 驱动实例的设备结构体的指针。 |
| `addr` | SMBus 外设的地址。 |
| `cmd` | 首先发送给外设的命令字节（Command Byte）。 |
| `byte` | 要发送给外设的字节（Byte）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时返回。 |
| `-EIO` | 一般输入／输出错误（I/O error）。 |
| `-ENOSYS` | 驱动尚未实现函数 `smbus_byte_data_write()`。 |

<a id="gadaef9dad3470a7e4d3360e0246271ca1"></a>

### `smbus_byte_read()`

```c
int smbus_byte_read ( const struct device * dev, uint16_t addr, uint8_t * byte )
```

```c
#include <zephyr/drivers/smbus.h>
```

执行 SMBus 字节读操作（Byte Read）。

此例程提供执行 SMBus 字节读操作（Byte Read）的通用接口。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向 SMBus 驱动实例的设备结构体的指针。 |
| `addr` | SMBus 外设的地址。 |
| `byte` | 从外设接收的字节（Byte）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时返回。 |
| `-EIO` | 一般输入／输出错误（I/O error）。 |
| `-ENOSYS` | 驱动尚未实现函数 `smbus_byte_read()`。 |

<a id="ga7dd01c1e00a0f8b0315e442707332251"></a>

### `smbus_byte_write()`

```c
int smbus_byte_write ( const struct device * dev, uint16_t addr, uint8_t byte )
```

```c
#include <zephyr/drivers/smbus.h>
```

执行 SMBus 字节写操作（Byte Write）。

此例程提供执行 SMBus 字节写操作（Byte Write）的通用接口。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向 SMBus 驱动实例的设备结构体的指针。 |
| `addr` | SMBus 外设的地址。 |
| `byte` | 要发送给外设的字节（Byte）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时返回。 |
| `-EIO` | 一般输入／输出错误（I/O error）。 |
| `-ENOSYS` | 驱动尚未实现函数 `smbus_byte_write()`。 |

<a id="ga517305aa7cc9c93ae449b3c548d6c835"></a>

### `smbus_configure()`

```c
int smbus_configure ( const struct device * dev, uint32_t dev_config )
```

```c
#include <zephyr/drivers/smbus.h>
```

配置 SMBus 主机控制器的运行方式。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向 SMBus 驱动实例的设备结构体的指针。 |
| `dev_config` | 以位打包（Bit-Packed）形式表示 SMBus 控制器设备运行时配置的 32 位值。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时返回。 |
| `-EIO` | 一般输入／输出错误（I/O error）。 |

<a id="ga9ca38ca95c0576bdc75b7eb8d0ca29ef"></a>

### `smbus_get_config()`

```c
int smbus_get_config ( const struct device * dev, uint32_t * dev_config )
```

```c
#include <zephyr/drivers/smbus.h>
```

获取 SMBus 主机控制器的配置。

此例程提供获取当前配置的方法。允许在 `smbus_configure` 之前调用，因为某些 SMBus 端口可能已在初始化过程中配置。但是，如果 SMBus 端口尚未配置，`smbus_get_config` 会返回错误。

`smbus_get_config` 可返回缓存配置或探测硬件，但结果必须与当前配置一致。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向 SMBus 驱动实例的设备结构体的指针。 |
| `dev_config` | 用于返回 SMBus 控制器配置的指针；配置是以位打包（Bit-Packed）形式表示的 32 位值。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时返回。 |
| `-EIO` | 一般输入／输出错误（I/O error）。 |
| `-ENOSYS` | 驱动尚未实现函数 `smbus_get_config()`。 |

<a id="ga9190cfe3ce0c41c0a37d5345bad812d4"></a>

### `smbus_host_notify_remove_cb()`

```c
int smbus_host_notify_remove_cb ( const struct device * dev, struct smbus_callback * cb )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/drivers/smbus.h>
```

从 SMBus 主机控制器移除主机通知（Host Notify）回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向 SMBus 驱动实例的设备结构体的指针。 |
| `cb` | 指向回调结构体（Callback Structure）的指针。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时返回。 |
| `-EIO` | 一般输入／输出错误（I/O error）。 |
| `-ENOSYS` | 驱动尚未实现函数 `smbus_host_notify_remove_cb()`。 |

<a id="ga5054a6de634b015f54dacbe81427d0d2"></a>

### `smbus_host_notify_set_cb()`

```c
int smbus_host_notify_set_cb ( const struct device * dev, struct smbus_callback * cb )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/drivers/smbus.h>
```

为 SMBus 主机控制器添加主机通知（Host Notify）回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向 SMBus 驱动实例的设备结构体的指针。 |
| `cb` | 指向回调结构体（Callback Structure）的指针。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时返回。 |
| `-EIO` | 一般输入／输出错误（I/O error）。 |
| `-ENOSYS` | 驱动尚未实现函数 `smbus_host_notify_set_cb()`。 |

<a id="ga2c1369835d3783bb5b5c3cb3711fec92"></a>

### `smbus_pcall()`

```c
int smbus_pcall ( const struct device * dev, uint16_t addr, uint8_t cmd, uint16_t send_word, uint16_t * recv_word )
```

```c
#include <zephyr/drivers/smbus.h>
```

执行 SMBus 过程调用（Process Call）。

此例程提供执行 SMBus 处理调用操作（Process Call）的通用接口，即先写入 2 字节，再读取 2 字节。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向 SMBus 驱动实例的设备结构体的指针。 |
| `addr` | SMBus 外设的地址。 |
| `cmd` | 首先发送给外设的命令字节（Command Byte）。 |
| `send_word` | 要发送给外设的字（Word，16 位）。 |
| `recv_word` | 从外设接收的字（Word，16 位）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时返回。 |
| `-EIO` | 一般输入／输出错误（I/O error）。 |
| `-ENOSYS` | 驱动尚未实现函数 `smbus_pcall()`。 |

<a id="gab008499bca4a4096672d5909fa71b21d"></a>

### `smbus_quick()`

```c
int smbus_quick ( const struct device * dev, uint16_t addr, enum smbus_direction direction )
```

```c
#include <zephyr/drivers/smbus.h>
```

执行 SMBus 快速操作（Quick）。

此例程提供执行 SMBus 快速操作（Quick）的通用接口。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向 SMBus 驱动实例的设备结构体的指针。驱动已配置为控制器模式（Controller Mode）。 |
| `addr` | SMBus 外设的地址。 |
| `direction` | 读取（Read）或写入（Write）方向。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时返回。 |
| `-EIO` | 一般输入／输出错误（I/O error）。 |
| `-ENOSYS` | 驱动尚未实现函数 `smbus_quick()`。 |

<a id="gaa18281b8f9859e46a138a874a8873366"></a>

### `smbus_smbalert_remove_cb()`

```c
int smbus_smbalert_remove_cb ( const struct device * dev, struct smbus_callback * cb )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/drivers/smbus.h>
```

从 SMBus 主机控制器移除 `SMBALERT` 回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向 SMBus 驱动实例的设备结构体的指针。 |
| `cb` | 指向回调结构体（Callback Structure）的指针。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时返回。 |
| `-EIO` | 一般输入／输出错误（I/O error）。 |
| `-ENOSYS` | 驱动尚未实现函数 `smbus_smbalert_remove_cb()`。 |

<a id="gadff533a6bc198815ee56d03a36b949e0"></a>

### `smbus_smbalert_set_cb()`

```c
int smbus_smbalert_set_cb ( const struct device * dev, struct smbus_callback * cb )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/drivers/smbus.h>
```

为 SMBus 主机控制器添加 `SMBALERT` 回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向 SMBus 驱动实例的设备结构体的指针。 |
| `cb` | 指向回调结构体（Callback Structure）的指针。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时返回。 |
| `-EIO` | 一般输入／输出错误（I/O error）。 |
| `-ENOSYS` | 驱动尚未实现函数 `smbus_smbalert_set_cb()`。 |

<a id="ga72a789110c7286a51c5cd5e2215abce1"></a>

### `smbus_word_data_read()`

```c
int smbus_word_data_read ( const struct device * dev, uint16_t addr, uint8_t cmd, uint16_t * word )
```

```c
#include <zephyr/drivers/smbus.h>
```

执行 SMBus 字数据读操作（Word Data Read）。

此例程提供执行 SMBus 字数据读操作（Word Data Read）的通用接口。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向 SMBus 驱动实例的设备结构体的指针。 |
| `addr` | SMBus 外设的地址。 |
| `cmd` | 首先发送给外设的命令字节（Command Byte）。 |
| `word` | 从外设接收的字（Word，16 位）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时返回。 |
| `-EIO` | 一般输入／输出错误（I/O error）。 |
| `-ENOSYS` | 驱动尚未实现函数 `smbus_word_data_read()`。 |

<a id="gade05f9bbbba609832df91fe804dd5d3c"></a>

### `smbus_word_data_write()`

```c
int smbus_word_data_write ( const struct device * dev, uint16_t addr, uint8_t cmd, uint16_t word )
```

```c
#include <zephyr/drivers/smbus.h>
```

执行 SMBus 字数据写操作（Word Data Write）。

此例程提供执行 SMBus 字数据写操作（Word Data Write）的通用接口。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向 SMBus 驱动实例的设备结构体的指针。 |
| `addr` | SMBus 外设的地址。 |
| `cmd` | 首先发送给外设的命令字节（Command Byte）。 |
| `word` | 要发送给外设的字（Word，16 位）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时返回。 |
| `-EIO` | 一般输入／输出错误（I/O error）。 |
| `-ENOSYS` | 驱动尚未实现函数 `smbus_word_data_write()`。 |

<a id="ga0a63b800c14f5831730372b9bad41864"></a>

### `smbus_xfer_stats()`

```c
void smbus_xfer_stats ( const struct device * dev, uint8_t sent, uint8_t recv )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/drivers/smbus.h>
```

更新 SMBus 统计信息（Stats）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向要更新统计信息（Stats）的 SMBus 驱动实例的设备结构体的指针。 |
| `sent` | 已发送的字节数（Bytes sent）。 |
| `recv` | 已接收的字节数（Bytes received）。 |


## 8.12\_原页交叉引用（Cross References）

- [SMBus 驱动后端 API](../api_transport_control_topic_reference/P021_SMBus 驱动后端 API.md)
- [smbus.h](../peripheral_bus_storage_header_reference/P027_zephyr__drivers__smbus.h_头文件参考.md)
- [smbus_callback](../peripheral_bus_storage_model_reference/P091_smbus_callback_结构体.md)
- [smbus_dt_spec](../peripheral_bus_storage_model_reference/P093_smbus_dt_spec_结构体.md)
- [pm_device](../power/P039_通用设备运行时电源结构.md)
- [DEVICE_DT_DEFINE()](../device_reference/P001_设备模型公共接口.md#gac49e26fbe91a14307d5ea08d41561dd1)
- [device](../device_reference/P002_设备对象结构.md)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [recv](../api_file_reference/P307_zephyr__posix__sys__socket.h_文件参考.md#adee01662b0cf762a014efd87ab811276)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [cmd](../api_scoped_clock_topic_reference/P012_FT8xx 参考 API.md#gacde1ca3945cbe6c828f65051c5c3a615)
- [BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)
- [DEVICE_DT_NAME](../device_reference/P001_设备模型公共接口.md#gad864d7a50ee45285dacd68be1e5a49ce)
- [UTIL_CAT](../util_reference/P006_内部宏工具头文件参考.md#a7e7766e792d1638bfbbc9d0f328d3d0d)
- [device_state](../device_reference/P003_设备运行状态结构.md)
- [CONFIG_SMBUS_STATS](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SMBUS_STATS)
- [SYS_INIT()](../device_reference/P005_系统初始化接口.md#gaf507cc0613add8113c41896bd631254f)
- [DT_DRV_INST](../dt_instance_reference/P001_设备树驱动实例宏.md#ga219f413efba2f4c0151468b9a25a8dc1)
- [DEVICE_DT_GET](../device_reference/P001_设备模型公共接口.md#ga9a65996ce21f43acb7db061e23b48ec7)
- [DT_BUS](../dt_node_reference/P001_设备树总线查询宏.md#ga1082d31ac2dafdf9e085d4c23f2169dc)
- [DT_REG_ADDR](../dt_reg_reference/P001_设备树寄存器属性宏.md#gac6d8279c32351ced4c0ac7f32270974e)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="agroup__device__model_html_gad864d7a50ee45285dacd68be1e5a49ce"></a>
<a id="astructpm__device_html"></a>
<a id="autil__internal_8h_html_a7e7766e792d1638bfbbc9d0f328d3d0d"></a>
<a id="agroup__devicetree-inst_html_ga219f413efba2f4c0151468b9a25a8dc1"></a>
<a id="agroup__smbus__interface_html_gaab024b741eb2c126d41d6db6e76333ee"></a>
<a id="agroup__device__model_html_ga9a65996ce21f43acb7db061e23b48ec7"></a>
<a id="agroup__devicetree-generic-bus_html_ga1082d31ac2dafdf9e085d4c23f2169dc"></a>
<a id="agroup__devicetree-reg-prop_html_gac6d8279c32351ced4c0ac7f32270974e"></a>
<a id="agroup__smbus__interface_html_gaf489d1b6c6aaaa1b3b1e9db823b24241"></a>
<a id="doc-typedef-members"></a>
<a id="header-doc-typedef-members"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="ggad0c28687977d0a7866bdea87aef88016a9c9dec19cbada732cef85784b0eedc54"></a>
<a id="ggad0c28687977d0a7866bdea87aef88016aa87094fdacefac89c0b1a03be1c0d22f"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P007_安全数字主机控制器（SDHC）.md) · [返回大纲](大纲.md) · [下一章](P009_视频控制 ID（Video Control IDs）.md)
