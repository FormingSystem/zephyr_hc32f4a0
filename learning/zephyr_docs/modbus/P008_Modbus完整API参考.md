---
id: learning.zephyr-docs.modbus.api-8
title: Modbus完整API参考
kind: reference
status: maintained
domains: [zephyr, modbus, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__modbus.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第8章\_Modbus完整API参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__modbus.html)。本次读取日期：2026-10-14；基线为保存的`latest`页面，HTML摘要见[来源记录](../SOURCES.md)。

## 8.1\_概述与头文件

MODBUS传输协议API（MODBUS Transport Protocol API）。

[modbus.h头文件参考](P009_Modbus头文件参考.md)定义本组接口；[源码浏览页](P010_Modbus头文件源码.md)保留官方页面展示的声明。以下接口均来自`<zephyr/modbus/modbus.h>`。

```c
#include <zephyr/modbus/modbus.h>
```

## 8.2\_数据结构（Data Structures）

| 名称／声明 | 说明 |
| --- | --- |
| [modbus_adu](P011_Modbus应用数据单元.md) | 供内部使用，并用于支持原始应用数据单元（Raw Application Data Unit，Raw ADU）的帧结构体（Frame Structure）。 |
| [modbus_user_callbacks](P016_Modbus服务器用户回调.md) | Modbus服务器用户回调（Server User Callback）结构体。 |
| [modbus_serial_param](P014_Modbus串行线路参数.md) | Modbus串行线路参数（Serial Line Parameter）。 |
| [modbus_server_param](P015_Modbus服务器参数.md) | Modbus服务器参数（Server Parameter）。 |
| [modbus_raw_cb](P013_Modbus原始ADU回调参数.md) | 原始应用数据单元回调参数（Raw ADU Callback Parameter）。 |
| [modbus_iface_param](P012_Modbus接口参数.md) | 用户参数结构体，用于将Modbus接口配置为客户端（Client）或服务器（Server）。 |

## 8.3\_宏定义与Modbus异常码（Macros and Exception Codes）

<a id="gaa0acc60971d0f773719431173632fd30"></a>
<a id="r_gaa0acc60971d0f773719431173632fd30"></a>

### `MODBUS_CUSTOM_FC_DEFINE`

```c
#define MODBUS_CUSTOM_FC_DEFINE( name, user_cb, user_fc, userdata )
```

初始化自定义功能码结构体（Custom Function Code Structure）的辅助宏。

展开值（Value）：

```c
static struct modbus_custom_fc modbus_cfg_##name = {            \
        .cb = user_cb,                                          \
        .user_data = userdata,                                  \
        .fc = user_fc,                                          \
        .excep_code = MODBUS_EXC_NONE,                          \
}
```

<a id="ga9cfec884c72b7fc404d82c16f57e858d"></a>
<a id="r_ga9cfec884c72b7fc404d82c16f57e858d"></a>

### `MODBUS_EXC_ACK`

```c
#define MODBUS_EXC_ACK 5
```

确认（Acknowledge）。

<a id="ga9903d7d283c11a4b8854ef5706b5aaba"></a>
<a id="r_ga9903d7d283c11a4b8854ef5706b5aaba"></a>

### `MODBUS_EXC_GW_PATH_UNAVAILABLE`

```c
#define MODBUS_EXC_GW_PATH_UNAVAILABLE 10
```

网关路径不可用（Gateway Path Unavailable）。

<a id="gae61e3ee73e2288006f3dd2f081b4d1de"></a>
<a id="r_gae61e3ee73e2288006f3dd2f081b4d1de"></a>

### `MODBUS_EXC_GW_TARGET_FAILED_TO_RESP`

```c
#define MODBUS_EXC_GW_TARGET_FAILED_TO_RESP 11
```

网关目标设备未响应（Gateway Target Device Failed to Respond）。

<a id="ga9ab4fc4caaf2e051ae697d44a9fa98e3"></a>
<a id="r_ga9ab4fc4caaf2e051ae697d44a9fa98e3"></a>

### `MODBUS_EXC_ILLEGAL_DATA_ADDR`

```c
#define MODBUS_EXC_ILLEGAL_DATA_ADDR 2
```

非法数据地址（Illegal Data Address）。

