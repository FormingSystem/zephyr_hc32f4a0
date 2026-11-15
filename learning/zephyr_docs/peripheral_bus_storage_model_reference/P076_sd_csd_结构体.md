---
id: learning.zephyr-docs.peripheral-bus-storage-model-reference.page-76
title: sd_csd_结构体
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structsd__csd.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第76章\_sd\_csd\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structsd__csd.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

SD卡专用数据寄存器（Card Specific Data Register）。

```c
#include <zephyr/sd/sd_spec.h>
```

<a id="details"></a>

SD 卡专用数据寄存器（Card Specific Data register，CSD），包含 SD 卡的附加数据。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 76.1\_数据成员（Data Fields）

<a id="r_a37b15b70967c9317183b3e5e7837b228"></a>

```c
uint8_t csd_structure
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[csd_structure](#a37b15b70967c9317183b3e5e7837b228)。

CSD 结构（CSD structure）`[127:126]`。

<a id="r_a583c715045b5934ad94ab9cf61b25b06"></a>

```c
uint8_t read_time1
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[read_time1](#a583c715045b5934ad94ab9cf61b25b06)。

数据读取访问时间 1（Data read access-time-1）`[119:112]`。

<a id="r_a96bc4672222dece77d29ffc9287c59ac"></a>

```c
uint8_t read_time2
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[read_time2](#a96bc4672222dece77d29ffc9287c59ac)。

数据读取访问时间 2（Data read access-time-2），以时钟周期计，值为 `NSAC*100`，位域 `[111:104]`。

<a id="r_ae39272173a5253d0d11ef04a2e129db6"></a>

```c
uint8_t xfer_rate
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[xfer_rate](#ae39272173a5253d0d11ef04a2e129db6)。

最大数据传输速率（Maximum data transfer rate）`[103:96]`。

<a id="r_a8bfd2c42066d85058d01076fcaa7a32d"></a>

```c
uint16_t cmd_class
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[cmd_class](#a8bfd2c42066d85058d01076fcaa7a32d)。

卡命令类别（Card command classes）`[95:84]`。

<a id="r_a06f6aef4f4745a78bcf769df5415daa6"></a>

```c
uint8_t read_blk_len
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[read_blk_len](#a06f6aef4f4745a78bcf769df5415daa6)。

最大读取数据块长度（Maximum read data block length）`[83:80]`。

<a id="r_ae10b32787aeedd4789d657eb1ef492eb"></a>

```c
uint16_t flags
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[flags](#ae10b32787aeedd4789d657eb1ef492eb)。

`_sd_csd_flag` 中的标志。

<a id="r_ad35b07abba80e9929c5eed40e37d25b3"></a>

```c
uint32_t device_size
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[device_size](#ad35b07abba80e9929c5eed40e37d25b3)。

设备大小（Device size）`[73:62]`。

<a id="r_aa868cfc1db75eb2913d21bffeaf29fd9"></a>

```c
uint8_t read_current_min
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[read_current_min](#aa868cfc1db75eb2913d21bffeaf29fd9)。

最小 VDD 下的最大读取电流 `[61:59]`。

<a id="r_ad2f31731d7ec0b101d911fe20b5d94db"></a>

```c
uint8_t read_current_max
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[read_current_max](#ad2f31731d7ec0b101d911fe20b5d94db)。

最大 VDD 下的最大读取电流 `[58:56]`。

<a id="r_a0d1efea12c467eacd0d0f98a0bb0ac91"></a>

```c
uint8_t write_current_min
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[write_current_min](#a0d1efea12c467eacd0d0f98a0bb0ac91)。

最小 VDD 下的最大写入电流 `[55:53]`。

<a id="r_a53b364ce0db06b9217259afeb625da44"></a>

```c
uint8_t write_current_max
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[write_current_max](#a53b364ce0db06b9217259afeb625da44)。

最大 VDD 下的最大写入电流 `[52:50]`。

<a id="r_a9d5a952bc6c2a6967e9a88cd93f19e89"></a>

```c
uint8_t dev_size_mul
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[dev_size_mul](#a9d5a952bc6c2a6967e9a88cd93f19e89)。

设备大小乘数（Device size multiplier）`[49:47]`。

<a id="r_ab8d5ae38b19f7ea83b0856ad093c65cb"></a>

```c
uint8_t erase_size
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[erase_size](#ab8d5ae38b19f7ea83b0856ad093c65cb)。

擦除扇区大小（Erase sector size）`[45:39]`。

<a id="r_a029a893cdcd3765864c70476eb6dd64e"></a>

```c
uint8_t write_prtect_size
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[write_prtect_size](#a029a893cdcd3765864c70476eb6dd64e)。

写保护组大小（Write protect group size）`[38:32]`。

<a id="r_a9c362eff38daf7d00776416ed064de24"></a>

```c
uint8_t write_speed_factor
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[write_speed_factor](#a9c362eff38daf7d00776416ed064de24)。

写入速度因子（Write speed factor）`[28:26]`。

<a id="r_adff7d405662589ec44f4d0a6b3548760"></a>

```c
uint8_t write_blk_len
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[write_blk_len](#adff7d405662589ec44f4d0a6b3548760)。

最大写入数据块长度 `[25:22]`。

<a id="r_af93239157610a6eeea420c29432d5412"></a>

```c
uint8_t file_fmt
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[file_fmt](#af93239157610a6eeea420c29432d5412)。

文件格式（File format）`[11:10]`。

## 76.2\_详细说明（Detailed Documentation）

<a id="a8bfd2c42066d85058d01076fcaa7a32d"></a>

### `cmd_class`

```c
uint16_t sd_csd::cmd_class
```

卡命令类别（Card command classes）`[95:84]`。

<a id="a37b15b70967c9317183b3e5e7837b228"></a>

### `csd_structure`

```c
uint8_t sd_csd::csd_structure
```

CSD 结构（CSD structure）`[127:126]`。

<a id="a9d5a952bc6c2a6967e9a88cd93f19e89"></a>

### `dev_size_mul`

```c
uint8_t sd_csd::dev_size_mul
```

设备大小乘数（Device size multiplier）`[49:47]`。

<a id="ad35b07abba80e9929c5eed40e37d25b3"></a>

### `device_size`

```c
uint32_t sd_csd::device_size
```

设备大小（Device size）`[73:62]`。

<a id="ab8d5ae38b19f7ea83b0856ad093c65cb"></a>

### `erase_size`

```c
uint8_t sd_csd::erase_size
```

擦除扇区大小（Erase sector size）`[45:39]`。

<a id="af93239157610a6eeea420c29432d5412"></a>

### `file_fmt`

```c
uint8_t sd_csd::file_fmt
```

文件格式（File format）`[11:10]`。

<a id="ae10b32787aeedd4789d657eb1ef492eb"></a>

### `flags`

```c
uint16_t sd_csd::flags
```

`_sd_csd_flag` 中的标志。

<a id="a06f6aef4f4745a78bcf769df5415daa6"></a>

### `read_blk_len`

```c
uint8_t sd_csd::read_blk_len
```

最大读取数据块长度（Maximum read data block length）`[83:80]`。

<a id="ad2f31731d7ec0b101d911fe20b5d94db"></a>

### `read_current_max`

```c
uint8_t sd_csd::read_current_max
```

最大 VDD 下的最大读取电流 `[58:56]`。

<a id="aa868cfc1db75eb2913d21bffeaf29fd9"></a>

### `read_current_min`

```c
uint8_t sd_csd::read_current_min
```

最小 VDD 下的最大读取电流 `[61:59]`。

<a id="a583c715045b5934ad94ab9cf61b25b06"></a>

### `read_time1`

```c
uint8_t sd_csd::read_time1
```

数据读取访问时间 1（Data read access-time-1）`[119:112]`。

<a id="a96bc4672222dece77d29ffc9287c59ac"></a>

### `read_time2`

```c
uint8_t sd_csd::read_time2
```

数据读取访问时间 2（Data read access-time-2），以时钟周期计，值为 `NSAC*100`，位域 `[111:104]`。

<a id="adff7d405662589ec44f4d0a6b3548760"></a>

### `write_blk_len`

```c
uint8_t sd_csd::write_blk_len
```

最大写入数据块长度 `[25:22]`。

<a id="a53b364ce0db06b9217259afeb625da44"></a>

### `write_current_max`

```c
uint8_t sd_csd::write_current_max
```

最大 VDD 下的最大写入电流 `[52:50]`。

<a id="a0d1efea12c467eacd0d0f98a0bb0ac91"></a>

### `write_current_min`

```c
uint8_t sd_csd::write_current_min
```

最小 VDD 下的最大写入电流 `[55:53]`。

<a id="a029a893cdcd3765864c70476eb6dd64e"></a>

### `write_prtect_size`

```c
uint8_t sd_csd::write_prtect_size
```

写保护组大小（Write protect group size）`[38:32]`。

<a id="a9c362eff38daf7d00776416ed064de24"></a>

### `write_speed_factor`

```c
uint8_t sd_csd::write_speed_factor
```

写入速度因子（Write speed factor）`[28:26]`。

<a id="ae39272173a5253d0d11ef04a2e129db6"></a>

### `xfer_rate`

```c
uint8_t sd_csd::xfer_rate
```

最大数据传输速率（Maximum data transfer rate）`[103:96]`。

本数据类型文档由以下文件生成：

- `zephyr/sd/sd_spec.h`

## 76.3\_原页交叉引用（Cross References）

- [zephyr/sd/sd_spec.h](https://docs.zephyrproject.org/latest/doxygen/html/sd__spec_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P075_sd_cid_结构体.md) · [返回大纲](大纲.md) · [下一章](P077_sd_scr_结构体.md)
