---
id: learning.zephyr-docs.api-file-reference.page-58
title: zephyr__drivers__power__atmel_sam_supc.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/drivers_2power_2atmel__sam__supc_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第58章\_zephyr\_\_drivers\_\_power\_\_atmel\_sam\_supc.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2power_2atmel__sam__supc_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

查看此文件的源码。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 58.1\_宏定义（Macros）

<a id="r_a694ffc7f2cd3ac2dad7a19111f983f5c"></a>

```c
#define SAM_DT_SUPC_CONTROLLER DEVICE_DT_GET(DT_NODELABEL(supc))
```

相关声明：[SAM_DT_SUPC_CONTROLLER](#a694ffc7f2cd3ac2dad7a19111f983f5c)、[DEVICE_DT_GET](../device_reference/P001_设备模型公共接口.md#ga9a65996ce21f43acb7db061e23b48ec7)、[DT_NODELABEL](../dt_identity_reference/P001_设备树节点标识宏.md#gab7d23294a6bf7fd44a98b48ec47d8a79)。

<a id="r_a30156dd2f0f5f9a1daea631866f9fbb7"></a>

```c
#define SAM_DT_SUPC_WAKEUP_SOURCE_ID(node_id)
```

相关声明：[SAM_DT_SUPC_WAKEUP_SOURCE_ID](#a30156dd2f0f5f9a1daea631866f9fbb7)。

<a id="r_ad12cd5eb9bcaea5ac08a39f1218dfff6"></a>

```c
#define SAM_DT_INST_SUPC_WAKEUP_SOURCE_ID(inst)
```

相关声明：[SAM_DT_INST_SUPC_WAKEUP_SOURCE_ID](#ad12cd5eb9bcaea5ac08a39f1218dfff6)。

## 58.2\_详细说明（Detailed Documentation）

<a id="ad12cd5eb9bcaea5ac08a39f1218dfff6"></a>

### `SAM_DT_INST_SUPC_WAKEUP_SOURCE_ID`

```c
#define SAM_DT_INST_SUPC_WAKEUP_SOURCE_ID ( inst)
```

展开值（Value）：

```c
SAM_DT_SUPC_WAKEUP_SOURCE_ID(DT_DRV_INST(inst))
```

<a id="a694ffc7f2cd3ac2dad7a19111f983f5c"></a>

### `SAM_DT_SUPC_CONTROLLER`

```c
#define SAM_DT_SUPC_CONTROLLER DEVICE_DT_GET(DT_NODELABEL(supc))
```

<a id="a30156dd2f0f5f9a1daea631866f9fbb7"></a>

### `SAM_DT_SUPC_WAKEUP_SOURCE_ID`

```c
#define SAM_DT_SUPC_WAKEUP_SOURCE_ID ( node_id)
```

展开值（Value）：

```c
DT_PHA(node_id, wakeup_source_id, wakeup_source_id)
```


## 58.3\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_reference/P170_atmel_sam_supc.h_源码浏览.md)
- [DEVICE_DT_GET](../device_reference/P001_设备模型公共接口.md#ga9a65996ce21f43acb7db061e23b48ec7)
- [DT_NODELABEL](../dt_identity_reference/P001_设备树节点标识宏.md#gab7d23294a6bf7fd44a98b48ec47d8a79)
- [DT_DRV_INST](../dt_instance_reference/P001_设备树驱动实例宏.md#ga219f413efba2f4c0151468b9a25a8dc1)
- [DT_PHA](../dt_property_reference/P001_设备树属性读取宏.md#gacef5921973a55433161fe0be3f8f628d)

<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="adrivers_2power_2atmel__sam__supc_8h_html_a30156dd2f0f5f9a1daea631866f9fbb7"></a>
<a id="agroup__devicetree-inst_html_ga219f413efba2f4c0151468b9a25a8dc1"></a>
<a id="agroup__devicetree-generic-prop_html_gacef5921973a55433161fe0be3f8f628d"></a>

---

[上一章](P057_zephyr__drivers__clock_control__renesas_cpg_mssr.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P059_zephyr__drivers__sensor__it8xxx2_vcmp.h_文件参考.md)