<a id="ga5bcd9c7edd91d59af1453cde2376412f"></a>
<a id="r_ga5bcd9c7edd91d59af1453cde2376412f"></a>

### `MODBUS_EXC_ILLEGAL_DATA_VAL`

```c
#define MODBUS_EXC_ILLEGAL_DATA_VAL 3
```

非法数据值（Illegal Data Value）。

<a id="ga934994f66a61c0d11d00dd52a748cc78"></a>
<a id="r_ga934994f66a61c0d11d00dd52a748cc78"></a>

### `MODBUS_EXC_ILLEGAL_FC`

```c
#define MODBUS_EXC_ILLEGAL_FC 1
```

非法功能码（Illegal Function Code）。

<a id="gad9b56cf73a31d77cd78d48695ea44659"></a>
<a id="r_gad9b56cf73a31d77cd78d48695ea44659"></a>

### `MODBUS_EXC_MEM_PARITY_ERROR`

```c
#define MODBUS_EXC_MEM_PARITY_ERROR 8
```

存储器奇偶校验错误（Memory Parity Error）。

<a id="ga12557dda3e72ac45aefee3f9cbb18960"></a>
<a id="r_ga12557dda3e72ac45aefee3f9cbb18960"></a>

### `MODBUS_EXC_NONE`

```c
#define MODBUS_EXC_NONE 0
```

无异常（No Exception）。

<a id="ga37f02ccee238e7c8ab33f150b2bcd793"></a>
<a id="r_ga37f02ccee238e7c8ab33f150b2bcd793"></a>

### `MODBUS_EXC_SERVER_DEVICE_BUSY`

```c
#define MODBUS_EXC_SERVER_DEVICE_BUSY 6
```

服务器设备忙（Server Device Busy）。

<a id="ga6bcf75ff2d522f1a542caa41b47a5ac8"></a>
<a id="r_ga6bcf75ff2d522f1a542caa41b47a5ac8"></a>

### `MODBUS_EXC_SERVER_DEVICE_FAILURE`

```c
#define MODBUS_EXC_SERVER_DEVICE_FAILURE 4
```

服务器设备故障（Server Device Failure）。

<a id="gae8a6fcfc117e7c4b2ac32aef90155698"></a>
<a id="r_gae8a6fcfc117e7c4b2ac32aef90155698"></a>

### `MODBUS_MBAP_AND_FC_LENGTH`

```c
#define MODBUS_MBAP_AND_FC_LENGTH (MODBUS_MBAP_LENGTH + 1)
```

MBAP报头加上功能码（Function Code）的长度。

<a id="ga1015513d4d3b6621fc18dcfda79116a2"></a>
<a id="r_ga1015513d4d3b6621fc18dcfda79116a2"></a>

### `MODBUS_MBAP_LENGTH`

```c
#define MODBUS_MBAP_LENGTH 7
```

Modbus应用协议报头（Modbus Application Protocol Header，MBAP Header）的长度。

## 8.4\_类型定义（Typedefs）

<a id="ga2a7ba41a2fb7f6bf5194c02dcab07ae3"></a>
<a id="r_ga2a7ba41a2fb7f6bf5194c02dcab07ae3"></a>

### `modbus_custom_cb_t`

```c
typedef bool(* modbus_custom_cb_t) (const int iface, const struct modbus_adu *const rx_adu, struct modbus_adu *const tx_adu, uint8_t *const excep_code, void *const user_data)
```

自定义功能码处理函数（Custom Function Code Handler）的函数签名。

Modbus允许用户定义功能码，以扩展基础协议。这些回调也可以实现Zephyr Modbus子系统当前尚未支持的功能码。

如果处理请求时发生错误，处理函数应将`excep_code`设置为一个Modbus异常码（Exception Code），以此报告错误。

用户数据指针（User Data Pointer）可用于在处理函数的相继调用之间传递状态。

**参数（Parameters）**

| 名称／声明 | 说明 |
| --- | --- |
| `iface` | Modbus接口索引（Interface Index）。 |
| `rx_adu` | 指向已接收ADU结构体的指针。 |
| `tx_adu` | 指向待发送ADU结构体的指针。 |
| `excep_code` | 指向可能发生的异常码（Exception Code）的指针。 |
| `user_data` | 指向用户数据（User Data）的指针。 |

**返回值（Returns）**：需要发送响应时返回`true`，否则返回`false`。

