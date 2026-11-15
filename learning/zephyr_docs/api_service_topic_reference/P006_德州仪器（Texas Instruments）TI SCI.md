---
id: learning.zephyr-docs.api-service-topic-reference.page-6
title: 德州仪器（Texas Instruments）TI SCI
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__tisci.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第6章\_德州仪器（Texas Instruments）TI SCI

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__clock__control__tisci.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

<a id="details"></a>



<a id="header-files"></a>
<a id="files"></a>

## 6.1\_文件（Files）

<a id="r_tisci_5Fclock_5Fcontrol_2Eh"></a>

```c
file tisci_clock_control.h
```

相关声明：[tisci_clock_control.h](../api_file_service_reference/P057_zephyr__drivers__clock_control__tisci_clock_control.h_文件参考.md)。

TI TISCI系统控制器（System Controller）接口的时钟控制定义。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 6.2\_数据结构（Data Structures）

<a id="r_tisci_5Fclock_5Fconfig"></a>

```c
struct tisci_clock_config
```

相关声明：[tisci_clock_config](../platform_security_model_reference/P064_tisci_clock_config_结构体.md)。

时钟配置结构（Clock Configuration Structure）。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 6.3\_宏定义（Macros）

<a id="r_ga4048d6a28a71a725f5e34362189e2cf4"></a>

```c
#define TISCI_GET_CLOCK(node_id)
```

相关声明：[TISCI_GET_CLOCK](#ga4048d6a28a71a725f5e34362189e2cf4)。

获取节点 `clocks` 引用句柄（Phandle）所引用的时钟控制器设备（Clock Controller Device）。

<a id="r_ga3176cb1d06b703090ede7e2e3264e743"></a>

```c
#define TISCI_GET_CLOCK_DETAILS(node_id)
```

相关声明：[TISCI_GET_CLOCK_DETAILS](#ga3176cb1d06b703090ede7e2e3264e743)。

根据节点的时钟说明符（Clock Specifier）初始化 `tisci_clock_config`。

<a id="r_ga845867bfd9264f27ac7bf99fcb8456d2"></a>

```c
#define TISCI_GET_CLOCK_BY_INST(inst)
```

相关声明：[TISCI_GET_CLOCK_BY_INST](#ga845867bfd9264f27ac7bf99fcb8456d2)。

对设备树实例（DT Instance）执行与 `TISCI_GET_CLOCK()` 等效的操作。

<a id="r_gac45d403310257b6aa58566b764a7022b"></a>

```c
#define TISCI_GET_CLOCK_DETAILS_BY_INST(inst)
```

相关声明：[TISCI_GET_CLOCK_DETAILS_BY_INST](#gac45d403310257b6aa58566b764a7022b)。

对设备树实例（DT Instance）执行与 `TISCI_GET_CLOCK_DETAILS()` 等效的操作。

## 6.4\_详细说明（Detailed Documentation）

<a id="ga4048d6a28a71a725f5e34362189e2cf4"></a>

### `TISCI_GET_CLOCK`

```c
#define TISCI_GET_CLOCK ( node_id)
```

```c
#include <zephyr/drivers/clock_control/tisci_clock_control.h>
```

展开值（Value）：

```c
DEVICE_DT_GET(DT_PHANDLE(node_id, clocks))
```

获取节点 `clocks` 引用句柄（Phandle）所引用的时钟控制器设备（Clock Controller Device）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `node_id` | 设备树节点标识符（Devicetree Node Identifier）。 |

<a id="ga845867bfd9264f27ac7bf99fcb8456d2"></a>

### `TISCI_GET_CLOCK_BY_INST`

```c
#define TISCI_GET_CLOCK_BY_INST ( inst)
```

```c
#include <zephyr/drivers/clock_control/tisci_clock_control.h>
```

展开值（Value）：

```c
TISCI_GET_CLOCK(DT_DRV_INST(inst))
```

对设备树实例（DT Instance）执行与 `TISCI_GET_CLOCK()` 等效的操作。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `inst` | 设备树实例编号（DT Instance Number）。 |

<a id="ga3176cb1d06b703090ede7e2e3264e743"></a>

### `TISCI_GET_CLOCK_DETAILS`

```c
#define TISCI_GET_CLOCK_DETAILS ( node_id)
```

```c
#include <zephyr/drivers/clock_control/tisci_clock_control.h>
```

展开值（Value）：

```c
{       \
        .dev_id = DT_CLOCKS_CELL(node_id, devid),       \
        .clk_id = DT_CLOCKS_CELL(node_id, clkid)        \
}
```

根据节点的时钟说明符（Clock Specifier）初始化 `tisci_clock_config`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `node_id` | 设备树节点标识符（Devicetree Node Identifier）。 |

<a id="gac45d403310257b6aa58566b764a7022b"></a>

### `TISCI_GET_CLOCK_DETAILS_BY_INST`

```c
#define TISCI_GET_CLOCK_DETAILS_BY_INST ( inst)
```

```c
#include <zephyr/drivers/clock_control/tisci_clock_control.h>
```

展开值（Value）：

```c
TISCI_GET_CLOCK_DETAILS(DT_DRV_INST(inst))
```

对设备树实例（DT Instance）执行与 `TISCI_GET_CLOCK_DETAILS()` 等效的操作。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `inst` | 设备树实例编号（DT Instance Number）。 |


## 6.5\_原页交叉引用（Cross References）

- [tisci_clock_control.h](../api_file_service_reference/P057_zephyr__drivers__clock_control__tisci_clock_control.h_文件参考.md)
- [tisci_clock_config](../platform_security_model_reference/P064_tisci_clock_config_结构体.md)
- [DEVICE_DT_GET](../device_reference/P001_设备模型公共接口.md#ga9a65996ce21f43acb7db061e23b48ec7)
- [DT_PHANDLE](../dt_property_reference/P001_设备树属性读取宏.md#ga7bd77c49472ba4547d87f00f40fd7171)
- [DT_DRV_INST](../dt_instance_reference/P001_设备树驱动实例宏.md#ga219f413efba2f4c0151468b9a25a8dc1)
- [DT_CLOCKS_CELL](https://docs.zephyrproject.org/latest/doxygen/html/group__devicetree-clocks.html#ga211bc385cbbb1d8b8fa52e2e0a52d23d)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="agroup__device__model_html_ga9a65996ce21f43acb7db061e23b48ec7"></a>
<a id="agroup__devicetree-generic-prop_html_ga7bd77c49472ba4547d87f00f40fd7171"></a>
<a id="agroup__clock__control__tisci_html_ga4048d6a28a71a725f5e34362189e2cf4"></a>
<a id="agroup__devicetree-inst_html_ga219f413efba2f4c0151468b9a25a8dc1"></a>
<a id="agroup__devicetree-clocks_html_ga211bc385cbbb1d8b8fa52e2e0a52d23d"></a>
<a id="agroup__clock__control__tisci_html_ga3176cb1d06b703090ede7e2e3264e743"></a>

---

[上一章](P005_芯科科技（Silicon Labs）.md) · [返回大纲](大纲.md) · [下一章](P007_CoAP 管理器事件（CoAP Manager Events）.md)
