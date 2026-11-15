---
id: learning.zephyr-docs.api-buffer-paging-topic-reference.page-17
title: 瑞昱（Realtek）RTS5912
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__rts5912__flash__ex__op.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第17章\_瑞昱（Realtek）RTS5912

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__rts5912__flash__ex__op.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

Realtek RTS5912 闪存控制器的扩展操作。

<a id="details"></a>

Realtek RTS5912 闪存控制器的扩展操作。

<a id="header-files"></a>
<a id="files"></a>

## 17.1\_文件（Files）

<a id="r_rts5912_5Fflash_5Fapi_5Fex_2Eh"></a>

```c
file rts5912_flash_api_ex.h
```

相关声明：[rts5912_flash_api_ex.h](../api_file_supplement_reference/P103_zephyr__drivers__flash__rts5912_flash_api_ex.h_文件参考.md)。

Realtek RTS5912闪存扩展操作（Flash Extended Operations）的头文件。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 17.2\_枚举（Enumerations）

<a id="r_ga76926a3c77ab9b717612e578b19ed839"></a>

```c
enum flash_rts5912_ex_ops { FLASH_RTS5912_EX_OP_WR_ENABLE = FLASH_EX_OP_VENDOR_BASE , FLASH_RTS5912_EX_OP_WR_DISABLE , FLASH_RTS5912_EX_OP_WR_SR , FLASH_RTS5912_EX_OP_WR_SR2 , FLASH_RTS5912_EX_OP_RD_SR , FLASH_RTS5912_EX_OP_RD_SR2 , FLASH_RTS5912_EX_OP_SET_WP , FLASH_RTS5912_EX_OP_GET_WP }
```