<a id="ga6d74be1fffb9d5697fe5708827aa7ef1"></a>
<a id="r_ga6d74be1fffb9d5697fe5708827aa7ef1"></a>

### `modbus_raw_cb_t`

```c
typedef int(* modbus_raw_cb_t) (const int iface, const struct modbus_adu *adu, void *user_data)
```

原始ADU回调函数（Raw ADU Callback）的函数签名。

**参数（Parameters）**

| 名称／声明 | 说明 |
| --- | --- |
| `iface` | Modbus RTU接口索引。 |
| `adu` | 指向待发送原始ADU结构体的指针。 |
| `user_data` | 指向用户数据（User Data）的指针。 |

**返回值（Return Values）**

| 名称／声明 | 说明 |
| --- | --- |
| `0` | 传输成功。 |

## 8.5\_枚举类型（Enumeration）

<a id="ga4bd8913e1c77a1e4b19585caa9f77c2e"></a>
<a id="r_ga4bd8913e1c77a1e4b19585caa9f77c2e"></a>

### `modbus_mode`

```c
enum modbus_mode
```

Modbus接口模式（Interface Mode）。

**枚举值（Enumerators）**

| 名称／声明 | 说明 |
| --- | --- |
| `MODBUS_MODE_RTU` | 串行线路上的Modbus远程终端单元（Remote Terminal Unit，RTU）模式。 |
| `MODBUS_MODE_ASCII` | 串行线路上的Modbus ASCII模式（ASCII Mode）。 |
| `MODBUS_MODE_RAW` | Modbus原始ADU模式（Raw ADU Mode）。 |

## 8.6\_函数参考（Functions）

<a id="ga32a6319cc51eb5a98dcb58b3231b9d34"></a>
<a id="r_ga32a6319cc51eb5a98dcb58b3231b9d34"></a>

### `modbus_disable()`

```c
int modbus_disable ( const uint8_t iface)
```

禁用Modbus接口（Interface）。

调用此函数可禁用Modbus接口。

**参数（Parameters）**

| 名称／声明 | 说明 |
| --- | --- |
| `iface` | Modbus接口索引（Interface Index）。 |

**返回值（Return Values）**

| 名称／声明 | 说明 |
| --- | --- |
| `0` | 函数执行成功。 |

<a id="gaa17880a268d6b3b9553de835c800af27"></a>
<a id="r_gaa17880a268d6b3b9553de835c800af27"></a>

### `modbus_iface_get_by_name()`

```c
int modbus_iface_get_by_name ( const char * iface_name)
```

根据接口名称获取Modbus接口索引（Interface Index）。

存在多个接口时，可用此函数在应用中明确区分各个接口。

**参数（Parameters）**

| 名称／声明 | 说明 |
| --- | --- |
| `iface_name` | Modbus接口名称（Interface Name）。 |

**返回值（Returns）**：Modbus接口索引，或负的错误值（Negative Error Value）。

<a id="ga943eff819ecf1bc268714783047888ef"></a>
<a id="r_ga943eff819ecf1bc268714783047888ef"></a>

### `modbus_init_client()`

```c
int modbus_init_client ( const int iface, struct modbus_iface_param param )
```

将Modbus接口配置为原始ADU客户端（Raw ADU Client）。

**参数（Parameters）**

| 名称／声明 | 说明 |
| --- | --- |
| `iface` | Modbus RTU接口索引。 |
| `param` | 客户端接口的配置参数（Configuration Parameter）。 |

**返回值（Return Values）**

| 名称／声明 | 说明 |
| --- | --- |
| `0` | 函数执行成功。 |

<a id="gae4d34276c467bf54e0849a1098e56f8b"></a>
<a id="r_gae4d34276c467bf54e0849a1098e56f8b"></a>

### `modbus_init_server()`

```c
int modbus_init_server ( const int iface, struct modbus_iface_param param )
```

将Modbus接口配置为原始ADU服务器（Raw ADU Server）。

**参数（Parameters）**

| 名称／声明 | 说明 |
| --- | --- |
| `iface` | Modbus RTU接口索引。 |
| `param` | 服务器接口的配置参数（Configuration Parameter）。 |

**返回值（Return Values）**

| 名称／声明 | 说明 |
| --- | --- |
| `0` | 函数执行成功。 |

