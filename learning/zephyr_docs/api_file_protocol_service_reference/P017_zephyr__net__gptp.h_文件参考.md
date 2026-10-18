---
id: learning.zephyr-docs.api-file-protocol-service-reference.page-17
title: zephyr__net__gptp.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/gptp_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第17章\_zephyr\_\_net\_\_gptp.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/gptp_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

精确时间协议栈（Precision Time Protocol Stack）的公共函数。

<a id="details"></a>

```c
#include <zephyr/net/net_core.h>
#include <zephyr/net/ptp_time.h>
#include <stdbool.h>
```

查看此文件的源码。

精确时间协议栈（Precision Time Protocol Stack）的公共函数。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 17.1\_数据结构（Data Structures）

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

## 17.2\_类型定义（Typedefs）

<a id="r_gade00e0d8398f015031d7f77317e4b97b"></a>

```c
typedef void(* gptp_phase_dis_callback_t) (uint8_t *gm_identity, uint16_t *time_base, struct gptp_scaled_ns *last_gm_ph_change, double *last_gm_freq_change)
```

相关声明：[gptp_phase_dis_callback_t](https://docs.zephyrproject.org/latest/doxygen/html/group__gptp.html#gade00e0d8398f015031d7f77317e4b97b)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[gptp_scaled_ns](../network_service_model_reference/P020_gptp_scaled_ns_结构体.md)。

定义在主时钟（Grandmaster）发出相位不连续（Phase Discontinuity）通知后调用的回调。

<a id="r_ga9bd009e6027d57cd9950b0387d727e3d"></a>

```c
typedef void(* gptp_port_cb_t) (int port, struct net_if *iface, void *user_data)
```

相关声明：[gptp_port_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__gptp.html#ga9bd009e6027d57cd9950b0387d727e3d)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

遍历广义精确时间协议（gPTP）端口时使用的回调。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 17.3\_函数（Functions）

<a id="r_gaad2282df9cbf7f05f557285323af8f07"></a>

```c
void gptp_register_phase_dis_cb (struct gptp_phase_dis_cb *phase_dis, gptp_phase_dis_callback_t cb)
```

相关声明：[gptp_register_phase_dis_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__gptp.html#gaad2282df9cbf7f05f557285323af8f07)、[gptp_phase_dis_cb](../network_service_model_reference/P018_gptp_phase_dis_cb_结构体.md)、[gptp_phase_dis_callback_t](https://docs.zephyrproject.org/latest/doxygen/html/group__gptp.html#gade00e0d8398f015031d7f77317e4b97b)。

注册相位不连续（Phase Discontinuity）回调。

<a id="r_ga55d95859e5ec586cb2341929901220dd"></a>

```c
void gptp_unregister_phase_dis_cb (struct gptp_phase_dis_cb *phase_dis)
```

相关声明：[gptp_unregister_phase_dis_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__gptp.html#ga55d95859e5ec586cb2341929901220dd)、[gptp_phase_dis_cb](../network_service_model_reference/P018_gptp_phase_dis_cb_结构体.md)。

注销相位不连续（Phase Discontinuity）回调。

<a id="r_ga29bf157d06a5ec5bb5a2a8a0e986709d"></a>

```c
void gptp_call_phase_dis_cb (void)
```

相关声明：[gptp_call_phase_dis_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__gptp.html#ga29bf157d06a5ec5bb5a2a8a0e986709d)。

调用相位不连续（Phase Discontinuity）回调函数。

<a id="r_ga9a8e2ccf20d0430b4e62f3302462c6eb"></a>

```c
int gptp_event_capture (struct net_ptp_time *slave_time, bool *gm_present)
```

相关声明：[gptp_event_capture](https://docs.zephyrproject.org/latest/doxygen/html/group__gptp.html#ga9a8e2ccf20d0430b4e62f3302462c6eb)、[net_ptp_time](../network_core_model_reference/P116_net_ptp_time_结构体.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

获取 gPTP 时间（Time）。

<a id="r_ga40121c2957d58b0b5bb4468eac5de259"></a>

```c
char * gptp_sprint_clock_id (const uint8_t *clk_id, char *output, size_t output_len)
```

相关声明：[gptp_sprint_clock_id](https://docs.zephyrproject.org/latest/doxygen/html/group__gptp.html#ga40121c2957d58b0b5bb4468eac5de259)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

将时钟 ID（Clock ID）打印到用户提供缓冲区的工具函数。

<a id="r_ga06ddd41c7adf9e387d1b23bcdfccbddc"></a>

```c
void gptp_foreach_port (gptp_port_cb_t cb, void *user_data)
```

相关声明：[gptp_foreach_port](https://docs.zephyrproject.org/latest/doxygen/html/group__gptp.html#ga06ddd41c7adf9e387d1b23bcdfccbddc)、[gptp_port_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__gptp.html#ga9bd009e6027d57cd9950b0387d727e3d)。

遍历全部 gPTP 端口（Ports），为每个端口调用回调。

<a id="r_gaf4366741c39144e244d7555582b3b62c"></a>

```c
int gptp_get_port_number (struct net_if *iface)
```

相关声明：[gptp_get_port_number](https://docs.zephyrproject.org/latest/doxygen/html/group__gptp.html#gaf4366741c39144e244d7555582b3b62c)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)。

获取网络接口（Network Interface）的 gPTP 端口号。

<a id="r_ga4af3bf8e0ef4e3833260b6365b2b1e2f"></a>

```c
int gptp_set_port_number (struct net_if *iface, uint16_t port)
```

相关声明：[gptp_set_port_number](https://docs.zephyrproject.org/latest/doxygen/html/group__gptp.html#ga4af3bf8e0ef4e3833260b6365b2b1e2f)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

为网络接口（Network Interface）设置 gPTP 端口号。

<a id="r_gae4c3aac6b88e9ce21a32ba3263b9ad59"></a>

```c
struct gptp_domain * gptp_get_domain (void)
```

相关声明：[gptp_get_domain](https://docs.zephyrproject.org/latest/doxygen/html/group__gptp.html#gae4c3aac6b88e9ce21a32ba3263b9ad59)。

获取 gPTP 域（Domain）。

<a id="r_ga9b27c9a741fb0ca72eff78e334e629fe"></a>

```c
void gptp_clk_src_time_invoke (struct gptp_clk_src_time_invoke_params *arg)
```

相关声明：[gptp_clk_src_time_invoke](https://docs.zephyrproject.org/latest/doxygen/html/group__gptp.html#ga9b27c9a741fb0ca72eff78e334e629fe)、[gptp_clk_src_time_invoke_params](../network_service_model_reference/P015_gptp_clk_src_time_invoke_params_结构体.md)。

时钟源（ClockSource）实体使用此接口，为时间感知系统（Time-aware System）的时钟主端（ClockMaster）实体提供时间。

<a id="r_ga5b46fb7bbe1a380e3c327c8f5abbabeb"></a>

```c
struct gptp_hdr * gptp_get_hdr (struct net_pkt *pkt)
```

相关声明：[gptp_hdr](../network_service_model_reference/P017_gptp_hdr_结构体.md)、[gptp_get_hdr](https://docs.zephyrproject.org/latest/doxygen/html/group__gptp.html#ga5b46fb7bbe1a380e3c327c8f5abbabeb)、[net_pkt](../network_core_model_reference/P114_net_pkt_结构体.md)。

返回指向网络数据包中 gPTP 包头（Packet Header）的指针。


## 17.4\_原页交叉引用（Cross References）

- [zephyr/net/net_core.h](../api_source_system_reference/P023_net_core.h_源码浏览.md)
- [zephyr/net/ptp_time.h](../api_source_reference/P681_ptp_time.h_源码浏览.md)
- [stdbool.h](../api_source_supplement_reference/P186_stdbool.h_源码浏览.md)
- [查看此文件的源码。](../api_source_device_reference/P019_gptp.h_源码浏览.md)
- [gptp_scaled_ns](../network_service_model_reference/P020_gptp_scaled_ns_结构体.md)
- [gptp_uscaled_ns](../network_service_model_reference/P021_gptp_uscaled_ns_结构体.md)
- [gptp_port_identity](../network_service_model_reference/P019_gptp_port_identity_结构体.md)
- [gptp_flags](../network_service_model_reference/P016_gptp_flags_结构体.md)
- [gptp_hdr](../network_service_model_reference/P017_gptp_hdr_结构体.md)
- [gptp_phase_dis_cb](../network_service_model_reference/P018_gptp_phase_dis_cb_结构体.md)
- [gptp_clk_src_time_invoke_params](../network_service_model_reference/P015_gptp_clk_src_time_invoke_params_结构体.md)
- [gptp_phase_dis_callback_t](https://docs.zephyrproject.org/latest/doxygen/html/group__gptp.html#gade00e0d8398f015031d7f77317e4b97b)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [gptp_port_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__gptp.html#ga9bd009e6027d57cd9950b0387d727e3d)
- [net_if](../network_core_model_reference/P079_net_if_结构体.md)
- [gptp_register_phase_dis_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__gptp.html#gaad2282df9cbf7f05f557285323af8f07)
- [gptp_unregister_phase_dis_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__gptp.html#ga55d95859e5ec586cb2341929901220dd)
- [gptp_call_phase_dis_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__gptp.html#ga29bf157d06a5ec5bb5a2a8a0e986709d)
- [gptp_event_capture](https://docs.zephyrproject.org/latest/doxygen/html/group__gptp.html#ga9a8e2ccf20d0430b4e62f3302462c6eb)
- [net_ptp_time](../network_core_model_reference/P116_net_ptp_time_结构体.md)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [gptp_sprint_clock_id](https://docs.zephyrproject.org/latest/doxygen/html/group__gptp.html#ga40121c2957d58b0b5bb4468eac5de259)
- [gptp_foreach_port](https://docs.zephyrproject.org/latest/doxygen/html/group__gptp.html#ga06ddd41c7adf9e387d1b23bcdfccbddc)
- [gptp_get_port_number](https://docs.zephyrproject.org/latest/doxygen/html/group__gptp.html#gaf4366741c39144e244d7555582b3b62c)
- [gptp_set_port_number](https://docs.zephyrproject.org/latest/doxygen/html/group__gptp.html#ga4af3bf8e0ef4e3833260b6365b2b1e2f)
- [gptp_get_domain](https://docs.zephyrproject.org/latest/doxygen/html/group__gptp.html#gae4c3aac6b88e9ce21a32ba3263b9ad59)
- [gptp_clk_src_time_invoke](https://docs.zephyrproject.org/latest/doxygen/html/group__gptp.html#ga9b27c9a741fb0ca72eff78e334e629fe)
- [gptp_get_hdr](https://docs.zephyrproject.org/latest/doxygen/html/group__gptp.html#ga5b46fb7bbe1a380e3c327c8f5abbabeb)
- [net_pkt](../network_core_model_reference/P114_net_pkt_结构体.md)

<a id="header-details"></a>

---

[上一章](P016_zephyr__dt-bindings__pinctrl__gecko-pinctrl-s1.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P018_zephyr__drivers__sensor__grow_r502a.h_文件参考.md)
