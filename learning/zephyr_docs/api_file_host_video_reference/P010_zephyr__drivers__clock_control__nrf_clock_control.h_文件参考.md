---
id: learning.zephyr-docs.api-file-host-video-reference.page-10
title: zephyr__drivers__clock_control__nrf_clock_control.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/nrf__clock__control_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第10章\_zephyr\_\_drivers\_\_clock\_control\_\_nrf\_clock\_control.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/nrf__clock__control_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

Nordic nRF设备的时钟控制定义（Clock Control Definitions）。

<a id="details"></a>

```c
#include <zephyr/device.h>
#include <zephyr/sys/onoff.h>
#include <zephyr/drivers/clock_control.h>
#include <hal/nrf_clock.h>
```

查看此文件的源码。

Nordic nRF设备的时钟控制定义（Clock Control Definitions）。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 10.1\_宏定义（Macros）

<a id="r_ga23770353a9de4e4bec02bca693c6709e"></a>

```c
#define NRF_CLOCK_CONTROL_FREQUENCY_MAX UINT32_MAX
```

相关声明：[NRF_CLOCK_CONTROL_FREQUENCY_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__nrf.html#ga23770353a9de4e4bec02bca693c6709e)、[UINT32_MAX](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#ab5eb23180f7cc12b7d6c04a8ec067fdd)。

指定对所给时钟使用最高可用频率（Maximum Available Frequency）。

<a id="r_gaf6cb7f3b8b7bb9540751639e1e48f229"></a>

```c
#define NRF_CLOCK_CONTROL_ACCURACY_MAX 1
```

相关声明：[NRF_CLOCK_CONTROL_ACCURACY_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__nrf.html#gaf6cb7f3b8b7bb9540751639e1e48f229)。

指定对所给时钟使用最高可用准确度（Maximum Available Accuracy）。

<a id="r_ga4a7fdc5110eef82b86b642d40d9dc02e"></a>

```c
#define NRF_CLOCK_CONTROL_ACCURACY_PPM(ppm)
```

相关声明：[NRF_CLOCK_CONTROL_ACCURACY_PPM](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__nrf.html#ga4a7fdc5110eef82b86b642d40d9dc02e)。

指定所需时钟准确度（Clock Accuracy），以百万分之一（ppm）为单位。

<a id="r_ga0c870f2b78d538f7a33cf47110ed6ea7"></a>

```c
#define NRF_CLOCK_CONTROL_PRECISION_HIGH 1
```

相关声明：[NRF_CLOCK_CONTROL_PRECISION_HIGH](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__nrf.html#ga0c870f2b78d538f7a33cf47110ed6ea7)。

指定需要高精度时钟（High Precision Clock）。

<a id="r_ga15b112b62c60a7b9ca0b7fd2fccd5cca"></a>

```c
#define NRF_CLOCK_CONTROL_PRECISION_DEFAULT 0
```

相关声明：[NRF_CLOCK_CONTROL_PRECISION_DEFAULT](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__nrf.html#ga15b112b62c60a7b9ca0b7fd2fccd5cca)。

指定默认时钟精度（Default Precision）已经足够。

<a id="r_ga7af5b4718beb72824e1e2a0d38fb1d7c"></a>

```c
#define CLOCK_CONTROL_NRF_AUXPLL_GET_FREQ(node)
```

相关声明：[CLOCK_CONTROL_NRF_AUXPLL_GET_FREQ](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__nrf.html#ga7af5b4718beb72824e1e2a0d38fb1d7c)。

获取辅助锁相环（AUXPLL）设备树节点（Devicetree Node）的输出频率。

<a id="define-members-0"></a>

### 辅助锁相环输出频率（AUXPLL Output Frequencies）

辅助锁相环（AUXPLL）的设备树（Devicetree）使用原始寄存器值；此处给出对应的实际输出频率。

<a id="r_ga445d6198c6ec95aec4d6e03ab3f17fcf"></a>

```c
#define CLOCK_CONTROL_NRF_AUXPLL_FREQ_OUT_MIN_HZ 80000000
```

相关声明：[CLOCK_CONTROL_NRF_AUXPLL_FREQ_OUT_MIN_HZ](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__nrf.html#ga445d6198c6ec95aec4d6e03ab3f17fcf)。

辅助锁相环（AUXPLL）的最小输出频率，单位为 Hz。

<a id="r_ga2c452d78c7b50a72fb865f310a9b6fc0"></a>

```c
#define CLOCK_CONTROL_NRF_AUXPLL_FREQ_OUT_AUDIO_44K1_HZ 11289591
```

相关声明：[CLOCK_CONTROL_NRF_AUXPLL_FREQ_OUT_AUDIO_44K1_HZ](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__nrf.html#ga2c452d78c7b50a72fb865f310a9b6fc0)。

用于 44.1 kHz 音频的辅助锁相环（AUXPLL）输出频率，单位为 Hz。

<a id="r_ga9c7eb645dc042e54a08c3ffc8173817a"></a>

```c
#define CLOCK_CONTROL_NRF_AUXPLL_FREQ_OUT_USB24M_HZ 24000000
```

相关声明：[CLOCK_CONTROL_NRF_AUXPLL_FREQ_OUT_USB24M_HZ](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__nrf.html#ga9c7eb645dc042e54a08c3ffc8173817a)。

用于 24 MHz USB 的辅助锁相环（AUXPLL）输出频率，单位为 Hz。

<a id="r_gaad21d734ae8305f9d0ce2882352dc206"></a>

```c
#define CLOCK_CONTROL_NRF_AUXPLL_FREQ_OUT_AUDIO_48K_HZ 12287963
```

相关声明：[CLOCK_CONTROL_NRF_AUXPLL_FREQ_OUT_AUDIO_48K_HZ](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__nrf.html#gaad21d734ae8305f9d0ce2882352dc206)。

用于 48 kHz 音频的辅助锁相环（AUXPLL）输出频率，单位为 Hz。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 10.2\_枚举（Enumerations）

<a id="r_gaadc162ec2c250d17572546d74a08ee7d"></a>

```c
enum nrf_lfclk_start_mode { CLOCK_CONTROL_NRF_LF_START_NOWAIT , CLOCK_CONTROL_NRF_LF_START_AVAILABLE , CLOCK_CONTROL_NRF_LF_START_STABLE }
```

相关声明：[nrf_lfclk_start_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__nrf.html#gaadc162ec2c250d17572546d74a08ee7d)、[CLOCK_CONTROL_NRF_LF_START_NOWAIT](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__nrf.html#ggaadc162ec2c250d17572546d74a08ee7dab4eb3c0c8038403f218a0147df6cdbec)、[CLOCK_CONTROL_NRF_LF_START_AVAILABLE](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__nrf.html#ggaadc162ec2c250d17572546d74a08ee7da92be9b702c66df1a2bfd95560f1278df)、[CLOCK_CONTROL_NRF_LF_START_STABLE](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__nrf.html#ggaadc162ec2c250d17572546d74a08ee7da949ac21a6fe976280b5fcc967608a8f4)。

低频时钟启动模式（LF Clock Start Modes）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 10.3\_函数（Functions）

<a id="r_ga2da9657c008b903a9131238bde6ed1ac"></a>

```c
static int nrf_clock_control_request (const struct device *dev, const struct nrf_clock_spec *spec, struct onoff_client *cli)
```

相关声明：[nrf_clock_control_request](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__nrf.html#ga2da9657c008b903a9131238bde6ed1ac)、[device](../device_reference/P002_设备对象结构.md)、[onoff_client](../memory_services/P019_开关客户端结构.md)。

请求预留具有指定属性的时钟使用权（Clock Reservation）。

<a id="r_gaf334bc4e8b5ca0eb63b2bc4b1d963ac8"></a>

```c
int nrf_clock_control_request_sync (const struct device *dev, const struct nrf_clock_spec *spec, k_timeout_t timeout)
```

相关声明：[nrf_clock_control_request_sync](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__nrf.html#gaf334bc4e8b5ca0eb63b2bc4b1d963ac8)、[device](../device_reference/P002_设备对象结构.md)、[k_timeout_t](../timer_reference/P087_内核超时类型.md)。

同步请求预留具有指定属性的时钟使用权（Synchronous Clock Reservation）。

<a id="r_gaa46e3e407fb02b206772c438a0108634"></a>

```c
static int nrf_clock_control_release (const struct device *dev, const struct nrf_clock_spec *spec)
```

相关声明：[nrf_clock_control_release](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__nrf.html#gaa46e3e407fb02b206772c438a0108634)、[device](../device_reference/P002_设备对象结构.md)。

释放已预留的时钟使用权（Reserved Use）。

<a id="r_ga3ecff5c6b37ced253c030fd032c61a70"></a>

```c
static int nrf_clock_control_cancel_or_release (const struct device *dev, const struct nrf_clock_spec *spec, struct onoff_client *cli)
```

相关声明：[nrf_clock_control_cancel_or_release](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__nrf.html#ga3ecff5c6b37ced253c030fd032c61a70)、[device](../device_reference/P002_设备对象结构.md)、[onoff_client](../memory_services/P019_开关客户端结构.md)。

安全取消预留请求（Reservation Request）。

<a id="r_gadd7ed9d76f521cc2894ba21abc8e4d94"></a>

```c
static int nrf_clock_control_resolve (const struct device *dev, const struct nrf_clock_spec *req_spec, struct nrf_clock_spec *res_spec)
```

相关声明：[nrf_clock_control_resolve](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__nrf.html#gadd7ed9d76f521cc2894ba21abc8e4d94)、[device](../device_reference/P002_设备对象结构.md)。

将请求的时钟规格（Clock Spec）解析为实际结果规格。

<a id="r_ga0ac2c96482c7551b16f1cc4eadd01560"></a>

```c
static int nrf_clock_control_get_startup_time (const struct device *dev, const struct nrf_clock_spec *spec, uint32_t *startup_time_us)
```

相关声明：[nrf_clock_control_get_startup_time](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__nrf.html#ga0ac2c96482c7551b16f1cc4eadd01560)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

获取时钟启动时间（Startup Time）。

<a id="r_ga259dfa1a679d21c4b92ecbf9fdfd3d13"></a>

```c
void nrf_clock_control_hfxo_request (void)
```

相关声明：[nrf_clock_control_hfxo_request](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__nrf.html#ga259dfa1a679d21c4b92ecbf9fdfd3d13)。

从零延迟中断上下文（Zero Latency Interrupt Context）请求高频晶体振荡器（HFXO）。

<a id="r_ga502110bf4c35eca120f883ba766705b7"></a>

```c
void nrf_clock_control_hfxo_release (void)
```

相关声明：[nrf_clock_control_hfxo_release](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__nrf.html#ga502110bf4c35eca120f883ba766705b7)。

从零延迟中断上下文（Zero Latency Interrupt Context）释放高频晶体振荡器（HFXO）。


## 10.4\_原页交叉引用（Cross References）

- [zephyr/device.h](../device_reference/P008_设备模型头文件源码.md)
- [zephyr/sys/onoff.h](../memory_services/P018_开关服务头文件源码.md)
- [zephyr/drivers/clock_control.h](../timer_reference/P096_时钟控制完整头文件.md)
- [查看此文件的源码。](../api_source_device_reference/P029_nrf_clock_control.h_源码浏览.md)
- [NRF_CLOCK_CONTROL_FREQUENCY_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__nrf.html#ga23770353a9de4e4bec02bca693c6709e)
- [UINT32_MAX](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#ab5eb23180f7cc12b7d6c04a8ec067fdd)
- [NRF_CLOCK_CONTROL_ACCURACY_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__nrf.html#gaf6cb7f3b8b7bb9540751639e1e48f229)
- [NRF_CLOCK_CONTROL_ACCURACY_PPM](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__nrf.html#ga4a7fdc5110eef82b86b642d40d9dc02e)
- [NRF_CLOCK_CONTROL_PRECISION_HIGH](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__nrf.html#ga0c870f2b78d538f7a33cf47110ed6ea7)
- [NRF_CLOCK_CONTROL_PRECISION_DEFAULT](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__nrf.html#ga15b112b62c60a7b9ca0b7fd2fccd5cca)
- [CLOCK_CONTROL_NRF_AUXPLL_GET_FREQ](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__nrf.html#ga7af5b4718beb72824e1e2a0d38fb1d7c)
- [CLOCK_CONTROL_NRF_AUXPLL_FREQ_OUT_MIN_HZ](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__nrf.html#ga445d6198c6ec95aec4d6e03ab3f17fcf)
- [CLOCK_CONTROL_NRF_AUXPLL_FREQ_OUT_AUDIO_44K1_HZ](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__nrf.html#ga2c452d78c7b50a72fb865f310a9b6fc0)
- [CLOCK_CONTROL_NRF_AUXPLL_FREQ_OUT_USB24M_HZ](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__nrf.html#ga9c7eb645dc042e54a08c3ffc8173817a)
- [CLOCK_CONTROL_NRF_AUXPLL_FREQ_OUT_AUDIO_48K_HZ](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__nrf.html#gaad21d734ae8305f9d0ce2882352dc206)
- [nrf_lfclk_start_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__nrf.html#gaadc162ec2c250d17572546d74a08ee7d)
- [CLOCK_CONTROL_NRF_LF_START_NOWAIT](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__nrf.html#ggaadc162ec2c250d17572546d74a08ee7dab4eb3c0c8038403f218a0147df6cdbec)
- [CLOCK_CONTROL_NRF_LF_START_AVAILABLE](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__nrf.html#ggaadc162ec2c250d17572546d74a08ee7da92be9b702c66df1a2bfd95560f1278df)
- [CLOCK_CONTROL_NRF_LF_START_STABLE](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__nrf.html#ggaadc162ec2c250d17572546d74a08ee7da949ac21a6fe976280b5fcc967608a8f4)
- [nrf_clock_control_request](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__nrf.html#ga2da9657c008b903a9131238bde6ed1ac)
- [device](../device_reference/P002_设备对象结构.md)
- [onoff_client](../memory_services/P019_开关客户端结构.md)
- [nrf_clock_control_request_sync](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__nrf.html#gaf334bc4e8b5ca0eb63b2bc4b1d963ac8)
- [k_timeout_t](../timer_reference/P087_内核超时类型.md)
- [nrf_clock_control_release](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__nrf.html#gaa46e3e407fb02b206772c438a0108634)
- [nrf_clock_control_cancel_or_release](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__nrf.html#ga3ecff5c6b37ced253c030fd032c61a70)
- [nrf_clock_control_resolve](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__nrf.html#gadd7ed9d76f521cc2894ba21abc8e4d94)
- [nrf_clock_control_get_startup_time](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__nrf.html#ga0ac2c96482c7551b16f1cc4eadd01560)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [nrf_clock_control_hfxo_request](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__nrf.html#ga259dfa1a679d21c4b92ecbf9fdfd3d13)
- [nrf_clock_control_hfxo_release](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__nrf.html#ga502110bf4c35eca120f883ba766705b7)

<a id="header-details"></a>

---

[上一章](P009_zephyr__dt-bindings__sensor__mc3419.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P011_zephyr__drivers__mfd__rv3032.h_文件参考.md)