<a id="ga7aa5dfd6e457980e9e9b8a77810ec31e"></a>
<a id="r_ga7aa5dfd6e457980e9e9b8a77810ec31e"></a>

### `modbus_raw_backend_txn()`

```c
int modbus_raw_backend_txn ( const int iface, struct modbus_adu * adu )
```

使用接口作为后端（Backend）发送和接收ADU。

此函数会覆写指针所指向的ADU。如果后端接口配置错误，或者目标设备不可达，函数会生成异常响应（Exception Response）。

**参数（Parameters）**

| 名称／声明 | 说明 |
| --- | --- |
| `iface` | Modbus客户端接口索引。 |
| `adu` | 指向原始ADU结构体的指针。 |

**返回值（Return Values）**

| 名称／声明 | 说明 |
| --- | --- |
| `0` | 传输成功。 |

<a id="ga333072d3536d7b6f0680ceecc2c5bddf"></a>
<a id="r_ga333072d3536d7b6f0680ceecc2c5bddf"></a>

### `modbus_raw_get_header()`

```c
void modbus_raw_get_header ( struct modbus_adu * adu, const uint8_t * header )
```

从缓冲区（Buffer）读取MBAP报头。

**参数（Parameters）**

| 名称／声明 | 说明 |
| --- | --- |
| `adu` | 指向原始ADU结构体的指针。 |
| `header` | 指向包含MBAP报头的缓冲区的指针。 |

<a id="ga8fdae6a92e27a845296c9d8ce4b8078e"></a>
<a id="r_ga8fdae6a92e27a845296c9d8ce4b8078e"></a>

### `modbus_raw_put_header()`

```c
void modbus_raw_put_header ( const struct modbus_adu * adu, uint8_t * header )
```

将MBAP报头写入缓冲区。

**参数（Parameters）**

| 名称／声明 | 说明 |
| --- | --- |
| `adu` | 指向原始ADU结构体的指针。 |
| `header` | 指向将要存放MBAP报头的缓冲区的指针。 |

<a id="gad250c40ba13a7d8c9189de17d1fd31aa"></a>
<a id="r_gad250c40ba13a7d8c9189de17d1fd31aa"></a>

### `modbus_raw_set_server_failure()`

```c
void modbus_raw_set_server_failure ( struct modbus_adu * adu)
```

设置服务器设备故障异常（Server Device Failure Exception）。

此函数会修改指针所指向的ADU。

**参数（Parameters）**

| 名称／声明 | 说明 |
| --- | --- |
| `adu` | 指向原始ADU结构体的指针。 |

<a id="ga6d40e9eda6b8ead6d071d4192ffe489b"></a>
<a id="r_ga6d40e9eda6b8ead6d071d4192ffe489b"></a>

### `modbus_raw_submit_rx()`

```c
int modbus_raw_submit_rx ( const int iface, const struct modbus_adu * adu )
```

提交原始ADU（Raw ADU）。

**参数（Parameters）**

| 名称／声明 | 说明 |
| --- | --- |
| `iface` | Modbus RTU接口索引。 |
| `adu` | 指向已接收原始ADU结构体的指针。 |

**返回值（Return Values）**

| 名称／声明 | 说明 |
| --- | --- |
| `0` | 传输成功。 |

<a id="ga05b118dc87ebe3739cac4e9572104ffb"></a>
<a id="r_ga05b118dc87ebe3739cac4e9572104ffb"></a>

### `modbus_read_coils()`

```c
int modbus_read_coils ( const int iface, const uint8_t unit_id, const uint16_t start_addr, uint8_t *const coil_tbl, const uint16_t num_coils )
```

读取线圈（Coil Read，FC01）。

发送Modbus消息，从服务器读取线圈状态（Coil Status）。

注意，用来接收线圈值的数组容量必须大于或等于`(num_coils - 1) / 8 + 1`字节。

**参数（Parameters）**

| 名称／声明 | 说明 |
| --- | --- |
| `iface` | Modbus接口索引（Interface Index）。 |
| `unit_id` | 服务器的Modbus单元标识符（Unit ID）。 |
| `start_addr` | 线圈起始地址（Coil Starting Address）。 |
| `coil_tbl` | 指向字节数组的指针，数组保存已读取的线圈值。位布局见下图。 |

