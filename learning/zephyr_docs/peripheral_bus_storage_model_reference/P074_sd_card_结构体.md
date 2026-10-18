---
id: learning.zephyr-docs.peripheral-bus-storage-model-reference.page-74
title: sd_card_结构体
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structsd__card.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第74章\_sd\_card\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structsd__card.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

SD卡（SD Card）结构。

```c
#include <zephyr/sd/sd.h>
```

<a id="details"></a>

SD 卡结构体（SD card structure）。子系统使用此结构体跟踪连接到系统的单个 SD 设备。应用程序可以访问这些字段，但修改其值时应谨慎。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 74.1\_数据成员（Data Fields）

<a id="r_afabeaa207f2f5caaec8cfedac6b35661"></a>

```c
const struct device * sdhc
```

相关声明：[device](../device_reference/P002_设备对象结构.md)、[sdhc](#afabeaa207f2f5caaec8cfedac6b35661)。

此卡对应的 SD 主机控制器（Host controller）。

<a id="r_a875b7081a3e647b782cdb835372f5029"></a>

```c
struct sdhc_io bus_io
```

相关声明：[sdhc_io](P084_sdhc_io_结构体.md)、[bus_io](#a875b7081a3e647b782cdb835372f5029)。

SDHC 当前的总线 I/O 属性。

<a id="r_ae8e85d2fc44a97b42247d87a5c2aafdf"></a>

```c
enum sd_voltage card_voltage
```

相关声明：[sd_voltage](https://docs.zephyrproject.org/latest/doxygen/html/group__sdhc__interface.html#ga34041edf280f125b8500809226b3de5d)、[card_voltage](#ae8e85d2fc44a97b42247d87a5c2aafdf)。

卡的信号电压（Signal voltage）。

<a id="r_aba2501397066d0930691c40778405aa7"></a>

```c
struct k_mutex lock
```

相关声明：[k_mutex](../synchronization_reference/P007_内核互斥量结构.md)、[lock](#aba2501397066d0930691c40778405aa7)。

卡的互斥锁（Mutex）。

<a id="r_a9f597007072d3af5b70ea5cc2a4cbd29"></a>

```c
struct sdhc_host_props host_props
```

相关声明：[sdhc_host_props](P083_sdhc_host_props_结构体.md)、[host_props](#a9f597007072d3af5b70ea5cc2a4cbd29)。

SDHC 主机属性。

<a id="r_a856e7ea75577c62be17dc5d8c99908f4"></a>

```c
uint32_t ocr
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[ocr](#a856e7ea75577c62be17dc5d8c99908f4)。

卡操作条件寄存器（OCR）的原始内容。

<a id="r_a03eac55046f7222c97d60fa919e3cae9"></a>

```c
struct sd_switch_caps switch_caps
```

相关声明：[sd_switch_caps](P078_sd_switch_caps_结构体.md)、[switch_caps](#a03eac55046f7222c97d60fa919e3cae9)。

SD切换能力（Switch Capabilities）。

<a id="r_a17a021db8aa3a8ad224e422f3854eafc"></a>

```c
unsigned int num_io: 3
```

相关声明：[unsigned](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a4089fb16419d359081465355db05f846)、[num_io](#a17a021db8aa3a8ad224e422f3854eafc)。

I/O 功能数量。

<a id="r_a1db9545598f0eb6b6440e63d4941d2ab"></a>

```c
uint16_t relative_addr
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[relative_addr](#a1db9545598f0eb6b6440e63d4941d2ab)。

卡相对地址（Relative Card Address）。

<a id="r_acdcfdaab67d284ef3a8ee3202fd7a538"></a>

```c
uint32_t block_count
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[block_count](#acdcfdaab67d284ef3a8ee3202fd7a538)。

SD 卡中的块数。

<a id="r_a3d29b73f029af5182475c2a2d365173b"></a>

```c
uint16_t block_size
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[block_size](#a3d29b73f029af5182475c2a2d365173b)。

SD 块大小。

<a id="r_a5a9a627df5daf23b468ce705bf5f5f81"></a>

```c
uint8_t sd_version
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[sd_version](#a5a9a627df5daf23b468ce705bf5f5f81)。

SD 规范版本。

<a id="r_a8beccfe60fc714c159528fbd2c122b16"></a>

```c
uint8_t card_speed
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[card_speed](#a8beccfe60fc714c159528fbd2c122b16)。

卡的时序模式（Timing mode）。

<a id="r_a03d7be3154dcd881df60921681a4f308"></a>

```c
enum card_status status
```

相关声明：[card_status](https://docs.zephyrproject.org/latest/doxygen/html/sd_8h.html#a52167aac735d93085a5eebc6f50e1bba)、[status](#a03d7be3154dcd881df60921681a4f308)。

卡状态。

<a id="r_a798acb1bb9495d1009a23f139d269108"></a>

```c
enum card_type type
```

相关声明：[card_type](https://docs.zephyrproject.org/latest/doxygen/html/sd_8h.html#aee707e2ff5691dbdefd9341a18de7b14)、[type](#a798acb1bb9495d1009a23f139d269108)。

卡类型。

<a id="r_ad5d6e798ae8b04d829fb8131f6cb1ccf"></a>

```c
uint16_t flags
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[flags](#ad5d6e798ae8b04d829fb8131f6cb1ccf)。

卡标志。

<a id="r_a38383b8f5c1f9bff1537f407fbec9faf"></a>

```c
uint8_t bus_width
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bus_width](#a38383b8f5c1f9bff1537f407fbec9faf)。

期望的总线宽度。

<a id="r_ab122e442ab3ba5078c99a98a861ec908"></a>

```c
uint32_t cccr_flags
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[cccr_flags](#ab122e442ab3ba5078c99a98a861ec908)。

SDIO 卡公共控制寄存器（CCCR）数据。

<a id="r_a93986ee5db729d9931b4ababe41c303a"></a>

```c
struct sdio_func func0
```

相关声明：[sdio_func](P086_sdio_func_结构体.md)、[func0](#a93986ee5db729d9931b4ababe41c303a)。

功能 0（Function 0）的卡公共数据。

<a id="r_a81c9ec36c79e77599c10163455c86e7c"></a>

```c
uint8_t card_buffer [CONFIG_SD_BUFFER_SIZE]
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[card_buffer](#a81c9ec36c79e77599c10163455c86e7c)。

## 74.2\_详细说明（Detailed Documentation）

<a id="acdcfdaab67d284ef3a8ee3202fd7a538"></a>

### `block_count`

```c
uint32_t sd_card::block_count
```

SD 卡中的块数。

<a id="a3d29b73f029af5182475c2a2d365173b"></a>

### `block_size`

```c
uint16_t sd_card::block_size
```

SD 块大小。

<a id="a875b7081a3e647b782cdb835372f5029"></a>

### `bus_io`

```c
struct sdhc_io sd_card::bus_io
```

SDHC 当前的总线 I/O 属性。

<a id="a38383b8f5c1f9bff1537f407fbec9faf"></a>

### `bus_width`

```c
uint8_t sd_card::bus_width
```

期望的总线宽度。

<a id="a81c9ec36c79e77599c10163455c86e7c"></a>

### `card_buffer`

```c
uint8_t sd_card::card_buffer[CONFIG_SD_BUFFER_SIZE]
```

<a id="a8beccfe60fc714c159528fbd2c122b16"></a>

### `card_speed`

```c
uint8_t sd_card::card_speed
```

卡的时序模式（Timing mode）。

<a id="ae8e85d2fc44a97b42247d87a5c2aafdf"></a>

### `card_voltage`

```c
enum sd_voltage sd_card::card_voltage
```

卡的信号电压（Signal voltage）。

<a id="ab122e442ab3ba5078c99a98a861ec908"></a>

### `cccr_flags`

```c
uint32_t sd_card::cccr_flags
```

SDIO 卡公共控制寄存器（CCCR）数据。

<a id="ad5d6e798ae8b04d829fb8131f6cb1ccf"></a>

### `flags`

```c
uint16_t sd_card::flags
```

卡标志。

<a id="a93986ee5db729d9931b4ababe41c303a"></a>

### `func0`

```c
struct sdio_func sd_card::func0
```

功能 0（Function 0）的卡公共数据。

<a id="a9f597007072d3af5b70ea5cc2a4cbd29"></a>

### `host_props`

```c
struct sdhc_host_props sd_card::host_props
```

SDHC 主机属性。

<a id="aba2501397066d0930691c40778405aa7"></a>

### `lock`

```c
struct k_mutex sd_card::lock
```

卡的互斥锁（Mutex）。

<a id="a17a021db8aa3a8ad224e422f3854eafc"></a>

### `num_io`

```c
unsigned int sd_card::num_io
```

I/O 功能数量。

对于 SD 卡为 `0`。

<a id="a856e7ea75577c62be17dc5d8c99908f4"></a>

### `ocr`

```c
uint32_t sd_card::ocr
```

卡操作条件寄存器（OCR）的原始内容。

<a id="a1db9545598f0eb6b6440e63d4941d2ab"></a>

### `relative_addr`

```c
uint16_t sd_card::relative_addr
```

卡相对地址（Relative Card Address）。

<a id="a5a9a627df5daf23b468ce705bf5f5f81"></a>

### `sd_version`

```c
uint8_t sd_card::sd_version
```

SD 规范版本。

<a id="afabeaa207f2f5caaec8cfedac6b35661"></a>

### `sdhc`

```c
const struct device* sd_card::sdhc
```

此卡对应的 SD 主机控制器（Host controller）。

<a id="a03d7be3154dcd881df60921681a4f308"></a>

### `status`

```c
enum card_status sd_card::status
```

卡状态。

<a id="a03eac55046f7222c97d60fa919e3cae9"></a>

### `switch_caps`

```c
struct sd_switch_caps sd_card::switch_caps
```

SD切换能力（Switch Capabilities）。

<a id="a798acb1bb9495d1009a23f139d269108"></a>

### `type`

```c
enum card_type sd_card::type
```

卡类型。

本数据类型文档由以下文件生成：

- `zephyr/sd/sd.h`

## 74.3\_原页交叉引用（Cross References）

- [zephyr/sd/sd.h](https://docs.zephyrproject.org/latest/doxygen/html/sd_8h_source.html)
- [device](../device_reference/P002_设备对象结构.md)
- [sdhc_io](P084_sdhc_io_结构体.md)
- [sd_voltage](https://docs.zephyrproject.org/latest/doxygen/html/group__sdhc__interface.html#ga34041edf280f125b8500809226b3de5d)
- [k_mutex](../synchronization_reference/P007_内核互斥量结构.md)
- [sdhc_host_props](P083_sdhc_host_props_结构体.md)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [sd_switch_caps](P078_sd_switch_caps_结构体.md)
- [unsigned](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a4089fb16419d359081465355db05f846)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [card_status](https://docs.zephyrproject.org/latest/doxygen/html/sd_8h.html#a52167aac735d93085a5eebc6f50e1bba)
- [card_type](https://docs.zephyrproject.org/latest/doxygen/html/sd_8h.html#aee707e2ff5691dbdefd9341a18de7b14)
- [sdio_func](P086_sdio_func_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P073_psi5_rx_callback_configs_结构体.md) · [返回大纲](大纲.md) · [下一章](P075_sd_cid_结构体.md)
