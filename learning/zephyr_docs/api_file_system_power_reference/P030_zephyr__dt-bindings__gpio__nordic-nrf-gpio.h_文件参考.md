---
id: learning.zephyr-docs.api-file-system-power-reference.page-30
title: zephyr__dt-bindings__gpio__nordic-nrf-gpio.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/nordic-nrf-gpio_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第30章\_zephyr\_\_dt-bindings\_\_gpio\_\_nordic-nrf-gpio.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/nordic-nrf-gpio_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

查看此文件的源码。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 30.1\_宏定义（Macros）

<a id="define-members-0"></a>

### nRF GPIO 驱动标志（Drive Flags）。

nRF GPIO 驱动标志（Drive Flags）。

标准（Standard，S）或强（High，H）驱动模式可应用于引脚的两个电平：`0` 或

引脚配置为开漏模式（Open-drain，线与／Wired-and）时，只能为 `0` 电平选择驱动模式（`1` 为断开）。类似地，开源模式（Open-source，线或／Wired-or）下，只能为 `1` 电平设置驱动模式（`0` 为断开）。

驱动标志（Drive Flags）编码在 `gpio_dt_flags_t` 的高 8 位，具体如下：

<a id="r_ga00ce8b0f371e41899b0379adc4647036"></a>

```c
#define NRF_GPIO_DRIVE_S0 (0U << 8U)
```

相关声明：[NRF_GPIO_DRIVE_S0](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface__nrf.html#ga00ce8b0f371e41899b0379adc4647036)。

逻辑 `0` 使用标准驱动（Standard Drive），为默认值，与 `GPIO_OPEN_DRAIN` 配合使用。

<a id="r_gaa21a50e68b9018384dc7b409673cd047"></a>

```c
#define NRF_GPIO_DRIVE_H0 (1U << 8U)
```

相关声明：[NRF_GPIO_DRIVE_H0](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface__nrf.html#gaa21a50e68b9018384dc7b409673cd047)。

逻辑 `0` 使用强驱动（High Drive），与 `GPIO_OPEN_DRAIN` 配合使用。

<a id="r_ga5909d23af54ccd8bea797e0f74871cb3"></a>

```c
#define NRF_GPIO_DRIVE_S1 (0U << 9U)
```

相关声明：[NRF_GPIO_DRIVE_S1](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface__nrf.html#ga5909d23af54ccd8bea797e0f74871cb3)。

逻辑 `1` 使用标准驱动（Standard Drive），为默认值，与 `GPIO_OPEN_SOURCE` 配合使用。

<a id="r_ga8adac513c62dfc12b9f4d7272d73a99f"></a>

```c
#define NRF_GPIO_DRIVE_H1 (1U << 9U)
```

相关声明：[NRF_GPIO_DRIVE_H1](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface__nrf.html#ga8adac513c62dfc12b9f4d7272d73a99f)。

逻辑 `1` 使用强驱动（High Drive），与 `GPIO_OPEN_SOURCE` 配合使用。

<a id="r_ga0b03a6717cc2e5d57aba54379188a884"></a>

```c
#define NRF_GPIO_DRIVE_S0S1 (NRF_GPIO_DRIVE_S0 | NRF_GPIO_DRIVE_S1)
```

相关声明：[NRF_GPIO_DRIVE_S0S1](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface__nrf.html#ga0b03a6717cc2e5d57aba54379188a884)、[NRF_GPIO_DRIVE_S0](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface__nrf.html#ga00ce8b0f371e41899b0379adc4647036)、[NRF_GPIO_DRIVE_S1](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface__nrf.html#ga5909d23af54ccd8bea797e0f74871cb3)。

逻辑 `0` 和 `1` 均使用标准驱动（Standard Drive），为默认值。

<a id="r_ga43697400db8d8cba4dd4bbaaae59a551"></a>

```c
#define NRF_GPIO_DRIVE_S0H1 (NRF_GPIO_DRIVE_S0 | NRF_GPIO_DRIVE_H1)
```

相关声明：[NRF_GPIO_DRIVE_S0H1](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface__nrf.html#ga43697400db8d8cba4dd4bbaaae59a551)、[NRF_GPIO_DRIVE_S0](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface__nrf.html#ga00ce8b0f371e41899b0379adc4647036)、[NRF_GPIO_DRIVE_H1](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface__nrf.html#ga8adac513c62dfc12b9f4d7272d73a99f)。

逻辑 `0` 使用标准驱动（Standard Drive），逻辑 `1` 使用强驱动（High Drive）。

<a id="r_ga4426bd906d7e2965f53e21a246ec0bbc"></a>

```c
#define NRF_GPIO_DRIVE_H0S1 (NRF_GPIO_DRIVE_H0 | NRF_GPIO_DRIVE_S1)
```

相关声明：[NRF_GPIO_DRIVE_H0S1](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface__nrf.html#ga4426bd906d7e2965f53e21a246ec0bbc)、[NRF_GPIO_DRIVE_H0](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface__nrf.html#gaa21a50e68b9018384dc7b409673cd047)、[NRF_GPIO_DRIVE_S1](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface__nrf.html#ga5909d23af54ccd8bea797e0f74871cb3)。

逻辑 `0` 使用强驱动（High Drive），逻辑 `1` 使用标准驱动（Standard Drive）。

<a id="r_ga905a8813a86d8cf1087a47eadc089987"></a>

```c
#define NRF_GPIO_DRIVE_H0H1 (NRF_GPIO_DRIVE_H0 | NRF_GPIO_DRIVE_H1)
```

相关声明：[NRF_GPIO_DRIVE_H0H1](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface__nrf.html#ga905a8813a86d8cf1087a47eadc089987)、[NRF_GPIO_DRIVE_H0](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface__nrf.html#gaa21a50e68b9018384dc7b409673cd047)、[NRF_GPIO_DRIVE_H1](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface__nrf.html#ga8adac513c62dfc12b9f4d7272d73a99f)。

逻辑 `0` 和 `1` 均使用强驱动（High Drive）。


## 30.2\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_reference/P585_nordic-nrf-gpio.h_源码浏览.md)
- [gpio_dt_flags_t](../hardware/P266_GPIO公共接口.md#gad435719dccdc37c05852960a7218fbd2)
- [NRF_GPIO_DRIVE_S0](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface__nrf.html#ga00ce8b0f371e41899b0379adc4647036)
- [NRF_GPIO_DRIVE_H0](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface__nrf.html#gaa21a50e68b9018384dc7b409673cd047)
- [NRF_GPIO_DRIVE_S1](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface__nrf.html#ga5909d23af54ccd8bea797e0f74871cb3)
- [NRF_GPIO_DRIVE_H1](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface__nrf.html#ga8adac513c62dfc12b9f4d7272d73a99f)
- [NRF_GPIO_DRIVE_S0S1](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface__nrf.html#ga0b03a6717cc2e5d57aba54379188a884)
- [NRF_GPIO_DRIVE_S0H1](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface__nrf.html#ga43697400db8d8cba4dd4bbaaae59a551)
- [NRF_GPIO_DRIVE_H0S1](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface__nrf.html#ga4426bd906d7e2965f53e21a246ec0bbc)
- [NRF_GPIO_DRIVE_H0H1](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface__nrf.html#ga905a8813a86d8cf1087a47eadc089987)

---

[上一章](P029_zephyr__net__net_config.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P031_zephyr__mgmt__mcumgr__grp__os_mgmt__os_mgmt.h_文件参考.md)