```text
                MSB                               LSB
                B7   B6   B5   B4   B3   B2   B1   B0
                -------------------------------------
coil_tbl[0]     #8   #7                            #1
coil_tbl[1]     #16  #15                           #9
     :
     :
```

图中MSB为最高有效位（Most Significant Bit），LSB为最低有效位（Least Significant Bit）。

**参数（Parameters）**

| 名称／声明 | 说明 |
| --- | --- |
| `num_coils` | 要读取的线圈数量。 |

**返回值（Return Values）**

| 名称／声明 | 说明 |
| --- | --- |
| `0` | 函数执行成功。 |

<a id="ga921fd6036ff1b8a416dc02e30bb6e653"></a>
<a id="r_ga921fd6036ff1b8a416dc02e30bb6e653"></a>

### `modbus_read_dinputs()`

```c
int modbus_read_dinputs ( const int iface, const uint8_t unit_id, const uint16_t start_addr, uint8_t *const di_tbl, const uint16_t num_di )
```

读取离散输入（Discrete Inputs，FC02）。

发送Modbus消息，从服务器读取离散输入状态。

注意，用来接收离散输入值的数组容量必须大于或等于`(num_di - 1) / 8 + 1`字节。

**参数（Parameters）**

| 名称／声明 | 说明 |
| --- | --- |
| `iface` | Modbus接口索引（Interface Index）。 |
| `unit_id` | 服务器的Modbus单元标识符（Unit ID）。 |
| `start_addr` | 离散输入起始地址（Discrete Input Starting Address）。 |
| `di_tbl` | 指向接收离散输入状态的数组的指针。位布局见下图。 |

```text
              MSB                               LSB
              B7   B6   B5   B4   B3   B2   B1   B0
              -------------------------------------
di_tbl[0]     #8   #7                            #1
di_tbl[1]     #16  #15                           #9
     :
     :
```

图中MSB为最高有效位（Most Significant Bit），LSB为最低有效位（Least Significant Bit）。

**参数（Parameters）**

| 名称／声明 | 说明 |
| --- | --- |
| `num_di` | 要读取的离散输入数量。 |

**返回值（Return Values）**

| 名称／声明 | 说明 |
| --- | --- |
| `0` | 函数执行成功。 |

<a id="ga7d7221b32fbf2395e69e25ef2dbaa036"></a>
<a id="r_ga7d7221b32fbf2395e69e25ef2dbaa036"></a>

### `modbus_read_holding_regs()`

```c
int modbus_read_holding_regs ( const int iface, const uint8_t unit_id, const uint16_t start_addr, uint16_t *const reg_buf, const uint16_t num_regs )
```

读取保持寄存器（Holding Registers，FC03）。

发送Modbus消息，从服务器读取保持寄存器的值。

**参数（Parameters）**

| 名称／声明 | 说明 |
| --- | --- |
| `iface` | Modbus接口索引（Interface Index）。 |
| `unit_id` | 服务器的Modbus单元标识符（Unit ID）。 |
| `start_addr` | 寄存器起始地址（Register Starting Address）。 |
| `reg_buf` | 指向数组的指针，该数组接收服务器中保持寄存器的当前值。`reg_buf`所指向的数组必须至少容纳`num_regs`个元素。 |
| `num_regs` | 要读取的寄存器数量。 |

**返回值（Return Values）**

| 名称／声明 | 说明 |
| --- | --- |
| `0` | 函数执行成功。 |

<a id="ga9a8ae6fb4b1aee398f5b19f074d07ea9"></a>
<a id="r_ga9a8ae6fb4b1aee398f5b19f074d07ea9"></a>

### `modbus_read_holding_regs_fp()`

```c
int modbus_read_holding_regs_fp ( const int iface, const uint8_t unit_id, const uint16_t start_addr, float *const reg_buf, const uint16_t num_regs )
```

读取浮点保持寄存器（Floating-point Holding Registers，FC03）。

发送Modbus消息，从服务器单元读取浮点保持寄存器的值。

**参数（Parameters）**

| 名称／声明 | 说明 |
| --- | --- |
| `iface` | Modbus接口索引（Interface Index）。 |
| `unit_id` | 服务器的Modbus单元标识符（Unit ID）。 |
| `start_addr` | 寄存器起始地址（Register Starting Address）。 |
| `reg_buf` | 指向数组的指针，该数组接收服务器中保持寄存器的当前值。`reg_buf`所指向的数组必须至少容纳`num_regs`个元素。 |
| `num_regs` | 要读取的寄存器数量。 |

