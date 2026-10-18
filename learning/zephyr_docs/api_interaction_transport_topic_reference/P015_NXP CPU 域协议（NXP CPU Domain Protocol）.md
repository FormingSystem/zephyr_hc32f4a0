---
id: learning.zephyr-docs.api-interaction-transport-topic-reference.page-15
title: NXP CPU 域协议（NXP CPU Domain Protocol）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__nxp__cpu.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第15章\_NXP CPU 域协议（NXP CPU Domain Protocol）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__scmi__nxp__cpu.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

通过 SCMI 进行 NXP 厂商专用的 CPU 域管理。

<a id="details"></a>

通过 SCMI 进行 NXP 厂商专用的 CPU 域管理。

<a id="header-files"></a>
<a id="files"></a>

## 15.1\_文件（Files）

<a id="r_cpu_2Eh"></a>

```c
file cpu.h
```

相关声明：[cpu.h](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2firmware_2scmi_2nxp_2cpu_8h.html)。

NXP SCMI CPU域协议（CPU Domain Protocol）的头文件。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 15.2\_数据结构（Data Structures）

<a id="r_scmi_5Fnxp_5Fcpu_5Fsleep_5Fmode_5Fconfig"></a>

```c
struct scmi_nxp_cpu_sleep_mode_config
```

相关声明：[scmi_nxp_cpu_sleep_mode_config](../platform_security_model_reference/P041_scmi_nxp_cpu_sleep_mode_config_结构体.md)。

描述CPU_STATE_SET命令的参数。

<a id="r_scmi_5Fpd_5Flpm_5Fsettings"></a>

```c
struct scmi_pd_lpm_settings
```

相关声明：[scmi_pd_lpm_settings](../platform_security_model_reference/P043_scmi_pd_lpm_settings_结构体.md)。

单个电源域（Power Domain）的低功耗模式设置。

<a id="r_scmi_5Fnxp_5Fcpu_5Fpd_5Flpm_5Fconfig"></a>

```c
struct scmi_nxp_cpu_pd_lpm_config
```

相关声明：[scmi_nxp_cpu_pd_lpm_config](../platform_security_model_reference/P040_scmi_nxp_cpu_pd_lpm_config_结构体.md)。

描述CPU电源域（Power Domain）的低功耗模式设置。

<a id="r_scmi_5Fnxp_5Fcpu_5Firq_5Fmask_5Fconfig"></a>

```c
struct scmi_nxp_cpu_irq_mask_config
```

相关声明：[scmi_nxp_cpu_irq_mask_config](../platform_security_model_reference/P039_scmi_nxp_cpu_irq_mask_config_结构体.md)。

描述CPU_IRQ_WAKE_SET命令的参数。

<a id="r_scmi_5Fnxp_5Fcpu_5Fvector_5Fconfig"></a>

```c
struct scmi_nxp_cpu_vector_config
```

相关声明：[scmi_nxp_cpu_vector_config](../platform_security_model_reference/P042_scmi_nxp_cpu_vector_config_结构体.md)。

描述CPU_RESET_VECTOR_SET命令的参数。

<a id="r_scmi_5Fnxp_5Fcpu_5Finfo"></a>

```c
struct scmi_nxp_cpu_info
```

相关声明：[scmi_nxp_cpu_info](../platform_security_model_reference/P038_scmi_nxp_cpu_info_结构体.md)。

描述CPU_INFO_GET命令的参数。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 15.3\_宏定义（Macros）

<a id="r_ga6633f6dde14c1d1836afe3f13d22d9c0"></a>

```c
#define SCMI_NXP_CPU_SLEEP_FLAG_IRQ_MUX 0x1U
```

