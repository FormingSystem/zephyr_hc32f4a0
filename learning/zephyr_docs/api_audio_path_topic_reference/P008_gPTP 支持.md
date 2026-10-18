---
id: learning.zephyr-docs.api-audio-path-topic-reference.page-8
title: gPTP 支持
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__gptp.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第8章\_gPTP 支持

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__gptp.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

通用精确时间协议（Generic Precision Time Protocol，gPTP）支持。

<a id="details"></a>

通用精确时间协议（generic Precision Time Protocol，gPTP）支持。自 1.13 起提供，版本 0.1.0。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 8.1\_数据结构（Data Structures）

<a id="r_gptp_5Fscaled_5Fns"></a>

```c
struct gptp_scaled_ns
```

相关声明：[gptp_scaled_ns](../network_service_model_reference/P020_gptp_scaled_ns_结构体.md)。

缩放纳秒（Scaled Nanoseconds）。

<a id="r_gptp_5Fuscaled_5Fns"></a>

```c
struct gptp_uscaled_ns
```

相关声明：[gptp_uscaled_ns](../network_service_model_reference/P021_gptp_uscaled_ns_结构体.md)。

无符号缩放纳秒（UScaled Nanoseconds）。

<a id="r_gptp_5Fport_5Fidentity"></a>

```c
struct gptp_port_identity
```

相关声明：[gptp_port_identity](../network_service_model_reference/P019_gptp_port_identity_结构体.md)。

端口标识（Port Identity）。

<a id="r_gptp_5Fflags"></a>

```c
struct gptp_flags
```

相关声明：[gptp_flags](../network_service_model_reference/P016_gptp_flags_结构体.md)。

通用精确时间协议（gPTP）的消息标志。

<a id="r_gptp_5Fhdr"></a>

```c
struct gptp_hdr
```

相关声明：[gptp_hdr](../network_service_model_reference/P017_gptp_hdr_结构体.md)。

通用精确时间协议（gPTP）的消息头部。

<a id="r_gptp_5Fphase_5Fdis_5Fcb"></a>

```c
struct gptp_phase_dis_cb
```

相关声明：[gptp_phase_dis_cb](../network_service_model_reference/P018_gptp_phase_dis_cb_结构体.md)。

相位不连续（Phase Discontinuity）的回调结构。

<a id="r_gptp_5Fclk_5Fsrc_5Ftime_5Finvoke_5Fparams"></a>

```c
struct gptp_clk_src_time_invoke_params
```

相关声明：[gptp_clk_src_time_invoke_params](../network_service_model_reference/P015_gptp_clk_src_time_invoke_params_结构体.md)。

ClockSourceTime.invoke函数的参数。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 8.2\_类型定义（Typedefs）

<a id="r_gade00e0d8398f015031d7f77317e4b97b"></a>

```c
typedef void(* gptp_phase_dis_callback_t) (uint8_t *gm_identity, uint16_t *time_base, struct gptp_scaled_ns *last_gm_ph_change, double *last_gm_freq_change)
```