**返回值（Return Values）**

| 名称／声明 | 说明 |
| --- | --- |
| `0` | 函数执行成功。 |

<a id="ga5ff31ca21cf2d1b081d172228d6c2154"></a>
<a id="r_ga5ff31ca21cf2d1b081d172228d6c2154"></a>

### `modbus_read_input_regs()`

```c
int modbus_read_input_regs ( const int iface, const uint8_t unit_id, const uint16_t start_addr, uint16_t *const reg_buf, const uint16_t num_regs )
```

读取输入寄存器（Input Registers，FC04）。

发送Modbus消息，从服务器读取输入寄存器的值。

**参数（Parameters）**

| 名称／声明 | 说明 |
| --- | --- |
| `iface` | Modbus接口索引（Interface Index）。 |
| `unit_id` | 服务器的Modbus单元标识符（Unit ID）。 |
| `start_addr` | 寄存器起始地址（Register Starting Address）。 |
| `reg_buf` | 指向数组的指针，该数组接收服务器中保持寄存器的当前值。`reg_buf`所指向的数组必须至少容纳`num_regs`个元素。 |
| `num_regs` | 要读取的寄存器数量。 |

**返回值（Return Values）**

| 名称／声明 | 说明 |
| --- | --- |
| `0` | 函数执行成功。 |

> 译注：上面的`reg_buf`原文写作“holding registers”。本函数标题、正文和FC04均指输入寄存器（Input Registers）；这里应理解为接收输入寄存器的值，不能据该措辞改用FC03。

<a id="gacd88a4f35a13cc6864654927296803c4"></a>
<a id="r_gacd88a4f35a13cc6864654927296803c4"></a>

### `modbus_register_user_fc()`

```c
int modbus_register_user_fc ( const int iface, struct modbus_custom_fc * custom_fc )
```

注册用户定义的功能码处理函数（User-defined Function Code Handler）。

Modbus规范允许用户实现Zephyr Modbus实现中尚缺少的标准功能码，也允许按规范在65～72和100～110这两个十进制范围内添加非标准功能码（Non-standard Function Codes）。

此函数在运行时（Runtime）为指定功能码注册新的处理函数。

**参数（Parameters）**

| 名称／声明 | 说明 |
| --- | --- |
| `iface` | Modbus客户端接口索引。 |
| `custom_fc` | 用户定义的功能码与回调函数的配对。 |

**返回值（Return Values）**

| 名称／声明 | 说明 |
| --- | --- |
| `0` | 成功。 |

<a id="gac924251f66ca6f357d8b7d90075df210"></a>
<a id="r_gac924251f66ca6f357d8b7d90075df210"></a>

### `modbus_request_diagnostic()`

```c
int modbus_request_diagnostic ( const int iface, const uint8_t unit_id, const uint16_t sfunc, const uint16_t data, uint16_t *const data_out )
```

读取诊断（Diagnostic，FC08）。

发送Modbus消息，执行服务器单元的诊断功能。

**参数（Parameters）**

| 名称／声明 | 说明 |
| --- | --- |
| `iface` | Modbus接口索引（Interface Index）。 |
| `unit_id` | 服务器的Modbus单元标识符（Unit ID）。 |
| `sfunc` | 诊断子功能码（Diagnostic Sub-function Code）。 |
| `data` | 子功能数据（Sub-function Data）。 |
| `data_out` | 指向数据值的指针。 |

**返回值（Return Values）**

| 名称／声明 | 说明 |
| --- | --- |
| `0` | 函数执行成功。 |

<a id="gaccac4f72b5d66a5a2e6c444dda251c41"></a>
<a id="r_gaccac4f72b5d66a5a2e6c444dda251c41"></a>

### `modbus_write_coil()`

```c
int modbus_write_coil ( const int iface, const uint8_t unit_id, const uint16_t coil_addr, const bool coil_state )
```

写入单个线圈（Write Single Coil，FC05）。

发送Modbus消息，向服务器写入一个线圈的值。

**参数（Parameters）**

