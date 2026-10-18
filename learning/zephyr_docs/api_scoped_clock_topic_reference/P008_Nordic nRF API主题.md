---
id: learning.zephyr-docs.api-scoped-clock-topic-reference.page-8
title: Nordic nRF API主题
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__nrf.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第8章\_Nordic nRF API主题

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__nrf.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

<a id="details"></a>



<a id="header-files"></a>
<a id="files"></a>

## 8.1\_文件（Files）

<a id="r_nrf_5Fclock_5Fcontrol_2Eh"></a>

```c
file nrf_clock_control.h
```

相关声明：[nrf_clock_control.h](../api_file_host_video_reference/P010_zephyr__drivers__clock_control__nrf_clock_control.h_文件参考.md)。

Nordic nRF设备的时钟控制定义（Clock Control Definitions）。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 8.2\_宏定义（Macros）

<a id="r_ga23770353a9de4e4bec02bca693c6709e"></a>

```c
#define NRF_CLOCK_CONTROL_FREQUENCY_MAX UINT32_MAX
```

相关声明：[NRF_CLOCK_CONTROL_FREQUENCY_MAX](#ga23770353a9de4e4bec02bca693c6709e)、[UINT32_MAX](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#ab5eb23180f7cc12b7d6c04a8ec067fdd)。

指定对所给时钟使用最高可用频率（Maximum Available Frequency）。

<a id="r_gaf6cb7f3b8b7bb9540751639e1e48f229"></a>

```c
#define NRF_CLOCK_CONTROL_ACCURACY_MAX 1
```

相关声明：[NRF_CLOCK_CONTROL_ACCURACY_MAX](#gaf6cb7f3b8b7bb9540751639e1e48f229)。

指定对所给时钟使用最高可用准确度（Maximum Available Accuracy）。

<a id="r_ga4a7fdc5110eef82b86b642d40d9dc02e"></a>

```c
#define NRF_CLOCK_CONTROL_ACCURACY_PPM(ppm)
```

相关声明：[NRF_CLOCK_CONTROL_ACCURACY_PPM](#ga4a7fdc5110eef82b86b642d40d9dc02e)。

指定所需时钟准确度（Clock Accuracy），以百万分之一（ppm）为单位。

<a id="r_ga0c870f2b78d538f7a33cf47110ed6ea7"></a>

```c
#define NRF_CLOCK_CONTROL_PRECISION_HIGH 1
```

相关声明：[NRF_CLOCK_CONTROL_PRECISION_HIGH](#ga0c870f2b78d538f7a33cf47110ed6ea7)。

指定需要高精度时钟（High Precision Clock）。

<a id="r_ga15b112b62c60a7b9ca0b7fd2fccd5cca"></a>

```c
#define NRF_CLOCK_CONTROL_PRECISION_DEFAULT 0
```

相关声明：[NRF_CLOCK_CONTROL_PRECISION_DEFAULT](#ga15b112b62c60a7b9ca0b7fd2fccd5cca)。

指定默认时钟精度（Default Precision）已经足够。

<a id="r_ga7af5b4718beb72824e1e2a0d38fb1d7c"></a>

```c
#define CLOCK_CONTROL_NRF_AUXPLL_GET_FREQ(node)
```

相关声明：[CLOCK_CONTROL_NRF_AUXPLL_GET_FREQ](#ga7af5b4718beb72824e1e2a0d38fb1d7c)。

获取辅助锁相环（AUXPLL）设备树节点（Devicetree Node）的输出频率。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 8.3\_枚举（Enumerations）

<a id="r_gaadc162ec2c250d17572546d74a08ee7d"></a>

```c
enum nrf_lfclk_start_mode { CLOCK_CONTROL_NRF_LF_START_NOWAIT , CLOCK_CONTROL_NRF_LF_START_AVAILABLE , CLOCK_CONTROL_NRF_LF_START_STABLE }
```

相关声明：[nrf_lfclk_start_mode](#gaadc162ec2c250d17572546d74a08ee7d)、[CLOCK_CONTROL_NRF_LF_START_NOWAIT](#ggaadc162ec2c250d17572546d74a08ee7dab4eb3c0c8038403f218a0147df6cdbec)、[CLOCK_CONTROL_NRF_LF_START_AVAILABLE](#ggaadc162ec2c250d17572546d74a08ee7da92be9b702c66df1a2bfd95560f1278df)、[CLOCK_CONTROL_NRF_LF_START_STABLE](#ggaadc162ec2c250d17572546d74a08ee7da949ac21a6fe976280b5fcc967608a8f4)。

低频时钟启动模式（LF Clock Start Modes）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 8.4\_函数（Functions）

<a id="r_ga2da9657c008b903a9131238bde6ed1ac"></a>

```c
static int nrf_clock_control_request (const struct device *dev, const struct nrf_clock_spec *spec, struct onoff_client *cli)
```

相关声明：[nrf_clock_control_request](#ga2da9657c008b903a9131238bde6ed1ac)、[device](../device_reference/P002_设备对象结构.md)、[onoff_client](../memory_services/P019_开关客户端结构.md)。

请求预留具有指定属性的时钟使用权（Clock Reservation）。

<a id="r_gaf334bc4e8b5ca0eb63b2bc4b1d963ac8"></a>

```c
int nrf_clock_control_request_sync (const struct device *dev, const struct nrf_clock_spec *spec, k_timeout_t timeout)
```

相关声明：[nrf_clock_control_request_sync](#gaf334bc4e8b5ca0eb63b2bc4b1d963ac8)、[device](../device_reference/P002_设备对象结构.md)、[k_timeout_t](../timer_reference/P087_内核超时类型.md)。

同步请求预留具有指定属性的时钟使用权（Synchronous Clock Reservation）。

<a id="r_gaa46e3e407fb02b206772c438a0108634"></a>

```c
static int nrf_clock_control_release (const struct device *dev, const struct nrf_clock_spec *spec)
```

相关声明：[nrf_clock_control_release](#gaa46e3e407fb02b206772c438a0108634)、[device](../device_reference/P002_设备对象结构.md)。

释放已预留的时钟使用权（Reserved Use）。

<a id="r_ga3ecff5c6b37ced253c030fd032c61a70"></a>

```c
static int nrf_clock_control_cancel_or_release (const struct device *dev, const struct nrf_clock_spec *spec, struct onoff_client *cli)
```

相关声明：[nrf_clock_control_cancel_or_release](#ga3ecff5c6b37ced253c030fd032c61a70)、[device](../device_reference/P002_设备对象结构.md)、[onoff_client](../memory_services/P019_开关客户端结构.md)。

安全取消预留请求（Reservation Request）。

<a id="r_gadd7ed9d76f521cc2894ba21abc8e4d94"></a>

```c
static int nrf_clock_control_resolve (const struct device *dev, const struct nrf_clock_spec *req_spec, struct nrf_clock_spec *res_spec)
```

相关声明：[nrf_clock_control_resolve](#gadd7ed9d76f521cc2894ba21abc8e4d94)、[device](../device_reference/P002_设备对象结构.md)。

将请求的时钟规格（Clock Spec）解析为实际结果规格。

<a id="r_ga0ac2c96482c7551b16f1cc4eadd01560"></a>

```c
static int nrf_clock_control_get_startup_time (const struct device *dev, const struct nrf_clock_spec *spec, uint32_t *startup_time_us)
```

相关声明：[nrf_clock_control_get_startup_time](#ga0ac2c96482c7551b16f1cc4eadd01560)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

获取时钟启动时间（Startup Time）。

<a id="r_ga259dfa1a679d21c4b92ecbf9fdfd3d13"></a>

```c
void nrf_clock_control_hfxo_request (void)
```

相关声明：[nrf_clock_control_hfxo_request](#ga259dfa1a679d21c4b92ecbf9fdfd3d13)。

从零延迟中断上下文（Zero Latency Interrupt Context）请求高频晶体振荡器（HFXO）。

<a id="r_ga502110bf4c35eca120f883ba766705b7"></a>

```c
void nrf_clock_control_hfxo_release (void)
```

相关声明：[nrf_clock_control_hfxo_release](#ga502110bf4c35eca120f883ba766705b7)。

从零延迟中断上下文（Zero Latency Interrupt Context）释放高频晶体振荡器（HFXO）。

<a id="header-member-group"></a>
<a id="member-group"></a>

## 8.5\_辅助锁相环输出频率（AUXPLL Output Frequencies）

辅助锁相环（AUXPLL）的设备树（Devicetree）使用原始寄存器值；此处给出对应的实际输出频率。

<a id="r_ga445d6198c6ec95aec4d6e03ab3f17fcf"></a>

```c
#define CLOCK_CONTROL_NRF_AUXPLL_FREQ_OUT_MIN_HZ 80000000
```

相关声明：[CLOCK_CONTROL_NRF_AUXPLL_FREQ_OUT_MIN_HZ](#ga445d6198c6ec95aec4d6e03ab3f17fcf)。

辅助锁相环（AUXPLL）的最小输出频率，单位为 Hz。

<a id="r_ga2c452d78c7b50a72fb865f310a9b6fc0"></a>

```c
#define CLOCK_CONTROL_NRF_AUXPLL_FREQ_OUT_AUDIO_44K1_HZ 11289591
```

相关声明：[CLOCK_CONTROL_NRF_AUXPLL_FREQ_OUT_AUDIO_44K1_HZ](#ga2c452d78c7b50a72fb865f310a9b6fc0)。

用于 44.1 kHz 音频的辅助锁相环（AUXPLL）输出频率，单位为 Hz。

<a id="r_ga9c7eb645dc042e54a08c3ffc8173817a"></a>

```c
#define CLOCK_CONTROL_NRF_AUXPLL_FREQ_OUT_USB24M_HZ 24000000
```

相关声明：[CLOCK_CONTROL_NRF_AUXPLL_FREQ_OUT_USB24M_HZ](#ga9c7eb645dc042e54a08c3ffc8173817a)。

用于 24 MHz USB 的辅助锁相环（AUXPLL）输出频率，单位为 Hz。

<a id="r_gaad21d734ae8305f9d0ce2882352dc206"></a>

```c
#define CLOCK_CONTROL_NRF_AUXPLL_FREQ_OUT_AUDIO_48K_HZ 12287963
```

相关声明：[CLOCK_CONTROL_NRF_AUXPLL_FREQ_OUT_AUDIO_48K_HZ](#gaad21d734ae8305f9d0ce2882352dc206)。

用于 48 kHz 音频的辅助锁相环（AUXPLL）输出频率，单位为 Hz。

## 8.6\_详细说明（Detailed Documentation）

<a id="ga2c452d78c7b50a72fb865f310a9b6fc0"></a>

### `CLOCK_CONTROL_NRF_AUXPLL_FREQ_OUT_AUDIO_44K1_HZ`

```c
#define CLOCK_CONTROL_NRF_AUXPLL_FREQ_OUT_AUDIO_44K1_HZ 11289591
```

```c
#include <zephyr/drivers/clock_control/nrf_clock_control.h>
```

用于 44.1 kHz 音频的辅助锁相环（AUXPLL）输出频率，单位为 Hz。

<a id="gaad21d734ae8305f9d0ce2882352dc206"></a>

### `CLOCK_CONTROL_NRF_AUXPLL_FREQ_OUT_AUDIO_48K_HZ`

```c
#define CLOCK_CONTROL_NRF_AUXPLL_FREQ_OUT_AUDIO_48K_HZ 12287963
```

```c
#include <zephyr/drivers/clock_control/nrf_clock_control.h>
```

用于 48 kHz 音频的辅助锁相环（AUXPLL）输出频率，单位为 Hz。

<a id="ga445d6198c6ec95aec4d6e03ab3f17fcf"></a>

### `CLOCK_CONTROL_NRF_AUXPLL_FREQ_OUT_MIN_HZ`

```c
#define CLOCK_CONTROL_NRF_AUXPLL_FREQ_OUT_MIN_HZ 80000000
```

```c
#include <zephyr/drivers/clock_control/nrf_clock_control.h>
```

辅助锁相环（AUXPLL）的最小输出频率，单位为 Hz。

<a id="ga9c7eb645dc042e54a08c3ffc8173817a"></a>

### `CLOCK_CONTROL_NRF_AUXPLL_FREQ_OUT_USB24M_HZ`

```c
#define CLOCK_CONTROL_NRF_AUXPLL_FREQ_OUT_USB24M_HZ 24000000
```

```c
#include <zephyr/drivers/clock_control/nrf_clock_control.h>
```

用于 24 MHz USB 的辅助锁相环（AUXPLL）输出频率，单位为 Hz。

<a id="ga7af5b4718beb72824e1e2a0d38fb1d7c"></a>

### `CLOCK_CONTROL_NRF_AUXPLL_GET_FREQ`

```c
#define CLOCK_CONTROL_NRF_AUXPLL_GET_FREQ ( node)
```

```c
#include <zephyr/drivers/clock_control/nrf_clock_control.h>
```

展开值（Value）：

```c
COND_CODE_1(DT_NODE_HAS_PROP(node, nordic_frequency), \
        (_CLOCK_CONTROL_NRF_AUXPLL_MAP_FREQ(DT_PROP(node, nordic_frequency))), \
        (0))
```

获取辅助锁相环（AUXPLL）设备树节点（Devicetree Node）的输出频率。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `node` | 辅助锁相环（AUXPLL）的设备树节点标识符（Devicetree Node Identifier）。 |

返回（Returns）：输出频率（Output Frequency），单位为 Hz；节点没有 nordic,frequency 属性时返回 0。

<a id="gaf6cb7f3b8b7bb9540751639e1e48f229"></a>

### `NRF_CLOCK_CONTROL_ACCURACY_MAX`

```c
#define NRF_CLOCK_CONTROL_ACCURACY_MAX 1
```

```c
#include <zephyr/drivers/clock_control/nrf_clock_control.h>
```

指定对所给时钟使用最高可用准确度（Maximum Available Accuracy）。

<a id="ga4a7fdc5110eef82b86b642d40d9dc02e"></a>

### `NRF_CLOCK_CONTROL_ACCURACY_PPM`

```c
#define NRF_CLOCK_CONTROL_ACCURACY_PPM ( ppm)
```

```c
#include <zephyr/drivers/clock_control/nrf_clock_control.h>
```

展开值（Value）：

```c
(ppm)
```

指定所需时钟准确度（Clock Accuracy），以百万分之一（ppm）为单位。

<a id="ga23770353a9de4e4bec02bca693c6709e"></a>

### `NRF_CLOCK_CONTROL_FREQUENCY_MAX`

```c
#define NRF_CLOCK_CONTROL_FREQUENCY_MAX UINT32_MAX
```

```c
#include <zephyr/drivers/clock_control/nrf_clock_control.h>
```

指定对所给时钟使用最高可用频率（Maximum Available Frequency）。

<a id="ga15b112b62c60a7b9ca0b7fd2fccd5cca"></a>

### `NRF_CLOCK_CONTROL_PRECISION_DEFAULT`

```c
#define NRF_CLOCK_CONTROL_PRECISION_DEFAULT 0
```

```c
#include <zephyr/drivers/clock_control/nrf_clock_control.h>
```

指定默认时钟精度（Default Precision）已经足够。

<a id="ga0c870f2b78d538f7a33cf47110ed6ea7"></a>

### `NRF_CLOCK_CONTROL_PRECISION_HIGH`

```c
#define NRF_CLOCK_CONTROL_PRECISION_HIGH 1
```

```c
#include <zephyr/drivers/clock_control/nrf_clock_control.h>
```

指定需要高精度时钟（High Precision Clock）。

<a id="gaadc162ec2c250d17572546d74a08ee7d"></a>

### `nrf_lfclk_start_mode`

```c
enum nrf_lfclk_start_mode
```

```c
#include <zephyr/drivers/clock_control/nrf_clock_control.h>
```

低频时钟启动模式（LF Clock Start Modes）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `CLOCK_CONTROL_NRF_LF_START_NOWAIT` | 立即返回，不等待时钟（Clock）。 |
| `CLOCK_CONTROL_NRF_LF_START_AVAILABLE` | 等待时钟可用（Available）。 |
| `CLOCK_CONTROL_NRF_LF_START_STABLE` | 等待时钟稳定（Stable）。 |

<a id="ga3ecff5c6b37ced253c030fd032c61a70"></a>

### `nrf_clock_control_cancel_or_release()`

```c
int nrf_clock_control_cancel_or_release ( const struct device * dev, const struct nrf_clock_spec * spec, struct onoff_client * cli )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/drivers/clock_control/nrf_clock_control.h>
```

安全取消预留请求（Reservation Request）。

客户端可能已经发出预留请求（Reservation Request），但需要在请求完成前关闭。此函数尝试取消请求；如果请求已完成而导致取消失败，则发出释放操作（Release）。这会同步确保所有权数据（Ownership Data）归还客户端，以便用于后续请求。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向时钟设备结构体（Clock Device Structure）的指针。 |
| `spec` | 与预留请求（Reservation Request）所用相同的时钟属性说明（Clock Attributes Specification）。 |
| `cli` | 指向同一客户端状态（Client State）的指针，即发起待取消操作时所提供的那个状态。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `ONOFF_STATE_TO_ON` | 在状态转换（Transition）完成之前取消时。 |
| `ONOFF_STATE_ON` | 在状态转换（Transition）完成之后取消时。 |
| `-EINVAL` | 参数无效（Invalid Parameters）时。 |
| `negative` | onoff_release() 产生的其他错误。 |

<a id="ga0ac2c96482c7551b16f1cc4eadd01560"></a>

### `nrf_clock_control_get_startup_time()`

```c
int nrf_clock_control_get_startup_time ( const struct device * dev, const struct nrf_clock_spec * spec, uint32_t * startup_time_us )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/drivers/clock_control/nrf_clock_control.h>
```

获取时钟启动时间（Startup Time）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 设备结构体（Device Structure）。 |
| `spec` | 要查询启动时间（Startup Time）的时钟说明（Clock Specification）。 |
| `startup_time_us` | 启动时间（Startup Time）的输出存储位置，单位为微秒。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `Successful` | 成功时。 |
| `-errno` | 失败时的错误码（Code）。 |

<a id="ga502110bf4c35eca120f883ba766705b7"></a>

### `nrf_clock_control_hfxo_release()`

```c
void nrf_clock_control_hfxo_release ( void )
```

```c
#include <zephyr/drivers/clock_control/nrf_clock_control.h>
```

从零延迟中断上下文（Zero Latency Interrupt Context）释放高频晶体振荡器（HFXO）。

此函数针对零延迟中断上下文（Zero Latency Interrupt Context）进行了优化。

调用此函数必须与先前的 nrf_clock_control_hfxo_request() 调用配对，因为它使用基本引用计数（Reference Counting），确保没有待处理请求时释放高频晶体振荡器（HFXO）。

<a id="ga259dfa1a679d21c4b92ecbf9fdfd3d13"></a>

### `nrf_clock_control_hfxo_request()`

```c
void nrf_clock_control_hfxo_request ( void )
```

```c
#include <zephyr/drivers/clock_control/nrf_clock_control.h>
```

从零延迟中断上下文（Zero Latency Interrupt Context）请求高频晶体振荡器（HFXO）。

此函数针对零延迟中断上下文（Zero Latency Interrupt Context）进行了优化。它不会在 HFXO 就绪时发出通知，因此每个用户都必须足够早地提交请求，确保 HFXO 的启动过程（Ramp-up）按时完成。

此函数使用引用计数（Reference Counting），因此调用者必须确保每次 nrf_clock_control_hfxo_request() 调用都有对应的 nrf_clock_control_hfxo_release() 调用。

<a id="gaa46e3e407fb02b206772c438a0108634"></a>

### `nrf_clock_control_release()`

```c
int nrf_clock_control_release ( const struct device * dev, const struct nrf_clock_spec * spec )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/drivers/clock_control/nrf_clock_control.h>
```

释放已预留的时钟使用权（Reserved Use）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向时钟设备结构体（Clock Device Structure）的指针。 |
| `spec` | 与预留请求（Reservation Request）所用相同的时钟属性说明（Clock Attributes Specification），以便时钟控制模块跟踪哪些属性仍被请求。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `non-negative` | 成功时，为处理请求时观察到的、与时钟状态机（Clock Machine）关联的开关服务状态（On-off Service State），参见 onoff_release()。 |
| `-EIO` | 服务已记录错误时。 |
| `-ENOTSUP` | 服务所处状态不允许释放（Release）时。 |

<a id="ga2da9657c008b903a9131238bde6ed1ac"></a>

### `nrf_clock_control_request()`

```c
int nrf_clock_control_request ( const struct device * dev, const struct nrf_clock_spec * spec, struct onoff_client * cli )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/drivers/clock_control/nrf_clock_control.h>
```

请求预留具有指定属性的时钟使用权（Clock Reservation）。

返回值表示是否成功发起请求时钟可用的操作（Request Operation）。如果成功发起，该请求操作的结果将通过配置的客户端通知方式（Client Notification Method）提供，通知可能在本次调用返回之前发生。

注意：此函数调用成功时，实际请求仍可能失败。必须检查操作完成结果（Operation Completion Result）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向时钟设备结构体（Clock Device Structure）的指针。 |
| `spec` | 时钟所需的最低可接受属性说明（Minimal Acceptable Attributes），例如频率（Frequency）、准确度（Accuracy）和精度（Precision）。值 0 表示默认（Default）；某项属性没有严格要求时，可以使用 0 代替该属性值。所有属性都没有具体要求时，此参数可以为 NULL。 |
| `cli` | 指向客户端状态（Client State）的指针，该状态给出同步行为要求以及请求完成时如何通知客户端。如果客户端传入的指针对象仍关联着未完成的服务操作，则行为未定义（Undefined Behavior）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `non-negative` | 成功时，为处理请求时观察到的、与时钟状态机（Clock Machine）关联的开关服务状态（On-off Service State），参见 onoff_request()。 |
| `-EIO` | 服务已记录错误时。 |
| `-EINVAL` | 函数参数无效，或无法提供所需时钟属性（Clock Attributes）时，例如无法达到要求的准确度。 |
| `-EAGAIN` | 引用计数（Reference Count）将溢出时。 |

<a id="gaf334bc4e8b5ca0eb63b2bc4b1d963ac8"></a>

### `nrf_clock_control_request_sync()`

```c
int nrf_clock_control_request_sync ( const struct device * dev, const struct nrf_clock_spec * spec, k_timeout_t timeout )
```

```c
#include <zephyr/drivers/clock_control/nrf_clock_control.h>
```

同步请求预留具有指定属性的时钟使用权（Synchronous Clock Reservation）。

此函数会阻塞至请求完成，因此只能在线程上下文（Thread Context）中调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向时钟设备结构体（Clock Device Structure）的指针。 |
| `spec` | 参见 nrf_clock_control_request()。 |
| `timeout` | 请求超时（Request Timeout）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 请求得到满足（Fulfilled）时。 |
| `-EWOULDBLOCK` | 从中断上下文（Interrupt Context）调用请求时。 |
| `negative` | 参见 nrf_clock_control_request() 返回的错误码（Error Codes）。 |

**参阅（See Also）**：另请参见（See Also）：nrf_clock_control_request()。

<a id="gadd7ed9d76f521cc2894ba21abc8e4d94"></a>

### `nrf_clock_control_resolve()`

```c
int nrf_clock_control_resolve ( const struct device * dev, const struct nrf_clock_spec * req_spec, struct nrf_clock_spec * res_spec )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/drivers/clock_control/nrf_clock_control.h>
```

将请求的时钟规格（Clock Spec）解析为实际结果规格。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 设备结构体（Device Structure）。 |
| `req_spec` | 所请求的时钟说明（Clock Specification）。 |
| `res_spec` | 用于保存结果时钟说明（Clock Specification）的目标位置。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `Successful` | 成功时。 |
| `-errno` | 失败时的错误码（Code）。 |


## 8.7\_原页交叉引用（Cross References）

- [nrf_clock_control.h](../api_file_host_video_reference/P010_zephyr__drivers__clock_control__nrf_clock_control.h_文件参考.md)
- [UINT32_MAX](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#ab5eb23180f7cc12b7d6c04a8ec067fdd)
- [device](../device_reference/P002_设备对象结构.md)
- [onoff_client](../memory_services/P019_开关客户端结构.md)
- [k_timeout_t](../timer_reference/P087_内核超时类型.md)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [COND_CODE_1](../util_reference/P001_通用工具公共接口.md#ga358bc3e7669c860a98839a51cd526b20)
- [DT_NODE_HAS_PROP](../dt_identity_reference/P002_设备树存在性与状态宏.md#gacce67bf20541cd2d07d8540058964692)
- [DT_PROP](../dt_property_reference/P001_设备树属性读取宏.md#ga8e1fd9ebacd85d2013df027d041d506b)
- [ONOFF_STATE_TO_ON](../memory_services/P016_开关服务接口.md#gac4a0d8a7b501adb011aa1c4c4da3f2a3)
- [ONOFF_STATE_ON](../memory_services/P016_开关服务接口.md#ga7cd0fba52afba2e337ab7c830d3058d7)
- [onoff_release()](../memory_services/P016_开关服务接口.md#ga19da5359f10fa2e2eb034d1e72235ea6)
- [onoff_request()](../memory_services/P016_开关服务接口.md#ga20dcb358e405deb87b7fbb7846ef9d68)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="agroup__devicetree-generic-exist_html_gacce67bf20541cd2d07d8540058964692"></a>
<a id="agroup__devicetree-generic-prop_html_ga8e1fd9ebacd85d2013df027d041d506b"></a>
<a id="agroup__sys-util_html_ga358bc3e7669c860a98839a51cd526b20"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="ggaadc162ec2c250d17572546d74a08ee7dab4eb3c0c8038403f218a0147df6cdbec"></a>
<a id="ggaadc162ec2c250d17572546d74a08ee7da92be9b702c66df1a2bfd95560f1278df"></a>
<a id="ggaadc162ec2c250d17572546d74a08ee7da949ac21a6fe976280b5fcc967608a8f4"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P007_Silicon Labs SiWx91x 时钟标识符（Clock identifiers）.md) · [返回大纲](大纲.md) · [下一章](P009_一致开销字节填充（Consistent Overhead Byte Stuffing，COBS）.md)