相关声明：[flash_rts5912_ex_ops](#ga76926a3c77ab9b717612e578b19ed839)、[FLASH_RTS5912_EX_OP_WR_ENABLE](#gga76926a3c77ab9b717612e578b19ed839acf8b81b0f577bf7916bbd9c71a01eab8)、[FLASH_RTS5912_EX_OP_WR_DISABLE](#gga76926a3c77ab9b717612e578b19ed839abd2ecf801e42710d563e3edf08724f9c)、[FLASH_RTS5912_EX_OP_WR_SR](#gga76926a3c77ab9b717612e578b19ed839aba07d1e19388fb24dcc3b0b03ffd1695)、[FLASH_RTS5912_EX_OP_WR_SR2](#gga76926a3c77ab9b717612e578b19ed839adf5f76fee83c48c041075aa6e3826584)、[FLASH_RTS5912_EX_OP_RD_SR](#gga76926a3c77ab9b717612e578b19ed839a62b267b7e87b85c185cbe7dd846c7a2e)、[FLASH_RTS5912_EX_OP_RD_SR2](#gga76926a3c77ab9b717612e578b19ed839ad3a6db835d8651b5a428caf610d3cb0f)、[FLASH_RTS5912_EX_OP_SET_WP](#gga76926a3c77ab9b717612e578b19ed839a8380795da4ba7f938d8ba1eaaf8a2614)、[FLASH_RTS5912_EX_OP_GET_WP](#gga76926a3c77ab9b717612e578b19ed839a982b4c3e330184dc7a70d93d78f3673e)。

Realtek RTS5912 闪存扩展操作（Flash Extended Operations）的枚举（Enumeration）。

## 17.3\_详细说明（Detailed Documentation）

<a id="ga76926a3c77ab9b717612e578b19ed839"></a>

### `flash_rts5912_ex_ops`

```c
enum flash_rts5912_ex_ops
```

```c
#include <zephyr/drivers/flash/rts5912_flash_api_ex.h>
```

Realtek RTS5912 闪存扩展操作（Flash Extended Operations）的枚举（Enumeration）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `FLASH_RTS5912_EX_OP_WR_ENABLE` | 向闪存芯片发送写使能（Write Enable，WREN）命令。此操作设置闪存状态寄存器中的写使能锁存位（Write Enable Latch，WEL），允许写入与擦除操作。 参数（Parameters）：in 未使用；out 未使用。 |
| `in` | 不使用（Not Used）。 |
| `out` | 不使用（Not Used）。 |
| `FLASH_RTS5912_EX_OP_WR_DISABLE` | 向闪存芯片发送写禁止（Write Disable，WRDI）命令。此操作清除写使能锁存位（Write Enable Latch，WEL），保护存储器免遭写入或擦除。 参数（Parameters）：in 未使用；out 未使用。 |
| `in` | 不使用（Not Used）。 |
| `out` | 不使用（Not Used）。 |
| `FLASH_RTS5912_EX_OP_WR_SR` | 写入闪存状态寄存器 1（Status Register 1，SR1）。此操作向主状态寄存器写入一个字节。 参数（Parameters）：in 未使用；out：指向 uint8_t 的指针，其中包含要写入 SR1 的值。 |
| `in` | 不使用（Not Used）。 |
| `out` | 指向 uint8_t 的指针，其中包含要写入 SR1 的值。 |
| `FLASH_RTS5912_EX_OP_WR_SR2` | 写入闪存状态寄存器 2（Status Register 2，SR2）。此操作向第二个状态寄存器写入一个字节。 参数（Parameters）：in 未使用；out：指向 uint8_t 的指针，其中包含要写入 SR2 的值。 |
| `in` | 不使用（Not Used）。 |
| `out` | 指向 uint8_t 的指针，其中包含要写入 SR2 的值。 |
| `FLASH_RTS5912_EX_OP_RD_SR` | 读取闪存状态寄存器 1（Status Register 1，SR1）。此操作从主状态寄存器读取一个字节。 参数（Parameters）：in 未使用；out：指向 uint8_t 缓冲区的指针，用于存放读取到的 SR1 值。 |
| `in` | 不使用（Not Used）。 |
| `out` | 指向 uint8_t 缓冲区的指针，用于存放读取到的 SR1 值。 |
| `FLASH_RTS5912_EX_OP_RD_SR2` | 读取闪存状态寄存器 2（Status Register 2，SR2）。此操作从第二个状态寄存器读取一个字节。 参数（Parameters）：in 未使用；out：指向 uint8_t 缓冲区的指针，用于存放读取到的 SR2 值。 |
| `in` | 不使用（Not Used）。 |
| `out` | 指向 uint8_t 缓冲区的指针，用于存放读取到的 SR2 值。 |
| `FLASH_RTS5912_EX_OP_SET_WP` | 设置硬件写保护引脚（Write Protect，WP#）的状态。此操作控制控制器的硬件 WP# 引脚输出。 参数（Parameters）：in 未使用；out：指向 uint8_t 的指针。值非零时使 WP# 引脚有效（Asserted，低电平有效）；值为零时使其无效（De-asserted）。 |
| `in` | 不使用（Not Used）。 |
| `out` | 指向 uint8_t 的指针。值非零时使 WP# 引脚有效（Asserted，低电平有效）；值为零时使其无效（De-asserted）。 |
| `FLASH_RTS5912_EX_OP_GET_WP` | 获取硬件写保护引脚（Write Protect，WP#）的状态。此操作读取控制器硬件 WP# 引脚设置的当前状态。 参数（Parameters）：in 未使用；out：指向 uint8_t 缓冲区的指针，用于存放当前 WP# 引脚状态。非零值表示引脚被配置为有效（Asserted）。 |
| `in` | 不使用（Not Used）。 |
| `out` | 指向 uint8_t 缓冲区的指针，用于存放当前 WP# 引脚状态。非零值表示引脚被配置为有效（Asserted）。 |

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `in` | 不使用（Not Used）。 |
| `out` | 不使用（Not Used）。 |

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `in` | 不使用（Not Used）。 |
| `out` | 不使用（Not Used）。 |

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `in` | 不使用（Not Used）。 |
| `out` | 指向 uint8_t 的指针，其中包含要写入 SR1 的值。 |

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `in` | 不使用（Not Used）。 |
| `out` | 指向 uint8_t 的指针，其中包含要写入 SR2 的值。 |

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `in` | 不使用（Not Used）。 |
| `out` | 指向 uint8_t 缓冲区的指针，用于存放读取到的 SR1 值。 |

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `in` | 不使用（Not Used）。 |
| `out` | 指向 uint8_t 缓冲区的指针，用于存放读取到的 SR2 值。 |

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `in` | 不使用（Not Used）。 |
| `out` | 指向 uint8_t 的指针。值非零时使 WP# 引脚有效（Asserted，低电平有效）；值为零时使其无效（De-asserted）。 |

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `in` | 不使用（Not Used）。 |
| `out` | 指向 uint8_t 缓冲区的指针，用于存放当前 WP# 引脚状态。非零值表示引脚被配置为有效（Asserted）。 |


## 17.4\_原页交叉引用（Cross References）

- [rts5912_flash_api_ex.h](../api_file_supplement_reference/P103_zephyr__drivers__flash__rts5912_flash_api_ex.h_文件参考.md)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="header-details"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="gga76926a3c77ab9b717612e578b19ed839acf8b81b0f577bf7916bbd9c71a01eab8"></a>
<a id="gga76926a3c77ab9b717612e578b19ed839abd2ecf801e42710d563e3edf08724f9c"></a>
<a id="gga76926a3c77ab9b717612e578b19ed839aba07d1e19388fb24dcc3b0b03ffd1695"></a>
<a id="gga76926a3c77ab9b717612e578b19ed839adf5f76fee83c48c041075aa6e3826584"></a>
<a id="gga76926a3c77ab9b717612e578b19ed839a62b267b7e87b85c185cbe7dd846c7a2e"></a>
<a id="gga76926a3c77ab9b717612e578b19ed839ad3a6db835d8651b5a428caf610d3cb0f"></a>
<a id="gga76926a3c77ab9b717612e578b19ed839a8380795da4ba7f938d8ba1eaaf8a2614"></a>
<a id="gga76926a3c77ab9b717612e578b19ed839a982b4c3e330184dc7a70d93d78f3673e"></a>

---

[上一章](P016_多路复用器（MUX）.md) · [返回大纲](大纲.md) · [下一章](P018_实用工具（Utilities）.md)