| 名称／声明 | 说明 |
| --- | --- |
| `iface` | Modbus接口索引（Interface Index）。 |
| `unit_id` | 服务器的Modbus单元标识符（Unit ID）。 |
| `coil_addr` | 线圈起始地址（Coil Starting Address）。 |
| `coil_state` | 线圈期望达到的状态。 |

**返回值（Return Values）**

| 名称／声明 | 说明 |
| --- | --- |
| `0` | 函数执行成功。 |

<a id="gac0fa22cd0d1fa861fdbc04b65ea60d7e"></a>
<a id="r_gac0fa22cd0d1fa861fdbc04b65ea60d7e"></a>

### `modbus_write_coils()`

```c
int modbus_write_coils ( const int iface, const uint8_t unit_id, const uint16_t start_addr, uint8_t *const coil_tbl, const uint16_t num_coils )
```

写入多个线圈（Write Coils，FC15）。

发送Modbus消息，写入服务器单元中的线圈。

注意，用来接收线圈值的数组容量必须大于或等于`(num_coils - 1) / 8 + 1`字节。

**参数（Parameters）**

| 名称／声明 | 说明 |
| --- | --- |
| `iface` | Modbus接口索引（Interface Index）。 |
| `unit_id` | 服务器的Modbus单元标识符（Unit ID）。 |
| `start_addr` | 线圈起始地址（Coil Starting Address）。 |
| `coil_tbl` | 指向字节数组的指针，数组保存要写入的线圈值。位布局见下图。 |

```text
                MSB                               LSB
                B7   B6   B5   B4   B3   B2   B1   B0
                -------------------------------------
coil_tbl[0]     #8   #7                            #1
coil_tbl[1]     #16  #15                           #9
     :
     :
```

图中MSB为最高有效位（Most Significant Bit），LSB为最低有效位（Least Significant Bit）。

**参数（Parameters）**

| 名称／声明 | 说明 |
| --- | --- |
| `num_coils` | 要写入的线圈数量。 |

**返回值（Return Values）**

| 名称／声明 | 说明 |
| --- | --- |
| `0` | 函数执行成功。 |

> 译注：上面的数组容量提示沿用了原文“receiving”的措辞。此函数为FC15写线圈，`coil_tbl`提供待写入的位值；数组格式和容量公式仍按原文保留。

<a id="gaf06d2553af8b8e9ab58f54b8b7e2055b"></a>
<a id="r_gaf06d2553af8b8e9ab58f54b8b7e2055b"></a>

### `modbus_write_holding_reg()`

```c
int modbus_write_holding_reg ( const int iface, const uint8_t unit_id, const uint16_t start_addr, const uint16_t reg_val )
```

写入单个保持寄存器（Write Single Holding Register，FC06）。

发送Modbus消息，向服务器单元写入一个保持寄存器的值。

**参数（Parameters）**

| 名称／声明 | 说明 |
| --- | --- |
| `iface` | Modbus接口索引（Interface Index）。 |
| `unit_id` | 服务器的Modbus单元标识符（Unit ID）。 |
| `start_addr` | 线圈起始地址（Coil Starting Address）。 |
| `reg_val` | 保持寄存器期望写入的值。 |

**返回值（Return Values）**

| 名称／声明 | 说明 |
| --- | --- |
| `0` | 函数执行成功。 |

> 译注：`start_addr`原文写作“Coils starting address”。本函数为FC06，写入对象是单个保持寄存器，因此该参数实际指保持寄存器地址（Holding Register Address）。

<a id="gadc8273292e0efc8c0d65c00eea7a22c5"></a>
<a id="r_gadc8273292e0efc8c0d65c00eea7a22c5"></a>

### `modbus_write_holding_regs()`

```c
int modbus_write_holding_regs ( const int iface, const uint8_t unit_id, const uint16_t start_addr, uint16_t *const reg_buf, const uint16_t num_regs )
```

写入多个保持寄存器（Write Holding Registers，FC16）。

发送Modbus消息，向服务器单元的整型保持寄存器（Integer Holding Registers）写入数据。

**参数（Parameters）**