相关声明：[SCMI_NXP_CPU_SLEEP_FLAG_IRQ_MUX](#ga6633f6dde14c1d1836afe3f13d22d9c0)。

CPU 休眠标志（Sleep Flag）：唤醒通过 IRQ 多路复用器（Mux）路由。

<a id="r_gaf5dccdbe0be392e7f6250ea2fdf7d59f"></a>

```c
#define SCMI_PROTOCOL_NXP_CPU_DOMAIN 130
```

相关声明：[SCMI_PROTOCOL_NXP_CPU_DOMAIN](#gaf5dccdbe0be392e7f6250ea2fdf7d59f)。

NXP CPU 域协议（CPU Domain Protocol）的协议 ID。

<a id="r_ga73ecf2457ad66f98f96b9eb654915c83"></a>

```c
#define SCMI_NXP_CPU_MAX_PDCONFIGS_T 7U
```

相关声明：[SCMI_NXP_CPU_MAX_PDCONFIGS_T](#ga73ecf2457ad66f98f96b9eb654915c83)。

每个请求允许的电源域低功耗模式（Power-domain LPM）配置数量上限。

<a id="r_ga49704cb9c07b198c7609f2f87628dfc0"></a>

```c
#define SCMI_NXP_CPU_IRQ_WAKE_NUM 22U
```

相关声明：[SCMI_NXP_CPU_IRQ_WAKE_NUM](#ga49704cb9c07b198c7609f2f87628dfc0)。

每个请求允许的 IRQ 唤醒掩码字（Wake Mask Word）数量上限。

<a id="r_ga7508afb7c58540b8479de566fb7d758d"></a>

```c
#define SCMI_NXP_CPU_VEC_FLAGS_BOOT BIT(29)
```

相关声明：[SCMI_NXP_CPU_VEC_FLAGS_BOOT](#ga7508afb7c58540b8479de566fb7d758d)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

CPU 向量标志（Vector Flag）：引导地址（Boot Address），用于冷启动／复位（Cold Boot/Reset）。

<a id="r_ga43ff18baef22c48e8d5b0ae1f3423819"></a>

```c
#define SCMI_NXP_CPU_VEC_FLAGS_START BIT(30)
```

相关声明：[SCMI_NXP_CPU_VEC_FLAGS_START](#ga43ff18baef22c48e8d5b0ae1f3423819)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

CPU 向量标志（Vector Flag）：启动地址（Start Address），用于热启动（Warm Start）。

<a id="r_gaa4890d55ca37230c5ac03bd191e6ac9f"></a>

```c
#define SCMI_NXP_CPU_VEC_FLAGS_RESUME BIT(31)
```

相关声明：[SCMI_NXP_CPU_VEC_FLAGS_RESUME](#gaa4890d55ca37230c5ac03bd191e6ac9f)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

CPU 向量标志（Vector Flag）：恢复地址（Resume Address），用于退出挂起（Suspend）。

<a id="r_gae9829ba24709ab2f91cd5d3f32d35ddc"></a>

```c
#define SCMI_NXP_CPU_PROTOCOL_SUPPORTED_VERSION 0x10000
```

相关声明：[SCMI_NXP_CPU_PROTOCOL_SUPPORTED_VERSION](#gae9829ba24709ab2f91cd5d3f32d35ddc)。

本驱动支持的 NXP SCMI CPU 域协议（CPU Domain Protocol）版本。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 15.4\_函数（Functions）

<a id="r_gab8211fd0eb9f9be04b441b5488fe8d93"></a>

```c
int scmi_nxp_cpu_sleep_mode_set (struct scmi_nxp_cpu_sleep_mode_config *cfg)
```

相关声明：[scmi_nxp_cpu_sleep_mode_set](#gab8211fd0eb9f9be04b441b5488fe8d93)、[scmi_nxp_cpu_sleep_mode_config](../platform_security_model_reference/P041_scmi_nxp_cpu_sleep_mode_config_结构体.md)。

发送 `CPU_SLEEP_MODE_SET` 命令并获取回复（Reply）。

<a id="r_ga346872d9b23f24a5f9d2636c6c31b9d8"></a>

```c
int scmi_nxp_cpu_pd_lpm_set (struct scmi_nxp_cpu_pd_lpm_config *cfg)
```

相关声明：[scmi_nxp_cpu_pd_lpm_set](#ga346872d9b23f24a5f9d2636c6c31b9d8)、[scmi_nxp_cpu_pd_lpm_config](../platform_security_model_reference/P040_scmi_nxp_cpu_pd_lpm_config_结构体.md)。

发送 `SCMI_NXP_CPU_DOMAIN_MSG_CPU_PD_LPM_CONFIG_SET` 命令并获取回复（Reply）。

<a id="r_gae8e104786d96b8c5a03fc54d201e09ed"></a>

```c
int scmi_nxp_cpu_set_irq_mask (struct scmi_nxp_cpu_irq_mask_config *cfg)
```

相关声明：[scmi_nxp_cpu_set_irq_mask](#gae8e104786d96b8c5a03fc54d201e09ed)、[scmi_nxp_cpu_irq_mask_config](../platform_security_model_reference/P039_scmi_nxp_cpu_irq_mask_config_结构体.md)。

发送 `CPU_IRQ_WAKE_SET` 命令并获取回复（Reply）。

<a id="r_ga493e417adeb9b63b48613e7ca1f625e8"></a>

```c
int scmi_nxp_cpu_reset_vector (struct scmi_nxp_cpu_vector_config *cfg)
```

相关声明：[scmi_nxp_cpu_reset_vector](#ga493e417adeb9b63b48613e7ca1f625e8)、[scmi_nxp_cpu_vector_config](../platform_security_model_reference/P042_scmi_nxp_cpu_vector_config_结构体.md)。

发送 `CPU_RESET_VECTOR_SET` 命令并获取回复（Reply）。

<a id="r_ga3f3524711a4dacadbb2fcfeae9d5e008"></a>

```c
int scmi_nxp_cpu_info_get (uint32_t cpu_id, struct scmi_nxp_cpu_info *cfg)
```

相关声明：[scmi_nxp_cpu_info_get](#ga3f3524711a4dacadbb2fcfeae9d5e008)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[scmi_nxp_cpu_info](../platform_security_model_reference/P038_scmi_nxp_cpu_info_结构体.md)。

发送 `CPU_INFO_GET` 命令并获取回复（Reply）。

## 15.5\_详细说明（Detailed Documentation）

<a id="ga49704cb9c07b198c7609f2f87628dfc0"></a>

### `SCMI_NXP_CPU_IRQ_WAKE_NUM`

```c
#define SCMI_NXP_CPU_IRQ_WAKE_NUM 22U
```

```c
#include <zephyr/drivers/firmware/scmi/nxp/cpu.h>
```

每个请求允许的 IRQ 唤醒掩码字（Wake Mask Word）数量上限。

<a id="ga73ecf2457ad66f98f96b9eb654915c83"></a>

### `SCMI_NXP_CPU_MAX_PDCONFIGS_T`

```c
#define SCMI_NXP_CPU_MAX_PDCONFIGS_T 7U
```

```c
#include <zephyr/drivers/firmware/scmi/nxp/cpu.h>
```

每个请求允许的电源域低功耗模式（Power-domain LPM）配置数量上限。

<a id="gae9829ba24709ab2f91cd5d3f32d35ddc"></a>

### `SCMI_NXP_CPU_PROTOCOL_SUPPORTED_VERSION`

```c
#define SCMI_NXP_CPU_PROTOCOL_SUPPORTED_VERSION 0x10000
```

```c
#include <zephyr/drivers/firmware/scmi/nxp/cpu.h>
```

本驱动支持的 NXP SCMI CPU 域协议（CPU Domain Protocol）版本。

<a id="ga6633f6dde14c1d1836afe3f13d22d9c0"></a>

### `SCMI_NXP_CPU_SLEEP_FLAG_IRQ_MUX`

```c
#define SCMI_NXP_CPU_SLEEP_FLAG_IRQ_MUX 0x1U
```

```c
#include <zephyr/drivers/firmware/scmi/nxp/cpu.h>
```

CPU 休眠标志（Sleep Flag）：唤醒通过 IRQ 多路复用器（Mux）路由。

<a id="ga7508afb7c58540b8479de566fb7d758d"></a>

### `SCMI_NXP_CPU_VEC_FLAGS_BOOT`

```c
#define SCMI_NXP_CPU_VEC_FLAGS_BOOT BIT(29)
```

```c
#include <zephyr/drivers/firmware/scmi/nxp/cpu.h>
```

CPU 向量标志（Vector Flag）：引导地址（Boot Address），用于冷启动／复位（Cold Boot/Reset）。

<a id="gaa4890d55ca37230c5ac03bd191e6ac9f"></a>

### `SCMI_NXP_CPU_VEC_FLAGS_RESUME`

```c
#define SCMI_NXP_CPU_VEC_FLAGS_RESUME BIT(31)
```

```c
#include <zephyr/drivers/firmware/scmi/nxp/cpu.h>
```

CPU 向量标志（Vector Flag）：恢复地址（Resume Address），用于退出挂起（Suspend）。

<a id="ga43ff18baef22c48e8d5b0ae1f3423819"></a>

### `SCMI_NXP_CPU_VEC_FLAGS_START`

```c
#define SCMI_NXP_CPU_VEC_FLAGS_START BIT(30)
```

```c
#include <zephyr/drivers/firmware/scmi/nxp/cpu.h>
```

CPU 向量标志（Vector Flag）：启动地址（Start Address），用于热启动（Warm Start）。

<a id="gaf5dccdbe0be392e7f6250ea2fdf7d59f"></a>

### `SCMI_PROTOCOL_NXP_CPU_DOMAIN`

```c
#define SCMI_PROTOCOL_NXP_CPU_DOMAIN 130
```

```c
#include <zephyr/drivers/firmware/scmi/nxp/cpu.h>
```

NXP CPU 域协议（CPU Domain Protocol）的协议 ID。

<a id="ga3f3524711a4dacadbb2fcfeae9d5e008"></a>

### `scmi_nxp_cpu_info_get()`

```c
int scmi_nxp_cpu_info_get ( uint32_t cpu_id, struct scmi_nxp_cpu_info * cfg )
```

```c
#include <zephyr/drivers/firmware/scmi/nxp/cpu.h>
```

发送 `CPU_INFO_GET` 命令并获取回复（Reply）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `cpu_id` | 要查询的 CPU ID（输入，Input）。 |
| `cfg` | 指向接收 CPU 信息的结构体的指针（输出，Output）。 |

返回（Returns）：成功时返回0，失败时返回负错误码（Negative errno Value）。

<a id="ga346872d9b23f24a5f9d2636c6c31b9d8"></a>

### `scmi_nxp_cpu_pd_lpm_set()`

```c
int scmi_nxp_cpu_pd_lpm_set ( struct scmi_nxp_cpu_pd_lpm_config * cfg)
```

```c
#include <zephyr/drivers/firmware/scmi/nxp/cpu.h>
```

发送 `SCMI_NXP_CPU_DOMAIN_MSG_CPU_PD_LPM_CONFIG_SET` 命令并获取回复（Reply）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `cfg` | 指向包含待设置配置的结构体的指针。 |

返回（Returns）：成功时返回0，失败时返回负错误码（Negative errno Value）。

<a id="ga493e417adeb9b63b48613e7ca1f625e8"></a>

### `scmi_nxp_cpu_reset_vector()`

```c
int scmi_nxp_cpu_reset_vector ( struct scmi_nxp_cpu_vector_config * cfg)
```

```c
#include <zephyr/drivers/firmware/scmi/nxp/cpu.h>
```

发送 `CPU_RESET_VECTOR_SET` 命令并获取回复（Reply）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `cfg` | 指向包含待设置配置的结构体的指针。 |

返回（Returns）：成功时返回0，失败时返回负错误码（Negative errno Value）。

<a id="gae8e104786d96b8c5a03fc54d201e09ed"></a>

### `scmi_nxp_cpu_set_irq_mask()`

```c
int scmi_nxp_cpu_set_irq_mask ( struct scmi_nxp_cpu_irq_mask_config * cfg)
```

```c
#include <zephyr/drivers/firmware/scmi/nxp/cpu.h>
```

发送 `CPU_IRQ_WAKE_SET` 命令并获取回复（Reply）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `cfg` | 指向包含待设置配置的结构体的指针。 |

返回（Returns）：成功时返回0，失败时返回负错误码（Negative errno Value）。

<a id="gab8211fd0eb9f9be04b441b5488fe8d93"></a>

### `scmi_nxp_cpu_sleep_mode_set()`

```c
int scmi_nxp_cpu_sleep_mode_set ( struct scmi_nxp_cpu_sleep_mode_config * cfg)
```

```c
#include <zephyr/drivers/firmware/scmi/nxp/cpu.h>
```

发送 `CPU_SLEEP_MODE_SET` 命令并获取回复（Reply）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `cfg` | 指向包含待设置配置的结构体的指针。 |

返回（Returns）：成功时返回0，失败时返回负错误码（Negative errno Value）。


## 15.6\_原页交叉引用（Cross References）

- [cpu.h](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2firmware_2scmi_2nxp_2cpu_8h.html)
- [scmi_nxp_cpu_sleep_mode_config](../platform_security_model_reference/P041_scmi_nxp_cpu_sleep_mode_config_结构体.md)
- [scmi_pd_lpm_settings](../platform_security_model_reference/P043_scmi_pd_lpm_settings_结构体.md)
- [scmi_nxp_cpu_pd_lpm_config](../platform_security_model_reference/P040_scmi_nxp_cpu_pd_lpm_config_结构体.md)
- [scmi_nxp_cpu_irq_mask_config](../platform_security_model_reference/P039_scmi_nxp_cpu_irq_mask_config_结构体.md)
- [scmi_nxp_cpu_vector_config](../platform_security_model_reference/P042_scmi_nxp_cpu_vector_config_结构体.md)
- [scmi_nxp_cpu_info](../platform_security_model_reference/P038_scmi_nxp_cpu_info_结构体.md)
- [BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P014_PCIe 虚拟通道（Virtual Channel）主机接口.md) · [返回大纲](大纲.md) · [下一章](P016_单边沿半字节传输（SENT）.md)