相关声明：[gptp_phase_dis_callback_t](#gade00e0d8398f015031d7f77317e4b97b)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[gptp_scaled_ns](../network_service_model_reference/P020_gptp_scaled_ns_结构体.md)。

定义在主时钟（Grandmaster）发出相位不连续（Phase Discontinuity）通知后调用的回调。

<a id="r_ga9bd009e6027d57cd9950b0387d727e3d"></a>

```c
typedef void(* gptp_port_cb_t) (int port, struct net_if *iface, void *user_data)
```

相关声明：[gptp_port_cb_t](#ga9bd009e6027d57cd9950b0387d727e3d)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

遍历广义精确时间协议（gPTP）端口时使用的回调。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 8.3\_函数（Functions）

<a id="r_gaad2282df9cbf7f05f557285323af8f07"></a>

```c
void gptp_register_phase_dis_cb (struct gptp_phase_dis_cb *phase_dis, gptp_phase_dis_callback_t cb)
```

相关声明：[gptp_register_phase_dis_cb](#gaad2282df9cbf7f05f557285323af8f07)、[gptp_phase_dis_cb](../network_service_model_reference/P018_gptp_phase_dis_cb_结构体.md)、[gptp_phase_dis_callback_t](#gade00e0d8398f015031d7f77317e4b97b)。

注册相位不连续（Phase Discontinuity）回调。

<a id="r_ga55d95859e5ec586cb2341929901220dd"></a>

```c
void gptp_unregister_phase_dis_cb (struct gptp_phase_dis_cb *phase_dis)
```

相关声明：[gptp_unregister_phase_dis_cb](#ga55d95859e5ec586cb2341929901220dd)、[gptp_phase_dis_cb](../network_service_model_reference/P018_gptp_phase_dis_cb_结构体.md)。

注销相位不连续（Phase Discontinuity）回调。

<a id="r_ga29bf157d06a5ec5bb5a2a8a0e986709d"></a>

```c
void gptp_call_phase_dis_cb (void)
```

相关声明：[gptp_call_phase_dis_cb](#ga29bf157d06a5ec5bb5a2a8a0e986709d)。

调用相位不连续（Phase Discontinuity）回调函数。

<a id="r_ga9a8e2ccf20d0430b4e62f3302462c6eb"></a>

```c
int gptp_event_capture (struct net_ptp_time *slave_time, bool *gm_present)
```

相关声明：[gptp_event_capture](#ga9a8e2ccf20d0430b4e62f3302462c6eb)、[net_ptp_time](../network_core_model_reference/P116_net_ptp_time_结构体.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

获取 gPTP 时间（Time）。

<a id="r_ga40121c2957d58b0b5bb4468eac5de259"></a>

```c
char * gptp_sprint_clock_id (const uint8_t *clk_id, char *output, size_t output_len)
```

相关声明：[gptp_sprint_clock_id](#ga40121c2957d58b0b5bb4468eac5de259)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

将时钟 ID（Clock ID）打印到用户提供缓冲区的工具函数。

<a id="r_ga06ddd41c7adf9e387d1b23bcdfccbddc"></a>

```c
void gptp_foreach_port (gptp_port_cb_t cb, void *user_data)
```

相关声明：[gptp_foreach_port](#ga06ddd41c7adf9e387d1b23bcdfccbddc)、[gptp_port_cb_t](#ga9bd009e6027d57cd9950b0387d727e3d)。

遍历全部 gPTP 端口（Ports），为每个端口调用回调。

<a id="r_gaf4366741c39144e244d7555582b3b62c"></a>

```c
int gptp_get_port_number (struct net_if *iface)
```

相关声明：[gptp_get_port_number](#gaf4366741c39144e244d7555582b3b62c)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

获取网络接口（Network Interface）的 gPTP 端口号。

<a id="r_ga4af3bf8e0ef4e3833260b6365b2b1e2f"></a>

```c
int gptp_set_port_number (struct net_if *iface, uint16_t port)
```

相关声明：[gptp_set_port_number](#ga4af3bf8e0ef4e3833260b6365b2b1e2f)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

为网络接口（Network Interface）设置 gPTP 端口号。

<a id="r_gae4c3aac6b88e9ce21a32ba3263b9ad59"></a>

```c
struct gptp_domain * gptp_get_domain (void)
```

相关声明：[gptp_get_domain](#gae4c3aac6b88e9ce21a32ba3263b9ad59)。

获取 gPTP 域（Domain）。

<a id="r_ga9b27c9a741fb0ca72eff78e334e629fe"></a>

```c
void gptp_clk_src_time_invoke (struct gptp_clk_src_time_invoke_params *arg)
```

相关声明：[gptp_clk_src_time_invoke](#ga9b27c9a741fb0ca72eff78e334e629fe)、[gptp_clk_src_time_invoke_params](../network_service_model_reference/P015_gptp_clk_src_time_invoke_params_结构体.md)。

时钟源（ClockSource）实体使用此接口，为时间感知系统（Time-aware System）的时钟主端（ClockMaster）实体提供时间。

<a id="r_ga5b46fb7bbe1a380e3c327c8f5abbabeb"></a>

```c
struct gptp_hdr * gptp_get_hdr (struct net_pkt *pkt)
```

相关声明：[gptp_hdr](../network_service_model_reference/P017_gptp_hdr_结构体.md)、[gptp_get_hdr](#ga5b46fb7bbe1a380e3c327c8f5abbabeb)、[net_pkt](../network_core_model_reference/P114_net_pkt_结构体.md)。

返回指向网络数据包中 gPTP 包头（Packet Header）的指针。

## 8.4\_详细说明（Detailed Documentation）

<a id="gade00e0d8398f015031d7f77317e4b97b"></a>

### `gptp_phase_dis_callback_t`

```c
typedef void(* gptp_phase_dis_callback_t) (uint8_t *gm_identity, uint16_t *time_base, struct gptp_scaled_ns *last_gm_ph_change, double *last_gm_freq_change)
```

```c
#include <zephyr/net/gptp.h>
```

定义在主时钟（Grandmaster）发出相位不连续（Phase Discontinuity）通知后调用的回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `gm_identity` | 指向 `ClockIdentity` 时钟标识数组首元素的指针。数组大小为 `GPTP_CLOCK_ID_LEN`。 |
| `time_base` | 指向当前最高主时钟（Grandmaster）的 `timeBaseIndicator` 值的指针。 |
| `last_gm_ph_change` | 指向从最高主时钟（Grandmaster）接收的 `lastGmPhaseChange` 值的指针。 |
| `last_gm_freq_change` | 指向从最高主时钟（Grandmaster）接收的 `lastGmFreqChange` 值的指针。 |

<a id="ga9bd009e6027d57cd9950b0387d727e3d"></a>

### `gptp_port_cb_t`

```c
typedef void(* gptp_port_cb_t) (int port, struct net_if *iface, void *user_data)
```

```c
#include <zephyr/net/gptp.h>
```

遍历广义精确时间协议（gPTP）端口时使用的回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `port` | 端口号（Port number）。 |
| `iface` | 指向网络接口（network interface）的指针。 |
| `user_data` | 指向用户数据的有效指针，或为 `NULL`。 |

<a id="ga29bf157d06a5ec5bb5a2a8a0e986709d"></a>

### `gptp_call_phase_dis_cb()`

```c
void gptp_call_phase_dis_cb ( void )
```

```c
#include <zephyr/net/gptp.h>
```

调用相位不连续（Phase Discontinuity）回调函数。

<a id="ga9b27c9a741fb0ca72eff78e334e629fe"></a>

### `gptp_clk_src_time_invoke()`

```c
void gptp_clk_src_time_invoke ( struct gptp_clk_src_time_invoke_params * arg)
```

```c
#include <zephyr/net/gptp.h>
```

时钟源（ClockSource）实体使用此接口，为时间感知系统（Time-aware System）的时钟主端（ClockMaster）实体提供时间。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `arg` | 时钟源实体（ClockSource Entity）的当前状态和参数。 |

<a id="ga9a8e2ccf20d0430b4e62f3302462c6eb"></a>

### `gptp_event_capture()`

```c
int gptp_event_capture ( struct net_ptp_time * slave_time, bool * gm_present )
```

```c
#include <zephyr/net/gptp.h>
```

获取 gPTP 时间（Time）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `slave_time` | 指向用于保存时间戳（Timestamp）的结构体的指针。 |
| `gm_present` | 指向布尔值的指针，用于保存是否存在最高主时钟（Grand Master）的状态。 |

**返回（Returns）**：返回值：错误码（Error Code），无错误时为 0。

<a id="ga06ddd41c7adf9e387d1b23bcdfccbddc"></a>

### `gptp_foreach_port()`

```c
void gptp_foreach_port ( gptp_port_cb_t cb, void * user_data )
```

```c
#include <zephyr/net/gptp.h>
```

遍历全部 gPTP 端口（Ports），为每个端口调用回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `cb` | 要调用的用户提供回调函数。 |
| `user_data` | 用户指定的数据。 |

<a id="gae4c3aac6b88e9ce21a32ba3263b9ad59"></a>

### `gptp_get_domain()`

```c
struct gptp_domain * gptp_get_domain ( void )
```

```c
#include <zephyr/net/gptp.h>
```

获取 gPTP 域（Domain）。

包含 gPTP 域（Domain）的全部配置和状态。

**返回（Returns）**：返回值：指向域（Domain）的指针；未找到则返回 `NULL`。

<a id="ga5b46fb7bbe1a380e3c327c8f5abbabeb"></a>

### `gptp_get_hdr()`

```c
struct gptp_hdr * gptp_get_hdr ( struct net_pkt * pkt)
```

```c
#include <zephyr/net/gptp.h>
```

返回指向网络数据包中 gPTP 包头（Packet Header）的指针。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `pkt` | 网络数据包（Network Packet），已接收或已发送。 |

**返回（Returns）**：返回值：指向 gPTP 头部（Header）的指针。

<a id="gaf4366741c39144e244d7555582b3b62c"></a>

### `gptp_get_port_number()`

```c
int gptp_get_port_number ( struct net_if * iface)
```

```c
#include <zephyr/net/gptp.h>
```

获取网络接口（Network Interface）的 gPTP 端口号。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `iface` | 充当 gPTP 端口的网络接口（Network Interface）。 |

**返回（Returns）**：返回值：找到时返回 gPTP 端口号，否则返回 `ENODEV`。

<a id="gaad2282df9cbf7f05f557285323af8f07"></a>

### `gptp_register_phase_dis_cb()`

```c
void gptp_register_phase_dis_cb ( struct gptp_phase_dis_cb * phase_dis, gptp_phase_dis_callback_t cb )
```

```c
#include <zephyr/net/gptp.h>
```

注册相位不连续（Phase Discontinuity）回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `phase_dis` | 调用方指定的回调处理函数（Callback Handler）。 |
| `cb` | 要注册的回调（Callback）。 |

<a id="ga4af3bf8e0ef4e3833260b6365b2b1e2f"></a>

### `gptp_set_port_number()`

```c
int gptp_set_port_number ( struct net_if * iface, uint16_t port )
```

```c
#include <zephyr/net/gptp.h>
```

为网络接口（Network Interface）设置 gPTP 端口号。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `iface` | 充当 gPTP 端口的网络接口（Network Interface）。 |
| `port` | gPTP 端口号（Port Number）。 |

**返回（Returns）**：返回值：设置成功返回 0，否则返回小于 0 的值。

<a id="ga40121c2957d58b0b5bb4468eac5de259"></a>

### `gptp_sprint_clock_id()`

```c
char * gptp_sprint_clock_id ( const uint8_t * clk_id, char * output, size_t output_len )
```

```c
#include <zephyr/net/gptp.h>
```

将时钟 ID（Clock ID）打印到用户提供缓冲区的工具函数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `clk_id` | 时钟 ID（Clock ID）。 |
| `output` | 输出缓冲区（Output Buffer）。 |
| `output_len` | 输出缓冲区长度（Output Buffer Length）。 |

**返回（Returns）**：返回值：指向输出缓冲区（Output Buffer）的指针。

<a id="ga55d95859e5ec586cb2341929901220dd"></a>

### `gptp_unregister_phase_dis_cb()`

```c
void gptp_unregister_phase_dis_cb ( struct gptp_phase_dis_cb * phase_dis)
```

```c
#include <zephyr/net/gptp.h>
```

注销相位不连续（Phase Discontinuity）回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `phase_dis` | 调用方指定的回调处理函数（Callback Handler）。 |


## 8.5\_原页交叉引用（Cross References）

- [gptp_scaled_ns](../network_service_model_reference/P020_gptp_scaled_ns_结构体.md)
- [gptp_uscaled_ns](../network_service_model_reference/P021_gptp_uscaled_ns_结构体.md)
- [gptp_port_identity](../network_service_model_reference/P019_gptp_port_identity_结构体.md)
- [gptp_flags](../network_service_model_reference/P016_gptp_flags_结构体.md)
- [gptp_hdr](../network_service_model_reference/P017_gptp_hdr_结构体.md)
- [gptp_phase_dis_cb](../network_service_model_reference/P018_gptp_phase_dis_cb_结构体.md)
- [gptp_clk_src_time_invoke_params](../network_service_model_reference/P015_gptp_clk_src_time_invoke_params_结构体.md)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [net_if](../network_core_model_reference/P079_net_if_结构体.md)
- [net_ptp_time](../network_core_model_reference/P116_net_ptp_time_结构体.md)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [net_pkt](../network_core_model_reference/P114_net_pkt_结构体.md)
- [zephyr/net/gptp.h](../api_file_protocol_service_reference/P017_zephyr__net__gptp.h_文件参考.md)

<a id="header-details"></a>
<a id="doc-typedef-members"></a>
<a id="header-doc-typedef-members"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P007_电话与媒体音频配置文件（Telephone and Media Audio Profile，TMAP）.md) · [返回大纲](大纲.md) · [下一章](P009_INA230 API主题.md)