| 名称／声明 | 说明 |
| --- | --- |
| `iface` | Modbus接口索引（Interface Index）。 |
| `unit_id` | 服务器的Modbus单元标识符（Unit ID）。 |
| `start_addr` | 寄存器起始地址（Register Starting Address）。 |
| `reg_buf` | 指向数组的指针，该数组包含待写入保持寄存器的值。注意，保存这些寄存器值的数组必须至少容纳`num_regs`个元素。 |
| `num_regs` | 要写入的寄存器数量。 |

**返回值（Return Values）**

| 名称／声明 | 说明 |
| --- | --- |
| `0` | 函数执行成功。 |

<a id="ga762da245db3ca4f60fb3aa6c5783c73d"></a>
<a id="r_ga762da245db3ca4f60fb3aa6c5783c73d"></a>

### `modbus_write_holding_regs_fp()`

```c
int modbus_write_holding_regs_fp ( const int iface, const uint8_t unit_id, const uint16_t start_addr, float *const reg_buf, const uint16_t num_regs )
```

写入浮点保持寄存器（Write Floating-point Holding Registers，FC16）。

发送Modbus消息，向服务器单元的浮点保持寄存器写入数据。

**参数（Parameters）**

| 名称／声明 | 说明 |
| --- | --- |
| `iface` | Modbus接口索引（Interface Index）。 |
| `unit_id` | 服务器的Modbus单元标识符（Unit ID）。 |
| `start_addr` | 寄存器起始地址（Register Starting Address）。 |
| `reg_buf` | 指向数组的指针，该数组包含待写入保持寄存器的值。注意，保存这些寄存器值的数组必须至少容纳`num_regs`个元素。 |
| `num_regs` | 要写入的寄存器数量。 |

**返回值（Return Values）**

| 名称／声明 | 说明 |
| --- | --- |
| `0` | 函数执行成功。 |

## 8.7\_相关示例与源码参照

译注：可结合[RTU客户端](P003_RTU客户端.md)、[RTU服务器](P004_RTU服务器.md)、[TCP转串行网关](P005_TCP转串行网关.md)和[TCP服务器](P006_TCP服务器.md)阅读这些接口。初始化函数原文摘要使用“raw ADU”措辞；接口参数本身另定义RTU、ASCII、RAW模式，具体选择见[接口参数](P012_Modbus接口参数.md)，不要将摘要理解成模式枚举中只有RAW。

本仓库的[Modbus头文件](../../../include/zephyr/modbus/modbus.h)可用于源码对照，实际版本可能与官网`latest`不同。以上原文错误在相应函数处明确标注，不通过改写声明或功能码掩盖差异。

<a id="files"></a>
<a id="nested-classes"></a>
<a id="define-members"></a>
<a id="typedef-members"></a>
<a id="enum-members"></a>
<a id="func-members"></a>
<a id="member-group"></a>
<a id="details"></a>
<a id="doc-define-members"></a>
<a id="doc-typedef-members"></a>
<a id="doc-enum-members"></a>
<a id="gga4bd8913e1c77a1e4b19585caa9f77c2ea52033dc2ef37fc286a590b1f97d946ef"></a>
<a id="gga4bd8913e1c77a1e4b19585caa9f77c2eafdf029741cc1bdecb2cb9baf4f06732a"></a>
<a id="gga4bd8913e1c77a1e4b19585caa9f77c2ea4d05b2cfd56ccf15eb1d8c7bb71071ec"></a>
<a id="doc-func-members"></a>
<a id="r_modbus_2Eh"></a>
<a id="r_modbus_5Fadu"></a>
<a id="r_modbus_5Fuser_5Fcallbacks"></a>
<a id="r_modbus_5Fserial_5Fparam"></a>
<a id="r_modbus_5Fserver_5Fparam"></a>
<a id="r_modbus_5Fraw_5Fcb"></a>
<a id="r_modbus_5Fiface_5Fparam"></a>
<a id="header-files"></a>
<a id="header-nested-classes"></a>
<a id="header-define-members"></a>
<a id="header-typedef-members"></a>
<a id="header-enum-members"></a>
<a id="header-func-members"></a>
<a id="header-member-group"></a>
<a id="header-details"></a>
<a id="header-doc-define-members"></a>
<a id="header-doc-typedef-members"></a>
<a id="header-doc-enum-members"></a>
<a id="header-doc-func-members"></a>

[上一章](P007_Modbus串行设备树绑定.md) · [返回大纲](大纲.md) · [下一章](P009_Modbus头文件参考.md)
