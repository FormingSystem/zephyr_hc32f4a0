---
id: learning.zephyr-docs.api-file-signal-device-reference.page-7
title: zephyr__dt-bindings__sensor__mcp9600.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/dt-bindings_2sensor_2mcp9600_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第7章\_zephyr\_\_dt-bindings\_\_sensor\_\_mcp9600.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/dt-bindings_2sensor_2mcp9600_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

the Microchip MCP9600 thermocouple converter的设备树绑定常量（Devicetree Binding Constants）。

查看此文件的源码。

<a id="details"></a>

the Microchip MCP9600 thermocouple converter的设备树绑定常量（Devicetree Binding Constants）。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 7.1\_宏定义（Macros）

<a id="define-members-0"></a>

### 热电偶类型选择（Thermocouple Type Selection）

设备树属性（Devicetree Property）`thermocouple-type` 的取值。

<a id="r_ga0f5dfe27994b5d2f6b31b5e0ff908a4e"></a>

```c
#define MCP9600_DT_TYPE_K 0x0
```

相关声明：[MCP9600_DT_TYPE_K](https://docs.zephyrproject.org/latest/doxygen/html/group__mcp9600__interface.html#ga0f5dfe27994b5d2f6b31b5e0ff908a4e)。

K 型热电偶（Thermocouple）。

<a id="r_gaf7595a59bd6795425c32385541dd5bba"></a>

```c
#define MCP9600_DT_TYPE_J 0x1
```

相关声明：[MCP9600_DT_TYPE_J](https://docs.zephyrproject.org/latest/doxygen/html/group__mcp9600__interface.html#gaf7595a59bd6795425c32385541dd5bba)。

J 型热电偶（Thermocouple）。

<a id="r_gadb382d020b9f5260ff2ddb6b5e4ba134"></a>

```c
#define MCP9600_DT_TYPE_T 0x2
```

相关声明：[MCP9600_DT_TYPE_T](https://docs.zephyrproject.org/latest/doxygen/html/group__mcp9600__interface.html#gadb382d020b9f5260ff2ddb6b5e4ba134)。

T 型热电偶（Thermocouple）。

<a id="r_ga347b21f9623b3d80458c2fe52e79a5b3"></a>

```c
#define MCP9600_DT_TYPE_N 0x3
```

相关声明：[MCP9600_DT_TYPE_N](https://docs.zephyrproject.org/latest/doxygen/html/group__mcp9600__interface.html#ga347b21f9623b3d80458c2fe52e79a5b3)。

N 型热电偶（Thermocouple）。

<a id="r_ga8f5a4f4fef7d9760989f9a803acc7454"></a>

```c
#define MCP9600_DT_TYPE_S 0x4
```

相关声明：[MCP9600_DT_TYPE_S](https://docs.zephyrproject.org/latest/doxygen/html/group__mcp9600__interface.html#ga8f5a4f4fef7d9760989f9a803acc7454)。

S 型热电偶（Thermocouple）。

<a id="r_gab6e2ea9fa3e8a48ab130476b996152c3"></a>

```c
#define MCP9600_DT_TYPE_E 0x5
```

相关声明：[MCP9600_DT_TYPE_E](https://docs.zephyrproject.org/latest/doxygen/html/group__mcp9600__interface.html#gab6e2ea9fa3e8a48ab130476b996152c3)。

E 型热电偶（Thermocouple）。

<a id="r_gabee3c050df7e174a6195097cd68bf5a4"></a>

```c
#define MCP9600_DT_TYPE_B 0x6
```

相关声明：[MCP9600_DT_TYPE_B](https://docs.zephyrproject.org/latest/doxygen/html/group__mcp9600__interface.html#gabee3c050df7e174a6195097cd68bf5a4)。

B 型热电偶（Thermocouple）。

<a id="r_ga58f49ac4ea31762a90c7604759061cc8"></a>

```c
#define MCP9600_DT_TYPE_R 0x7
```

相关声明：[MCP9600_DT_TYPE_R](https://docs.zephyrproject.org/latest/doxygen/html/group__mcp9600__interface.html#ga58f49ac4ea31762a90c7604759061cc8)。

R 型热电偶（Thermocouple）。

<a id="define-members-1"></a>

### 模数转换器分辨率选项（ADC Resolution Options）

设备树属性（Devicetree Property）`adc-resolution` 的取值。

<a id="r_ga69e6b3961082b348e59e4f31d272caa1"></a>

```c
#define MCP9600_DT_ADC_RES_18BIT 0x0
```

相关声明：[MCP9600_DT_ADC_RES_18BIT](https://docs.zephyrproject.org/latest/doxygen/html/group__mcp9600__interface.html#ga69e6b3961082b348e59e4f31d272caa1)。

18 位分辨率（Resolution）。

<a id="r_ga1e8952f8a92ee540e1b7f2ae2732f093"></a>

```c
#define MCP9600_DT_ADC_RES_16BIT 0x1
```

相关声明：[MCP9600_DT_ADC_RES_16BIT](https://docs.zephyrproject.org/latest/doxygen/html/group__mcp9600__interface.html#ga1e8952f8a92ee540e1b7f2ae2732f093)。

16 位分辨率（Resolution）。

<a id="r_gaa117b84e7ffd54a2e2462f83fd17d64f"></a>

```c
#define MCP9600_DT_ADC_RES_14BIT 0x2
```

相关声明：[MCP9600_DT_ADC_RES_14BIT](https://docs.zephyrproject.org/latest/doxygen/html/group__mcp9600__interface.html#gaa117b84e7ffd54a2e2462f83fd17d64f)。

14 位分辨率（Resolution）。

<a id="r_ga34675b172d46c573e78af00c82f380e1"></a>

```c
#define MCP9600_DT_ADC_RES_12BIT 0x3
```

相关声明：[MCP9600_DT_ADC_RES_12BIT](https://docs.zephyrproject.org/latest/doxygen/html/group__mcp9600__interface.html#ga34675b172d46c573e78af00c82f380e1)。

12 位分辨率（Resolution）。

<a id="define-members-2"></a>

### 冷端温度分辨率（Cold-junction Temperature Resolution）

设备树属性（Devicetree Property）`cold-junction-temp-resolution` 的取值。

<a id="r_gaa793d96692f26f416f5e69d8e15a6dc3"></a>

```c
#define MCP9600_DT_COLD_JUNC_TMP_RES_0_0625C 0x0
```

相关声明：[MCP9600_DT_COLD_JUNC_TMP_RES_0_0625C](https://docs.zephyrproject.org/latest/doxygen/html/group__mcp9600__interface.html#gaa793d96692f26f416f5e69d8e15a6dc3)。

0.0625 °C 分辨率（Resolution）。

<a id="r_gac90effdfb0eabfa2827c5cb346eacf12"></a>

```c
#define MCP9600_DT_COLD_JUNC_TMP_RES_0_25C 0x1
```

相关声明：[MCP9600_DT_COLD_JUNC_TMP_RES_0_25C](https://docs.zephyrproject.org/latest/doxygen/html/group__mcp9600__interface.html#gac90effdfb0eabfa2827c5cb346eacf12)。

0.25 °C 分辨率（Resolution）。


## 7.2\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_reference/P209_mcp9600.h_源码浏览.md)
- [MCP9600_DT_TYPE_K](https://docs.zephyrproject.org/latest/doxygen/html/group__mcp9600__interface.html#ga0f5dfe27994b5d2f6b31b5e0ff908a4e)
- [MCP9600_DT_TYPE_J](https://docs.zephyrproject.org/latest/doxygen/html/group__mcp9600__interface.html#gaf7595a59bd6795425c32385541dd5bba)
- [MCP9600_DT_TYPE_T](https://docs.zephyrproject.org/latest/doxygen/html/group__mcp9600__interface.html#gadb382d020b9f5260ff2ddb6b5e4ba134)
- [MCP9600_DT_TYPE_N](https://docs.zephyrproject.org/latest/doxygen/html/group__mcp9600__interface.html#ga347b21f9623b3d80458c2fe52e79a5b3)
- [MCP9600_DT_TYPE_S](https://docs.zephyrproject.org/latest/doxygen/html/group__mcp9600__interface.html#ga8f5a4f4fef7d9760989f9a803acc7454)
- [MCP9600_DT_TYPE_E](https://docs.zephyrproject.org/latest/doxygen/html/group__mcp9600__interface.html#gab6e2ea9fa3e8a48ab130476b996152c3)
- [MCP9600_DT_TYPE_B](https://docs.zephyrproject.org/latest/doxygen/html/group__mcp9600__interface.html#gabee3c050df7e174a6195097cd68bf5a4)
- [MCP9600_DT_TYPE_R](https://docs.zephyrproject.org/latest/doxygen/html/group__mcp9600__interface.html#ga58f49ac4ea31762a90c7604759061cc8)
- [MCP9600_DT_ADC_RES_18BIT](https://docs.zephyrproject.org/latest/doxygen/html/group__mcp9600__interface.html#ga69e6b3961082b348e59e4f31d272caa1)
- [MCP9600_DT_ADC_RES_16BIT](https://docs.zephyrproject.org/latest/doxygen/html/group__mcp9600__interface.html#ga1e8952f8a92ee540e1b7f2ae2732f093)
- [MCP9600_DT_ADC_RES_14BIT](https://docs.zephyrproject.org/latest/doxygen/html/group__mcp9600__interface.html#gaa117b84e7ffd54a2e2462f83fd17d64f)
- [MCP9600_DT_ADC_RES_12BIT](https://docs.zephyrproject.org/latest/doxygen/html/group__mcp9600__interface.html#ga34675b172d46c573e78af00c82f380e1)
- [MCP9600_DT_COLD_JUNC_TMP_RES_0_0625C](https://docs.zephyrproject.org/latest/doxygen/html/group__mcp9600__interface.html#gaa793d96692f26f416f5e69d8e15a6dc3)
- [MCP9600_DT_COLD_JUNC_TMP_RES_0_25C](https://docs.zephyrproject.org/latest/doxygen/html/group__mcp9600__interface.html#gac90effdfb0eabfa2827c5cb346eacf12)

<a id="header-details"></a>

---

[上一章](P006_zephyr__drivers__i3c__devicetree.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P008_zephyr__drivers__edac.h_文件参考.md)
